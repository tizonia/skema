# Copyright (C) 2011-2017 Aratelia Limited - Juan A. Rubio
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Skema's OpenMAX IL Base Profile Manager
"""

import os
import sys
import Queue
import threading

from abc import abstractmethod, abstractproperty

from skema.omxil12 import __all_indexes__ as omxil12_indexes
from skema.omxil12 import OMX_GetParameter
from skema.omxil12 import OMX_AllocateBuffer
from skema.omxil12 import OMX_UseBuffer
from skema.omxil12 import OMX_UseEGLImage
from skema.omxil12 import OMX_FreeBuffer
from skema.omxil12 import OMX_FillThisBuffer
from skema.omxil12 import OMX_EmptyThisBuffer
from skema.omxil12 import OMX_BUFFERHEADERTYPE
from skema.omxil12 import get_il_enum_from_string
from skema.omxil12 import get_string_from_il_enum

from skema.utils import log_line
from skema.config import get_config

from ctypes import CDLL
from ctypes import sizeof
from ctypes import byref
from ctypes import cast
from ctypes import addressof
from ctypes import POINTER
from ctypes import c_ubyte
from ctypes import memmove

class SkemaBaseProfileCmdIf(object):
    """
    Abstract class for commands that will be processed by the base profile
    worker thread
    """

    @abstractmethod
    def run(self, manager):
        """
        Runs the command.
        """

class SkemaBaseProfilePort(SkemaBaseProfileCmdIf):
    """

    """

    def __init__ (self, alias, pid, allocator, mode, uri):
        self.alias        = alias
        self.pid          = pid
        if allocator.lower() == "true":
            self.allocator = True
        else:
            self.allocator = False
        self.mode               = mode
        self.uri                = uri

        self.nBufferCountActual = 0
        self.nBufferSize        = 0
        self.is_input           = False
        self.EOS                = False

        self.fd                 = file(os.devnull)
        self.headers            = []
        self.buffers            = []
        self.allocation_count   = 0
        self.deallocation_count = 0

    def run(self, manager):

        if self.alias not in manager.aliases2ports:
            ports                         = dict()
            ports[self.pid]               = self
            manager.aliases2ports[self.alias] = ports
        else:
            manager.aliases2ports[self.alias][self.pid] = self

class SkemaBaseProfileAllocate(SkemaBaseProfileCmdIf):
    """

    """

    def __init__ (self, alias, pid, howmany):
        self.alias   = alias
        self.pid     = pid
        self.howmany = howmany

    def run (self, manager):

        if self.alias not in manager.aliases2ports:
            print "allocate_buffer: Wrong alias specified"
            sys.exit(1)

        if self.pid not in manager.aliases2ports[self.alias]:
            print "allocate_buffer: Wrong port index specified"
            sys.exit(1)

        port = manager.aliases2ports[self.alias][self.pid]

        config = get_config()
        handle = config.handles[self.alias]

        # Retrieve the port definition
        indexstr                = "OMX_IndexParamPortDefinition"
        index                   = get_il_enum_from_string(indexstr)
        param_type              = omxil12_indexes[indexstr]
        param_struct            = param_type()
        param_struct.nSize      = sizeof(param_type)
        param_struct.nPortIndex = int(self.pid)

        omxerror = OMX_GetParameter(handle, index, byref(param_struct))
        interror = int(omxerror & 0xffffffff)
        err = get_string_from_il_enum(interror, "OMX_Error")

        port.nBufferCountActual = param_struct.nBufferCountActual
        port.nBufferSize        = param_struct.nBufferSize

        dirstr = get_string_from_il_enum \
            (getattr(param_struct, "eDir"), "OMX_Dir")

        if "OMX_DirInput" == dirstr:
            port.is_input = True
        else:
            port.is_input       = False

        if self.howmany.lower() == "all":
            self.howmany = port.nBufferCountActual
        else:
            self.howmany = int(self.howmany)
            log_line ("Allocate %d total" % self.howmany)

        if self.howmany == 0:
            print "allocate_buffer: Need to allocate at least 1 buffer"
            sys.exit(1)

        if port.allocation_count + self.howmany > \
                port.nBufferCountActual:
            print "allocate_buffer: Need to allocate at most " \
                "nBufferCountActual buffers"
            sys.exit(1)

        libc = CDLL('libc.so.6')
        for i in range(port.allocation_count,
                       port.allocation_count + self.howmany):

            p_header = POINTER(OMX_BUFFERHEADERTYPE)()

            if port.allocator:
                buf = (c_ubyte * port.nBufferSize)()
                omxerror = OMX_UseBuffer(handle,
                                         byref(p_header),
                                         param_struct.nPortIndex,
                                         None,
                                         port.nBufferSize,
                                         buf)
                port.buffers.append(buf)
            else:
                omxerror = OMX_AllocateBuffer(handle,
                                              byref(p_header),
                                              param_struct.nPortIndex,
                                              None,
                                              port.nBufferSize)

            port.headers.append(p_header)

        port.allocation_count += self.howmany

class SkemaBaseProfileUseEGLImages(SkemaBaseProfileCmdIf):
    """

    """

    def __init__ (self, alias, pid, howmany):
        self.alias   = alias
        self.pid     = pid
        self.howmany = howmany

    def run (self, manager):

        if self.alias not in manager.aliases2ports:
            print "use_egl_images: Wrong alias specified"
            sys.exit(1)

        if self.pid not in manager.aliases2ports[self.alias]:
            print "use_egl_images: Wrong port index specified"
            sys.exit(1)

        port = manager.aliases2ports[self.alias][self.pid]

        config = get_config()
        handle = config.handles[self.alias]

        # Retrieve the port definition
        indexstr                = "OMX_IndexParamPortDefinition"
        index                   = get_il_enum_from_string(indexstr)
        param_type              = omxil12_indexes[indexstr]
        param_struct            = param_type()
        param_struct.nSize      = sizeof(param_type)
        param_struct.nPortIndex = int(self.pid)

        omxerror = OMX_GetParameter(handle, index, byref(param_struct))
        interror = int(omxerror & 0xffffffff)
        err = get_string_from_il_enum(interror, "OMX_Error")

        port.nBufferCountActual = param_struct.nBufferCountActual
        port.nBufferSize        = param_struct.nBufferSize

        dirstr = get_string_from_il_enum \
            (getattr(param_struct, "eDir"), "OMX_Dir")

        if "OMX_DirInput" == dirstr:
            port.is_input = True
        else:
            port.is_input = False

        if self.howmany.lower() == "all":
            self.howmany = port.nBufferCountActual
        else:
            self.howmany = int(self.howmany)
            log_line ("Allocate %d total" % self.howmany)

        if self.howmany == 0:
            print "use_egl_images: Need to allocate at least 1 buffer"
            sys.exit(1)

        if port.allocation_count + self.howmany > \
                port.nBufferCountActual:
            print "use_egl_images: Need to allocate at most " \
                "nBufferCountActual buffers"
            sys.exit(1)

        libc = CDLL('libc.so.6')
        for i in range(port.allocation_count,
                       port.allocation_count + self.howmany):

            p_header = POINTER(OMX_BUFFERHEADERTYPE)()

            if port.allocator:
                print "use_egl_images: Port can't be allocate buffers. " \
                    "Invalid test setup."
                sys.exit(1)

            eglimage = (c_ubyte * port.nBufferSize)()
            omxerror = OMX_UseEGLImage(handle,
                                       byref(p_header),
                                       param_struct.nPortIndex,
                                       None,
                                       eglimage)

            port.headers.append(p_header)
            port.buffers.append(eglimage)

        port.allocation_count += self.howmany

class SkemaBaseProfileFree(SkemaBaseProfileCmdIf):
    """

    """

    def __init__ (self, alias, pid, howmany):
        self.alias   = alias
        self.pid     = pid
        self.howmany = howmany

    def run (self, manager):

        if self.alias not in manager.aliases2ports:
            print "free_buffer: Wrong alias specified"
            sys.exit(1)

        if self.pid not in manager.aliases2ports[self.alias]:
            print "free_buffer: Wrong port index specified"
            sys.exit(1)

        port = manager.aliases2ports[self.alias][self.pid]

        if port.allocation_count == 0:
            print "free_buffer: Nothing to free "
            sys.exit(1)

        config = get_config()
        handle = config.handles[self.alias]

        if self.howmany.lower() == "all":
            self.howmany = port.nBufferCountActual
        else:
            self.howmany = int(self.howmany)

        if self.howmany == 0:
            print "free_buffer: Need to free at least 1 buffer"
            sys.exit(1)

        if port.allocation_count < self.howmany:
            print "free_buffer: Too many buffers to be freed"
            sys.exit(1)

        config = get_config()
        handle = config.handles[self.alias]

        libc = CDLL('libc.so.6')
        for i in range(port.deallocation_count,
                       port.deallocation_count + self.howmany):


            omxerror = OMX_FreeBuffer(handle, int(self.pid), port.headers[i])

            # NOTE: We simply don't bother deleting the buffers that we would
            # have allocated if we were using OMX_UseBuffer

        port.allocation_count   -= self.howmany
        port.deallocation_count += self.howmany

        if port.allocation_count == 0:
            del port.headers[:]


class SkemaBaseProfileExchange(SkemaBaseProfileCmdIf):
    """

    """

    def __init__ (self, alias, pid):
        self.alias      = alias
        self.pid        = pid

    def run (self, manager):

        if self.alias not in manager.aliases2ports:
            print "free_buffer: Wrong alias specified"
            sys.exit(1)

        if self.pid not in manager.aliases2ports[self.alias]:
            print "free_buffer: Wrong port index specified"
            sys.exit(1)

        port = manager.aliases2ports[self.alias][self.pid]

        if port.is_input:
            port.fd = open(port.uri, "rb")
        else:
            port.fd = open(port.uri, "wb")

        config = get_config()
        handle = config.handles[self.alias]

        for i in range(0, port.nBufferCountActual):
            if port.is_input:
                buf        = port.fd.read(port.nBufferSize)
                read_bytes = len(buf)

                if port.headers[i].contents.pBuffer:
                    memmove(port.headers[i].contents.pBuffer, buf, read_bytes)

                port.headers[i].contents.nFilledLen = read_bytes
                if read_bytes < port.nBufferSize:
                    port.headers[i].contents.nFlags = 1
                    port.EOS                        = True

                OMX_EmptyThisBuffer(handle, port.headers[i])

                if port.EOS:
                    return

            else:
                port.fd.write(port.buffers[i])
                OMX_FillThisBuffer(handle, port.headers[i])


class SkemaBaseProfileFill(SkemaBaseProfileCmdIf):
    """

    """

    def __init__ (self, alias, pid, buffer_idx):
        self.alias      = alias
        self.pid        = pid
        self.buffer_idx = buffer_idx

    def run (self, manager):
        log_line ("SkemaBaseProfileEmpty.run")

class SkemaBaseProfileEmpty(SkemaBaseProfileCmdIf):
    """

    """

    def __init__ (self, alias, pid, buffer_idx):
        self.alias      = alias
        self.pid        = pid
        self.buffer_idx = buffer_idx

    def run (self, manager):
        log_line ("SkemaBaseProfileEmpty.run")


class SkemaBaseProfileFillDone(SkemaBaseProfileCmdIf):
    """

    """

    def __init__ (self, handle, alias, filled_buffer):
        self.handle        = handle
        self.alias         = alias
        self.filled_buffer = filled_buffer

    def run (self, manager):

        pid = self.filled_buffer.contents.nOutputPortIndex
        port = manager.aliases2ports[self.alias][str(pid)]

        if port.EOS:
            return

        OMX_FillThisBuffer(self.handle, self.filled_buffer)


class SkemaBaseProfileEmptyDone(SkemaBaseProfileCmdIf):
    """

    """

    def __init__ (self, handle, alias, emptied_buffer):
        self.handle         = handle
        self.alias          = alias
        self.emptied_buffer = emptied_buffer

    def run (self, manager):

        pid = self.emptied_buffer.contents.nInputPortIndex
        port = manager.aliases2ports[self.alias][str(pid)]

        if port.EOS:
            return

        buf  = port.fd.read(port.nBufferSize)
        read_bytes = len(buf)

        if self.emptied_buffer.contents.pBuffer:
            memmove(self.emptied_buffer.contents.pBuffer, buf, read_bytes)

        self.emptied_buffer.contents.nFilledLen = read_bytes
        if read_bytes < port.nBufferSize:
            self.emptied_buffer.contents.nFlags = 1
            port.EOS = True

        OMX_EmptyThisBuffer(self.handle, self.emptied_buffer)


class SkemaBaseProfileManager(threading.Thread):
    """

    """
    aliases2ports = dict()

    def __init__ (self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.queue = Queue.Queue(0)

    def manage_port (self, alias, pid, allocator, mode, uri):
        self.queue.put(SkemaBaseProfilePort(alias, pid, allocator, mode, uri))

    def allocate_buffers (self, alias, pid, howmany):
        self.queue.put(SkemaBaseProfileAllocate(alias, pid, howmany))

    def use_egl_images (self, alias, pid, howmany):
        self.queue.put(SkemaBaseProfileUseEGLImages(alias, pid, howmany))

    def free_buffers (self, alias, pid, howmany):
        self.queue.put(SkemaBaseProfileFree(alias, pid, howmany))

    def start_exchange (self, alias, pid):
        self.queue.put(SkemaBaseProfileExchange(alias, pid))

    def fill_buffer (self, alias, pid, buffer_idx):
        log_line ("fill_buffer")
        self.queue.put(SkemaBaseProfileFill(alias, pid, buffer_idx))

    def empty_buffer (self, alias, pid, buffer_idx):
        log_line ("empty_buffer")
        self.queue.put(SkemaBaseProfileEmpty(alias, pid, buffer_idx))

    def wait_for_buffer (self, alias, pid, buffer_idx):
        log_line ("wait_for_buffer")

    # OpenMAX IL callbacks

    def fill_buffer_done (self, handle, alias, filled_buffer):
        self.queue.put(SkemaBaseProfileFillDone(handle, alias, filled_buffer))

    def empty_buffer_done (self, handle, alias, emptied_buffer):
        self.queue.put(SkemaBaseProfileEmptyDone(handle, alias, emptied_buffer))

    def stop(self):
        self.queue.put(None)
        self.queue.join()

    def run (self):

        while True:
            cmd = self.queue.get()
            if cmd is None:
                break
            cmd.run(self)
            self.queue.task_done()

        self.queue.task_done()
        return
