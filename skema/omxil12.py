# Copyright (C) 2011-2014 Aratelia Limited - Juan A. Rubio
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

'''Wrapper for OpenMAX IL 1.2 headers

Mostly generated with: ctypesgen.py

'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys, pwd
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (C) 2008 David James
# Copyright (C) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs.extend(other_dirs)

load_library = loader.load_library

del loaderclass

# End loader

# By default, add some additional library search paths

# /usr/local/lib
add_library_search_dirs(['/usr/local/lib'])

# /home/user/temp/lib
userdir = pwd.getpwuid(os.getuid())[5]
usertmpdir = os.path.join(userdir, "temp")
usertmplibdir = os.path.join(usertmpdir, "lib")
add_library_search_dirs([usertmplibdir])

# Begin libraries

_libs["libtizcore.so"] = load_library("libtizcore.so")

# 1 library
# End libraries

# No modules

OMX_U8 = c_ubyte # OMX_Types.h: 78

OMX_S8 = c_char # OMX_Types.h: 80

OMX_U16 = c_ushort # OMX_Types.h: 82

OMX_S16 = c_short # OMX_Types.h: 84

OMX_U32 = c_ulong # OMX_Types.h: 86

OMX_S32 = c_long # OMX_Types.h: 88

OMX_U64 = c_ulonglong # OMX_Types.h: 110

OMX_S64 = c_longlong # OMX_Types.h: 111

enum_OMX_BOOL = c_int # OMX_Types.h: 120

OMX_FALSE = 0 # OMX_Types.h: 120

OMX_TRUE = (not OMX_FALSE) # OMX_Types.h: 120

OMX_BOOL_MAX = 2147483647 # OMX_Types.h: 120

OMX_BOOL = enum_OMX_BOOL # OMX_Types.h: 120

OMX_PTR = POINTER(None) # OMX_Types.h: 122

OMX_STRING = String # OMX_Types.h: 124

OMX_UUIDTYPE = c_ubyte * 128 # OMX_Types.h: 126

enum_OMX_DIRTYPE = c_int # OMX_Types.h: 133

OMX_DirInput = 0 # OMX_Types.h: 133

OMX_DirOutput = (OMX_DirInput + 1) # OMX_Types.h: 133

OMX_DirMax = 2147483647 # OMX_Types.h: 133

OMX_DIRTYPE = enum_OMX_DIRTYPE # OMX_Types.h: 133

enum_OMX_ENDIANTYPE = c_int # OMX_Types.h: 140

OMX_EndianBig = 0 # OMX_Types.h: 140

OMX_EndianLittle = (OMX_EndianBig + 1) # OMX_Types.h: 140

OMX_EndianMax = 2147483647 # OMX_Types.h: 140

OMX_ENDIANTYPE = enum_OMX_ENDIANTYPE # OMX_Types.h: 140

enum_OMX_NUMERICALDATATYPE = c_int # OMX_Types.h: 147

OMX_NumericalDataSigned = 0 # OMX_Types.h: 147

OMX_NumericalDataUnsigned = (OMX_NumericalDataSigned + 1) # OMX_Types.h: 147

OMX_NumercialDataMax = 2147483647 # OMX_Types.h: 147

OMX_NUMERICALDATATYPE = enum_OMX_NUMERICALDATATYPE # OMX_Types.h: 147

# OMX_Types.h: 154
class struct_OMX_BU32(Structure):
    pass

struct_OMX_BU32.__slots__ = [
    'nValue',
    'nMin',
    'nMax',
]
struct_OMX_BU32._fields_ = [
    ('nValue', OMX_U32),
    ('nMin', OMX_U32),
    ('nMax', OMX_U32),
]

OMX_BU32 = struct_OMX_BU32 # OMX_Types.h: 154

# OMX_Types.h: 161
class struct_OMX_BS32(Structure):
    pass

struct_OMX_BS32.__slots__ = [
    'nValue',
    'nMin',
    'nMax',
]
struct_OMX_BS32._fields_ = [
    ('nValue', OMX_S32),
    ('nMin', OMX_S32),
    ('nMax', OMX_S32),
]

OMX_BS32 = struct_OMX_BS32 # OMX_Types.h: 161

OMX_TICKS = OMX_S64 # OMX_Types.h: 165

OMX_HANDLETYPE = POINTER(None) # OMX_Types.h: 178

# OMX_Types.h: 188
class struct_OMX_MARKTYPE(Structure):
    pass

struct_OMX_MARKTYPE.__slots__ = [
    'hMarkTargetComponent',
    'pMarkData',
]
struct_OMX_MARKTYPE._fields_ = [
    ('hMarkTargetComponent', OMX_HANDLETYPE),
    ('pMarkData', OMX_PTR),
]

OMX_MARKTYPE = struct_OMX_MARKTYPE # OMX_Types.h: 188

OMX_NATIVE_DEVICETYPE = POINTER(None) # OMX_Types.h: 194

OMX_NATIVE_WINDOWTYPE = POINTER(None) # OMX_Types.h: 198

# OMX_Types.h: 226
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    'nVersionMajor',
    'nVersionMinor',
    'nRevision',
    'nStep',
]
struct_anon_1._fields_ = [
    ('nVersionMajor', OMX_U8),
    ('nVersionMinor', OMX_U8),
    ('nRevision', OMX_U8),
    ('nStep', OMX_U8),
]

# OMX_Types.h: 236
class union_OMX_VERSIONTYPE(Union):
    pass

union_OMX_VERSIONTYPE.__slots__ = [
    's',
    'nVersion',
]
union_OMX_VERSIONTYPE._fields_ = [
    ('s', struct_anon_1),
    ('nVersion', OMX_U32),
]

OMX_VERSIONTYPE = union_OMX_VERSIONTYPE # OMX_Types.h: 236

enum_OMX_INDEXTYPE = c_int # OMX_Index.h: 296

OMX_IndexComponentStartUnused = 16777216 # OMX_Index.h: 296

OMX_IndexParamPriorityMgmt = (OMX_IndexComponentStartUnused + 1) # OMX_Index.h: 296

OMX_IndexParamAudioInit = (OMX_IndexParamPriorityMgmt + 1) # OMX_Index.h: 296

OMX_IndexParamImageInit = (OMX_IndexParamAudioInit + 1) # OMX_Index.h: 296

OMX_IndexParamVideoInit = (OMX_IndexParamImageInit + 1) # OMX_Index.h: 296

OMX_IndexParamOtherInit = (OMX_IndexParamVideoInit + 1) # OMX_Index.h: 296

OMX_IndexParamNumAvailableStreams = (OMX_IndexParamOtherInit + 1) # OMX_Index.h: 296

OMX_IndexParamActiveStream = (OMX_IndexParamNumAvailableStreams + 1) # OMX_Index.h: 296

OMX_IndexParamSuspensionPolicy = (OMX_IndexParamActiveStream + 1) # OMX_Index.h: 296

OMX_IndexParamComponentSuspended = (OMX_IndexParamSuspensionPolicy + 1) # OMX_Index.h: 296

OMX_IndexConfigCapturing = (OMX_IndexParamComponentSuspended + 1) # OMX_Index.h: 296

OMX_IndexConfigCaptureMode = (OMX_IndexConfigCapturing + 1) # OMX_Index.h: 296

OMX_IndexAutoPauseAfterCapture = (OMX_IndexConfigCaptureMode + 1) # OMX_Index.h: 296

OMX_IndexParamContentURI = (OMX_IndexAutoPauseAfterCapture + 1) # OMX_Index.h: 296

OMX_IndexReserved_0x0100000E = (OMX_IndexParamContentURI + 1) # OMX_Index.h: 296

OMX_IndexParamDisableResourceConcealment = (OMX_IndexReserved_0x0100000E + 1) # OMX_Index.h: 296

OMX_IndexConfigMetadataItemCount = (OMX_IndexParamDisableResourceConcealment + 1) # OMX_Index.h: 296

OMX_IndexConfigContainerNodeCount = (OMX_IndexConfigMetadataItemCount + 1) # OMX_Index.h: 296

OMX_IndexConfigMetadataItem = (OMX_IndexConfigContainerNodeCount + 1) # OMX_Index.h: 296

OMX_IndexConfigCounterNodeID = (OMX_IndexConfigMetadataItem + 1) # OMX_Index.h: 296

OMX_IndexParamMetadataFilterType = (OMX_IndexConfigCounterNodeID + 1) # OMX_Index.h: 296

OMX_IndexParamMetadataKeyFilter = (OMX_IndexParamMetadataFilterType + 1) # OMX_Index.h: 296

OMX_IndexConfigPriorityMgmt = (OMX_IndexParamMetadataKeyFilter + 1) # OMX_Index.h: 296

OMX_IndexParamStandardComponentRole = (OMX_IndexConfigPriorityMgmt + 1) # OMX_Index.h: 296

OMX_IndexConfigContentURI = (OMX_IndexParamStandardComponentRole + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonPortCapturing = (OMX_IndexConfigContentURI + 1) # OMX_Index.h: 296

OMX_IndexConfigTunneledPortStatus = (OMX_IndexConfigCommonPortCapturing + 1) # OMX_Index.h: 296

OMX_IndexPortStartUnused = 33554432 # OMX_Index.h: 296

OMX_IndexParamPortDefinition = (OMX_IndexPortStartUnused + 1) # OMX_Index.h: 296

OMX_IndexParamCompBufferSupplier = (OMX_IndexParamPortDefinition + 1) # OMX_Index.h: 296

OMX_IndexReservedStartUnused = 50331648 # OMX_Index.h: 296

OMX_IndexAudioStartUnused = 67108864 # OMX_Index.h: 296

OMX_IndexParamAudioPortFormat = (OMX_IndexAudioStartUnused + 1) # OMX_Index.h: 296

OMX_IndexParamAudioPcm = (OMX_IndexParamAudioPortFormat + 1) # OMX_Index.h: 296

OMX_IndexParamAudioAac = (OMX_IndexParamAudioPcm + 1) # OMX_Index.h: 296

OMX_IndexParamAudioRa = (OMX_IndexParamAudioAac + 1) # OMX_Index.h: 296

OMX_IndexParamAudioMp3 = (OMX_IndexParamAudioRa + 1) # OMX_Index.h: 296

OMX_IndexParamAudioAdpcm = (OMX_IndexParamAudioMp3 + 1) # OMX_Index.h: 296

OMX_IndexParamAudioG723 = (OMX_IndexParamAudioAdpcm + 1) # OMX_Index.h: 296

OMX_IndexParamAudioG729 = (OMX_IndexParamAudioG723 + 1) # OMX_Index.h: 296

OMX_IndexParamAudioAmr = (OMX_IndexParamAudioG729 + 1) # OMX_Index.h: 296

OMX_IndexParamAudioWma = (OMX_IndexParamAudioAmr + 1) # OMX_Index.h: 296

OMX_IndexParamAudioSbc = (OMX_IndexParamAudioWma + 1) # OMX_Index.h: 296

OMX_IndexParamAudioMidi = (OMX_IndexParamAudioSbc + 1) # OMX_Index.h: 296

OMX_IndexParamAudioGsm_FR = (OMX_IndexParamAudioMidi + 1) # OMX_Index.h: 296

OMX_IndexParamAudioMidiLoadUserSound = (OMX_IndexParamAudioGsm_FR + 1) # OMX_Index.h: 296

OMX_IndexParamAudioG726 = (OMX_IndexParamAudioMidiLoadUserSound + 1) # OMX_Index.h: 296

OMX_IndexParamAudioGsm_EFR = (OMX_IndexParamAudioG726 + 1) # OMX_Index.h: 296

OMX_IndexParamAudioGsm_HR = (OMX_IndexParamAudioGsm_EFR + 1) # OMX_Index.h: 296

OMX_IndexParamAudioPdc_FR = (OMX_IndexParamAudioGsm_HR + 1) # OMX_Index.h: 296

OMX_IndexParamAudioPdc_EFR = (OMX_IndexParamAudioPdc_FR + 1) # OMX_Index.h: 296

OMX_IndexParamAudioPdc_HR = (OMX_IndexParamAudioPdc_EFR + 1) # OMX_Index.h: 296

OMX_IndexParamAudioTdma_FR = (OMX_IndexParamAudioPdc_HR + 1) # OMX_Index.h: 296

OMX_IndexParamAudioTdma_EFR = (OMX_IndexParamAudioTdma_FR + 1) # OMX_Index.h: 296

OMX_IndexParamAudioQcelp8 = (OMX_IndexParamAudioTdma_EFR + 1) # OMX_Index.h: 296

OMX_IndexParamAudioQcelp13 = (OMX_IndexParamAudioQcelp8 + 1) # OMX_Index.h: 296

OMX_IndexParamAudioEvrc = (OMX_IndexParamAudioQcelp13 + 1) # OMX_Index.h: 296

OMX_IndexParamAudioSmv = (OMX_IndexParamAudioEvrc + 1) # OMX_Index.h: 296

OMX_IndexParamAudioVorbis = (OMX_IndexParamAudioSmv + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioMidiImmediateEvent = (OMX_IndexParamAudioVorbis + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioMidiControl = (OMX_IndexConfigAudioMidiImmediateEvent + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioMidiSoundBankProgram = (OMX_IndexConfigAudioMidiControl + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioMidiStatus = (OMX_IndexConfigAudioMidiSoundBankProgram + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioMidiMetaEvent = (OMX_IndexConfigAudioMidiStatus + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioMidiMetaEventData = (OMX_IndexConfigAudioMidiMetaEvent + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioVolume = (OMX_IndexConfigAudioMidiMetaEventData + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioBalance = (OMX_IndexConfigAudioVolume + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioChannelMute = (OMX_IndexConfigAudioBalance + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioMute = (OMX_IndexConfigAudioChannelMute + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioLoudness = (OMX_IndexConfigAudioMute + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioEchoCancelation = (OMX_IndexConfigAudioLoudness + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioNoiseReduction = (OMX_IndexConfigAudioEchoCancelation + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioBass = (OMX_IndexConfigAudioNoiseReduction + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioTreble = (OMX_IndexConfigAudioBass + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioStereoWidening = (OMX_IndexConfigAudioTreble + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioChorus = (OMX_IndexConfigAudioStereoWidening + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioEqualizer = (OMX_IndexConfigAudioChorus + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioReverberation = (OMX_IndexConfigAudioEqualizer + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioChannelVolume = (OMX_IndexConfigAudioReverberation + 1) # OMX_Index.h: 296

OMX_IndexConfigAudio3DOutput = (OMX_IndexConfigAudioChannelVolume + 1) # OMX_Index.h: 296

OMX_IndexConfigAudio3DLocation = (OMX_IndexConfigAudio3DOutput + 1) # OMX_Index.h: 296

OMX_IndexParamAudio3DDopplerMode = (OMX_IndexConfigAudio3DLocation + 1) # OMX_Index.h: 296

OMX_IndexConfigAudio3DDopplerSettings = (OMX_IndexParamAudio3DDopplerMode + 1) # OMX_Index.h: 296

OMX_IndexConfigAudio3DLevels = (OMX_IndexConfigAudio3DDopplerSettings + 1) # OMX_Index.h: 296

OMX_IndexConfigAudio3DDistanceAttenuation = (OMX_IndexConfigAudio3DLevels + 1) # OMX_Index.h: 296

OMX_IndexConfigAudio3DDirectivitySettings = (OMX_IndexConfigAudio3DDistanceAttenuation + 1) # OMX_Index.h: 296

OMX_IndexConfigAudio3DDirectivityOrientation = (OMX_IndexConfigAudio3DDirectivitySettings + 1) # OMX_Index.h: 296

OMX_IndexConfigAudio3DMacroscopicOrientation = (OMX_IndexConfigAudio3DDirectivityOrientation + 1) # OMX_Index.h: 296

OMX_IndexConfigAudio3DMacroscopicSize = (OMX_IndexConfigAudio3DMacroscopicOrientation + 1) # OMX_Index.h: 296

OMX_IndexParamAudioQueryChannelMapping = (OMX_IndexConfigAudio3DMacroscopicSize + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioSbcBitpool = (OMX_IndexParamAudioQueryChannelMapping + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioAmrMode = (OMX_IndexConfigAudioSbcBitpool + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioBitrate = (OMX_IndexConfigAudioAmrMode + 1) # OMX_Index.h: 296

OMX_IndexConfigAudioAMRISFIndex = (OMX_IndexConfigAudioBitrate + 1) # OMX_Index.h: 296

OMX_IndexParamAudioFixedPoint = (OMX_IndexConfigAudioAMRISFIndex + 1) # OMX_Index.h: 296

OMX_IndexImageStartUnused = 83886080 # OMX_Index.h: 296

OMX_IndexParamImagePortFormat = (OMX_IndexImageStartUnused + 1) # OMX_Index.h: 296

OMX_IndexParamFlashControl = (OMX_IndexParamImagePortFormat + 1) # OMX_Index.h: 296

OMX_IndexConfigFocusControl = (OMX_IndexParamFlashControl + 1) # OMX_Index.h: 296

OMX_IndexParamQFactor = (OMX_IndexConfigFocusControl + 1) # OMX_Index.h: 296

OMX_IndexParamQuantizationTable = (OMX_IndexParamQFactor + 1) # OMX_Index.h: 296

OMX_IndexParamHuffmanTable = (OMX_IndexParamQuantizationTable + 1) # OMX_Index.h: 296

OMX_IndexConfigFlashControl = (OMX_IndexParamHuffmanTable + 1) # OMX_Index.h: 296

OMX_IndexConfigFlickerRejection = (OMX_IndexConfigFlashControl + 1) # OMX_Index.h: 296

OMX_IndexConfigImageHistogram = (OMX_IndexConfigFlickerRejection + 1) # OMX_Index.h: 296

OMX_IndexConfigImageHistogramData = (OMX_IndexConfigImageHistogram + 1) # OMX_Index.h: 296

OMX_IndexConfigImageHistogramInfo = (OMX_IndexConfigImageHistogramData + 1) # OMX_Index.h: 296

OMX_IndexConfigImageCaptureStarted = (OMX_IndexConfigImageHistogramInfo + 1) # OMX_Index.h: 296

OMX_IndexConfigImageCaptureEnded = (OMX_IndexConfigImageCaptureStarted + 1) # OMX_Index.h: 296

OMX_IndexVideoStartUnused = 100663296 # OMX_Index.h: 296

OMX_IndexParamVideoPortFormat = (OMX_IndexVideoStartUnused + 1) # OMX_Index.h: 296

OMX_IndexParamVideoQuantization = (OMX_IndexParamVideoPortFormat + 1) # OMX_Index.h: 296

OMX_IndexParamVideoFastUpdate = (OMX_IndexParamVideoQuantization + 1) # OMX_Index.h: 296

OMX_IndexParamVideoBitrate = (OMX_IndexParamVideoFastUpdate + 1) # OMX_Index.h: 296

OMX_IndexParamVideoMotionVector = (OMX_IndexParamVideoBitrate + 1) # OMX_Index.h: 296

OMX_IndexParamVideoIntraRefresh = (OMX_IndexParamVideoMotionVector + 1) # OMX_Index.h: 296

OMX_IndexParamVideoErrorCorrection = (OMX_IndexParamVideoIntraRefresh + 1) # OMX_Index.h: 296

OMX_IndexParamVideoVBSMC = (OMX_IndexParamVideoErrorCorrection + 1) # OMX_Index.h: 296

OMX_IndexParamVideoMpeg2 = (OMX_IndexParamVideoVBSMC + 1) # OMX_Index.h: 296

OMX_IndexParamVideoMpeg4 = (OMX_IndexParamVideoMpeg2 + 1) # OMX_Index.h: 296

OMX_IndexParamVideoWmv = (OMX_IndexParamVideoMpeg4 + 1) # OMX_Index.h: 296

OMX_IndexParamVideoRv = (OMX_IndexParamVideoWmv + 1) # OMX_Index.h: 296

OMX_IndexParamVideoAvc = (OMX_IndexParamVideoRv + 1) # OMX_Index.h: 296

OMX_IndexParamVideoH263 = (OMX_IndexParamVideoAvc + 1) # OMX_Index.h: 296

OMX_IndexParamVideoProfileLevelQuerySupported = (OMX_IndexParamVideoH263 + 1) # OMX_Index.h: 296

OMX_IndexParamVideoProfileLevelCurrent = (OMX_IndexParamVideoProfileLevelQuerySupported + 1) # OMX_Index.h: 296

OMX_IndexConfigVideoBitrate = (OMX_IndexParamVideoProfileLevelCurrent + 1) # OMX_Index.h: 296

OMX_IndexConfigVideoFramerate = (OMX_IndexConfigVideoBitrate + 1) # OMX_Index.h: 296

OMX_IndexConfigVideoIntraVOPRefresh = (OMX_IndexConfigVideoFramerate + 1) # OMX_Index.h: 296

OMX_IndexConfigVideoIntraMBRefresh = (OMX_IndexConfigVideoIntraVOPRefresh + 1) # OMX_Index.h: 296

OMX_IndexConfigVideoMBErrorReporting = (OMX_IndexConfigVideoIntraMBRefresh + 1) # OMX_Index.h: 296

OMX_IndexParamVideoMacroblocksPerFrame = (OMX_IndexConfigVideoMBErrorReporting + 1) # OMX_Index.h: 296

OMX_IndexConfigVideoMacroBlockErrorMap = (OMX_IndexParamVideoMacroblocksPerFrame + 1) # OMX_Index.h: 296

OMX_IndexParamVideoSliceFMO = (OMX_IndexConfigVideoMacroBlockErrorMap + 1) # OMX_Index.h: 296

OMX_IndexConfigVideoAVCIntraPeriod = (OMX_IndexParamVideoSliceFMO + 1) # OMX_Index.h: 296

OMX_IndexConfigVideoNalSize = (OMX_IndexConfigVideoAVCIntraPeriod + 1) # OMX_Index.h: 296

OMX_IndexParamNalStreamFormatSupported = (OMX_IndexConfigVideoNalSize + 1) # OMX_Index.h: 296

OMX_IndexParamNalStreamFormat = (OMX_IndexParamNalStreamFormatSupported + 1) # OMX_Index.h: 296

OMX_IndexParamNalStreamFormatSelect = (OMX_IndexParamNalStreamFormat + 1) # OMX_Index.h: 296

OMX_IndexParamVideoVC1 = (OMX_IndexParamNalStreamFormatSelect + 1) # OMX_Index.h: 296

OMX_IndexConfigVideoIntraPeriod = (OMX_IndexParamVideoVC1 + 1) # OMX_Index.h: 296

OMX_IndexConfigVideoIntraRefresh = (OMX_IndexConfigVideoIntraPeriod + 1) # OMX_Index.h: 296

OMX_IndexParamVideoVp8 = (OMX_IndexConfigVideoIntraRefresh + 1) # OMX_Index.h: 296

OMX_IndexConfigVideoVp8ReferenceFrame = (OMX_IndexParamVideoVp8 + 1) # OMX_Index.h: 296

OMX_IndexConfigVideoVp8ReferenceFrameType = (OMX_IndexConfigVideoVp8ReferenceFrame + 1) # OMX_Index.h: 296

OMX_IndexCommonStartUnused = 117440512 # OMX_Index.h: 296

OMX_IndexParamCommonDeblocking = (OMX_IndexCommonStartUnused + 1) # OMX_Index.h: 296

OMX_IndexParamCommonSensorMode = (OMX_IndexParamCommonDeblocking + 1) # OMX_Index.h: 296

OMX_IndexParamCommonInterleave = (OMX_IndexParamCommonSensorMode + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonColorFormatConversion = (OMX_IndexParamCommonInterleave + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonScale = (OMX_IndexConfigCommonColorFormatConversion + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonImageFilter = (OMX_IndexConfigCommonScale + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonColorEnhancement = (OMX_IndexConfigCommonImageFilter + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonColorKey = (OMX_IndexConfigCommonColorEnhancement + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonColorBlend = (OMX_IndexConfigCommonColorKey + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonFrameStabilisation = (OMX_IndexConfigCommonColorBlend + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonRotate = (OMX_IndexConfigCommonFrameStabilisation + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonMirror = (OMX_IndexConfigCommonRotate + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonOutputPosition = (OMX_IndexConfigCommonMirror + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonInputCrop = (OMX_IndexConfigCommonOutputPosition + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonOutputCrop = (OMX_IndexConfigCommonInputCrop + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonDigitalZoom = (OMX_IndexConfigCommonOutputCrop + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonOpticalZoom = (OMX_IndexConfigCommonDigitalZoom + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonWhiteBalance = (OMX_IndexConfigCommonOpticalZoom + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonExposure = (OMX_IndexConfigCommonWhiteBalance + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonContrast = (OMX_IndexConfigCommonExposure + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonBrightness = (OMX_IndexConfigCommonContrast + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonBacklight = (OMX_IndexConfigCommonBrightness + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonGamma = (OMX_IndexConfigCommonBacklight + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonSaturation = (OMX_IndexConfigCommonGamma + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonLightness = (OMX_IndexConfigCommonSaturation + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonExclusionRect = (OMX_IndexConfigCommonLightness + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonDithering = (OMX_IndexConfigCommonExclusionRect + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonPlaneBlend = (OMX_IndexConfigCommonDithering + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonExposureValue = (OMX_IndexConfigCommonPlaneBlend + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonOutputSize = (OMX_IndexConfigCommonExposureValue + 1) # OMX_Index.h: 296

OMX_IndexParamCommonExtraQuantData = (OMX_IndexConfigCommonOutputSize + 1) # OMX_Index.h: 296

OMX_IndexReserved_0x0700002A = (OMX_IndexParamCommonExtraQuantData + 1) # OMX_Index.h: 296

OMX_IndexReserved_0x0700002B = (OMX_IndexReserved_0x0700002A + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonTransitionEffect = (OMX_IndexReserved_0x0700002B + 1) # OMX_Index.h: 296

OMX_IndexConfigSharpness = (OMX_IndexConfigCommonTransitionEffect + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonExtDigitalZoom = (OMX_IndexConfigSharpness + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonExtOpticalZoom = (OMX_IndexConfigCommonExtDigitalZoom + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonCenterFieldOfView = (OMX_IndexConfigCommonExtOpticalZoom + 1) # OMX_Index.h: 296

OMX_IndexConfigImageExposureLock = (OMX_IndexConfigCommonCenterFieldOfView + 1) # OMX_Index.h: 296

OMX_IndexConfigImageWhiteBalanceLock = (OMX_IndexConfigImageExposureLock + 1) # OMX_Index.h: 296

OMX_IndexConfigImageFocusLock = (OMX_IndexConfigImageWhiteBalanceLock + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonFocusRange = (OMX_IndexConfigImageFocusLock + 1) # OMX_Index.h: 296

OMX_IndexConfigImageFlashStatus = (OMX_IndexConfigCommonFocusRange + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonExtCaptureMode = (OMX_IndexConfigImageFlashStatus + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonNDFilterControl = (OMX_IndexConfigCommonExtCaptureMode + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonAFAssistantLight = (OMX_IndexConfigCommonNDFilterControl + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonFocusRegionStatus = (OMX_IndexConfigCommonAFAssistantLight + 1) # OMX_Index.h: 296

OMX_IndexConfigCommonFocusRegionControl = (OMX_IndexConfigCommonFocusRegionStatus + 1) # OMX_Index.h: 296

OMX_IndexParamInterlaceFormat = (OMX_IndexConfigCommonFocusRegionControl + 1) # OMX_Index.h: 296

OMX_IndexConfigDeInterlace = (OMX_IndexParamInterlaceFormat + 1) # OMX_Index.h: 296

OMX_IndexConfigStreamInterlaceFormats = (OMX_IndexConfigDeInterlace + 1) # OMX_Index.h: 296

OMX_IndexOtherStartUnused = 134217728 # OMX_Index.h: 296

OMX_IndexParamOtherPortFormat = (OMX_IndexOtherStartUnused + 1) # OMX_Index.h: 296

OMX_IndexConfigOtherPower = (OMX_IndexParamOtherPortFormat + 1) # OMX_Index.h: 296

OMX_IndexConfigOtherStats = (OMX_IndexConfigOtherPower + 1) # OMX_Index.h: 296

OMX_IndexTimeStartUnused = 150994944 # OMX_Index.h: 296

OMX_IndexConfigTimeScale = (OMX_IndexTimeStartUnused + 1) # OMX_Index.h: 296

OMX_IndexConfigTimeClockState = (OMX_IndexConfigTimeScale + 1) # OMX_Index.h: 296

OMX_IndexReserved_0x90000003 = (OMX_IndexConfigTimeClockState + 1) # OMX_Index.h: 296

OMX_IndexConfigTimeCurrentMediaTime = (OMX_IndexReserved_0x90000003 + 1) # OMX_Index.h: 296

OMX_IndexConfigTimeCurrentWallTime = (OMX_IndexConfigTimeCurrentMediaTime + 1) # OMX_Index.h: 296

OMX_IndexReserved_0x09000006 = (OMX_IndexConfigTimeCurrentWallTime + 1) # OMX_Index.h: 296

OMX_IndexReserved_0x09000007 = (OMX_IndexReserved_0x09000006 + 1) # OMX_Index.h: 296

OMX_IndexConfigTimeMediaTimeRequest = (OMX_IndexReserved_0x09000007 + 1) # OMX_Index.h: 296

OMX_IndexConfigTimeClientStartTime = (OMX_IndexConfigTimeMediaTimeRequest + 1) # OMX_Index.h: 296

OMX_IndexConfigTimePosition = (OMX_IndexConfigTimeClientStartTime + 1) # OMX_Index.h: 296

OMX_IndexConfigTimeSeekMode = (OMX_IndexConfigTimePosition + 1) # OMX_Index.h: 296

OMX_IndexConfigTimeCurrentReference = (OMX_IndexConfigTimeSeekMode + 1) # OMX_Index.h: 296

OMX_IndexConfigTimeActiveRefClockUpdate = (OMX_IndexConfigTimeCurrentReference + 1) # OMX_Index.h: 296

OMX_IndexConfigTimeRenderingDelay = (OMX_IndexConfigTimeActiveRefClockUpdate + 1) # OMX_Index.h: 296

OMX_IndexConfigTimeUpdate = (OMX_IndexConfigTimeRenderingDelay + 1) # OMX_Index.h: 296

OMX_IndexCommonIndependentStartUnused = 167772160 # OMX_Index.h: 296

OMX_IndexConfigCommitMode = (OMX_IndexCommonIndependentStartUnused + 1) # OMX_Index.h: 296

OMX_IndexConfigCommit = (OMX_IndexConfigCommitMode + 1) # OMX_Index.h: 296

OMX_IndexConfigCallbackRequest = (OMX_IndexConfigCommit + 1) # OMX_Index.h: 296

OMX_IndexParamMediaContainer = (OMX_IndexConfigCallbackRequest + 1) # OMX_Index.h: 296

OMX_IndexParamReadOnlyBuffers = (OMX_IndexParamMediaContainer + 1) # OMX_Index.h: 296

OMX_IndexKhronosExtensions = 1862270976 # OMX_Index.h: 296

OMX_IndexVendorStartUnused = 2130706432 # OMX_Index.h: 296

OMX_IndexMax = 2147483647 # OMX_Index.h: 296

OMX_INDEXTYPE = enum_OMX_INDEXTYPE # OMX_Index.h: 296

enum_OMX_COMMANDTYPE = c_int # OMX_Core.h: 56

OMX_CommandStateSet = 0 # OMX_Core.h: 56

OMX_CommandFlush = (OMX_CommandStateSet + 1) # OMX_Core.h: 56

OMX_CommandPortDisable = (OMX_CommandFlush + 1) # OMX_Core.h: 56

OMX_CommandPortEnable = (OMX_CommandPortDisable + 1) # OMX_Core.h: 56

OMX_CommandMarkBuffer = (OMX_CommandPortEnable + 1) # OMX_Core.h: 56

OMX_CommandKhronosExtensions = 1862270976 # OMX_Core.h: 56

OMX_CommandVendorStartUnused = 2130706432 # OMX_Core.h: 56

OMX_CommandMax = 2147483647 # OMX_Core.h: 56

OMX_COMMANDTYPE = enum_OMX_COMMANDTYPE # OMX_Core.h: 56

enum_OMX_STATETYPE = c_int # OMX_Core.h: 69

OMX_StateReserved_0x00000000 = 0 # OMX_Core.h: 69

OMX_StateLoaded = (OMX_StateReserved_0x00000000 + 1) # OMX_Core.h: 69

OMX_StateIdle = (OMX_StateLoaded + 1) # OMX_Core.h: 69

OMX_StateExecuting = (OMX_StateIdle + 1) # OMX_Core.h: 69

OMX_StatePause = (OMX_StateExecuting + 1) # OMX_Core.h: 69

OMX_StateWaitForResources = (OMX_StatePause + 1) # OMX_Core.h: 69

OMX_StateKhronosExtensions = 1862270976 # OMX_Core.h: 69

OMX_StateVendorStartUnused = 2130706432 # OMX_Core.h: 69

OMX_StateMax = 2147483647 # OMX_Core.h: 69

OMX_STATETYPE = enum_OMX_STATETYPE # OMX_Core.h: 69

enum_OMX_ERRORTYPE = c_int # OMX_Core.h: 166

OMX_ErrorNone = 0 # OMX_Core.h: 166

OMX_ErrorInsufficientResources = 2147487744L # OMX_Core.h: 166

OMX_ErrorUndefined = 2147487745L # OMX_Core.h: 166

OMX_ErrorInvalidComponentName = 2147487746L # OMX_Core.h: 166

OMX_ErrorComponentNotFound = 2147487747L # OMX_Core.h: 166

OMX_ErrorReserved_0x80001004 = 2147487748L # OMX_Core.h: 166

OMX_ErrorBadParameter = 2147487749L # OMX_Core.h: 166

OMX_ErrorNotImplemented = 2147487750L # OMX_Core.h: 166

OMX_ErrorUnderflow = 2147487751L # OMX_Core.h: 166

OMX_ErrorOverflow = 2147487752L # OMX_Core.h: 166

OMX_ErrorHardware = 2147487753L # OMX_Core.h: 166

OMX_ErrorReserved_0x8000100A = 2147487754L # OMX_Core.h: 166

OMX_ErrorStreamCorrupt = 2147487755L # OMX_Core.h: 166

OMX_ErrorPortsNotCompatible = 2147487756L # OMX_Core.h: 166

OMX_ErrorResourcesLost = 2147487757L # OMX_Core.h: 166

OMX_ErrorNoMore = 2147487758L # OMX_Core.h: 166

OMX_ErrorVersionMismatch = 2147487759L # OMX_Core.h: 166

OMX_ErrorNotReady = 2147487760L # OMX_Core.h: 166

OMX_ErrorTimeout = 2147487761L # OMX_Core.h: 166

OMX_ErrorSameState = 2147487762L # OMX_Core.h: 166

OMX_ErrorResourcesPreempted = 2147487763L # OMX_Core.h: 166

OMX_ErrorReserved_0x80001014 = 2147487764L # OMX_Core.h: 166

OMX_ErrorReserved_0x80001015 = 2147487765L # OMX_Core.h: 166

OMX_ErrorReserved_0x80001016 = 2147487766L # OMX_Core.h: 166

OMX_ErrorIncorrectStateTransition = 2147487767L # OMX_Core.h: 166

OMX_ErrorIncorrectStateOperation = 2147487768L # OMX_Core.h: 166

OMX_ErrorUnsupportedSetting = 2147487769L # OMX_Core.h: 166

OMX_ErrorUnsupportedIndex = 2147487770L # OMX_Core.h: 166

OMX_ErrorBadPortIndex = 2147487771L # OMX_Core.h: 166

OMX_ErrorPortUnpopulated = 2147487772L # OMX_Core.h: 166

OMX_ErrorComponentSuspended = 2147487773L # OMX_Core.h: 166

OMX_ErrorDynamicResourcesUnavailable = 2147487774L # OMX_Core.h: 166

OMX_ErrorMbErrorsInFrame = 2147487775L # OMX_Core.h: 166

OMX_ErrorFormatNotDetected = 2147487776L # OMX_Core.h: 166

OMX_ErrorReserved_0x80001021 = 2147487777L # OMX_Core.h: 166

OMX_ErrorReserved_0x80001022 = 2147487778L # OMX_Core.h: 166

OMX_ErrorSeperateTablesUsed = 2147487779L # OMX_Core.h: 166

OMX_ErrorTunnelingUnsupported = 2147487780L # OMX_Core.h: 166

OMX_ErrorInvalidMode = 2147487781L # OMX_Core.h: 166

OMX_ErrorStreamCorruptStalled = 2147487782L # OMX_Core.h: 166

OMX_ErrorStreamCorruptFatal = 2147487783L # OMX_Core.h: 166

OMX_ErrorPortsNotConnected = 2147487784L # OMX_Core.h: 166

OMX_ErrorContentURINotSpecified = 2147487785L # OMX_Core.h: 166

OMX_ErrorContentURIError = 2147487786L # OMX_Core.h: 166

OMX_ErrorCommandCanceled = 2147487787L # OMX_Core.h: 166

OMX_ErrorKhronosExtensions = 2399141888L # OMX_Core.h: 166

OMX_ErrorVendorStartUnused = 2415919104L # OMX_Core.h: 166

OMX_ErrorMax = 2147483647 # OMX_Core.h: 166

OMX_ERRORTYPE = enum_OMX_ERRORTYPE # OMX_Core.h: 166

OMX_COMPONENTINITTYPE = CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE) # OMX_Core.h: 168

# OMX_Core.h: 174
class struct_OMX_COMPONENTREGISTERTYPE(Structure):
    pass

struct_OMX_COMPONENTREGISTERTYPE.__slots__ = [
    'pName',
    'pInitialize',
]
struct_OMX_COMPONENTREGISTERTYPE._fields_ = [
    ('pName', String),
    ('pInitialize', OMX_COMPONENTINITTYPE),
]

OMX_COMPONENTREGISTERTYPE = struct_OMX_COMPONENTREGISTERTYPE # OMX_Core.h: 174

# OMX_Core.h: 176
for _lib in _libs.values():
    try:
        OMX_ComponentRegistered = (POINTER(OMX_COMPONENTREGISTERTYPE)).in_dll(_lib, 'OMX_ComponentRegistered')
        break
    except:
        pass

# OMX_Core.h: 183
class struct_OMX_PRIORITYMGMTTYPE(Structure):
    pass

struct_OMX_PRIORITYMGMTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nGroupPriority',
    'nGroupID',
]
struct_OMX_PRIORITYMGMTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nGroupPriority', OMX_U32),
    ('nGroupID', OMX_U32),
]

OMX_PRIORITYMGMTTYPE = struct_OMX_PRIORITYMGMTTYPE # OMX_Core.h: 183

# OMX_Core.h: 191
class struct_OMX_PARAM_COMPONENTROLETYPE(Structure):
    pass

struct_OMX_PARAM_COMPONENTROLETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'cRole',
]
struct_OMX_PARAM_COMPONENTROLETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('cRole', OMX_U8 * 128),
]

OMX_PARAM_COMPONENTROLETYPE = struct_OMX_PARAM_COMPONENTROLETYPE # OMX_Core.h: 191

# OMX_Core.h: 225
class struct_OMX_BUFFERHEADERTYPE(Structure):
    pass

struct_OMX_BUFFERHEADERTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'pBuffer',
    'nAllocLen',
    'nFilledLen',
    'nOffset',
    'pAppPrivate',
    'pPlatformPrivate',
    'pInputPortPrivate',
    'pOutputPortPrivate',
    'hMarkTargetComponent',
    'pMarkData',
    'nTickCount',
    'nTimeStamp',
    'nFlags',
    'nOutputPortIndex',
    'nInputPortIndex',
]
struct_OMX_BUFFERHEADERTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('pBuffer', POINTER(OMX_U8)),
    ('nAllocLen', OMX_U32),
    ('nFilledLen', OMX_U32),
    ('nOffset', OMX_U32),
    ('pAppPrivate', OMX_PTR),
    ('pPlatformPrivate', OMX_PTR),
    ('pInputPortPrivate', OMX_PTR),
    ('pOutputPortPrivate', OMX_PTR),
    ('hMarkTargetComponent', OMX_HANDLETYPE),
    ('pMarkData', OMX_PTR),
    ('nTickCount', OMX_U32),
    ('nTimeStamp', OMX_TICKS),
    ('nFlags', OMX_U32),
    ('nOutputPortIndex', OMX_U32),
    ('nInputPortIndex', OMX_U32),
]

OMX_BUFFERHEADERTYPE = struct_OMX_BUFFERHEADERTYPE # OMX_Core.h: 225

enum_OMX_EXTRADATATYPE = c_int # OMX_Core.h: 235

OMX_ExtraDataNone = 0 # OMX_Core.h: 235

OMX_ExtraDataQuantization = (OMX_ExtraDataNone + 1) # OMX_Core.h: 235

OMX_ExtraDataInterlaceFormat = (OMX_ExtraDataQuantization + 1) # OMX_Core.h: 235

OMX_ExtraDataKhronosExtensions = 1862270976 # OMX_Core.h: 235

OMX_ExtraDataVendorStartUnused = 2130706432 # OMX_Core.h: 235

OMX_ExtraDataMax = 2147483647 # OMX_Core.h: 235

OMX_EXTRADATATYPE = enum_OMX_EXTRADATATYPE # OMX_Core.h: 235

# OMX_Core.h: 244
class struct_OMX_OTHER_EXTRADATATYPE(Structure):
    pass

struct_OMX_OTHER_EXTRADATATYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eType',
    'nDataSize',
    'data',
]
struct_OMX_OTHER_EXTRADATATYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eType', OMX_EXTRADATATYPE),
    ('nDataSize', OMX_U32),
    ('data', OMX_U8 * 1),
]

OMX_OTHER_EXTRADATATYPE = struct_OMX_OTHER_EXTRADATATYPE # OMX_Core.h: 244

# OMX_Core.h: 251
class struct_OMX_PORT_PARAM_TYPE(Structure):
    pass

struct_OMX_PORT_PARAM_TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPorts',
    'nStartPortNumber',
]
struct_OMX_PORT_PARAM_TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPorts', OMX_U32),
    ('nStartPortNumber', OMX_U32),
]

OMX_PORT_PARAM_TYPE = struct_OMX_PORT_PARAM_TYPE # OMX_Core.h: 251

enum_OMX_EVENTTYPE = c_int # OMX_Core.h: 270

OMX_EventCmdComplete = 0 # OMX_Core.h: 270

OMX_EventError = (OMX_EventCmdComplete + 1) # OMX_Core.h: 270

OMX_EventMark = (OMX_EventError + 1) # OMX_Core.h: 270

OMX_EventPortSettingsChanged = (OMX_EventMark + 1) # OMX_Core.h: 270

OMX_EventBufferFlag = (OMX_EventPortSettingsChanged + 1) # OMX_Core.h: 270

OMX_EventResourcesAcquired = (OMX_EventBufferFlag + 1) # OMX_Core.h: 270

OMX_EventComponentResumed = (OMX_EventResourcesAcquired + 1) # OMX_Core.h: 270

OMX_EventDynamicResourcesAvailable = (OMX_EventComponentResumed + 1) # OMX_Core.h: 270

OMX_EventPortFormatDetected = (OMX_EventDynamicResourcesAvailable + 1) # OMX_Core.h: 270

OMX_EventIndexSettingChanged = (OMX_EventPortFormatDetected + 1) # OMX_Core.h: 270

OMX_EventPortNeedsDisable = (OMX_EventIndexSettingChanged + 1) # OMX_Core.h: 270

OMX_EventPortNeedsFlush = (OMX_EventPortNeedsDisable + 1) # OMX_Core.h: 270

OMX_EventKhronosExtensions = 1862270976 # OMX_Core.h: 270

OMX_EventVendorStartUnused = 2130706432 # OMX_Core.h: 270

OMX_EventMax = 2147483647 # OMX_Core.h: 270

OMX_EVENTTYPE = enum_OMX_EVENTTYPE # OMX_Core.h: 270

# OMX_Core.h: 290
class struct_OMX_CALLBACKTYPE(Structure):
    pass

struct_OMX_CALLBACKTYPE.__slots__ = [
    'EventHandler',
    'EmptyBufferDone',
    'FillBufferDone',
]
struct_OMX_CALLBACKTYPE._fields_ = [
    ('EventHandler', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, OMX_PTR, OMX_EVENTTYPE, OMX_U32, OMX_U32, OMX_PTR)),
    ('EmptyBufferDone', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, OMX_PTR, POINTER(OMX_BUFFERHEADERTYPE))),
    ('FillBufferDone', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, OMX_PTR, POINTER(OMX_BUFFERHEADERTYPE))),
]

OMX_CALLBACKTYPE = struct_OMX_CALLBACKTYPE # OMX_Core.h: 290

enum_OMX_BUFFERSUPPLIERTYPE = c_int # OMX_Core.h: 300

OMX_BufferSupplyUnspecified = 0 # OMX_Core.h: 300

OMX_BufferSupplyInput = (OMX_BufferSupplyUnspecified + 1) # OMX_Core.h: 300

OMX_BufferSupplyOutput = (OMX_BufferSupplyInput + 1) # OMX_Core.h: 300

OMX_BufferSupplyKhronosExtensions = 1862270976 # OMX_Core.h: 300

OMX_BufferSupplyVendorStartUnused = 2130706432 # OMX_Core.h: 300

OMX_BufferSupplyMax = 2147483647 # OMX_Core.h: 300

OMX_BUFFERSUPPLIERTYPE = enum_OMX_BUFFERSUPPLIERTYPE # OMX_Core.h: 300

# OMX_Core.h: 307
class struct_OMX_PARAM_BUFFERSUPPLIERTYPE(Structure):
    pass

struct_OMX_PARAM_BUFFERSUPPLIERTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eBufferSupplier',
]
struct_OMX_PARAM_BUFFERSUPPLIERTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eBufferSupplier', OMX_BUFFERSUPPLIERTYPE),
]

OMX_PARAM_BUFFERSUPPLIERTYPE = struct_OMX_PARAM_BUFFERSUPPLIERTYPE # OMX_Core.h: 307

# OMX_Core.h: 315
class struct_OMX_TUNNELSETUPTYPE(Structure):
    pass

struct_OMX_TUNNELSETUPTYPE.__slots__ = [
    'nTunnelFlags',
    'eSupplier',
]
struct_OMX_TUNNELSETUPTYPE._fields_ = [
    ('nTunnelFlags', OMX_U32),
    ('eSupplier', OMX_BUFFERSUPPLIERTYPE),
]

OMX_TUNNELSETUPTYPE = struct_OMX_TUNNELSETUPTYPE # OMX_Core.h: 315

# OMX_Core.h: 466
if hasattr(_libs['libtizcore.so'], 'OMX_Init'):
    OMX_Init = _libs['libtizcore.so'].OMX_Init
    OMX_Init.argtypes = []
    OMX_Init.restype = OMX_ERRORTYPE

# OMX_Core.h: 468
if hasattr(_libs['libtizcore.so'], 'OMX_Deinit'):
    OMX_Deinit = _libs['libtizcore.so'].OMX_Deinit
    OMX_Deinit.argtypes = []
    OMX_Deinit.restype = OMX_ERRORTYPE

# OMX_Core.h: 470
if hasattr(_libs['libtizcore.so'], 'OMX_ComponentNameEnum'):
    OMX_ComponentNameEnum = _libs['libtizcore.so'].OMX_ComponentNameEnum
    OMX_ComponentNameEnum.argtypes = [OMX_STRING, OMX_U32, OMX_U32]
    OMX_ComponentNameEnum.restype = OMX_ERRORTYPE

# OMX_Core.h: 475
if hasattr(_libs['libtizcore.so'], 'OMX_GetHandle'):
    OMX_GetHandle = _libs['libtizcore.so'].OMX_GetHandle
    OMX_GetHandle.argtypes = [POINTER(OMX_HANDLETYPE), OMX_STRING, OMX_PTR, POINTER(OMX_CALLBACKTYPE)]
    OMX_GetHandle.restype = OMX_ERRORTYPE

# OMX_Core.h: 481
if hasattr(_libs['libtizcore.so'], 'OMX_FreeHandle'):
    OMX_FreeHandle = _libs['libtizcore.so'].OMX_FreeHandle
    OMX_FreeHandle.argtypes = [OMX_HANDLETYPE]
    OMX_FreeHandle.restype = OMX_ERRORTYPE

# OMX_Core.h: 484
if hasattr(_libs['libtizcore.so'], 'OMX_SetupTunnel'):
    OMX_SetupTunnel = _libs['libtizcore.so'].OMX_SetupTunnel
    OMX_SetupTunnel.argtypes = [OMX_HANDLETYPE, OMX_U32, OMX_HANDLETYPE, OMX_U32]
    OMX_SetupTunnel.restype = OMX_ERRORTYPE

# OMX_Core.h: 490
if hasattr(_libs['libtizcore.so'], 'OMX_TeardownTunnel'):
    OMX_TeardownTunnel = _libs['libtizcore.so'].OMX_TeardownTunnel
    OMX_TeardownTunnel.argtypes = [OMX_HANDLETYPE, OMX_U32, OMX_HANDLETYPE, OMX_U32]
    OMX_TeardownTunnel.restype = OMX_ERRORTYPE

# OMX_Core.h: 496
if hasattr(_libs['libtizcore.so'], 'OMX_ComponentOfRoleEnum'):
    OMX_ComponentOfRoleEnum = _libs['libtizcore.so'].OMX_ComponentOfRoleEnum
    OMX_ComponentOfRoleEnum.argtypes = [OMX_STRING, OMX_STRING, OMX_U32]
    OMX_ComponentOfRoleEnum.restype = OMX_ERRORTYPE

# OMX_Core.h: 501
if hasattr(_libs['libtizcore.so'], 'OMX_RoleOfComponentEnum'):
    OMX_RoleOfComponentEnum = _libs['libtizcore.so'].OMX_RoleOfComponentEnum
    OMX_RoleOfComponentEnum.argtypes = [OMX_STRING, OMX_STRING, OMX_U32]
    OMX_RoleOfComponentEnum.restype = OMX_ERRORTYPE

# OMX_Core.h: 512
class struct_OMX_CONFIG_CALLBACKREQUESTTYPE(Structure):
    pass

struct_OMX_CONFIG_CALLBACKREQUESTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nIndex',
    'bEnable',
]
struct_OMX_CONFIG_CALLBACKREQUESTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nIndex', OMX_INDEXTYPE),
    ('bEnable', OMX_BOOL),
]

OMX_CONFIG_CALLBACKREQUESTTYPE = struct_OMX_CONFIG_CALLBACKREQUESTTYPE # OMX_Core.h: 512

# OMX_Core.h: 515
if hasattr(_libs['libtizcore.so'], 'OMX_GetCoreInterface'):
    OMX_GetCoreInterface = _libs['libtizcore.so'].OMX_GetCoreInterface
    OMX_GetCoreInterface.argtypes = [POINTER(POINTER(None)), OMX_STRING]
    OMX_GetCoreInterface.restype = OMX_ERRORTYPE

# OMX_Core.h: 519
if hasattr(_libs['libtizcore.so'], 'OMX_FreeCoreInterface'):
    OMX_FreeCoreInterface = _libs['libtizcore.so'].OMX_FreeCoreInterface
    OMX_FreeCoreInterface.argtypes = [POINTER(None)]
    OMX_FreeCoreInterface.restype = None

enum_OMX_AUDIO_CODINGTYPE = c_int # OMX_Audio.h: 77

OMX_AUDIO_CodingUnused = 0 # OMX_Audio.h: 77

OMX_AUDIO_CodingAutoDetect = (OMX_AUDIO_CodingUnused + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingPCM = (OMX_AUDIO_CodingAutoDetect + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingADPCM = (OMX_AUDIO_CodingPCM + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingAMR = (OMX_AUDIO_CodingADPCM + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingGSMFR = (OMX_AUDIO_CodingAMR + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingGSMEFR = (OMX_AUDIO_CodingGSMFR + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingGSMHR = (OMX_AUDIO_CodingGSMEFR + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingPDCFR = (OMX_AUDIO_CodingGSMHR + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingPDCEFR = (OMX_AUDIO_CodingPDCFR + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingPDCHR = (OMX_AUDIO_CodingPDCEFR + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingTDMAFR = (OMX_AUDIO_CodingPDCHR + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingTDMAEFR = (OMX_AUDIO_CodingTDMAFR + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingQCELP8 = (OMX_AUDIO_CodingTDMAEFR + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingQCELP13 = (OMX_AUDIO_CodingQCELP8 + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingEVRC = (OMX_AUDIO_CodingQCELP13 + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingSMV = (OMX_AUDIO_CodingEVRC + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingG711 = (OMX_AUDIO_CodingSMV + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingG723 = (OMX_AUDIO_CodingG711 + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingG726 = (OMX_AUDIO_CodingG723 + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingG729 = (OMX_AUDIO_CodingG726 + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingAAC = (OMX_AUDIO_CodingG729 + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingMP3 = (OMX_AUDIO_CodingAAC + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingSBC = (OMX_AUDIO_CodingMP3 + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingVORBIS = (OMX_AUDIO_CodingSBC + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingWMA = (OMX_AUDIO_CodingVORBIS + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingRA = (OMX_AUDIO_CodingWMA + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingMIDI = (OMX_AUDIO_CodingRA + 1) # OMX_Audio.h: 77

OMX_AUDIO_CodingKhronosExtensions = 1862270976 # OMX_Audio.h: 77

OMX_AUDIO_CodingVendorStartUnused = 2130706432 # OMX_Audio.h: 77

# START: Tizonia extensions
OMX_AUDIO_CodingOPUS = (OMX_AUDIO_CodingVendorStartUnused + 1)
OMX_AUDIO_CodingFLAC = (OMX_AUDIO_CodingOPUS + 1)
OMX_AUDIO_CodingSPEEX = (OMX_AUDIO_CodingFLAC + 1)
OMX_AUDIO_CodingOGA = (OMX_AUDIO_CodingSPEEX + 1)
# END: Tizonia extensions

OMX_AUDIO_CodingMax = 2147483647 # OMX_Audio.h: 77

OMX_AUDIO_CODINGTYPE = enum_OMX_AUDIO_CODINGTYPE # OMX_Audio.h: 77

# OMX_Audio.h: 83
class struct_OMX_AUDIO_PORTDEFINITIONTYPE(Structure):
    pass

struct_OMX_AUDIO_PORTDEFINITIONTYPE.__slots__ = [
    'pNativeRender',
    'bFlagErrorConcealment',
    'eEncoding',
]
struct_OMX_AUDIO_PORTDEFINITIONTYPE._fields_ = [
    ('pNativeRender', OMX_NATIVE_DEVICETYPE),
    ('bFlagErrorConcealment', OMX_BOOL),
    ('eEncoding', OMX_AUDIO_CODINGTYPE),
]

OMX_AUDIO_PORTDEFINITIONTYPE = struct_OMX_AUDIO_PORTDEFINITIONTYPE # OMX_Audio.h: 83

# OMX_Audio.h: 91
class struct_OMX_AUDIO_PARAM_PORTFORMATTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_PORTFORMATTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nIndex',
    'eEncoding',
]
struct_OMX_AUDIO_PARAM_PORTFORMATTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nIndex', OMX_U32),
    ('eEncoding', OMX_AUDIO_CODINGTYPE),
]

OMX_AUDIO_PARAM_PORTFORMATTYPE = struct_OMX_AUDIO_PARAM_PORTFORMATTYPE # OMX_Audio.h: 91

enum_OMX_AUDIO_PCMMODETYPE = c_int # OMX_Audio.h: 100

OMX_AUDIO_PCMModeLinear = 0 # OMX_Audio.h: 100

OMX_AUDIO_PCMModeALaw = (OMX_AUDIO_PCMModeLinear + 1) # OMX_Audio.h: 100

OMX_AUDIO_PCMModeMULaw = (OMX_AUDIO_PCMModeALaw + 1) # OMX_Audio.h: 100

OMX_AUDIO_PCMModeKhronosExtensions = 1862270976 # OMX_Audio.h: 100

OMX_AUDIO_PCMModeVendorStartUnused = 2130706432 # OMX_Audio.h: 100

OMX_AUDIO_PCMModeMax = 2147483647 # OMX_Audio.h: 100

OMX_AUDIO_PCMMODETYPE = enum_OMX_AUDIO_PCMMODETYPE # OMX_Audio.h: 100

enum_OMX_AUDIO_CHANNELTYPE = c_int # OMX_Audio.h: 128

OMX_AUDIO_ChannelNone = 0 # OMX_Audio.h: 128

OMX_AUDIO_ChannelLF = 1 # OMX_Audio.h: 128

OMX_AUDIO_ChannelRF = 2 # OMX_Audio.h: 128

OMX_AUDIO_ChannelCF = 3 # OMX_Audio.h: 128

OMX_AUDIO_ChannelLS = 4 # OMX_Audio.h: 128

OMX_AUDIO_ChannelRS = 5 # OMX_Audio.h: 128

OMX_AUDIO_ChannelLFE = 6 # OMX_Audio.h: 128

OMX_AUDIO_ChannelCS = 7 # OMX_Audio.h: 128

OMX_AUDIO_ChannelLR = 8 # OMX_Audio.h: 128

OMX_AUDIO_ChannelRR = 9 # OMX_Audio.h: 128

OMX_AUDIO_ChannelLCF = 10 # OMX_Audio.h: 128

OMX_AUDIO_ChannelRCF = 11 # OMX_Audio.h: 128

OMX_AUDIO_ChannelLHS = 12 # OMX_Audio.h: 128

OMX_AUDIO_ChannelRHS = 13 # OMX_Audio.h: 128

OMX_AUDIO_ChannelCT = 14 # OMX_Audio.h: 128

OMX_AUDIO_ChannelFLT = 15 # OMX_Audio.h: 128

OMX_AUDIO_ChannelFCT = 16 # OMX_Audio.h: 128

OMX_AUDIO_ChannelFRT = 17 # OMX_Audio.h: 128

OMX_AUDIO_ChannelBLT = 18 # OMX_Audio.h: 128

OMX_AUDIO_ChannelBCT = 19 # OMX_Audio.h: 128

OMX_AUDIO_ChannelBRT = 20 # OMX_Audio.h: 128

OMX_AUDIO_ChannelUnknown = 1862270975 # OMX_Audio.h: 128

OMX_AUDIO_ChannelKhronosExtensions = 1862270976 # OMX_Audio.h: 128

OMX_AUDIO_ChannelVendorStartUnused = 2130706432 # OMX_Audio.h: 128

OMX_AUDIO_ChannelMax = 2147483647 # OMX_Audio.h: 128

OMX_AUDIO_CHANNELTYPE = enum_OMX_AUDIO_CHANNELTYPE # OMX_Audio.h: 128

# OMX_Audio.h: 145
class struct_OMX_AUDIO_PARAM_PCMMODETYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_PCMMODETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'eNumData',
    'eEndian',
    'bInterleaved',
    'nBitPerSample',
    'nSamplingRate',
    'ePCMMode',
    'eChannelMapping',
]
struct_OMX_AUDIO_PARAM_PCMMODETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('eNumData', OMX_NUMERICALDATATYPE),
    ('eEndian', OMX_ENDIANTYPE),
    ('bInterleaved', OMX_BOOL),
    ('nBitPerSample', OMX_U32),
    ('nSamplingRate', OMX_U32),
    ('ePCMMode', OMX_AUDIO_PCMMODETYPE),
    ('eChannelMapping', OMX_AUDIO_CHANNELTYPE * 36),
]

OMX_AUDIO_PARAM_PCMMODETYPE = struct_OMX_AUDIO_PARAM_PCMMODETYPE # OMX_Audio.h: 145

enum_OMX_AUDIO_CHANNELMODETYPE = c_int # OMX_Audio.h: 155

OMX_AUDIO_ChannelModeStereo = 0 # OMX_Audio.h: 155

OMX_AUDIO_ChannelModeJointStereo = (OMX_AUDIO_ChannelModeStereo + 1) # OMX_Audio.h: 155

OMX_AUDIO_ChannelModeDual = (OMX_AUDIO_ChannelModeJointStereo + 1) # OMX_Audio.h: 155

OMX_AUDIO_ChannelModeMono = (OMX_AUDIO_ChannelModeDual + 1) # OMX_Audio.h: 155

OMX_AUDIO_ChannelModeKhronosExtensions = 1862270976 # OMX_Audio.h: 155

OMX_AUDIO_ChannelModeVendorStartUnused = 2130706432 # OMX_Audio.h: 155

OMX_AUDIO_ChannelModeMax = 2147483647 # OMX_Audio.h: 155

OMX_AUDIO_CHANNELMODETYPE = enum_OMX_AUDIO_CHANNELMODETYPE # OMX_Audio.h: 155

enum_OMX_AUDIO_MP3STREAMFORMATTYPE = c_int # OMX_Audio.h: 165

OMX_AUDIO_MP3StreamFormatMP1Layer3 = 0 # OMX_Audio.h: 165

OMX_AUDIO_MP3StreamFormatMP2Layer3 = (OMX_AUDIO_MP3StreamFormatMP1Layer3 + 1) # OMX_Audio.h: 165

OMX_AUDIO_MP3StreamFormatMP2_5Layer3 = (OMX_AUDIO_MP3StreamFormatMP2Layer3 + 1) # OMX_Audio.h: 165

OMX_AUDIO_MP3StreamFormatUnknown = 1862270975 # OMX_Audio.h: 165

OMX_AUDIO_MP3StreamFormatKhronosExtensions = 1862270976 # OMX_Audio.h: 165

OMX_AUDIO_MP3StreamFormatVendorStartUnused = 2130706432 # OMX_Audio.h: 165

OMX_AUDIO_MP3StreamFormatMax = 2147483647 # OMX_Audio.h: 165

OMX_AUDIO_MP3STREAMFORMATTYPE = enum_OMX_AUDIO_MP3STREAMFORMATTYPE # OMX_Audio.h: 165

# OMX_Audio.h: 177
class struct_OMX_AUDIO_PARAM_MP3TYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_MP3TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'nBitRate',
    'nSampleRate',
    'nAudioBandWidth',
    'eChannelMode',
    'eFormat',
]
struct_OMX_AUDIO_PARAM_MP3TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('nBitRate', OMX_U32),
    ('nSampleRate', OMX_U32),
    ('nAudioBandWidth', OMX_U32),
    ('eChannelMode', OMX_AUDIO_CHANNELMODETYPE),
    ('eFormat', OMX_AUDIO_MP3STREAMFORMATTYPE),
]

OMX_AUDIO_PARAM_MP3TYPE = struct_OMX_AUDIO_PARAM_MP3TYPE # OMX_Audio.h: 177

enum_OMX_AUDIO_AACSTREAMFORMATTYPE = c_int # OMX_Audio.h: 191

OMX_AUDIO_AACStreamFormatMP2ADTS = 0 # OMX_Audio.h: 191

OMX_AUDIO_AACStreamFormatMP4ADTS = (OMX_AUDIO_AACStreamFormatMP2ADTS + 1) # OMX_Audio.h: 191

OMX_AUDIO_AACStreamFormatMP4LOAS = (OMX_AUDIO_AACStreamFormatMP4ADTS + 1) # OMX_Audio.h: 191

OMX_AUDIO_AACStreamFormatMP4LATM = (OMX_AUDIO_AACStreamFormatMP4LOAS + 1) # OMX_Audio.h: 191

OMX_AUDIO_AACStreamFormatADIF = (OMX_AUDIO_AACStreamFormatMP4LATM + 1) # OMX_Audio.h: 191

OMX_AUDIO_AACStreamFormatMP4FF = (OMX_AUDIO_AACStreamFormatADIF + 1) # OMX_Audio.h: 191

OMX_AUDIO_AACStreamFormatRAW = (OMX_AUDIO_AACStreamFormatMP4FF + 1) # OMX_Audio.h: 191

OMX_AUDIO_AACStreamFormatUnknown = 1862270975 # OMX_Audio.h: 191

OMX_AUDIO_AACStreamFormatKhronosExtensions = 1862270976 # OMX_Audio.h: 191

OMX_AUDIO_AACStreamFormatVendorStartUnused = 2130706432 # OMX_Audio.h: 191

OMX_AUDIO_AACStreamFormatMax = 2147483647 # OMX_Audio.h: 191

OMX_AUDIO_AACSTREAMFORMATTYPE = enum_OMX_AUDIO_AACSTREAMFORMATTYPE # OMX_Audio.h: 191

enum_OMX_AUDIO_AACPROFILETYPE = c_int # OMX_Audio.h: 208

OMX_AUDIO_AACObjectNull = 0 # OMX_Audio.h: 208

OMX_AUDIO_AACObjectMain = 1 # OMX_Audio.h: 208

OMX_AUDIO_AACObjectLC = (OMX_AUDIO_AACObjectMain + 1) # OMX_Audio.h: 208

OMX_AUDIO_AACObjectSSR = (OMX_AUDIO_AACObjectLC + 1) # OMX_Audio.h: 208

OMX_AUDIO_AACObjectLTP = (OMX_AUDIO_AACObjectSSR + 1) # OMX_Audio.h: 208

OMX_AUDIO_AACObjectHE = (OMX_AUDIO_AACObjectLTP + 1) # OMX_Audio.h: 208

OMX_AUDIO_AACObjectScalable = (OMX_AUDIO_AACObjectHE + 1) # OMX_Audio.h: 208

OMX_AUDIO_AACObjectERLC = 17 # OMX_Audio.h: 208

OMX_AUDIO_AACObjectLD = 23 # OMX_Audio.h: 208

OMX_AUDIO_AACObjectHE_PS = 29 # OMX_Audio.h: 208

OMX_AUDIO_AACObjectUnknown = 1862270975 # OMX_Audio.h: 208

OMX_AUDIO_AACObjectKhronosExtensions = 1862270976 # OMX_Audio.h: 208

OMX_AUDIO_AACObjectVendorStartUnused = 2130706432 # OMX_Audio.h: 208

OMX_AUDIO_AACObjectMax = 2147483647 # OMX_Audio.h: 208

OMX_AUDIO_AACPROFILETYPE = enum_OMX_AUDIO_AACPROFILETYPE # OMX_Audio.h: 208

# OMX_Audio.h: 238
class struct_OMX_AUDIO_PARAM_AACPROFILETYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_AACPROFILETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'nSampleRate',
    'nBitRate',
    'nAudioBandWidth',
    'nFrameLength',
    'nAACtools',
    'nAACERtools',
    'eAACProfile',
    'eAACStreamFormat',
    'eChannelMode',
]
struct_OMX_AUDIO_PARAM_AACPROFILETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('nSampleRate', OMX_U32),
    ('nBitRate', OMX_U32),
    ('nAudioBandWidth', OMX_U32),
    ('nFrameLength', OMX_U32),
    ('nAACtools', OMX_U32),
    ('nAACERtools', OMX_U32),
    ('eAACProfile', OMX_AUDIO_AACPROFILETYPE),
    ('eAACStreamFormat', OMX_AUDIO_AACSTREAMFORMATTYPE),
    ('eChannelMode', OMX_AUDIO_CHANNELMODETYPE),
]

OMX_AUDIO_PARAM_AACPROFILETYPE = struct_OMX_AUDIO_PARAM_AACPROFILETYPE # OMX_Audio.h: 238

# OMX_Audio.h: 253
class struct_OMX_AUDIO_PARAM_VORBISTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_VORBISTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'nBitRate',
    'nMinBitRate',
    'nMaxBitRate',
    'nSampleRate',
    'nAudioBandWidth',
    'nQuality',
    'bManaged',
    'bDownmix',
]
struct_OMX_AUDIO_PARAM_VORBISTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('nBitRate', OMX_U32),
    ('nMinBitRate', OMX_U32),
    ('nMaxBitRate', OMX_U32),
    ('nSampleRate', OMX_U32),
    ('nAudioBandWidth', OMX_U32),
    ('nQuality', OMX_S32),
    ('bManaged', OMX_BOOL),
    ('bDownmix', OMX_BOOL),
]

OMX_AUDIO_PARAM_VORBISTYPE = struct_OMX_AUDIO_PARAM_VORBISTYPE # OMX_Audio.h: 253

enum_OMX_AUDIO_WMAFORMATTYPE = c_int # OMX_Audio.h: 269

OMX_AUDIO_WMAFormatUnused = 0 # OMX_Audio.h: 269

OMX_AUDIO_WMAFormat7 = (OMX_AUDIO_WMAFormatUnused + 1) # OMX_Audio.h: 269

OMX_AUDIO_WMAFormat8 = (OMX_AUDIO_WMAFormat7 + 1) # OMX_Audio.h: 269

OMX_AUDIO_WMAFormat9 = (OMX_AUDIO_WMAFormat8 + 1) # OMX_Audio.h: 269

OMX_AUDIO_WMAFormat9_Professional = (OMX_AUDIO_WMAFormat9 + 1) # OMX_Audio.h: 269

OMX_AUDIO_WMAFormat9_Lossless = (OMX_AUDIO_WMAFormat9_Professional + 1) # OMX_Audio.h: 269

OMX_AUDIO_WMAFormat9_Voice = (OMX_AUDIO_WMAFormat9_Lossless + 1) # OMX_Audio.h: 269

OMX_AUDIO_WMAFormat10_Professional = (OMX_AUDIO_WMAFormat9_Voice + 1) # OMX_Audio.h: 269

OMX_AUDIO_WMAFormat10_Voice = (OMX_AUDIO_WMAFormat10_Professional + 1) # OMX_Audio.h: 269

OMX_AUDIO_WMAFormatUnknown = 1862270975 # OMX_Audio.h: 269

OMX_AUDIO_WMAFormatKhronosExtensions = 1862270976 # OMX_Audio.h: 269

OMX_AUDIO_WMAFormatVendorStartUnused = 2130706432 # OMX_Audio.h: 269

OMX_AUDIO_WMAFormatMax = 2147483647 # OMX_Audio.h: 269

OMX_AUDIO_WMAFORMATTYPE = enum_OMX_AUDIO_WMAFORMATTYPE # OMX_Audio.h: 269

enum_OMX_AUDIO_WMAPROFILETYPE = c_int # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileUnused = 0 # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileL1 = (OMX_AUDIO_WMAProfileUnused + 1) # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileL2 = (OMX_AUDIO_WMAProfileL1 + 1) # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileL3 = (OMX_AUDIO_WMAProfileL2 + 1) # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileM0 = (OMX_AUDIO_WMAProfileL3 + 1) # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileM1 = (OMX_AUDIO_WMAProfileM0 + 1) # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileM2 = (OMX_AUDIO_WMAProfileM1 + 1) # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileM3 = (OMX_AUDIO_WMAProfileM2 + 1) # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileN1 = (OMX_AUDIO_WMAProfileM3 + 1) # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileN2 = (OMX_AUDIO_WMAProfileN1 + 1) # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileN3 = (OMX_AUDIO_WMAProfileN2 + 1) # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileS1 = (OMX_AUDIO_WMAProfileN3 + 1) # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileS2 = (OMX_AUDIO_WMAProfileS1 + 1) # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileUnknown = 1862270975 # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileKhronosExtensions = 1862270976 # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileVendorStartUnused = 2130706432 # OMX_Audio.h: 289

OMX_AUDIO_WMAProfileMax = 2147483647 # OMX_Audio.h: 289

OMX_AUDIO_WMAPROFILETYPE = enum_OMX_AUDIO_WMAPROFILETYPE # OMX_Audio.h: 289

# OMX_Audio.h: 306
class struct_OMX_AUDIO_PARAM_WMATYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_WMATYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'nBitRate',
    'eFormat',
    'eProfile',
    'nSamplingRate',
    'nBlockAlign',
    'nEncodeOptions',
    'nSuperBlockAlign',
    'nBitsPerSample',
    'nAdvancedEncodeOpt',
    'nAdvancedEncodeOpt2',
]
struct_OMX_AUDIO_PARAM_WMATYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U16),
    ('nBitRate', OMX_U32),
    ('eFormat', OMX_AUDIO_WMAFORMATTYPE),
    ('eProfile', OMX_AUDIO_WMAPROFILETYPE),
    ('nSamplingRate', OMX_U32),
    ('nBlockAlign', OMX_U16),
    ('nEncodeOptions', OMX_U16),
    ('nSuperBlockAlign', OMX_U32),
    ('nBitsPerSample', OMX_U32),
    ('nAdvancedEncodeOpt', OMX_U32),
    ('nAdvancedEncodeOpt2', OMX_U32),
]

OMX_AUDIO_PARAM_WMATYPE = struct_OMX_AUDIO_PARAM_WMATYPE # OMX_Audio.h: 306

enum_OMX_AUDIO_RAFORMATTYPE = c_int # OMX_Audio.h: 321

OMX_AUDIO_RAFormatUnused = 0 # OMX_Audio.h: 321

OMX_AUDIO_RA8 = (OMX_AUDIO_RAFormatUnused + 1) # OMX_Audio.h: 321

OMX_AUDIO_RA9 = (OMX_AUDIO_RA8 + 1) # OMX_Audio.h: 321

OMX_AUDIO_RA10_AAC = (OMX_AUDIO_RA9 + 1) # OMX_Audio.h: 321

OMX_AUDIO_RA10_CODEC = (OMX_AUDIO_RA10_AAC + 1) # OMX_Audio.h: 321

OMX_AUDIO_RA10_LOSSLESS = (OMX_AUDIO_RA10_CODEC + 1) # OMX_Audio.h: 321

OMX_AUDIO_RA10_MULTICHANNEL = (OMX_AUDIO_RA10_LOSSLESS + 1) # OMX_Audio.h: 321

OMX_AUDIO_RA10_VOICE = (OMX_AUDIO_RA10_MULTICHANNEL + 1) # OMX_Audio.h: 321

OMX_AUDIO_RAFormatUnknown = 1862270975 # OMX_Audio.h: 321

OMX_AUDIO_RAFormatKhronosExtensions = 1862270976 # OMX_Audio.h: 321

OMX_AUDIO_RAFormatVendorStartUnused = 2130706432 # OMX_Audio.h: 321

OMX_VIDEO_RAFormatMax = 2147483647 # OMX_Audio.h: 321

OMX_AUDIO_RAFORMATTYPE = enum_OMX_AUDIO_RAFORMATTYPE # OMX_Audio.h: 321

# OMX_Audio.h: 335
class struct_OMX_AUDIO_PARAM_RATYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_RATYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'nSamplingRate',
    'nBitsPerFrame',
    'nSamplePerFrame',
    'nCouplingQuantBits',
    'nCouplingStartRegion',
    'nNumRegions',
    'eFormat',
]
struct_OMX_AUDIO_PARAM_RATYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('nSamplingRate', OMX_U32),
    ('nBitsPerFrame', OMX_U32),
    ('nSamplePerFrame', OMX_U32),
    ('nCouplingQuantBits', OMX_U32),
    ('nCouplingStartRegion', OMX_U32),
    ('nNumRegions', OMX_U32),
    ('eFormat', OMX_AUDIO_RAFORMATTYPE),
]

OMX_AUDIO_PARAM_RATYPE = struct_OMX_AUDIO_PARAM_RATYPE # OMX_Audio.h: 335

enum_OMX_AUDIO_SBCALLOCMETHODTYPE = c_int # OMX_Audio.h: 343

OMX_AUDIO_SBCAllocMethodLoudness = 0 # OMX_Audio.h: 343

OMX_AUDIO_SBCAllocMethodSNR = (OMX_AUDIO_SBCAllocMethodLoudness + 1) # OMX_Audio.h: 343

OMX_AUDIO_SBCAllocMethodKhronosExtensions = 1862270976 # OMX_Audio.h: 343

OMX_AUDIO_SBCAllocMethodVendorStartUnused = 2130706432 # OMX_Audio.h: 343

OMX_AUDIO_SBCAllocMethodMax = 2147483647 # OMX_Audio.h: 343

OMX_AUDIO_SBCALLOCMETHODTYPE = enum_OMX_AUDIO_SBCALLOCMETHODTYPE # OMX_Audio.h: 343

# OMX_Audio.h: 358
class struct_OMX_AUDIO_PARAM_SBCTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_SBCTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'nBitRate',
    'nSampleRate',
    'nBlocks',
    'nSubbands',
    'nBitPool',
    'bEnableBitrate',
    'eChannelMode',
    'eSBCAllocType',
]
struct_OMX_AUDIO_PARAM_SBCTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('nBitRate', OMX_U32),
    ('nSampleRate', OMX_U32),
    ('nBlocks', OMX_U32),
    ('nSubbands', OMX_U32),
    ('nBitPool', OMX_U32),
    ('bEnableBitrate', OMX_BOOL),
    ('eChannelMode', OMX_AUDIO_CHANNELMODETYPE),
    ('eSBCAllocType', OMX_AUDIO_SBCALLOCMETHODTYPE),
]

OMX_AUDIO_PARAM_SBCTYPE = struct_OMX_AUDIO_PARAM_SBCTYPE # OMX_Audio.h: 358

# OMX_Audio.h: 368
class struct_OMX_AUDIO_PARAM_ADPCMTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_ADPCMTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'nBitsPerSample',
    'nSampleRate',
    'nBlockSize',
]
struct_OMX_AUDIO_PARAM_ADPCMTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('nBitsPerSample', OMX_U32),
    ('nSampleRate', OMX_U32),
    ('nBlockSize', OMX_U32),
]

OMX_AUDIO_PARAM_ADPCMTYPE = struct_OMX_AUDIO_PARAM_ADPCMTYPE # OMX_Audio.h: 368

enum_OMX_AUDIO_G723RATE = c_int # OMX_Audio.h: 377

OMX_AUDIO_G723ModeUnused = 0 # OMX_Audio.h: 377

OMX_AUDIO_G723ModeLow = (OMX_AUDIO_G723ModeUnused + 1) # OMX_Audio.h: 377

OMX_AUDIO_G723ModeHigh = (OMX_AUDIO_G723ModeLow + 1) # OMX_Audio.h: 377

OMX_AUDIO_G723ModeKhronosExtensions = 1862270976 # OMX_Audio.h: 377

OMX_AUDIO_G723ModeVendorStartUnused = 2130706432 # OMX_Audio.h: 377

OMX_AUDIO_G723ModeMax = 2147483647 # OMX_Audio.h: 377

OMX_AUDIO_G723RATE = enum_OMX_AUDIO_G723RATE # OMX_Audio.h: 377

# OMX_Audio.h: 388
class struct_OMX_AUDIO_PARAM_G723TYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_G723TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'bDTX',
    'eBitRate',
    'bHiPassFilter',
    'bPostFilter',
]
struct_OMX_AUDIO_PARAM_G723TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('bDTX', OMX_BOOL),
    ('eBitRate', OMX_AUDIO_G723RATE),
    ('bHiPassFilter', OMX_BOOL),
    ('bPostFilter', OMX_BOOL),
]

OMX_AUDIO_PARAM_G723TYPE = struct_OMX_AUDIO_PARAM_G723TYPE # OMX_Audio.h: 388

enum_OMX_AUDIO_G726MODE = c_int # OMX_Audio.h: 399

OMX_AUDIO_G726ModeUnused = 0 # OMX_Audio.h: 399

OMX_AUDIO_G726Mode16 = (OMX_AUDIO_G726ModeUnused + 1) # OMX_Audio.h: 399

OMX_AUDIO_G726Mode24 = (OMX_AUDIO_G726Mode16 + 1) # OMX_Audio.h: 399

OMX_AUDIO_G726Mode32 = (OMX_AUDIO_G726Mode24 + 1) # OMX_Audio.h: 399

OMX_AUDIO_G726Mode40 = (OMX_AUDIO_G726Mode32 + 1) # OMX_Audio.h: 399

OMX_AUDIO_G726ModeKhronosExtensions = 1862270976 # OMX_Audio.h: 399

OMX_AUDIO_G726ModeVendorStartUnused = 2130706432 # OMX_Audio.h: 399

OMX_AUDIO_G726ModeMax = 2147483647 # OMX_Audio.h: 399

OMX_AUDIO_G726MODE = enum_OMX_AUDIO_G726MODE # OMX_Audio.h: 399

# OMX_Audio.h: 407
class struct_OMX_AUDIO_PARAM_G726TYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_G726TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'eG726Mode',
]
struct_OMX_AUDIO_PARAM_G726TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('eG726Mode', OMX_AUDIO_G726MODE),
]

OMX_AUDIO_PARAM_G726TYPE = struct_OMX_AUDIO_PARAM_G726TYPE # OMX_Audio.h: 407

enum_OMX_AUDIO_G729TYPE = c_int # OMX_Audio.h: 417

OMX_AUDIO_G729 = 0 # OMX_Audio.h: 417

OMX_AUDIO_G729A = (OMX_AUDIO_G729 + 1) # OMX_Audio.h: 417

OMX_AUDIO_G729B = (OMX_AUDIO_G729A + 1) # OMX_Audio.h: 417

OMX_AUDIO_G729AB = (OMX_AUDIO_G729B + 1) # OMX_Audio.h: 417

OMX_AUDIO_G729KhronosExtensions = 1862270976 # OMX_Audio.h: 417

OMX_AUDIO_G729VendorStartUnused = 2130706432 # OMX_Audio.h: 417

OMX_AUDIO_G729Max = 2147483647 # OMX_Audio.h: 417

OMX_AUDIO_G729TYPE = enum_OMX_AUDIO_G729TYPE # OMX_Audio.h: 417

# OMX_Audio.h: 426
class struct_OMX_AUDIO_PARAM_G729TYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_G729TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'bDTX',
    'eBitType',
]
struct_OMX_AUDIO_PARAM_G729TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('bDTX', OMX_BOOL),
    ('eBitType', OMX_AUDIO_G729TYPE),
]

OMX_AUDIO_PARAM_G729TYPE = struct_OMX_AUDIO_PARAM_G729TYPE # OMX_Audio.h: 426

enum_OMX_AUDIO_AMRFRAMEFORMATTYPE = c_int # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatConformance = 0 # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatIF1 = (OMX_AUDIO_AMRFrameFormatConformance + 1) # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatIF2 = (OMX_AUDIO_AMRFrameFormatIF1 + 1) # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatFSF = (OMX_AUDIO_AMRFrameFormatIF2 + 1) # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatRTPPayloadFull = (OMX_AUDIO_AMRFrameFormatFSF + 1) # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatITU = (OMX_AUDIO_AMRFrameFormatRTPPayloadFull + 1) # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatRTPPayloadConstrained = (OMX_AUDIO_AMRFrameFormatITU + 1) # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatWBPlusTIF = (OMX_AUDIO_AMRFrameFormatRTPPayloadConstrained + 1) # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatWBPlusFSF = (OMX_AUDIO_AMRFrameFormatWBPlusTIF + 1) # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatWBPlusRTPPayloadBasic = (OMX_AUDIO_AMRFrameFormatWBPlusFSF + 1) # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatWBPlusRTPPayloadInterleaved = (OMX_AUDIO_AMRFrameFormatWBPlusRTPPayloadBasic + 1) # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatKhronosExtensions = 1862270976 # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatVendorStartUnused = 2130706432 # OMX_Audio.h: 443

OMX_AUDIO_AMRFrameFormatMax = 2147483647 # OMX_Audio.h: 443

OMX_AUDIO_AMRFRAMEFORMATTYPE = enum_OMX_AUDIO_AMRFRAMEFORMATTYPE # OMX_Audio.h: 443

enum_OMX_AUDIO_AMRBANDMODETYPE = c_int # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeUnused = 0 # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeNB0 = (OMX_AUDIO_AMRBandModeUnused + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeNB1 = (OMX_AUDIO_AMRBandModeNB0 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeNB2 = (OMX_AUDIO_AMRBandModeNB1 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeNB3 = (OMX_AUDIO_AMRBandModeNB2 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeNB4 = (OMX_AUDIO_AMRBandModeNB3 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeNB5 = (OMX_AUDIO_AMRBandModeNB4 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeNB6 = (OMX_AUDIO_AMRBandModeNB5 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeNB7 = (OMX_AUDIO_AMRBandModeNB6 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWB0 = (OMX_AUDIO_AMRBandModeNB7 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWB1 = (OMX_AUDIO_AMRBandModeWB0 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWB2 = (OMX_AUDIO_AMRBandModeWB1 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWB3 = (OMX_AUDIO_AMRBandModeWB2 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWB4 = (OMX_AUDIO_AMRBandModeWB3 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWB5 = (OMX_AUDIO_AMRBandModeWB4 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWB6 = (OMX_AUDIO_AMRBandModeWB5 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWB7 = (OMX_AUDIO_AMRBandModeWB6 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWB8 = (OMX_AUDIO_AMRBandModeWB7 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP0 = (OMX_AUDIO_AMRBandModeWB8 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP1 = (OMX_AUDIO_AMRBandModeWBP0 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP2 = (OMX_AUDIO_AMRBandModeWBP1 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP3 = (OMX_AUDIO_AMRBandModeWBP2 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP4 = (OMX_AUDIO_AMRBandModeWBP3 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP5 = (OMX_AUDIO_AMRBandModeWBP4 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP6 = (OMX_AUDIO_AMRBandModeWBP5 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP7 = (OMX_AUDIO_AMRBandModeWBP6 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP8 = (OMX_AUDIO_AMRBandModeWBP7 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP9 = (OMX_AUDIO_AMRBandModeWBP8 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP10 = (OMX_AUDIO_AMRBandModeWBP9 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP11 = (OMX_AUDIO_AMRBandModeWBP10 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP12 = (OMX_AUDIO_AMRBandModeWBP11 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP13 = (OMX_AUDIO_AMRBandModeWBP12 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP14 = (OMX_AUDIO_AMRBandModeWBP13 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP15 = (OMX_AUDIO_AMRBandModeWBP14 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP16 = (OMX_AUDIO_AMRBandModeWBP15 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP17 = (OMX_AUDIO_AMRBandModeWBP16 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP18 = (OMX_AUDIO_AMRBandModeWBP17 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP19 = (OMX_AUDIO_AMRBandModeWBP18 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP20 = (OMX_AUDIO_AMRBandModeWBP19 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP21 = (OMX_AUDIO_AMRBandModeWBP20 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP22 = (OMX_AUDIO_AMRBandModeWBP21 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP23 = (OMX_AUDIO_AMRBandModeWBP22 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP24 = (OMX_AUDIO_AMRBandModeWBP23 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP25 = (OMX_AUDIO_AMRBandModeWBP24 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP26 = (OMX_AUDIO_AMRBandModeWBP25 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP27 = (OMX_AUDIO_AMRBandModeWBP26 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP28 = (OMX_AUDIO_AMRBandModeWBP27 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP29 = (OMX_AUDIO_AMRBandModeWBP28 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP30 = (OMX_AUDIO_AMRBandModeWBP29 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP31 = (OMX_AUDIO_AMRBandModeWBP30 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP32 = (OMX_AUDIO_AMRBandModeWBP31 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP33 = (OMX_AUDIO_AMRBandModeWBP32 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP34 = (OMX_AUDIO_AMRBandModeWBP33 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP35 = (OMX_AUDIO_AMRBandModeWBP34 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP36 = (OMX_AUDIO_AMRBandModeWBP35 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP37 = (OMX_AUDIO_AMRBandModeWBP36 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP38 = (OMX_AUDIO_AMRBandModeWBP37 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP39 = (OMX_AUDIO_AMRBandModeWBP38 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP40 = (OMX_AUDIO_AMRBandModeWBP39 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP41 = (OMX_AUDIO_AMRBandModeWBP40 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP42 = (OMX_AUDIO_AMRBandModeWBP41 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP43 = (OMX_AUDIO_AMRBandModeWBP42 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP44 = (OMX_AUDIO_AMRBandModeWBP43 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP45 = (OMX_AUDIO_AMRBandModeWBP44 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP46 = (OMX_AUDIO_AMRBandModeWBP45 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeWBP47 = (OMX_AUDIO_AMRBandModeWBP46 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeAuto = (OMX_AUDIO_AMRBandModeWBP47 + 1) # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeKhronosExtensions = 1862270976 # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeVendorStartUnused = 2130706432 # OMX_Audio.h: 516

OMX_AUDIO_AMRBandModeMax = 2147483647 # OMX_Audio.h: 516

OMX_AUDIO_AMRBANDMODETYPE = enum_OMX_AUDIO_AMRBANDMODETYPE # OMX_Audio.h: 516

enum_OMX_AUDIO_AMRDTXMODETYPE = c_int # OMX_Audio.h: 527

OMX_AUDIO_AMRDTXModeOff = 0 # OMX_Audio.h: 527

OMX_AUDIO_AMRDTXModeOnVAD1 = (OMX_AUDIO_AMRDTXModeOff + 1) # OMX_Audio.h: 527

OMX_AUDIO_AMRDTXModeOnVAD2 = (OMX_AUDIO_AMRDTXModeOnVAD1 + 1) # OMX_Audio.h: 527

OMX_AUDIO_AMRDTXModeOnAuto = (OMX_AUDIO_AMRDTXModeOnVAD2 + 1) # OMX_Audio.h: 527

OMX_AUDIO_AMRDTXasEFR = (OMX_AUDIO_AMRDTXModeOnAuto + 1) # OMX_Audio.h: 527

OMX_AUDIO_AMRDTXModeKhronosExtensions = 1862270976 # OMX_Audio.h: 527

OMX_AUDIO_AMRDTXModeVendorStartUnused = 2130706432 # OMX_Audio.h: 527

OMX_AUDIO_AMRDTXModeMax = 2147483647 # OMX_Audio.h: 527

OMX_AUDIO_AMRDTXMODETYPE = enum_OMX_AUDIO_AMRDTXMODETYPE # OMX_Audio.h: 527

enum_OMX_AUDIO_AMRISFINDEXTYPE = c_int # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex0 = 0 # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex1 = (OMX_AUDIO_AMRISFIndex0 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex2 = (OMX_AUDIO_AMRISFIndex1 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex3 = (OMX_AUDIO_AMRISFIndex2 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex4 = (OMX_AUDIO_AMRISFIndex3 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex5 = (OMX_AUDIO_AMRISFIndex4 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex6 = (OMX_AUDIO_AMRISFIndex5 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex7 = (OMX_AUDIO_AMRISFIndex6 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex8 = (OMX_AUDIO_AMRISFIndex7 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex9 = (OMX_AUDIO_AMRISFIndex8 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex10 = (OMX_AUDIO_AMRISFIndex9 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex11 = (OMX_AUDIO_AMRISFIndex10 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex12 = (OMX_AUDIO_AMRISFIndex11 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndex13 = (OMX_AUDIO_AMRISFIndex12 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndexAuto = (OMX_AUDIO_AMRISFIndex13 + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndexUknown = (OMX_AUDIO_AMRISFIndexAuto + 1) # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndexKhronosExtensions = 1862270976 # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndexVendorStartUnused = 2130706432 # OMX_Audio.h: 549

OMX_AUDIO_AMRISFIndexMax = 2147483647 # OMX_Audio.h: 549

OMX_AUDIO_AMRISFINDEXTYPE = enum_OMX_AUDIO_AMRISFINDEXTYPE # OMX_Audio.h: 549

# OMX_Audio.h: 561
class struct_OMX_AUDIO_PARAM_AMRTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_AMRTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'nBitRate',
    'eAMRBandMode',
    'eAMRDTXMode',
    'eAMRFrameFormat',
    'eAMRISFIndex',
]
struct_OMX_AUDIO_PARAM_AMRTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('nBitRate', OMX_U32),
    ('eAMRBandMode', OMX_AUDIO_AMRBANDMODETYPE),
    ('eAMRDTXMode', OMX_AUDIO_AMRDTXMODETYPE),
    ('eAMRFrameFormat', OMX_AUDIO_AMRFRAMEFORMATTYPE),
    ('eAMRISFIndex', OMX_AUDIO_AMRISFINDEXTYPE),
]

OMX_AUDIO_PARAM_AMRTYPE = struct_OMX_AUDIO_PARAM_AMRTYPE # OMX_Audio.h: 561

# OMX_Audio.h: 569
class struct_OMX_AUDIO_PARAM_GSMFRTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_GSMFRTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bDTX',
    'bHiPassFilter',
]
struct_OMX_AUDIO_PARAM_GSMFRTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bDTX', OMX_BOOL),
    ('bHiPassFilter', OMX_BOOL),
]

OMX_AUDIO_PARAM_GSMFRTYPE = struct_OMX_AUDIO_PARAM_GSMFRTYPE # OMX_Audio.h: 569

# OMX_Audio.h: 577
class struct_OMX_AUDIO_PARAM_GSMHRTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_GSMHRTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bDTX',
    'bHiPassFilter',
]
struct_OMX_AUDIO_PARAM_GSMHRTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bDTX', OMX_BOOL),
    ('bHiPassFilter', OMX_BOOL),
]

OMX_AUDIO_PARAM_GSMHRTYPE = struct_OMX_AUDIO_PARAM_GSMHRTYPE # OMX_Audio.h: 577

# OMX_Audio.h: 585
class struct_OMX_AUDIO_PARAM_GSMEFRTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_GSMEFRTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bDTX',
    'bHiPassFilter',
]
struct_OMX_AUDIO_PARAM_GSMEFRTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bDTX', OMX_BOOL),
    ('bHiPassFilter', OMX_BOOL),
]

OMX_AUDIO_PARAM_GSMEFRTYPE = struct_OMX_AUDIO_PARAM_GSMEFRTYPE # OMX_Audio.h: 585

# OMX_Audio.h: 594
class struct_OMX_AUDIO_PARAM_TDMAFRTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_TDMAFRTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'bDTX',
    'bHiPassFilter',
]
struct_OMX_AUDIO_PARAM_TDMAFRTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('bDTX', OMX_BOOL),
    ('bHiPassFilter', OMX_BOOL),
]

OMX_AUDIO_PARAM_TDMAFRTYPE = struct_OMX_AUDIO_PARAM_TDMAFRTYPE # OMX_Audio.h: 594

# OMX_Audio.h: 603
class struct_OMX_AUDIO_PARAM_TDMAEFRTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_TDMAEFRTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'bDTX',
    'bHiPassFilter',
]
struct_OMX_AUDIO_PARAM_TDMAEFRTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('bDTX', OMX_BOOL),
    ('bHiPassFilter', OMX_BOOL),
]

OMX_AUDIO_PARAM_TDMAEFRTYPE = struct_OMX_AUDIO_PARAM_TDMAEFRTYPE # OMX_Audio.h: 603

# OMX_Audio.h: 612
class struct_OMX_AUDIO_PARAM_PDCFRTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_PDCFRTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'bDTX',
    'bHiPassFilter',
]
struct_OMX_AUDIO_PARAM_PDCFRTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('bDTX', OMX_BOOL),
    ('bHiPassFilter', OMX_BOOL),
]

OMX_AUDIO_PARAM_PDCFRTYPE = struct_OMX_AUDIO_PARAM_PDCFRTYPE # OMX_Audio.h: 612

# OMX_Audio.h: 621
class struct_OMX_AUDIO_PARAM_PDCEFRTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_PDCEFRTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'bDTX',
    'bHiPassFilter',
]
struct_OMX_AUDIO_PARAM_PDCEFRTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('bDTX', OMX_BOOL),
    ('bHiPassFilter', OMX_BOOL),
]

OMX_AUDIO_PARAM_PDCEFRTYPE = struct_OMX_AUDIO_PARAM_PDCEFRTYPE # OMX_Audio.h: 621

# OMX_Audio.h: 630
class struct_OMX_AUDIO_PARAM_PDCHRTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_PDCHRTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'bDTX',
    'bHiPassFilter',
]
struct_OMX_AUDIO_PARAM_PDCHRTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('bDTX', OMX_BOOL),
    ('bHiPassFilter', OMX_BOOL),
]

OMX_AUDIO_PARAM_PDCHRTYPE = struct_OMX_AUDIO_PARAM_PDCHRTYPE # OMX_Audio.h: 630

enum_OMX_AUDIO_CDMARATETYPE = c_int # OMX_Audio.h: 642

OMX_AUDIO_CDMARateBlank = 0 # OMX_Audio.h: 642

OMX_AUDIO_CDMARateFull = (OMX_AUDIO_CDMARateBlank + 1) # OMX_Audio.h: 642

OMX_AUDIO_CDMARateHalf = (OMX_AUDIO_CDMARateFull + 1) # OMX_Audio.h: 642

OMX_AUDIO_CDMARateQuarter = (OMX_AUDIO_CDMARateHalf + 1) # OMX_Audio.h: 642

OMX_AUDIO_CDMARateEighth = (OMX_AUDIO_CDMARateQuarter + 1) # OMX_Audio.h: 642

OMX_AUDIO_CDMARateErasure = (OMX_AUDIO_CDMARateEighth + 1) # OMX_Audio.h: 642

OMX_AUDIO_CDMARateKhronosExtensions = 1862270976 # OMX_Audio.h: 642

OMX_AUDIO_CDMARateVendorStartUnused = 2130706432 # OMX_Audio.h: 642

OMX_AUDIO_CDMARateMax = 2147483647 # OMX_Audio.h: 642

OMX_AUDIO_CDMARATETYPE = enum_OMX_AUDIO_CDMARATETYPE # OMX_Audio.h: 642

# OMX_Audio.h: 653
class struct_OMX_AUDIO_PARAM_QCELP8TYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_QCELP8TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'nBitRate',
    'eCDMARate',
    'nMinBitRate',
    'nMaxBitRate',
]
struct_OMX_AUDIO_PARAM_QCELP8TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('nBitRate', OMX_U32),
    ('eCDMARate', OMX_AUDIO_CDMARATETYPE),
    ('nMinBitRate', OMX_U32),
    ('nMaxBitRate', OMX_U32),
]

OMX_AUDIO_PARAM_QCELP8TYPE = struct_OMX_AUDIO_PARAM_QCELP8TYPE # OMX_Audio.h: 653

# OMX_Audio.h: 663
class struct_OMX_AUDIO_PARAM_QCELP13TYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_QCELP13TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'eCDMARate',
    'nMinBitRate',
    'nMaxBitRate',
]
struct_OMX_AUDIO_PARAM_QCELP13TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('eCDMARate', OMX_AUDIO_CDMARATETYPE),
    ('nMinBitRate', OMX_U32),
    ('nMaxBitRate', OMX_U32),
]

OMX_AUDIO_PARAM_QCELP13TYPE = struct_OMX_AUDIO_PARAM_QCELP13TYPE # OMX_Audio.h: 663

# OMX_Audio.h: 677
class struct_OMX_AUDIO_PARAM_EVRCTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_EVRCTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'eCDMARate',
    'bRATE_REDUCon',
    'nMinBitRate',
    'nMaxBitRate',
    'bHiPassFilter',
    'bNoiseSuppressor',
    'bPostFilter',
]
struct_OMX_AUDIO_PARAM_EVRCTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('eCDMARate', OMX_AUDIO_CDMARATETYPE),
    ('bRATE_REDUCon', OMX_BOOL),
    ('nMinBitRate', OMX_U32),
    ('nMaxBitRate', OMX_U32),
    ('bHiPassFilter', OMX_BOOL),
    ('bNoiseSuppressor', OMX_BOOL),
    ('bPostFilter', OMX_BOOL),
]

OMX_AUDIO_PARAM_EVRCTYPE = struct_OMX_AUDIO_PARAM_EVRCTYPE # OMX_Audio.h: 677

# OMX_Audio.h: 691
class struct_OMX_AUDIO_PARAM_SMVTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_SMVTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'eCDMARate',
    'bRATE_REDUCon',
    'nMinBitRate',
    'nMaxBitRate',
    'bHiPassFilter',
    'bNoiseSuppressor',
    'bPostFilter',
]
struct_OMX_AUDIO_PARAM_SMVTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('eCDMARate', OMX_AUDIO_CDMARATETYPE),
    ('bRATE_REDUCon', OMX_BOOL),
    ('nMinBitRate', OMX_U32),
    ('nMaxBitRate', OMX_U32),
    ('bHiPassFilter', OMX_BOOL),
    ('bNoiseSuppressor', OMX_BOOL),
    ('bPostFilter', OMX_BOOL),
]

OMX_AUDIO_PARAM_SMVTYPE = struct_OMX_AUDIO_PARAM_SMVTYPE # OMX_Audio.h: 691

enum_OMX_AUDIO_MIDIFORMATTYPE = c_int # OMX_Audio.h: 706

OMX_AUDIO_MIDIFormatUnknown = 0 # OMX_Audio.h: 706

OMX_AUDIO_MIDIFormatSMF0 = (OMX_AUDIO_MIDIFormatUnknown + 1) # OMX_Audio.h: 706

OMX_AUDIO_MIDIFormatSMF1 = (OMX_AUDIO_MIDIFormatSMF0 + 1) # OMX_Audio.h: 706

OMX_AUDIO_MIDIFormatSMF2 = (OMX_AUDIO_MIDIFormatSMF1 + 1) # OMX_Audio.h: 706

OMX_AUDIO_MIDIFormatSPMIDI = (OMX_AUDIO_MIDIFormatSMF2 + 1) # OMX_Audio.h: 706

OMX_AUDIO_MIDIFormatXMF0 = (OMX_AUDIO_MIDIFormatSPMIDI + 1) # OMX_Audio.h: 706

OMX_AUDIO_MIDIFormatXMF1 = (OMX_AUDIO_MIDIFormatXMF0 + 1) # OMX_Audio.h: 706

OMX_AUDIO_MIDIFormatMobileXMF = (OMX_AUDIO_MIDIFormatXMF1 + 1) # OMX_Audio.h: 706

OMX_AUDIO_MIDIFormatKhronosExtensions = 1862270976 # OMX_Audio.h: 706

OMX_AUDIO_MIDIFormatVendorStartUnused = 2130706432 # OMX_Audio.h: 706

OMX_AUDIO_MIDIFormatMax = 2147483647 # OMX_Audio.h: 706

OMX_AUDIO_MIDIFORMATTYPE = enum_OMX_AUDIO_MIDIFORMATTYPE # OMX_Audio.h: 706

# OMX_Audio.h: 716
class struct_OMX_AUDIO_PARAM_MIDITYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_MIDITYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nFileSize',
    'sMaxPolyphony',
    'bLoadDefaultSound',
    'eMidiFormat',
]
struct_OMX_AUDIO_PARAM_MIDITYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nFileSize', OMX_U32),
    ('sMaxPolyphony', OMX_BU32),
    ('bLoadDefaultSound', OMX_BOOL),
    ('eMidiFormat', OMX_AUDIO_MIDIFORMATTYPE),
]

OMX_AUDIO_PARAM_MIDITYPE = struct_OMX_AUDIO_PARAM_MIDITYPE # OMX_Audio.h: 716

enum_OMX_AUDIO_MIDISOUNDBANKTYPE = c_int # OMX_Audio.h: 727

OMX_AUDIO_MIDISoundBankUnused = 0 # OMX_Audio.h: 727

OMX_AUDIO_MIDISoundBankDLS1 = (OMX_AUDIO_MIDISoundBankUnused + 1) # OMX_Audio.h: 727

OMX_AUDIO_MIDISoundBankDLS2 = (OMX_AUDIO_MIDISoundBankDLS1 + 1) # OMX_Audio.h: 727

OMX_AUDIO_MIDISoundBankMobileDLSBase = (OMX_AUDIO_MIDISoundBankDLS2 + 1) # OMX_Audio.h: 727

OMX_AUDIO_MIDISoundBankMobileDLSPlusOptions = (OMX_AUDIO_MIDISoundBankMobileDLSBase + 1) # OMX_Audio.h: 727

OMX_AUDIO_MIDISoundBankKhronosExtensions = 1862270976 # OMX_Audio.h: 727

OMX_AUDIO_MIDISoundBankVendorStartUnused = 2130706432 # OMX_Audio.h: 727

OMX_AUDIO_MIDISoundBankMax = 2147483647 # OMX_Audio.h: 727

OMX_AUDIO_MIDISOUNDBANKTYPE = enum_OMX_AUDIO_MIDISOUNDBANKTYPE # OMX_Audio.h: 727

enum_OMX_AUDIO_MIDISOUNDBANKLAYOUTTYPE = c_int # OMX_Audio.h: 737

OMX_AUDIO_MIDISoundBankLayoutUnused = 0 # OMX_Audio.h: 737

OMX_AUDIO_MIDISoundBankLayoutGM = (OMX_AUDIO_MIDISoundBankLayoutUnused + 1) # OMX_Audio.h: 737

OMX_AUDIO_MIDISoundBankLayoutGM2 = (OMX_AUDIO_MIDISoundBankLayoutGM + 1) # OMX_Audio.h: 737

OMX_AUDIO_MIDISoundBankLayoutUser = (OMX_AUDIO_MIDISoundBankLayoutGM2 + 1) # OMX_Audio.h: 737

OMX_AUDIO_MIDISoundBankLayoutKhronosExtensions = 1862270976 # OMX_Audio.h: 737

OMX_AUDIO_MIDISoundBankLayoutVendorStartUnused = 2130706432 # OMX_Audio.h: 737

OMX_AUDIO_MIDISoundBankLayoutMax = 2147483647 # OMX_Audio.h: 737

OMX_AUDIO_MIDISOUNDBANKLAYOUTTYPE = enum_OMX_AUDIO_MIDISOUNDBANKLAYOUTTYPE # OMX_Audio.h: 737

# OMX_Audio.h: 748
class struct_OMX_AUDIO_PARAM_MIDILOADUSERSOUNDTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_MIDILOADUSERSOUNDTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nDLSIndex',
    'nDLSSize',
    'pDLSData',
    'eMidiSoundBank',
    'eMidiSoundBankLayout',
]
struct_OMX_AUDIO_PARAM_MIDILOADUSERSOUNDTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nDLSIndex', OMX_U32),
    ('nDLSSize', OMX_U32),
    ('pDLSData', OMX_PTR),
    ('eMidiSoundBank', OMX_AUDIO_MIDISOUNDBANKTYPE),
    ('eMidiSoundBankLayout', OMX_AUDIO_MIDISOUNDBANKLAYOUTTYPE),
]

OMX_AUDIO_PARAM_MIDILOADUSERSOUNDTYPE = struct_OMX_AUDIO_PARAM_MIDILOADUSERSOUNDTYPE # OMX_Audio.h: 748

# OMX_Audio.h: 756
class struct_OMX_AUDIO_CONFIG_MIDIIMMEDIATEEVENTTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_MIDIIMMEDIATEEVENTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nMidiEventSize',
    'nMidiEvents',
]
struct_OMX_AUDIO_CONFIG_MIDIIMMEDIATEEVENTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nMidiEventSize', OMX_U32),
    ('nMidiEvents', OMX_U8 * 1),
]

OMX_AUDIO_CONFIG_MIDIIMMEDIATEEVENTTYPE = struct_OMX_AUDIO_CONFIG_MIDIIMMEDIATEEVENTTYPE # OMX_Audio.h: 756

# OMX_Audio.h: 766
class struct_OMX_AUDIO_CONFIG_MIDISOUNDBANKPROGRAMTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_MIDISOUNDBANKPROGRAMTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannel',
    'nIDProgram',
    'nIDSoundBank',
    'nUserSoundBankIndex',
]
struct_OMX_AUDIO_CONFIG_MIDISOUNDBANKPROGRAMTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannel', OMX_U32),
    ('nIDProgram', OMX_U16),
    ('nIDSoundBank', OMX_U16),
    ('nUserSoundBankIndex', OMX_U32),
]

OMX_AUDIO_CONFIG_MIDISOUNDBANKPROGRAMTYPE = struct_OMX_AUDIO_CONFIG_MIDISOUNDBANKPROGRAMTYPE # OMX_Audio.h: 766

# OMX_Audio.h: 784
class struct_OMX_AUDIO_CONFIG_MIDICONTROLTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_MIDICONTROLTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'sPitchTransposition',
    'sPlayBackRate',
    'sTempo',
    'nMaxPolyphony',
    'nNumRepeat',
    'nStopTime',
    'nChannelMuteMask',
    'nChannelSoloMask',
    'nTrack0031MuteMask',
    'nTrack3263MuteMask',
    'nTrack0031SoloMask',
    'nTrack3263SoloMask',
]
struct_OMX_AUDIO_CONFIG_MIDICONTROLTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('sPitchTransposition', OMX_BS32),
    ('sPlayBackRate', OMX_BU32),
    ('sTempo', OMX_BU32),
    ('nMaxPolyphony', OMX_U32),
    ('nNumRepeat', OMX_U32),
    ('nStopTime', OMX_U32),
    ('nChannelMuteMask', OMX_U16),
    ('nChannelSoloMask', OMX_U16),
    ('nTrack0031MuteMask', OMX_U32),
    ('nTrack3263MuteMask', OMX_U32),
    ('nTrack0031SoloMask', OMX_U32),
    ('nTrack3263SoloMask', OMX_U32),
]

OMX_AUDIO_CONFIG_MIDICONTROLTYPE = struct_OMX_AUDIO_CONFIG_MIDICONTROLTYPE # OMX_Audio.h: 784

enum_OMX_AUDIO_MIDIPLAYBACKSTATETYPE = c_int # OMX_Audio.h: 797

OMX_AUDIO_MIDIPlayBackStateUnknown = 0 # OMX_Audio.h: 797

OMX_AUDIO_MIDIPlayBackStateClosedEngaged = (OMX_AUDIO_MIDIPlayBackStateUnknown + 1) # OMX_Audio.h: 797

OMX_AUDIO_MIDIPlayBackStateParsing = (OMX_AUDIO_MIDIPlayBackStateClosedEngaged + 1) # OMX_Audio.h: 797

OMX_AUDIO_MIDIPlayBackStateOpenEngaged = (OMX_AUDIO_MIDIPlayBackStateParsing + 1) # OMX_Audio.h: 797

OMX_AUDIO_MIDIPlayBackStatePlaying = (OMX_AUDIO_MIDIPlayBackStateOpenEngaged + 1) # OMX_Audio.h: 797

OMX_AUDIO_MIDIPlayBackStatePlayingPartially = (OMX_AUDIO_MIDIPlayBackStatePlaying + 1) # OMX_Audio.h: 797

OMX_AUDIO_MIDIPlayBackStatePlayingSilently = (OMX_AUDIO_MIDIPlayBackStatePlayingPartially + 1) # OMX_Audio.h: 797

OMX_AUDIO_MIDIPlayBackStateKhronosExtensions = 1862270976 # OMX_Audio.h: 797

OMX_AUDIO_MIDIPlayBackStateVendorStartUnused = 2130706432 # OMX_Audio.h: 797

OMX_AUDIO_MIDIPlayBackStateMax = 2147483647 # OMX_Audio.h: 797

OMX_AUDIO_MIDIPLAYBACKSTATETYPE = enum_OMX_AUDIO_MIDIPLAYBACKSTATETYPE # OMX_Audio.h: 797

# OMX_Audio.h: 810
class struct_OMX_AUDIO_CONFIG_MIDISTATUSTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_MIDISTATUSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nNumTracks',
    'nDuration',
    'nPosition',
    'bVibra',
    'nNumMetaEvents',
    'nNumActiveVoices',
    'eMIDIPlayBackState',
]
struct_OMX_AUDIO_CONFIG_MIDISTATUSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nNumTracks', OMX_U16),
    ('nDuration', OMX_U32),
    ('nPosition', OMX_U32),
    ('bVibra', OMX_BOOL),
    ('nNumMetaEvents', OMX_U32),
    ('nNumActiveVoices', OMX_U32),
    ('eMIDIPlayBackState', OMX_AUDIO_MIDIPLAYBACKSTATETYPE),
]

OMX_AUDIO_CONFIG_MIDISTATUSTYPE = struct_OMX_AUDIO_CONFIG_MIDISTATUSTYPE # OMX_Audio.h: 810

# OMX_Audio.h: 821
class struct_OMX_AUDIO_CONFIG_MIDIMETAEVENTTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_MIDIMETAEVENTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nIndex',
    'nMetaEventType',
    'nMetaEventSize',
    'nTrack',
    'nPosition',
]
struct_OMX_AUDIO_CONFIG_MIDIMETAEVENTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nIndex', OMX_U32),
    ('nMetaEventType', OMX_U8),
    ('nMetaEventSize', OMX_U32),
    ('nTrack', OMX_U32),
    ('nPosition', OMX_U32),
]

OMX_AUDIO_CONFIG_MIDIMETAEVENTTYPE = struct_OMX_AUDIO_CONFIG_MIDIMETAEVENTTYPE # OMX_Audio.h: 821

# OMX_Audio.h: 830
class struct_OMX_AUDIO_CONFIG_MIDIMETAEVENTDATATYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_MIDIMETAEVENTDATATYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nIndex',
    'nMetaEventSize',
    'nData',
]
struct_OMX_AUDIO_CONFIG_MIDIMETAEVENTDATATYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nIndex', OMX_U32),
    ('nMetaEventSize', OMX_U32),
    ('nData', OMX_U8 * 1),
]

OMX_AUDIO_CONFIG__MIDIMETAEVENTDATATYPE = struct_OMX_AUDIO_CONFIG_MIDIMETAEVENTDATATYPE # OMX_Audio.h: 830

# OMX_Audio.h: 838
class struct_OMX_AUDIO_CONFIG_VOLUMETYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_VOLUMETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bLinear',
    'sVolume',
]
struct_OMX_AUDIO_CONFIG_VOLUMETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bLinear', OMX_BOOL),
    ('sVolume', OMX_BS32),
]

OMX_AUDIO_CONFIG_VOLUMETYPE = struct_OMX_AUDIO_CONFIG_VOLUMETYPE # OMX_Audio.h: 838

# OMX_Audio.h: 848
class struct_OMX_AUDIO_CONFIG_CHANNELVOLUMETYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_CHANNELVOLUMETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannel',
    'bLinear',
    'sVolume',
    'bIsMIDI',
]
struct_OMX_AUDIO_CONFIG_CHANNELVOLUMETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannel', OMX_U32),
    ('bLinear', OMX_BOOL),
    ('sVolume', OMX_BS32),
    ('bIsMIDI', OMX_BOOL),
]

OMX_AUDIO_CONFIG_CHANNELVOLUMETYPE = struct_OMX_AUDIO_CONFIG_CHANNELVOLUMETYPE # OMX_Audio.h: 848

# OMX_Audio.h: 855
class struct_OMX_AUDIO_CONFIG_BALANCETYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_BALANCETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nBalance',
]
struct_OMX_AUDIO_CONFIG_BALANCETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nBalance', OMX_S32),
]

OMX_AUDIO_CONFIG_BALANCETYPE = struct_OMX_AUDIO_CONFIG_BALANCETYPE # OMX_Audio.h: 855

# OMX_Audio.h: 862
class struct_OMX_AUDIO_CONFIG_MUTETYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_MUTETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bMute',
]
struct_OMX_AUDIO_CONFIG_MUTETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bMute', OMX_BOOL),
]

OMX_AUDIO_CONFIG_MUTETYPE = struct_OMX_AUDIO_CONFIG_MUTETYPE # OMX_Audio.h: 862

# OMX_Audio.h: 871
class struct_OMX_AUDIO_CONFIG_CHANNELMUTETYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_CHANNELMUTETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannel',
    'bMute',
    'bIsMIDI',
]
struct_OMX_AUDIO_CONFIG_CHANNELMUTETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannel', OMX_U32),
    ('bMute', OMX_BOOL),
    ('bIsMIDI', OMX_BOOL),
]

OMX_AUDIO_CONFIG_CHANNELMUTETYPE = struct_OMX_AUDIO_CONFIG_CHANNELMUTETYPE # OMX_Audio.h: 871

# OMX_Audio.h: 878
class struct_OMX_AUDIO_CONFIG_LOUDNESSTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_LOUDNESSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bLoudness',
]
struct_OMX_AUDIO_CONFIG_LOUDNESSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bLoudness', OMX_BOOL),
]

OMX_AUDIO_CONFIG_LOUDNESSTYPE = struct_OMX_AUDIO_CONFIG_LOUDNESSTYPE # OMX_Audio.h: 878

# OMX_Audio.h: 886
class struct_OMX_AUDIO_CONFIG_BASSTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_BASSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnable',
    'nBass',
]
struct_OMX_AUDIO_CONFIG_BASSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnable', OMX_BOOL),
    ('nBass', OMX_S32),
]

OMX_AUDIO_CONFIG_BASSTYPE = struct_OMX_AUDIO_CONFIG_BASSTYPE # OMX_Audio.h: 886

# OMX_Audio.h: 894
class struct_OMX_AUDIO_CONFIG_TREBLETYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_TREBLETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnable',
    'nTreble',
]
struct_OMX_AUDIO_CONFIG_TREBLETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnable', OMX_BOOL),
    ('nTreble', OMX_S32),
]

OMX_AUDIO_CONFIG_TREBLETYPE = struct_OMX_AUDIO_CONFIG_TREBLETYPE # OMX_Audio.h: 894

# OMX_Audio.h: 904
class struct_OMX_AUDIO_CONFIG_EQUALIZERTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_EQUALIZERTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnable',
    'sBandIndex',
    'sCenterFreq',
    'sBandLevel',
]
struct_OMX_AUDIO_CONFIG_EQUALIZERTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnable', OMX_BOOL),
    ('sBandIndex', OMX_BU32),
    ('sCenterFreq', OMX_BU32),
    ('sBandLevel', OMX_BS32),
]

OMX_AUDIO_CONFIG_EQUALIZERTYPE = struct_OMX_AUDIO_CONFIG_EQUALIZERTYPE # OMX_Audio.h: 904

enum_OMX_AUDIO_STEREOWIDENINGTYPE = c_int # OMX_Audio.h: 912

OMX_AUDIO_StereoWideningHeadphones = 0 # OMX_Audio.h: 912

OMX_AUDIO_StereoWideningLoudspeakers = (OMX_AUDIO_StereoWideningHeadphones + 1) # OMX_Audio.h: 912

OMX_AUDIO_StereoWideningKhronosExtensions = 1862270976 # OMX_Audio.h: 912

OMX_AUDIO_StereoWideningVendorStartUnused = 2130706432 # OMX_Audio.h: 912

OMX_AUDIO_StereoWideningMax = 2147483647 # OMX_Audio.h: 912

OMX_AUDIO_STEREOWIDENINGTYPE = enum_OMX_AUDIO_STEREOWIDENINGTYPE # OMX_Audio.h: 912

# OMX_Audio.h: 921
class struct_OMX_AUDIO_CONFIG_STEREOWIDENINGTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_STEREOWIDENINGTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnable',
    'eWideningType',
    'nStereoWidening',
]
struct_OMX_AUDIO_CONFIG_STEREOWIDENINGTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnable', OMX_BOOL),
    ('eWideningType', OMX_AUDIO_STEREOWIDENINGTYPE),
    ('nStereoWidening', OMX_U32),
]

OMX_AUDIO_CONFIG_STEREOWIDENINGTYPE = struct_OMX_AUDIO_CONFIG_STEREOWIDENINGTYPE # OMX_Audio.h: 921

# OMX_Audio.h: 932
class struct_OMX_AUDIO_CONFIG_CHORUSTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_CHORUSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnable',
    'sDelay',
    'sModulationRate',
    'nModulationDepth',
    'nFeedback',
]
struct_OMX_AUDIO_CONFIG_CHORUSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnable', OMX_BOOL),
    ('sDelay', OMX_BU32),
    ('sModulationRate', OMX_BU32),
    ('nModulationDepth', OMX_U32),
    ('nFeedback', OMX_BU32),
]

OMX_AUDIO_CONFIG_CHORUSTYPE = struct_OMX_AUDIO_CONFIG_CHORUSTYPE # OMX_Audio.h: 932

# OMX_Audio.h: 950
class struct_OMX_AUDIO_CONFIG_REVERBERATIONTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_REVERBERATIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnable',
    'sRoomLevel',
    'sRoomHighFreqLevel',
    'sReflectionsLevel',
    'sReflectionsDelay',
    'sReverbLevel',
    'sReverbDelay',
    'sDecayTime',
    'nDecayHighFreqRatio',
    'nDensity',
    'nDiffusion',
    'sReferenceHighFreq',
]
struct_OMX_AUDIO_CONFIG_REVERBERATIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnable', OMX_BOOL),
    ('sRoomLevel', OMX_BS32),
    ('sRoomHighFreqLevel', OMX_BS32),
    ('sReflectionsLevel', OMX_BS32),
    ('sReflectionsDelay', OMX_BU32),
    ('sReverbLevel', OMX_BS32),
    ('sReverbDelay', OMX_BU32),
    ('sDecayTime', OMX_BU32),
    ('nDecayHighFreqRatio', OMX_BU32),
    ('nDensity', OMX_U32),
    ('nDiffusion', OMX_U32),
    ('sReferenceHighFreq', OMX_BU32),
]

OMX_AUDIO_CONFIG_REVERBERATIONTYPE = struct_OMX_AUDIO_CONFIG_REVERBERATIONTYPE # OMX_Audio.h: 950

enum_OMX_AUDIO_ECHOCANTYPE = c_int # OMX_Audio.h: 960

OMX_AUDIO_EchoCanOff = 0 # OMX_Audio.h: 960

OMX_AUDIO_EchoCanNormal = (OMX_AUDIO_EchoCanOff + 1) # OMX_Audio.h: 960

OMX_AUDIO_EchoCanHFree = (OMX_AUDIO_EchoCanNormal + 1) # OMX_Audio.h: 960

OMX_AUDIO_EchoCanCarKit = (OMX_AUDIO_EchoCanHFree + 1) # OMX_Audio.h: 960

OMX_AUDIO_EchoCanKhronosExtensions = 1862270976 # OMX_Audio.h: 960

OMX_AUDIO_EchoCanVendorStartUnused = 2130706432 # OMX_Audio.h: 960

OMX_AUDIO_EchoCanMax = 2147483647 # OMX_Audio.h: 960

OMX_AUDIO_ECHOCANTYPE = enum_OMX_AUDIO_ECHOCANTYPE # OMX_Audio.h: 960

# OMX_Audio.h: 967
class struct_OMX_AUDIO_CONFIG_ECHOCANCELATIONTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_ECHOCANCELATIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eEchoCancelation',
]
struct_OMX_AUDIO_CONFIG_ECHOCANCELATIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eEchoCancelation', OMX_AUDIO_ECHOCANTYPE),
]

OMX_AUDIO_CONFIG_ECHOCANCELATIONTYPE = struct_OMX_AUDIO_CONFIG_ECHOCANCELATIONTYPE # OMX_Audio.h: 967

# OMX_Audio.h: 974
class struct_OMX_AUDIO_CONFIG_NOISEREDUCTIONTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_NOISEREDUCTIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bNoiseReduction',
]
struct_OMX_AUDIO_CONFIG_NOISEREDUCTIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bNoiseReduction', OMX_BOOL),
]

OMX_AUDIO_CONFIG_NOISEREDUCTIONTYPE = struct_OMX_AUDIO_CONFIG_NOISEREDUCTIONTYPE # OMX_Audio.h: 974

enum_OMX_AUDIO_3DOUTPUTTYPE = c_int # OMX_Audio.h: 980

OMX_AUDIO_3DOutputHeadphones = 0 # OMX_Audio.h: 980

OMX_AUDIO_3DOutputLoudspeakers = (OMX_AUDIO_3DOutputHeadphones + 1) # OMX_Audio.h: 980

OMX_AUDIO_3DOutputMax = 2147483647 # OMX_Audio.h: 980

OMX_AUDIO_3DOUTPUTTYPE = enum_OMX_AUDIO_3DOUTPUTTYPE # OMX_Audio.h: 980

# OMX_Audio.h: 987
class struct_OMX_AUDIO_CONFIG_3DOUTPUTTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_3DOUTPUTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'e3DOutputType',
]
struct_OMX_AUDIO_CONFIG_3DOUTPUTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('e3DOutputType', OMX_AUDIO_3DOUTPUTTYPE),
]

OMX_AUDIO_CONFIG_3DOUTPUTTYPE = struct_OMX_AUDIO_CONFIG_3DOUTPUTTYPE # OMX_Audio.h: 987

# OMX_Audio.h: 996
class struct_OMX_AUDIO_CONFIG_3DLOCATIONTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_3DLOCATIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nX',
    'nY',
    'nZ',
]
struct_OMX_AUDIO_CONFIG_3DLOCATIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nX', OMX_S32),
    ('nY', OMX_S32),
    ('nZ', OMX_S32),
]

OMX_AUDIO_CONFIG_3DLOCATIONTYPE = struct_OMX_AUDIO_CONFIG_3DLOCATIONTYPE # OMX_Audio.h: 996

# OMX_Audio.h: 1003
class struct_OMX_AUDIO_PARAM_3DDOPPLERMODETYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_3DDOPPLERMODETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnabled',
]
struct_OMX_AUDIO_PARAM_3DDOPPLERMODETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnabled', OMX_BOOL),
]

OMX_AUDIO_PARAM_3DDOPPLERMODETYPE = struct_OMX_AUDIO_PARAM_3DDOPPLERMODETYPE # OMX_Audio.h: 1003

# OMX_Audio.h: 1012
class struct_OMX_AUDIO_CONFIG_3DDOPPLERSETTINGSTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_3DDOPPLERSETTINGSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nSoundSpeed',
    'nSourceVelocity',
    'nListenerVelocity',
]
struct_OMX_AUDIO_CONFIG_3DDOPPLERSETTINGSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nSoundSpeed', OMX_U32),
    ('nSourceVelocity', OMX_S32),
    ('nListenerVelocity', OMX_S32),
]

OMX_AUDIO_CONFIG_3DDOPPLERSETTINGSTYPE = struct_OMX_AUDIO_CONFIG_3DDOPPLERSETTINGSTYPE # OMX_Audio.h: 1012

# OMX_Audio.h: 1020
class struct_OMX_AUDIO_CONFIG_3DLEVELSTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_3DLEVELSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'sDirectLevel',
    'sRoomLevel',
]
struct_OMX_AUDIO_CONFIG_3DLEVELSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('sDirectLevel', OMX_BS32),
    ('sRoomLevel', OMX_BS32),
]

OMX_AUDIO_CONFIG_3DLEVELSTYPE = struct_OMX_AUDIO_CONFIG_3DLEVELSTYPE # OMX_Audio.h: 1020

enum_OMX_AUDIO_ROLLOFFMODELTYPE = c_int # OMX_Audio.h: 1026

OMX_AUDIO_RollOffExponential = 0 # OMX_Audio.h: 1026

OMX_AUDIO_RollOffLinear = (OMX_AUDIO_RollOffExponential + 1) # OMX_Audio.h: 1026

OMX_AUDIO_RollOffMax = 2147483647 # OMX_Audio.h: 1026

OMX_AUDIO_ROLLOFFMODELTYPE = enum_OMX_AUDIO_ROLLOFFMODELTYPE # OMX_Audio.h: 1026

# OMX_Audio.h: 1038
class struct_OMX_AUDIO_CONFIG_3DDISTANCEATTENUATIONTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_3DDISTANCEATTENUATIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'sMinDistance',
    'sMaxDistance',
    'sRollOffFactor',
    'sRoomRollOffFactor',
    'eRollOffModel',
    'bMuteAfterMax',
]
struct_OMX_AUDIO_CONFIG_3DDISTANCEATTENUATIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('sMinDistance', OMX_BS32),
    ('sMaxDistance', OMX_BS32),
    ('sRollOffFactor', OMX_BS32),
    ('sRoomRollOffFactor', OMX_BS32),
    ('eRollOffModel', OMX_AUDIO_ROLLOFFMODELTYPE),
    ('bMuteAfterMax', OMX_BOOL),
]

OMX_AUDIO_CONFIG_3DDISTANCEATTENUATIONTYPE = struct_OMX_AUDIO_CONFIG_3DDISTANCEATTENUATIONTYPE # OMX_Audio.h: 1038

# OMX_Audio.h: 1047
class struct_OMX_AUDIO_CONFIG_3DDIRECTIVITYSETTINGSTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_3DDIRECTIVITYSETTINGSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'sInnerAngle',
    'sOuterAngle',
    'sOuterLevel',
]
struct_OMX_AUDIO_CONFIG_3DDIRECTIVITYSETTINGSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('sInnerAngle', OMX_BS32),
    ('sOuterAngle', OMX_BS32),
    ('sOuterLevel', OMX_BS32),
]

OMX_AUDIO_CONFIG_3DDIRECTIVITYSETTINGSTYPE = struct_OMX_AUDIO_CONFIG_3DDIRECTIVITYSETTINGSTYPE # OMX_Audio.h: 1047

# OMX_Audio.h: 1056
class struct_OMX_AUDIO_CONFIG_3DDIRECTIVITYORIENTATIONTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_3DDIRECTIVITYORIENTATIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nXFront',
    'nYFront',
    'nZFront',
]
struct_OMX_AUDIO_CONFIG_3DDIRECTIVITYORIENTATIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nXFront', OMX_S32),
    ('nYFront', OMX_S32),
    ('nZFront', OMX_S32),
]

OMX_AUDIO_CONFIG_3DDIRECTIVITYORIENTATIONTYPE = struct_OMX_AUDIO_CONFIG_3DDIRECTIVITYORIENTATIONTYPE # OMX_Audio.h: 1056

# OMX_Audio.h: 1068
class struct_OMX_AUDIO_CONFIG_3DMACROSCOPICORIENTATIONTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_3DMACROSCOPICORIENTATIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nXFront',
    'nYFront',
    'nZFront',
    'nXAbove',
    'nYAbove',
    'nZAbove',
]
struct_OMX_AUDIO_CONFIG_3DMACROSCOPICORIENTATIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nXFront', OMX_S32),
    ('nYFront', OMX_S32),
    ('nZFront', OMX_S32),
    ('nXAbove', OMX_S32),
    ('nYAbove', OMX_S32),
    ('nZAbove', OMX_S32),
]

OMX_AUDIO_CONFIG_3DMACROSCOPICORIENTATIONTYPE = struct_OMX_AUDIO_CONFIG_3DMACROSCOPICORIENTATIONTYPE # OMX_Audio.h: 1068

# OMX_Audio.h: 1077
class struct_OMX_AUDIO_CONFIG_3DMACROSCOPICSIZETYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_3DMACROSCOPICSIZETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nWidth',
    'nHeight',
    'nDepth',
]
struct_OMX_AUDIO_CONFIG_3DMACROSCOPICSIZETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nWidth', OMX_S32),
    ('nHeight', OMX_S32),
    ('nDepth', OMX_S32),
]

OMX_AUDIO_CONFIG_3DMACROSCOPICSIZETYPE = struct_OMX_AUDIO_CONFIG_3DMACROSCOPICSIZETYPE # OMX_Audio.h: 1077

# OMX_Audio.h: 1085
class struct_OMX_AUDIO_PARAM_CHANNELMAPPINGTYPE(Structure):
    pass

struct_OMX_AUDIO_PARAM_CHANNELMAPPINGTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nChannels',
    'nChannelsMapping',
]
struct_OMX_AUDIO_PARAM_CHANNELMAPPINGTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nChannels', OMX_U32),
    ('nChannelsMapping', OMX_AUDIO_CHANNELTYPE * 36),
]

OMX_AUDIO_PARAM_CHANNELMAPPINGTYPE = struct_OMX_AUDIO_PARAM_CHANNELMAPPINGTYPE # OMX_Audio.h: 1085

# OMX_Audio.h: 1092
class struct_OMX_AUDIO_SBCBITPOOLTYPE(Structure):
    pass

struct_OMX_AUDIO_SBCBITPOOLTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nNewBitPool',
]
struct_OMX_AUDIO_SBCBITPOOLTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nNewBitPool', OMX_U32),
]

OMX_AUDIO_SBCBITPOOLTYPE = struct_OMX_AUDIO_SBCBITPOOLTYPE # OMX_Audio.h: 1092

# OMX_Audio.h: 1100
class struct_OMX_AUDIO_AMRMODETYPE(Structure):
    pass

struct_OMX_AUDIO_AMRMODETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nBitRate',
    'eAMRBandMode',
]
struct_OMX_AUDIO_AMRMODETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nBitRate', OMX_U32),
    ('eAMRBandMode', OMX_AUDIO_AMRBANDMODETYPE),
]

OMX_AUDIO_AMRMODETYPE = struct_OMX_AUDIO_AMRMODETYPE # OMX_Audio.h: 1100

# OMX_Audio.h: 1107
class struct_OMX_AUDIO_CONFIG_BITRATETYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_BITRATETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nEncodeBitrate',
]
struct_OMX_AUDIO_CONFIG_BITRATETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nEncodeBitrate', OMX_U32),
]

OMX_AUDIO_CONFIG_BITRATETYPE = struct_OMX_AUDIO_CONFIG_BITRATETYPE # OMX_Audio.h: 1107

# OMX_Audio.h: 1114
class struct_OMX_AUDIO_CONFIG_AMRISFTYPE(Structure):
    pass

struct_OMX_AUDIO_CONFIG_AMRISFTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eTargetAMRISFIndex',
]
struct_OMX_AUDIO_CONFIG_AMRISFTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eTargetAMRISFIndex', OMX_AUDIO_AMRISFINDEXTYPE),
]

OMX_AUDIO_CONFIG_AMRISFTYPE = struct_OMX_AUDIO_CONFIG_AMRISFTYPE # OMX_Audio.h: 1114

# OMX_Audio.h: 1124
class struct_OMX_AUDIO_FIXEDPOINTTYPE(Structure):
    pass

struct_OMX_AUDIO_FIXEDPOINTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nValueStartBit',
    'nValueBits',
    'nSignExtensionBits',
    'nValuePointPosition',
]
struct_OMX_AUDIO_FIXEDPOINTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nValueStartBit', OMX_U32),
    ('nValueBits', OMX_U32),
    ('nSignExtensionBits', OMX_U32),
    ('nValuePointPosition', OMX_S32),
]

OMX_AUDIO_FIXEDPOINTTYPE = struct_OMX_AUDIO_FIXEDPOINTTYPE # OMX_Audio.h: 1124

enum_OMX_COLOR_FORMATTYPE = c_int # OMX_IVCommon.h: 112

OMX_COLOR_FormatUnused = 0 # OMX_IVCommon.h: 112

OMX_COLOR_FormatMonochrome = (OMX_COLOR_FormatUnused + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format8bitRGB332 = (OMX_COLOR_FormatMonochrome + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format12bitRGB444 = (OMX_COLOR_Format8bitRGB332 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format16bitARGB4444 = (OMX_COLOR_Format12bitRGB444 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format16bitARGB1555 = (OMX_COLOR_Format16bitARGB4444 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format16bitRGB565 = (OMX_COLOR_Format16bitARGB1555 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format16bitBGR565 = (OMX_COLOR_Format16bitRGB565 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format18bitRGB666 = (OMX_COLOR_Format16bitBGR565 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format18bitARGB1665 = (OMX_COLOR_Format18bitRGB666 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format19bitARGB1666 = (OMX_COLOR_Format18bitARGB1665 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format24bitRGB888 = (OMX_COLOR_Format19bitARGB1666 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format24bitBGR888 = (OMX_COLOR_Format24bitRGB888 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format24bitARGB1887 = (OMX_COLOR_Format24bitBGR888 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format25bitARGB1888 = (OMX_COLOR_Format24bitARGB1887 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format32bitBGRA8888 = (OMX_COLOR_Format25bitARGB1888 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format32bitARGB8888 = (OMX_COLOR_Format32bitBGRA8888 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYUV411Planar = (OMX_COLOR_Format32bitARGB8888 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYUV411PackedPlanar = (OMX_COLOR_FormatYUV411Planar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYUV420Planar = (OMX_COLOR_FormatYUV411PackedPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYUV420PackedPlanar = (OMX_COLOR_FormatYUV420Planar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYUV420SemiPlanar = (OMX_COLOR_FormatYUV420PackedPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYUV422Planar = (OMX_COLOR_FormatYUV420SemiPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYUV422PackedPlanar = (OMX_COLOR_FormatYUV422Planar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYUV422SemiPlanar = (OMX_COLOR_FormatYUV422PackedPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYCbYCr = (OMX_COLOR_FormatYUV422SemiPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYCrYCb = (OMX_COLOR_FormatYCbYCr + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatCbYCrY = (OMX_COLOR_FormatYCrYCb + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatCrYCbY = (OMX_COLOR_FormatCbYCrY + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYUV444Interleaved = (OMX_COLOR_FormatCrYCbY + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatRawBayer8bit = (OMX_COLOR_FormatYUV444Interleaved + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatRawBayer10bit = (OMX_COLOR_FormatRawBayer8bit + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatRawBayer8bitcompressed = (OMX_COLOR_FormatRawBayer10bit + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatL2 = (OMX_COLOR_FormatRawBayer8bitcompressed + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatL4 = (OMX_COLOR_FormatL2 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatL8 = (OMX_COLOR_FormatL4 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatL16 = (OMX_COLOR_FormatL8 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatL24 = (OMX_COLOR_FormatL16 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatL32 = (OMX_COLOR_FormatL24 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYUV420PackedSemiPlanar = (OMX_COLOR_FormatL32 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYUV422PackedSemiPlanar = (OMX_COLOR_FormatYUV420PackedSemiPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format18BitBGR666 = (OMX_COLOR_FormatYUV422PackedSemiPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format24BitARGB6666 = (OMX_COLOR_Format18BitBGR666 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format24BitABGR6666 = (OMX_COLOR_Format24BitARGB6666 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format32bitABGR8888 = (OMX_COLOR_Format24BitABGR6666 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYVU420Planar = (OMX_COLOR_Format32bitABGR8888 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYVU420PackedPlanar = (OMX_COLOR_FormatYVU420Planar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYVU420SemiPlanar = (OMX_COLOR_FormatYVU420PackedPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYVU420PackedSemiPlanar = (OMX_COLOR_FormatYVU420SemiPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYVU422Planar = (OMX_COLOR_FormatYVU420PackedSemiPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYVU422PackedPlanar = (OMX_COLOR_FormatYVU422Planar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYVU422SemiPlanar = (OMX_COLOR_FormatYVU422PackedPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatYVU422PackedSemiPlanar = (OMX_COLOR_FormatYVU422SemiPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format8bitBGR233 = (OMX_COLOR_FormatYVU422PackedSemiPlanar + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format12bitBGR444 = (OMX_COLOR_Format8bitBGR233 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format16bitBGRA4444 = (OMX_COLOR_Format12bitBGR444 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format16bitBGRA5551 = (OMX_COLOR_Format16bitBGRA4444 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format18bitBGRA5661 = (OMX_COLOR_Format16bitBGRA5551 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format19bitBGRA6661 = (OMX_COLOR_Format18bitBGRA5661 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format24bitBGRA7881 = (OMX_COLOR_Format19bitBGRA6661 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format25bitBGRA8881 = (OMX_COLOR_Format24bitBGRA7881 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format24BitBGRA6666 = (OMX_COLOR_Format25bitBGRA8881 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_Format24BitRGBA6666 = (OMX_COLOR_Format24BitBGRA6666 + 1) # OMX_IVCommon.h: 112

OMX_COLOR_FormatKhronosExtensions = 1862270976 # OMX_IVCommon.h: 112

OMX_COLOR_FormatVendorStartUnused = 2130706432 # OMX_IVCommon.h: 112

OMX_COLOR_FormatMax = 2147483647 # OMX_IVCommon.h: 112

OMX_COLOR_FORMATTYPE = enum_OMX_COLOR_FORMATTYPE # OMX_IVCommon.h: 112

# OMX_IVCommon.h: 120
class struct_OMX_CONFIG_COLORCONVERSIONTYPE(Structure):
    pass

struct_OMX_CONFIG_COLORCONVERSIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'xColorMatrix',
    'xColorOffset',
]
struct_OMX_CONFIG_COLORCONVERSIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('xColorMatrix', (OMX_S32 * 3) * 3),
    ('xColorOffset', OMX_S32 * 4),
]

OMX_CONFIG_COLORCONVERSIONTYPE = struct_OMX_CONFIG_COLORCONVERSIONTYPE # OMX_IVCommon.h: 120

# OMX_IVCommon.h: 128
class struct_OMX_CONFIG_SCALEFACTORTYPE(Structure):
    pass

struct_OMX_CONFIG_SCALEFACTORTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'xWidth',
    'xHeight',
]
struct_OMX_CONFIG_SCALEFACTORTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('xWidth', OMX_S32),
    ('xHeight', OMX_S32),
]

OMX_CONFIG_SCALEFACTORTYPE = struct_OMX_CONFIG_SCALEFACTORTYPE # OMX_IVCommon.h: 128

enum_OMX_IMAGEFILTERTYPE = c_int # OMX_IVCommon.h: 156

OMX_ImageFilterNone = 0 # OMX_IVCommon.h: 156

OMX_ImageFilterNoise = (OMX_ImageFilterNone + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterEmboss = (OMX_ImageFilterNoise + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterNegative = (OMX_ImageFilterEmboss + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterSketch = (OMX_ImageFilterNegative + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterOilPaint = (OMX_ImageFilterSketch + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterHatch = (OMX_ImageFilterOilPaint + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterGpen = (OMX_ImageFilterHatch + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterAntialias = (OMX_ImageFilterGpen + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterDeRing = (OMX_ImageFilterAntialias + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterSolarize = (OMX_ImageFilterDeRing + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterPastel = (OMX_ImageFilterSolarize + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterMosaic = (OMX_ImageFilterPastel + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterPosterize = (OMX_ImageFilterMosaic + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterWhiteboard = (OMX_ImageFilterPosterize + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterBlackboard = (OMX_ImageFilterWhiteboard + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterSepia = (OMX_ImageFilterBlackboard + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterGrayscale = (OMX_ImageFilterSepia + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterNatural = (OMX_ImageFilterGrayscale + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterVivid = (OMX_ImageFilterNatural + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterWaterColor = (OMX_ImageFilterVivid + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterFilm = (OMX_ImageFilterWaterColor + 1) # OMX_IVCommon.h: 156

OMX_ImageFilterKhronosExtensions = 1862270976 # OMX_IVCommon.h: 156

OMX_ImageFilterVendorStartUnused = 2130706432 # OMX_IVCommon.h: 156

OMX_ImageFilterMax = 2147483647 # OMX_IVCommon.h: 156

OMX_IMAGEFILTERTYPE = enum_OMX_IMAGEFILTERTYPE # OMX_IVCommon.h: 156

# OMX_IVCommon.h: 163
class struct_OMX_CONFIG_IMAGEFILTERTYPE(Structure):
    pass

struct_OMX_CONFIG_IMAGEFILTERTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eImageFilter',
]
struct_OMX_CONFIG_IMAGEFILTERTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eImageFilter', OMX_IMAGEFILTERTYPE),
]

OMX_CONFIG_IMAGEFILTERTYPE = struct_OMX_CONFIG_IMAGEFILTERTYPE # OMX_IVCommon.h: 163

# OMX_IVCommon.h: 172
class struct_OMX_CONFIG_COLORENHANCEMENTTYPE(Structure):
    pass

struct_OMX_CONFIG_COLORENHANCEMENTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bColorEnhancement',
    'nCustomizedU',
    'nCustomizedV',
]
struct_OMX_CONFIG_COLORENHANCEMENTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bColorEnhancement', OMX_BOOL),
    ('nCustomizedU', OMX_U8),
    ('nCustomizedV', OMX_U8),
]

OMX_CONFIG_COLORENHANCEMENTTYPE = struct_OMX_CONFIG_COLORENHANCEMENTTYPE # OMX_IVCommon.h: 172

# OMX_IVCommon.h: 180
class struct_OMX_CONFIG_COLORKEYTYPE(Structure):
    pass

struct_OMX_CONFIG_COLORKEYTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nARGBColor',
    'nARGBMask',
]
struct_OMX_CONFIG_COLORKEYTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nARGBColor', OMX_U32),
    ('nARGBMask', OMX_U32),
]

OMX_CONFIG_COLORKEYTYPE = struct_OMX_CONFIG_COLORKEYTYPE # OMX_IVCommon.h: 180

enum_OMX_COLORBLENDTYPE = c_int # OMX_IVCommon.h: 193

OMX_ColorBlendNone = 0 # OMX_IVCommon.h: 193

OMX_ColorBlendAlphaConstant = (OMX_ColorBlendNone + 1) # OMX_IVCommon.h: 193

OMX_ColorBlendAlphaPerPixel = (OMX_ColorBlendAlphaConstant + 1) # OMX_IVCommon.h: 193

OMX_ColorBlendAlternate = (OMX_ColorBlendAlphaPerPixel + 1) # OMX_IVCommon.h: 193

OMX_ColorBlendAnd = (OMX_ColorBlendAlternate + 1) # OMX_IVCommon.h: 193

OMX_ColorBlendOr = (OMX_ColorBlendAnd + 1) # OMX_IVCommon.h: 193

OMX_ColorBlendInvert = (OMX_ColorBlendOr + 1) # OMX_IVCommon.h: 193

OMX_ColorBlendKhronosExtensions = 1862270976 # OMX_IVCommon.h: 193

OMX_ColorBlendVendorStartUnused = 2130706432 # OMX_IVCommon.h: 193

OMX_ColorBlendMax = 2147483647 # OMX_IVCommon.h: 193

OMX_COLORBLENDTYPE = enum_OMX_COLORBLENDTYPE # OMX_IVCommon.h: 193

# OMX_IVCommon.h: 201
class struct_OMX_CONFIG_COLORBLENDTYPE(Structure):
    pass

struct_OMX_CONFIG_COLORBLENDTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nRGBAlphaConstant',
    'eColorBlend',
]
struct_OMX_CONFIG_COLORBLENDTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nRGBAlphaConstant', OMX_U32),
    ('eColorBlend', OMX_COLORBLENDTYPE),
]

OMX_CONFIG_COLORBLENDTYPE = struct_OMX_CONFIG_COLORBLENDTYPE # OMX_IVCommon.h: 201

# OMX_IVCommon.h: 209
class struct_OMX_FRAMESIZETYPE(Structure):
    pass

struct_OMX_FRAMESIZETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nWidth',
    'nHeight',
]
struct_OMX_FRAMESIZETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nWidth', OMX_U32),
    ('nHeight', OMX_U32),
]

OMX_FRAMESIZETYPE = struct_OMX_FRAMESIZETYPE # OMX_IVCommon.h: 209

# OMX_IVCommon.h: 216
class struct_OMX_CONFIG_ROTATIONTYPE(Structure):
    pass

struct_OMX_CONFIG_ROTATIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nRotation',
]
struct_OMX_CONFIG_ROTATIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nRotation', OMX_S32),
]

OMX_CONFIG_ROTATIONTYPE = struct_OMX_CONFIG_ROTATIONTYPE # OMX_IVCommon.h: 216

enum_OMX_MIRRORTYPE = c_int # OMX_IVCommon.h: 226

OMX_MirrorNone = 0 # OMX_IVCommon.h: 226

OMX_MirrorVertical = (OMX_MirrorNone + 1) # OMX_IVCommon.h: 226

OMX_MirrorHorizontal = (OMX_MirrorVertical + 1) # OMX_IVCommon.h: 226

OMX_MirrorBoth = (OMX_MirrorHorizontal + 1) # OMX_IVCommon.h: 226

OMX_MirrorKhronosExtensions = 1862270976 # OMX_IVCommon.h: 226

OMX_MirrorVendorStartUnused = 2130706432 # OMX_IVCommon.h: 226

OMX_MirrorMax = 2147483647 # OMX_IVCommon.h: 226

OMX_MIRRORTYPE = enum_OMX_MIRRORTYPE # OMX_IVCommon.h: 226

# OMX_IVCommon.h: 233
class struct_OMX_CONFIG_MIRRORTYPE(Structure):
    pass

struct_OMX_CONFIG_MIRRORTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eMirror',
]
struct_OMX_CONFIG_MIRRORTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eMirror', OMX_MIRRORTYPE),
]

OMX_CONFIG_MIRRORTYPE = struct_OMX_CONFIG_MIRRORTYPE # OMX_IVCommon.h: 233

# OMX_IVCommon.h: 241
class struct_OMX_CONFIG_POINTTYPE(Structure):
    pass

struct_OMX_CONFIG_POINTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nX',
    'nY',
]
struct_OMX_CONFIG_POINTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nX', OMX_S32),
    ('nY', OMX_S32),
]

OMX_CONFIG_POINTTYPE = struct_OMX_CONFIG_POINTTYPE # OMX_IVCommon.h: 241

# OMX_IVCommon.h: 251
class struct_OMX_CONFIG_RECTTYPE(Structure):
    pass

struct_OMX_CONFIG_RECTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nLeft',
    'nTop',
    'nWidth',
    'nHeight',
]
struct_OMX_CONFIG_RECTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nLeft', OMX_S32),
    ('nTop', OMX_S32),
    ('nWidth', OMX_U32),
    ('nHeight', OMX_U32),
]

OMX_CONFIG_RECTTYPE = struct_OMX_CONFIG_RECTTYPE # OMX_IVCommon.h: 251

# OMX_IVCommon.h: 258
class struct_OMX_PARAM_DEBLOCKINGTYPE(Structure):
    pass

struct_OMX_PARAM_DEBLOCKINGTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bDeblocking',
]
struct_OMX_PARAM_DEBLOCKINGTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bDeblocking', OMX_BOOL),
]

OMX_PARAM_DEBLOCKINGTYPE = struct_OMX_PARAM_DEBLOCKINGTYPE # OMX_IVCommon.h: 258

# OMX_IVCommon.h: 265
class struct_OMX_CONFIG_FRAMESTABTYPE(Structure):
    pass

struct_OMX_CONFIG_FRAMESTABTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bStab',
]
struct_OMX_CONFIG_FRAMESTABTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bStab', OMX_BOOL),
]

OMX_CONFIG_FRAMESTABTYPE = struct_OMX_CONFIG_FRAMESTABTYPE # OMX_IVCommon.h: 265

enum_OMX_WHITEBALCONTROLTYPE = c_int # OMX_IVCommon.h: 281

OMX_WhiteBalControlOff = 0 # OMX_IVCommon.h: 281

OMX_WhiteBalControlAuto = (OMX_WhiteBalControlOff + 1) # OMX_IVCommon.h: 281

OMX_WhiteBalControlSunLight = (OMX_WhiteBalControlAuto + 1) # OMX_IVCommon.h: 281

OMX_WhiteBalControlCloudy = (OMX_WhiteBalControlSunLight + 1) # OMX_IVCommon.h: 281

OMX_WhiteBalControlShade = (OMX_WhiteBalControlCloudy + 1) # OMX_IVCommon.h: 281

OMX_WhiteBalControlTungsten = (OMX_WhiteBalControlShade + 1) # OMX_IVCommon.h: 281

OMX_WhiteBalControlFluorescent = (OMX_WhiteBalControlTungsten + 1) # OMX_IVCommon.h: 281

OMX_WhiteBalControlIncandescent = (OMX_WhiteBalControlFluorescent + 1) # OMX_IVCommon.h: 281

OMX_WhiteBalControlFlash = (OMX_WhiteBalControlIncandescent + 1) # OMX_IVCommon.h: 281

OMX_WhiteBalControlHorizon = (OMX_WhiteBalControlFlash + 1) # OMX_IVCommon.h: 281

OMX_WhiteBalControlKhronosExtensions = 1862270976 # OMX_IVCommon.h: 281

OMX_WhiteBalControlVendorStartUnused = 2130706432 # OMX_IVCommon.h: 281

OMX_WhiteBalControlMax = 2147483647 # OMX_IVCommon.h: 281

OMX_WHITEBALCONTROLTYPE = enum_OMX_WHITEBALCONTROLTYPE # OMX_IVCommon.h: 281

# OMX_IVCommon.h: 288
class struct_OMX_CONFIG_WHITEBALCONTROLTYPE(Structure):
    pass

struct_OMX_CONFIG_WHITEBALCONTROLTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eWhiteBalControl',
]
struct_OMX_CONFIG_WHITEBALCONTROLTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eWhiteBalControl', OMX_WHITEBALCONTROLTYPE),
]

OMX_CONFIG_WHITEBALCONTROLTYPE = struct_OMX_CONFIG_WHITEBALCONTROLTYPE # OMX_IVCommon.h: 288

enum_OMX_EXPOSURECONTROLTYPE = c_int # OMX_IVCommon.h: 304

OMX_ExposureControlOff = 0 # OMX_IVCommon.h: 304

OMX_ExposureControlAuto = (OMX_ExposureControlOff + 1) # OMX_IVCommon.h: 304

OMX_ExposureControlNight = (OMX_ExposureControlAuto + 1) # OMX_IVCommon.h: 304

OMX_ExposureControlBackLight = (OMX_ExposureControlNight + 1) # OMX_IVCommon.h: 304

OMX_ExposureControlSpotLight = (OMX_ExposureControlBackLight + 1) # OMX_IVCommon.h: 304

OMX_ExposureControlSports = (OMX_ExposureControlSpotLight + 1) # OMX_IVCommon.h: 304

OMX_ExposureControlSnow = (OMX_ExposureControlSports + 1) # OMX_IVCommon.h: 304

OMX_ExposureControlBeach = (OMX_ExposureControlSnow + 1) # OMX_IVCommon.h: 304

OMX_ExposureControlLargeAperture = (OMX_ExposureControlBeach + 1) # OMX_IVCommon.h: 304

OMX_ExposureControlSmallApperture = (OMX_ExposureControlLargeAperture + 1) # OMX_IVCommon.h: 304

OMX_ExposureControlKhronosExtensions = 1862270976 # OMX_IVCommon.h: 304

OMX_ExposureControlVendorStartUnused = 2130706432 # OMX_IVCommon.h: 304

OMX_ExposureControlMax = 2147483647 # OMX_IVCommon.h: 304

OMX_EXPOSURECONTROLTYPE = enum_OMX_EXPOSURECONTROLTYPE # OMX_IVCommon.h: 304

# OMX_IVCommon.h: 311
class struct_OMX_CONFIG_EXPOSURECONTROLTYPE(Structure):
    pass

struct_OMX_CONFIG_EXPOSURECONTROLTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eExposureControl',
]
struct_OMX_CONFIG_EXPOSURECONTROLTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eExposureControl', OMX_EXPOSURECONTROLTYPE),
]

OMX_CONFIG_EXPOSURECONTROLTYPE = struct_OMX_CONFIG_EXPOSURECONTROLTYPE # OMX_IVCommon.h: 311

# OMX_IVCommon.h: 320
class struct_OMX_PARAM_SENSORMODETYPE(Structure):
    pass

struct_OMX_PARAM_SENSORMODETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nFrameRate',
    'bOneShot',
    'sFrameSize',
]
struct_OMX_PARAM_SENSORMODETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nFrameRate', OMX_U32),
    ('bOneShot', OMX_BOOL),
    ('sFrameSize', OMX_FRAMESIZETYPE),
]

OMX_PARAM_SENSORMODETYPE = struct_OMX_PARAM_SENSORMODETYPE # OMX_IVCommon.h: 320

# OMX_IVCommon.h: 327
class struct_OMX_CONFIG_CONTRASTTYPE(Structure):
    pass

struct_OMX_CONFIG_CONTRASTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nContrast',
]
struct_OMX_CONFIG_CONTRASTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nContrast', OMX_S32),
]

OMX_CONFIG_CONTRASTTYPE = struct_OMX_CONFIG_CONTRASTTYPE # OMX_IVCommon.h: 327

# OMX_IVCommon.h: 334
class struct_OMX_CONFIG_BRIGHTNESSTYPE(Structure):
    pass

struct_OMX_CONFIG_BRIGHTNESSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nBrightness',
]
struct_OMX_CONFIG_BRIGHTNESSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nBrightness', OMX_U32),
]

OMX_CONFIG_BRIGHTNESSTYPE = struct_OMX_CONFIG_BRIGHTNESSTYPE # OMX_IVCommon.h: 334

# OMX_IVCommon.h: 342
class struct_OMX_CONFIG_BACKLIGHTTYPE(Structure):
    pass

struct_OMX_CONFIG_BACKLIGHTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nBacklight',
    'nTimeout',
]
struct_OMX_CONFIG_BACKLIGHTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nBacklight', OMX_U32),
    ('nTimeout', OMX_U32),
]

OMX_CONFIG_BACKLIGHTTYPE = struct_OMX_CONFIG_BACKLIGHTTYPE # OMX_IVCommon.h: 342

# OMX_IVCommon.h: 349
class struct_OMX_CONFIG_GAMMATYPE(Structure):
    pass

struct_OMX_CONFIG_GAMMATYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nGamma',
]
struct_OMX_CONFIG_GAMMATYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nGamma', OMX_S32),
]

OMX_CONFIG_GAMMATYPE = struct_OMX_CONFIG_GAMMATYPE # OMX_IVCommon.h: 349

# OMX_IVCommon.h: 356
class struct_OMX_CONFIG_SATURATIONTYPE(Structure):
    pass

struct_OMX_CONFIG_SATURATIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nSaturation',
]
struct_OMX_CONFIG_SATURATIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nSaturation', OMX_S32),
]

OMX_CONFIG_SATURATIONTYPE = struct_OMX_CONFIG_SATURATIONTYPE # OMX_IVCommon.h: 356

# OMX_IVCommon.h: 363
class struct_OMX_CONFIG_LIGHTNESSTYPE(Structure):
    pass

struct_OMX_CONFIG_LIGHTNESSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nLightness',
]
struct_OMX_CONFIG_LIGHTNESSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nLightness', OMX_S32),
]

OMX_CONFIG_LIGHTNESSTYPE = struct_OMX_CONFIG_LIGHTNESSTYPE # OMX_IVCommon.h: 363

# OMX_IVCommon.h: 371
class struct_OMX_CONFIG_PLANEBLENDTYPE(Structure):
    pass

struct_OMX_CONFIG_PLANEBLENDTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nDepth',
    'nAlpha',
]
struct_OMX_CONFIG_PLANEBLENDTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nDepth', OMX_U32),
    ('nAlpha', OMX_U32),
]

OMX_CONFIG_PLANEBLENDTYPE = struct_OMX_CONFIG_PLANEBLENDTYPE # OMX_IVCommon.h: 371

# OMX_IVCommon.h: 379
class struct_OMX_PARAM_INTERLEAVETYPE(Structure):
    pass

struct_OMX_PARAM_INTERLEAVETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnable',
    'nInterleavePortIndex',
]
struct_OMX_PARAM_INTERLEAVETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnable', OMX_BOOL),
    ('nInterleavePortIndex', OMX_U32),
]

OMX_PARAM_INTERLEAVETYPE = struct_OMX_PARAM_INTERLEAVETYPE # OMX_IVCommon.h: 379

enum_OMX_TRANSITIONEFFECTTYPE = c_int # OMX_IVCommon.h: 392

OMX_EffectNone = 0 # OMX_IVCommon.h: 392

OMX_EffectFadeFromBlack = (OMX_EffectNone + 1) # OMX_IVCommon.h: 392

OMX_EffectFadeToBlack = (OMX_EffectFadeFromBlack + 1) # OMX_IVCommon.h: 392

OMX_EffectUnspecifiedThroughConstantColor = (OMX_EffectFadeToBlack + 1) # OMX_IVCommon.h: 392

OMX_EffectDissolve = (OMX_EffectUnspecifiedThroughConstantColor + 1) # OMX_IVCommon.h: 392

OMX_EffectWipe = (OMX_EffectDissolve + 1) # OMX_IVCommon.h: 392

OMX_EffectUnspecifiedMixOfTwoScenes = (OMX_EffectWipe + 1) # OMX_IVCommon.h: 392

OMX_EffectKhronosExtensions = 1862270976 # OMX_IVCommon.h: 392

OMX_EffectVendorStartUnused = 2130706432 # OMX_IVCommon.h: 392

OMX_EffectMax = 2147483647 # OMX_IVCommon.h: 392

OMX_TRANSITIONEFFECTTYPE = enum_OMX_TRANSITIONEFFECTTYPE # OMX_IVCommon.h: 392

# OMX_IVCommon.h: 399
class struct_OMX_CONFIG_TRANSITIONEFFECTTYPE(Structure):
    pass

struct_OMX_CONFIG_TRANSITIONEFFECTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eEffect',
]
struct_OMX_CONFIG_TRANSITIONEFFECTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eEffect', OMX_TRANSITIONEFFECTTYPE),
]

OMX_CONFIG_TRANSITIONEFFECTTYPE = struct_OMX_CONFIG_TRANSITIONEFFECTTYPE # OMX_IVCommon.h: 399

enum_OMX_DATAUNITTYPE = c_int # OMX_IVCommon.h: 409

OMX_DataUnitCodedPicture = 0 # OMX_IVCommon.h: 409

OMX_DataUnitVideoSegment = (OMX_DataUnitCodedPicture + 1) # OMX_IVCommon.h: 409

OMX_DataUnitSeveralSegments = (OMX_DataUnitVideoSegment + 1) # OMX_IVCommon.h: 409

OMX_DataUnitArbitraryStreamSection = (OMX_DataUnitSeveralSegments + 1) # OMX_IVCommon.h: 409

OMX_DataUnitKhronosExtensions = 1862270976 # OMX_IVCommon.h: 409

OMX_DataUnitVendorStartUnused = 2130706432 # OMX_IVCommon.h: 409

OMX_DataUnitMax = 2147483647 # OMX_IVCommon.h: 409

OMX_DATAUNITTYPE = enum_OMX_DATAUNITTYPE # OMX_IVCommon.h: 409

enum_OMX_DATAUNITENCAPSULATIONTYPE = c_int # OMX_IVCommon.h: 418

OMX_DataEncapsulationElementaryStream = 0 # OMX_IVCommon.h: 418

OMX_DataEncapsulationGenericPayload = (OMX_DataEncapsulationElementaryStream + 1) # OMX_IVCommon.h: 418

OMX_DataEncapsulationRtpPayload = (OMX_DataEncapsulationGenericPayload + 1) # OMX_IVCommon.h: 418

OMX_DataEncapsulationKhronosExtensions = 1862270976 # OMX_IVCommon.h: 418

OMX_DataEncapsulationVendorStartUnused = 2130706432 # OMX_IVCommon.h: 418

OMX_DataEncapsulationMax = 2147483647 # OMX_IVCommon.h: 418

OMX_DATAUNITENCAPSULATIONTYPE = enum_OMX_DATAUNITENCAPSULATIONTYPE # OMX_IVCommon.h: 418

# OMX_IVCommon.h: 426
class struct_OMX_PARAM_DATAUNITTYPE(Structure):
    pass

struct_OMX_PARAM_DATAUNITTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eUnitType',
    'eEncapsulationType',
]
struct_OMX_PARAM_DATAUNITTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eUnitType', OMX_DATAUNITTYPE),
    ('eEncapsulationType', OMX_DATAUNITENCAPSULATIONTYPE),
]

OMX_PARAM_DATAUNITTYPE = struct_OMX_PARAM_DATAUNITTYPE # OMX_IVCommon.h: 426

enum_OMX_DITHERTYPE = c_int # OMX_IVCommon.h: 436

OMX_DitherNone = 0 # OMX_IVCommon.h: 436

OMX_DitherOrdered = (OMX_DitherNone + 1) # OMX_IVCommon.h: 436

OMX_DitherErrorDiffusion = (OMX_DitherOrdered + 1) # OMX_IVCommon.h: 436

OMX_DitherOther = (OMX_DitherErrorDiffusion + 1) # OMX_IVCommon.h: 436

OMX_DitherKhronosExtensions = 1862270976 # OMX_IVCommon.h: 436

OMX_DitherVendorStartUnused = 2130706432 # OMX_IVCommon.h: 436

OMX_DitherMax = 2147483647 # OMX_IVCommon.h: 436

OMX_DITHERTYPE = enum_OMX_DITHERTYPE # OMX_IVCommon.h: 436

# OMX_IVCommon.h: 443
class struct_OMX_CONFIG_DITHERTYPE(Structure):
    pass

struct_OMX_CONFIG_DITHERTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eDither',
]
struct_OMX_CONFIG_DITHERTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eDither', OMX_DITHERTYPE),
]

OMX_CONFIG_DITHERTYPE = struct_OMX_CONFIG_DITHERTYPE # OMX_IVCommon.h: 443

# OMX_IVCommon.h: 452
class struct_OMX_CONFIG_CAPTUREMODETYPE(Structure):
    pass

struct_OMX_CONFIG_CAPTUREMODETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bContinuous',
    'bFrameLimited',
    'nFrameLimit',
]
struct_OMX_CONFIG_CAPTUREMODETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bContinuous', OMX_BOOL),
    ('bFrameLimited', OMX_BOOL),
    ('nFrameLimit', OMX_U32),
]

OMX_CONFIG_CAPTUREMODETYPE = struct_OMX_CONFIG_CAPTUREMODETYPE # OMX_IVCommon.h: 452

enum_OMX_METERINGTYPE = c_int # OMX_IVCommon.h: 461

OMX_MeteringModeAverage = 0 # OMX_IVCommon.h: 461

OMX_MeteringModeSpot = (OMX_MeteringModeAverage + 1) # OMX_IVCommon.h: 461

OMX_MeteringModeMatrix = (OMX_MeteringModeSpot + 1) # OMX_IVCommon.h: 461

OMX_MeteringKhronosExtensions = 1862270976 # OMX_IVCommon.h: 461

OMX_MeteringVendorStartUnused = 2130706432 # OMX_IVCommon.h: 461

OMX_EVModeMax = 2147483647 # OMX_IVCommon.h: 461

OMX_METERINGTYPE = enum_OMX_METERINGTYPE # OMX_IVCommon.h: 461

# OMX_IVCommon.h: 475
class struct_OMX_CONFIG_EXPOSUREVALUETYPE(Structure):
    pass

struct_OMX_CONFIG_EXPOSUREVALUETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eMetering',
    'xEVCompensation',
    'nApertureFNumber',
    'bAutoAperture',
    'nShutterSpeedMsec',
    'bAutoShutterSpeed',
    'nSensitivity',
    'bAutoSensitivity',
]
struct_OMX_CONFIG_EXPOSUREVALUETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eMetering', OMX_METERINGTYPE),
    ('xEVCompensation', OMX_S32),
    ('nApertureFNumber', OMX_U32),
    ('bAutoAperture', OMX_BOOL),
    ('nShutterSpeedMsec', OMX_U32),
    ('bAutoShutterSpeed', OMX_BOOL),
    ('nSensitivity', OMX_U32),
    ('bAutoSensitivity', OMX_BOOL),
]

OMX_CONFIG_EXPOSUREVALUETYPE = struct_OMX_CONFIG_EXPOSUREVALUETYPE # OMX_IVCommon.h: 475

enum_OMX_FOCUSSTATUSTYPE = c_int # OMX_IVCommon.h: 486

OMX_FocusStatusOff = 0 # OMX_IVCommon.h: 486

OMX_FocusStatusRequest = (OMX_FocusStatusOff + 1) # OMX_IVCommon.h: 486

OMX_FocusStatusReached = (OMX_FocusStatusRequest + 1) # OMX_IVCommon.h: 486

OMX_FocusStatusUnableToReach = (OMX_FocusStatusReached + 1) # OMX_IVCommon.h: 486

OMX_FocusStatusLost = (OMX_FocusStatusUnableToReach + 1) # OMX_IVCommon.h: 486

OMX_FocusStatusKhronosExtensions = 1862270976 # OMX_IVCommon.h: 486

OMX_FocusStatusVendorStartUnused = 2130706432 # OMX_IVCommon.h: 486

OMX_FocusStatusMax = 2147483647 # OMX_IVCommon.h: 486

OMX_FOCUSSTATUSTYPE = enum_OMX_FOCUSSTATUSTYPE # OMX_IVCommon.h: 486

# OMX_IVCommon.h: 493
class struct_OMX_SHARPNESSTYPE(Structure):
    pass

struct_OMX_SHARPNESSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nSharpness',
]
struct_OMX_SHARPNESSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nSharpness', OMX_S32),
]

OMX_SHARPNESSTYPE = struct_OMX_SHARPNESSTYPE # OMX_IVCommon.h: 493

# OMX_IVCommon.h: 500
class struct_OMX_CONFIG_ZOOMFACTORTYPE(Structure):
    pass

struct_OMX_CONFIG_ZOOMFACTORTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'xZoomFactor',
]
struct_OMX_CONFIG_ZOOMFACTORTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('xZoomFactor', OMX_BU32),
]

OMX_CONFIG_ZOOMFACTORTYPE = struct_OMX_CONFIG_ZOOMFACTORTYPE # OMX_IVCommon.h: 500

enum_OMX_IMAGE_LOCKTYPE = c_int # OMX_IVCommon.h: 509

OMX_IMAGE_LockOff = 0 # OMX_IVCommon.h: 509

OMX_IMAGE_LockImmediate = (OMX_IMAGE_LockOff + 1) # OMX_IVCommon.h: 509

OMX_IMAGE_LockAtCapture = (OMX_IMAGE_LockImmediate + 1) # OMX_IVCommon.h: 509

OMX_IMAGE_LockKhronosExtensions = 1862270976 # OMX_IVCommon.h: 509

OMX_IMAGE_LockVendorStartUnused = 2130706432 # OMX_IVCommon.h: 509

OMX_IMAGE_LockMax = 2147483647 # OMX_IVCommon.h: 509

OMX_IMAGE_LOCKTYPE = enum_OMX_IMAGE_LOCKTYPE # OMX_IVCommon.h: 509

# OMX_IVCommon.h: 516
class struct_OMX_IMAGE_CONFIG_LOCKTYPE(Structure):
    pass

struct_OMX_IMAGE_CONFIG_LOCKTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eImageLock',
]
struct_OMX_IMAGE_CONFIG_LOCKTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eImageLock', OMX_IMAGE_LOCKTYPE),
]

OMX_IMAGE_CONFIG_LOCKTYPE = struct_OMX_IMAGE_CONFIG_LOCKTYPE # OMX_IVCommon.h: 516

enum_OMX_FOCUSRANGETYPE = c_int # OMX_IVCommon.h: 528

OMX_FocusRangeAuto = 0 # OMX_IVCommon.h: 528

OMX_FocusRangeHyperfocal = (OMX_FocusRangeAuto + 1) # OMX_IVCommon.h: 528

OMX_FocusRangeNormal = (OMX_FocusRangeHyperfocal + 1) # OMX_IVCommon.h: 528

OMX_FocusRangeSuperMacro = (OMX_FocusRangeNormal + 1) # OMX_IVCommon.h: 528

OMX_FocusRangeMacro = (OMX_FocusRangeSuperMacro + 1) # OMX_IVCommon.h: 528

OMX_FocusRangeInfinity = (OMX_FocusRangeMacro + 1) # OMX_IVCommon.h: 528

OMX_FocusRangeKhronosExtensions = 1862270976 # OMX_IVCommon.h: 528

OMX_FocusRangeVendorStartUnused = 2130706432 # OMX_IVCommon.h: 528

OMX_FocusRangeMax = 2147483647 # OMX_IVCommon.h: 528

OMX_FOCUSRANGETYPE = enum_OMX_FOCUSRANGETYPE # OMX_IVCommon.h: 528

# OMX_IVCommon.h: 535
class struct_OMX_CONFIG_FOCUSRANGETYPE(Structure):
    pass

struct_OMX_CONFIG_FOCUSRANGETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eFocusRange',
]
struct_OMX_CONFIG_FOCUSRANGETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eFocusRange', OMX_FOCUSRANGETYPE),
]

OMX_CONFIG_FOCUSRANGETYPE = struct_OMX_CONFIG_FOCUSRANGETYPE # OMX_IVCommon.h: 535

enum_OMX_IMAGE_FLASHSTATUSTYPE = c_int # OMX_IVCommon.h: 548

OMX_IMAGE_FlashUnknown = 0 # OMX_IVCommon.h: 548

OMX_IMAGE_FlashOff = (OMX_IMAGE_FlashUnknown + 1) # OMX_IVCommon.h: 548

OMX_IMAGE_FlashCharging = (OMX_IMAGE_FlashOff + 1) # OMX_IVCommon.h: 548

OMX_IMAGE_FlashReady = (OMX_IMAGE_FlashCharging + 1) # OMX_IVCommon.h: 548

OMX_IMAGE_FlashNotAvailable = (OMX_IMAGE_FlashReady + 1) # OMX_IVCommon.h: 548

OMX_IMAGE_FlashInsufficientCharge = (OMX_IMAGE_FlashNotAvailable + 1) # OMX_IVCommon.h: 548

OMX_IMAGE_FlashKhronosExtensions = 1862270976 # OMX_IVCommon.h: 548

OMX_IMAGE_FlashVendorStartUnused = 2130706432 # OMX_IVCommon.h: 548

OMX_IMAGE_FlashMax = 2147483647 # OMX_IVCommon.h: 548

OMX_IMAGE_FLASHSTATUSTYPE = enum_OMX_IMAGE_FLASHSTATUSTYPE # OMX_IVCommon.h: 548

# OMX_IVCommon.h: 554
class struct_OMX_IMAGE_CONFIG_FLASHSTATUSTYPE(Structure):
    pass

struct_OMX_IMAGE_CONFIG_FLASHSTATUSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'eFlashStatus',
]
struct_OMX_IMAGE_CONFIG_FLASHSTATUSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('eFlashStatus', OMX_IMAGE_FLASHSTATUSTYPE),
]

OMX_IMAGE_CONFIG_FLASHSTATUSTYPE = struct_OMX_IMAGE_CONFIG_FLASHSTATUSTYPE # OMX_IVCommon.h: 554

# OMX_IVCommon.h: 562
class struct_OMX_CONFIG_EXTCAPTUREMODETYPE(Structure):
    pass

struct_OMX_CONFIG_EXTCAPTUREMODETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nFrameBefore',
    'bPrepareCapture',
]
struct_OMX_CONFIG_EXTCAPTUREMODETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nFrameBefore', OMX_U32),
    ('bPrepareCapture', OMX_BOOL),
]

OMX_CONFIG_EXTCAPTUREMODETYPE = struct_OMX_CONFIG_EXTCAPTUREMODETYPE # OMX_IVCommon.h: 562

enum_OMX_NDFILTERCONTROLTYPE = c_int # OMX_IVCommon.h: 571

OMX_NDFilterOff = 0 # OMX_IVCommon.h: 571

OMX_NDFilterOn = (OMX_NDFilterOff + 1) # OMX_IVCommon.h: 571

OMX_NDFilterAuto = (OMX_NDFilterOn + 1) # OMX_IVCommon.h: 571

OMX_NDFilterKhronosExtensions = 1862270976 # OMX_IVCommon.h: 571

OMX_NDFilterVendorStartUnused = 2130706432 # OMX_IVCommon.h: 571

OMX_NDFilterMax = 2147483647 # OMX_IVCommon.h: 571

OMX_NDFILTERCONTROLTYPE = enum_OMX_NDFILTERCONTROLTYPE # OMX_IVCommon.h: 571

# OMX_IVCommon.h: 577
class struct_OMX_CONFIG_NDFILTERCONTROLTYPE(Structure):
    pass

struct_OMX_CONFIG_NDFILTERCONTROLTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'eNDFilterControl',
]
struct_OMX_CONFIG_NDFILTERCONTROLTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('eNDFilterControl', OMX_NDFILTERCONTROLTYPE),
]

OMX_CONFIG_NDFILTERCONTROLTYPE = struct_OMX_CONFIG_NDFILTERCONTROLTYPE # OMX_IVCommon.h: 577

enum_OMX_AFASSISTANTLIGHTTYPE = c_int # OMX_IVCommon.h: 586

OMX_AFAssistantLightOff = 0 # OMX_IVCommon.h: 586

OMX_AFAssistantLightOn = (OMX_AFAssistantLightOff + 1) # OMX_IVCommon.h: 586

OMX_AFAssistantLightAuto = (OMX_AFAssistantLightOn + 1) # OMX_IVCommon.h: 586

OMX_AFAssistantLightKhronosExtensions = 1862270976 # OMX_IVCommon.h: 586

OMX_AFAssistantLightVendorStartUnused = 2130706432 # OMX_IVCommon.h: 586

OMX_AFAssistantLightMax = 2147483647 # OMX_IVCommon.h: 586

OMX_AFASSISTANTLIGHTTYPE = enum_OMX_AFASSISTANTLIGHTTYPE # OMX_IVCommon.h: 586

# OMX_IVCommon.h: 592
class struct_OMX_CONFIG_AFASSISTANTLIGHTTYPE(Structure):
    pass

struct_OMX_CONFIG_AFASSISTANTLIGHTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'eAFAssistantLight',
]
struct_OMX_CONFIG_AFASSISTANTLIGHTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('eAFAssistantLight', OMX_AFASSISTANTLIGHTTYPE),
]

OMX_CONFIG_AFASSISTANTLIGHTTYPE = struct_OMX_CONFIG_AFASSISTANTLIGHTTYPE # OMX_IVCommon.h: 592

# OMX_IVCommon.h: 608
class struct_OMX_INTERLACEFORMATTYPE(Structure):
    pass

struct_OMX_INTERLACEFORMATTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nFormat',
    'nTimeStamp',
]
struct_OMX_INTERLACEFORMATTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nFormat', OMX_U32),
    ('nTimeStamp', OMX_TICKS),
]

OMX_INTERLACEFORMATTYPE = struct_OMX_INTERLACEFORMATTYPE # OMX_IVCommon.h: 608

# OMX_IVCommon.h: 615
class struct_OMX_DEINTERLACETYPE(Structure):
    pass

struct_OMX_DEINTERLACETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnable',
]
struct_OMX_DEINTERLACETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnable', OMX_BOOL),
]

OMX_DEINTERLACETYPE = struct_OMX_DEINTERLACETYPE # OMX_IVCommon.h: 615

# OMX_IVCommon.h: 623
class struct_OMX_STREAMINTERLACEFORMATTYPE(Structure):
    pass

struct_OMX_STREAMINTERLACEFORMATTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bInterlaceFormat',
    'nInterlaceFormats',
]
struct_OMX_STREAMINTERLACEFORMATTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bInterlaceFormat', OMX_BOOL),
    ('nInterlaceFormats', OMX_U32),
]

OMX_STREAMINTERLACEFORMAT = struct_OMX_STREAMINTERLACEFORMATTYPE # OMX_IVCommon.h: 623

# OMX_IVCommon.h: 632
class struct_OMX_FROITYPE(Structure):
    pass

struct_OMX_FROITYPE.__slots__ = [
    'nRectX',
    'nRectY',
    'nRectWidth',
    'nRectHeight',
    'xFocusDistance',
    'eFocusStatus',
]
struct_OMX_FROITYPE._fields_ = [
    ('nRectX', OMX_S32),
    ('nRectY', OMX_S32),
    ('nRectWidth', OMX_S32),
    ('nRectHeight', OMX_S32),
    ('xFocusDistance', OMX_S32),
    ('eFocusStatus', OMX_FOCUSSTATUSTYPE),
]

OMX_FROITYPE = struct_OMX_FROITYPE # OMX_IVCommon.h: 632

# OMX_IVCommon.h: 641
class struct_OMX_CONFIG_FOCUSREGIONSTATUSTYPE(Structure):
    pass

struct_OMX_CONFIG_FOCUSREGIONSTATUSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'bFocused',
    'nMaxFAreas',
    'nFAreas',
    'sFROIs',
]
struct_OMX_CONFIG_FOCUSREGIONSTATUSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('bFocused', OMX_BOOL),
    ('nMaxFAreas', OMX_U32),
    ('nFAreas', OMX_U32),
    ('sFROIs', OMX_FROITYPE * 1),
]

OMX_CONFIG_FOCUSREGIONSTATUSTYPE = struct_OMX_CONFIG_FOCUSREGIONSTATUSTYPE # OMX_IVCommon.h: 641

enum_OMX_FOCUSREGIONCONTROLTYPE = c_int # OMX_IVCommon.h: 651

OMX_FocusRegionControlAuto = 0 # OMX_IVCommon.h: 651

OMX_FocusRegionControlManual = (OMX_FocusRegionControlAuto + 1) # OMX_IVCommon.h: 651

OMX_FocusRegionControlFacePriority = (OMX_FocusRegionControlManual + 1) # OMX_IVCommon.h: 651

OMX_FocusRegionControlObjectPriority = (OMX_FocusRegionControlFacePriority + 1) # OMX_IVCommon.h: 651

OMX_FocusRegionControlKhronosExtensions = 1862270976 # OMX_IVCommon.h: 651

OMX_FocusRegionControlVendorStartUnused = 2130706432 # OMX_IVCommon.h: 651

OMX_FocusRegionControlMax = 2147483647 # OMX_IVCommon.h: 651

OMX_FOCUSREGIONCONTROLTYPE = enum_OMX_FOCUSREGIONCONTROLTYPE # OMX_IVCommon.h: 651

# OMX_IVCommon.h: 658
class struct_OMX_MANUALFOCUSRECTTYPE(Structure):
    pass

struct_OMX_MANUALFOCUSRECTTYPE.__slots__ = [
    'nRectX',
    'nRectY',
    'nRectWidth',
    'nRectHeight',
]
struct_OMX_MANUALFOCUSRECTTYPE._fields_ = [
    ('nRectX', OMX_S32),
    ('nRectY', OMX_S32),
    ('nRectWidth', OMX_S32),
    ('nRectHeight', OMX_S32),
]

OMX_MANUALFOCUSRECTTYPE = struct_OMX_MANUALFOCUSRECTTYPE # OMX_IVCommon.h: 658

# OMX_IVCommon.h: 666
class struct_OMX_CONFIG_FOCUSREGIONCONTROLTYPE(Structure):
    pass

struct_OMX_CONFIG_FOCUSREGIONCONTROLTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nFAreas',
    'eFocusRegionsControl',
    'sManualFRegions',
]
struct_OMX_CONFIG_FOCUSREGIONCONTROLTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nFAreas', OMX_U32),
    ('eFocusRegionsControl', OMX_FOCUSREGIONCONTROLTYPE),
    ('sManualFRegions', OMX_MANUALFOCUSRECTTYPE * 1),
]

OMX_CONFIG_FOCUSREGIONCONTROLTYPE = struct_OMX_CONFIG_FOCUSREGIONCONTROLTYPE # OMX_IVCommon.h: 666

enum_OMX_VIDEO_CODINGTYPE = c_int # OMX_Video.h: 61

OMX_VIDEO_CodingUnused = 0 # OMX_Video.h: 61

OMX_VIDEO_CodingAutoDetect = (OMX_VIDEO_CodingUnused + 1) # OMX_Video.h: 61

OMX_VIDEO_CodingMPEG2 = (OMX_VIDEO_CodingAutoDetect + 1) # OMX_Video.h: 61

OMX_VIDEO_CodingH263 = (OMX_VIDEO_CodingMPEG2 + 1) # OMX_Video.h: 61

OMX_VIDEO_CodingMPEG4 = (OMX_VIDEO_CodingH263 + 1) # OMX_Video.h: 61

OMX_VIDEO_CodingWMV = (OMX_VIDEO_CodingMPEG4 + 1) # OMX_Video.h: 61

OMX_VIDEO_CodingRV = (OMX_VIDEO_CodingWMV + 1) # OMX_Video.h: 61

OMX_VIDEO_CodingAVC = (OMX_VIDEO_CodingRV + 1) # OMX_Video.h: 61

OMX_VIDEO_CodingMJPEG = (OMX_VIDEO_CodingAVC + 1) # OMX_Video.h: 61

OMX_VIDEO_CodingVC1 = (OMX_VIDEO_CodingMJPEG + 1) # OMX_Video.h: 61

OMX_VIDEO_CodingVP8 = (OMX_VIDEO_CodingVC1 + 1) # OMX_Video.h: 61

OMX_VIDEO_CodingKhronosExtensions = 1862270976 # OMX_Video.h: 61

OMX_VIDEO_CodingVendorStartUnused = 2130706432 # OMX_Video.h: 61

OMX_VIDEO_CodingMax = 2147483647 # OMX_Video.h: 61

OMX_VIDEO_CODINGTYPE = enum_OMX_VIDEO_CODINGTYPE # OMX_Video.h: 61

# OMX_Video.h: 75
class struct_OMX_VIDEO_PORTDEFINITIONTYPE(Structure):
    pass

struct_OMX_VIDEO_PORTDEFINITIONTYPE.__slots__ = [
    'pNativeRender',
    'nFrameWidth',
    'nFrameHeight',
    'nStride',
    'nSliceHeight',
    'nBitrate',
    'xFramerate',
    'bFlagErrorConcealment',
    'eCompressionFormat',
    'eColorFormat',
    'pNativeWindow',
]
struct_OMX_VIDEO_PORTDEFINITIONTYPE._fields_ = [
    ('pNativeRender', OMX_NATIVE_DEVICETYPE),
    ('nFrameWidth', OMX_U32),
    ('nFrameHeight', OMX_U32),
    ('nStride', OMX_S32),
    ('nSliceHeight', OMX_U32),
    ('nBitrate', OMX_U32),
    ('xFramerate', OMX_U32),
    ('bFlagErrorConcealment', OMX_BOOL),
    ('eCompressionFormat', OMX_VIDEO_CODINGTYPE),
    ('eColorFormat', OMX_COLOR_FORMATTYPE),
    ('pNativeWindow', OMX_NATIVE_WINDOWTYPE),
]

OMX_VIDEO_PORTDEFINITIONTYPE = struct_OMX_VIDEO_PORTDEFINITIONTYPE # OMX_Video.h: 75

# OMX_Video.h: 85
class struct_OMX_VIDEO_PARAM_PORTFORMATTYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_PORTFORMATTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nIndex',
    'eCompressionFormat',
    'eColorFormat',
    'xFramerate',
]
struct_OMX_VIDEO_PARAM_PORTFORMATTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nIndex', OMX_U32),
    ('eCompressionFormat', OMX_VIDEO_CODINGTYPE),
    ('eColorFormat', OMX_COLOR_FORMATTYPE),
    ('xFramerate', OMX_U32),
]

OMX_VIDEO_PARAM_PORTFORMATTYPE = struct_OMX_VIDEO_PARAM_PORTFORMATTYPE # OMX_Video.h: 85

# OMX_Video.h: 94
class struct_OMX_VIDEO_PARAM_QUANTIZATIONTYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_QUANTIZATIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nQpI',
    'nQpP',
    'nQpB',
]
struct_OMX_VIDEO_PARAM_QUANTIZATIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nQpI', OMX_U32),
    ('nQpP', OMX_U32),
    ('nQpB', OMX_U32),
]

OMX_VIDEO_PARAM_QUANTIZATIONTYPE = struct_OMX_VIDEO_PARAM_QUANTIZATIONTYPE # OMX_Video.h: 94

# OMX_Video.h: 104
class struct_OMX_VIDEO_PARAM_VIDEOFASTUPDATETYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_VIDEOFASTUPDATETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnableVFU',
    'nFirstGOB',
    'nFirstMB',
    'nNumMBs',
]
struct_OMX_VIDEO_PARAM_VIDEOFASTUPDATETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnableVFU', OMX_BOOL),
    ('nFirstGOB', OMX_U32),
    ('nFirstMB', OMX_U32),
    ('nNumMBs', OMX_U32),
]

OMX_VIDEO_PARAM_VIDEOFASTUPDATETYPE = struct_OMX_VIDEO_PARAM_VIDEOFASTUPDATETYPE # OMX_Video.h: 104

enum_OMX_VIDEO_CONTROLRATETYPE = c_int # OMX_Video.h: 115

OMX_Video_ControlRateDisable = 0 # OMX_Video.h: 115

OMX_Video_ControlRateVariable = (OMX_Video_ControlRateDisable + 1) # OMX_Video.h: 115

OMX_Video_ControlRateConstant = (OMX_Video_ControlRateVariable + 1) # OMX_Video.h: 115

OMX_Video_ControlRateVariableSkipFrames = (OMX_Video_ControlRateConstant + 1) # OMX_Video.h: 115

OMX_Video_ControlRateConstantSkipFrames = (OMX_Video_ControlRateVariableSkipFrames + 1) # OMX_Video.h: 115

OMX_Video_ControlRateKhronosExtensions = 1862270976 # OMX_Video.h: 115

OMX_Video_ControlRateVendorStartUnused = 2130706432 # OMX_Video.h: 115

OMX_Video_ControlRateMax = 2147483647 # OMX_Video.h: 115

OMX_VIDEO_CONTROLRATETYPE = enum_OMX_VIDEO_CONTROLRATETYPE # OMX_Video.h: 115

# OMX_Video.h: 123
class struct_OMX_VIDEO_PARAM_BITRATETYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_BITRATETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eControlRate',
    'nTargetBitrate',
]
struct_OMX_VIDEO_PARAM_BITRATETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eControlRate', OMX_VIDEO_CONTROLRATETYPE),
    ('nTargetBitrate', OMX_U32),
]

OMX_VIDEO_PARAM_BITRATETYPE = struct_OMX_VIDEO_PARAM_BITRATETYPE # OMX_Video.h: 123

enum_OMX_VIDEO_MOTIONVECTORTYPE = c_int # OMX_Video.h: 133

OMX_Video_MotionVectorPixel = 0 # OMX_Video.h: 133

OMX_Video_MotionVectorHalfPel = (OMX_Video_MotionVectorPixel + 1) # OMX_Video.h: 133

OMX_Video_MotionVectorQuarterPel = (OMX_Video_MotionVectorHalfPel + 1) # OMX_Video.h: 133

OMX_Video_MotionVectorEighthPel = (OMX_Video_MotionVectorQuarterPel + 1) # OMX_Video.h: 133

OMX_Video_MotionVectorKhronosExtensions = 1862270976 # OMX_Video.h: 133

OMX_Video_MotionVectorVendorStartUnused = 2130706432 # OMX_Video.h: 133

OMX_Video_MotionVectorMax = 2147483647 # OMX_Video.h: 133

OMX_VIDEO_MOTIONVECTORTYPE = enum_OMX_VIDEO_MOTIONVECTORTYPE # OMX_Video.h: 133

# OMX_Video.h: 144
class struct_OMX_VIDEO_PARAM_MOTIONVECTORTYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_MOTIONVECTORTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eAccuracy',
    'bUnrestrictedMVs',
    'bFourMV',
    'sXSearchRange',
    'sYSearchRange',
]
struct_OMX_VIDEO_PARAM_MOTIONVECTORTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eAccuracy', OMX_VIDEO_MOTIONVECTORTYPE),
    ('bUnrestrictedMVs', OMX_BOOL),
    ('bFourMV', OMX_BOOL),
    ('sXSearchRange', OMX_S32),
    ('sYSearchRange', OMX_S32),
]

OMX_VIDEO_PARAM_MOTIONVECTORTYPE = struct_OMX_VIDEO_PARAM_MOTIONVECTORTYPE # OMX_Video.h: 144

enum_OMX_VIDEO_INTRAREFRESHTYPE = c_int # OMX_Video.h: 153

OMX_VIDEO_IntraRefreshCyclic = 0 # OMX_Video.h: 153

OMX_VIDEO_IntraRefreshAdaptive = (OMX_VIDEO_IntraRefreshCyclic + 1) # OMX_Video.h: 153

OMX_VIDEO_IntraRefreshBoth = (OMX_VIDEO_IntraRefreshAdaptive + 1) # OMX_Video.h: 153

OMX_VIDEO_IntraRefreshKhronosExtensions = 1862270976 # OMX_Video.h: 153

OMX_VIDEO_IntraRefreshVendorStartUnused = 2130706432 # OMX_Video.h: 153

OMX_VIDEO_IntraRefreshMax = 2147483647 # OMX_Video.h: 153

OMX_VIDEO_INTRAREFRESHTYPE = enum_OMX_VIDEO_INTRAREFRESHTYPE # OMX_Video.h: 153

# OMX_Video.h: 163
class struct_OMX_VIDEO_PARAM_INTRAREFRESHTYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_INTRAREFRESHTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eRefreshMode',
    'nAirMBs',
    'nAirRef',
    'nCirMBs',
]
struct_OMX_VIDEO_PARAM_INTRAREFRESHTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eRefreshMode', OMX_VIDEO_INTRAREFRESHTYPE),
    ('nAirMBs', OMX_U32),
    ('nAirRef', OMX_U32),
    ('nCirMBs', OMX_U32),
]

OMX_VIDEO_PARAM_INTRAREFRESHTYPE = struct_OMX_VIDEO_PARAM_INTRAREFRESHTYPE # OMX_Video.h: 163

# OMX_Video.h: 174
class struct_OMX_VIDEO_PARAM_ERRORCORRECTIONTYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_ERRORCORRECTIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnableHEC',
    'bEnableResync',
    'nResynchMarkerSpacing',
    'bEnableDataPartitioning',
    'bEnableRVLC',
]
struct_OMX_VIDEO_PARAM_ERRORCORRECTIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnableHEC', OMX_BOOL),
    ('bEnableResync', OMX_BOOL),
    ('nResynchMarkerSpacing', OMX_U32),
    ('bEnableDataPartitioning', OMX_BOOL),
    ('bEnableRVLC', OMX_BOOL),
]

OMX_VIDEO_PARAM_ERRORCORRECTIONTYPE = struct_OMX_VIDEO_PARAM_ERRORCORRECTIONTYPE # OMX_Video.h: 174

# OMX_Video.h: 187
class struct_OMX_VIDEO_PARAM_VBSMCTYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_VBSMCTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'b16x16',
    'b16x8',
    'b8x16',
    'b8x8',
    'b8x4',
    'b4x8',
    'b4x4',
]
struct_OMX_VIDEO_PARAM_VBSMCTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('b16x16', OMX_BOOL),
    ('b16x8', OMX_BOOL),
    ('b8x16', OMX_BOOL),
    ('b8x8', OMX_BOOL),
    ('b8x4', OMX_BOOL),
    ('b4x8', OMX_BOOL),
    ('b4x4', OMX_BOOL),
]

OMX_VIDEO_PARAM_VBSMCTYPE = struct_OMX_VIDEO_PARAM_VBSMCTYPE # OMX_Video.h: 187

enum_OMX_VIDEO_H263PROFILETYPE = c_int # OMX_Video.h: 203

OMX_VIDEO_H263ProfileBaseline = 1 # OMX_Video.h: 203

OMX_VIDEO_H263ProfileH320Coding = 2 # OMX_Video.h: 203

OMX_VIDEO_H263ProfileBackwardCompatible = 4 # OMX_Video.h: 203

OMX_VIDEO_H263ProfileISWV2 = 8 # OMX_Video.h: 203

OMX_VIDEO_H263ProfileISWV3 = 16 # OMX_Video.h: 203

OMX_VIDEO_H263ProfileHighCompression = 32 # OMX_Video.h: 203

OMX_VIDEO_H263ProfileInternet = 64 # OMX_Video.h: 203

OMX_VIDEO_H263ProfileInterlace = 128 # OMX_Video.h: 203

OMX_VIDEO_H263ProfileHighLatency = 256 # OMX_Video.h: 203

OMX_VIDEO_H263ProfileUnknown = 1862270975 # OMX_Video.h: 203

OMX_VIDEO_H263ProfileKhronosExtensions = 1862270976 # OMX_Video.h: 203

OMX_VIDEO_H263ProfileVendorStartUnused = 2130706432 # OMX_Video.h: 203

OMX_VIDEO_H263ProfileMax = 2147483647 # OMX_Video.h: 203

OMX_VIDEO_H263PROFILETYPE = enum_OMX_VIDEO_H263PROFILETYPE # OMX_Video.h: 203

enum_OMX_VIDEO_H263LEVELTYPE = c_int # OMX_Video.h: 218

OMX_VIDEO_H263Level10 = 1 # OMX_Video.h: 218

OMX_VIDEO_H263Level20 = 2 # OMX_Video.h: 218

OMX_VIDEO_H263Level30 = 4 # OMX_Video.h: 218

OMX_VIDEO_H263Level40 = 8 # OMX_Video.h: 218

OMX_VIDEO_H263Level45 = 16 # OMX_Video.h: 218

OMX_VIDEO_H263Level50 = 32 # OMX_Video.h: 218

OMX_VIDEO_H263Level60 = 64 # OMX_Video.h: 218

OMX_VIDEO_H263Level70 = 128 # OMX_Video.h: 218

OMX_VIDEO_H263LevelUnknown = 1862270975 # OMX_Video.h: 218

OMX_VIDEO_H263LevelKhronosExtensions = 1862270976 # OMX_Video.h: 218

OMX_VIDEO_H263LevelVendorStartUnused = 2130706432 # OMX_Video.h: 218

OMX_VIDEO_H263LevelMax = 2147483647 # OMX_Video.h: 218

OMX_VIDEO_H263LEVELTYPE = enum_OMX_VIDEO_H263LEVELTYPE # OMX_Video.h: 218

enum_OMX_VIDEO_PICTURETYPE = c_int # OMX_Video.h: 230

OMX_VIDEO_PictureTypeI = (1 << 0) # OMX_Video.h: 230

OMX_VIDEO_PictureTypeP = (1 << 1) # OMX_Video.h: 230

OMX_VIDEO_PictureTypeB = (1 << 2) # OMX_Video.h: 230

OMX_VIDEO_PictureTypeSI = (1 << 3) # OMX_Video.h: 230

OMX_VIDEO_PictureTypeSP = (1 << 4) # OMX_Video.h: 230

OMX_VIDEO_PictureTypeEI = (1 << 5) # OMX_Video.h: 230

OMX_VIDEO_PictureTypeEP = (1 << 6) # OMX_Video.h: 230

OMX_VIDEO_PictureTypeS = (1 << 7) # OMX_Video.h: 230

OMX_VIDEO_PictureTypeMax = 2147483647 # OMX_Video.h: 230

OMX_VIDEO_PICTURETYPE = enum_OMX_VIDEO_PICTURETYPE # OMX_Video.h: 230

# OMX_Video.h: 245
class struct_OMX_VIDEO_PARAM_H263TYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_H263TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nPFrames',
    'nBFrames',
    'eProfile',
    'eLevel',
    'bPLUSPTYPEAllowed',
    'nAllowedPictureTypes',
    'bForceRoundingTypeToZero',
    'nPictureHeaderRepetition',
    'nGOBHeaderInterval',
]
struct_OMX_VIDEO_PARAM_H263TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nPFrames', OMX_U32),
    ('nBFrames', OMX_U32),
    ('eProfile', OMX_VIDEO_H263PROFILETYPE),
    ('eLevel', OMX_VIDEO_H263LEVELTYPE),
    ('bPLUSPTYPEAllowed', OMX_BOOL),
    ('nAllowedPictureTypes', OMX_U32),
    ('bForceRoundingTypeToZero', OMX_BOOL),
    ('nPictureHeaderRepetition', OMX_U32),
    ('nGOBHeaderInterval', OMX_U32),
]

OMX_VIDEO_PARAM_H263TYPE = struct_OMX_VIDEO_PARAM_H263TYPE # OMX_Video.h: 245

enum_OMX_VIDEO_MPEG2PROFILETYPE = c_int # OMX_Video.h: 258

OMX_VIDEO_MPEG2ProfileSimple = 0 # OMX_Video.h: 258

OMX_VIDEO_MPEG2ProfileMain = (OMX_VIDEO_MPEG2ProfileSimple + 1) # OMX_Video.h: 258

OMX_VIDEO_MPEG2Profile422 = (OMX_VIDEO_MPEG2ProfileMain + 1) # OMX_Video.h: 258

OMX_VIDEO_MPEG2ProfileSNR = (OMX_VIDEO_MPEG2Profile422 + 1) # OMX_Video.h: 258

OMX_VIDEO_MPEG2ProfileSpatial = (OMX_VIDEO_MPEG2ProfileSNR + 1) # OMX_Video.h: 258

OMX_VIDEO_MPEG2ProfileHigh = (OMX_VIDEO_MPEG2ProfileSpatial + 1) # OMX_Video.h: 258

OMX_VIDEO_MPEG2ProfileUnknown = 1862270975 # OMX_Video.h: 258

OMX_VIDEO_MPEG2ProfileKhronosExtensions = 1862270976 # OMX_Video.h: 258

OMX_VIDEO_MPEG2ProfileVendorStartUnused = 2130706432 # OMX_Video.h: 258

OMX_VIDEO_MPEG2ProfileMax = 2147483647 # OMX_Video.h: 258

OMX_VIDEO_MPEG2PROFILETYPE = enum_OMX_VIDEO_MPEG2PROFILETYPE # OMX_Video.h: 258

enum_OMX_VIDEO_MPEG2LEVELTYPE = c_int # OMX_Video.h: 269

OMX_VIDEO_MPEG2LevelLL = 0 # OMX_Video.h: 269

OMX_VIDEO_MPEG2LevelML = (OMX_VIDEO_MPEG2LevelLL + 1) # OMX_Video.h: 269

OMX_VIDEO_MPEG2LevelH14 = (OMX_VIDEO_MPEG2LevelML + 1) # OMX_Video.h: 269

OMX_VIDEO_MPEG2LevelHL = (OMX_VIDEO_MPEG2LevelH14 + 1) # OMX_Video.h: 269

OMX_VIDEO_MPEG2LevelUnknown = 1862270975 # OMX_Video.h: 269

OMX_VIDEO_MPEG2LevelKhronosExtensions = 1862270976 # OMX_Video.h: 269

OMX_VIDEO_MPEG2LevelVendorStartUnused = 2130706432 # OMX_Video.h: 269

OMX_VIDEO_MPEG2LevelMax = 2147483647 # OMX_Video.h: 269

OMX_VIDEO_MPEG2LEVELTYPE = enum_OMX_VIDEO_MPEG2LEVELTYPE # OMX_Video.h: 269

# OMX_Video.h: 279
class struct_OMX_VIDEO_PARAM_MPEG2TYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_MPEG2TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nPFrames',
    'nBFrames',
    'eProfile',
    'eLevel',
]
struct_OMX_VIDEO_PARAM_MPEG2TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nPFrames', OMX_U32),
    ('nBFrames', OMX_U32),
    ('eProfile', OMX_VIDEO_MPEG2PROFILETYPE),
    ('eLevel', OMX_VIDEO_MPEG2LEVELTYPE),
]

OMX_VIDEO_PARAM_MPEG2TYPE = struct_OMX_VIDEO_PARAM_MPEG2TYPE # OMX_Video.h: 279

enum_OMX_VIDEO_MPEG4PROFILETYPE = c_int # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileSimple = 1 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileSimpleScalable = 2 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileCore = 4 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileMain = 8 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileNbit = 16 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileScalableTexture = 32 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileSimpleFace = 64 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileSimpleFBA = 128 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileBasicAnimated = 256 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileHybrid = 512 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileAdvancedRealTime = 1024 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileCoreScalable = 2048 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileAdvancedCoding = 4096 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileAdvancedCore = 8192 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileAdvancedScalable = 16384 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileAdvancedSimple = 32768 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileUnknown = 1862270975 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileKhronosExtensions = 1862270976 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileVendorStartUnused = 2130706432 # OMX_Video.h: 302

OMX_VIDEO_MPEG4ProfileMax = 2147483647 # OMX_Video.h: 302

OMX_VIDEO_MPEG4PROFILETYPE = enum_OMX_VIDEO_MPEG4PROFILETYPE # OMX_Video.h: 302

enum_OMX_VIDEO_MPEG4LEVELTYPE = c_int # OMX_Video.h: 317

OMX_VIDEO_MPEG4Level0 = 1 # OMX_Video.h: 317

OMX_VIDEO_MPEG4Level0b = 2 # OMX_Video.h: 317

OMX_VIDEO_MPEG4Level1 = 4 # OMX_Video.h: 317

OMX_VIDEO_MPEG4Level2 = 8 # OMX_Video.h: 317

OMX_VIDEO_MPEG4Level3 = 16 # OMX_Video.h: 317

OMX_VIDEO_MPEG4Level4 = 32 # OMX_Video.h: 317

OMX_VIDEO_MPEG4Level4a = 64 # OMX_Video.h: 317

OMX_VIDEO_MPEG4Level5 = 128 # OMX_Video.h: 317

OMX_VIDEO_MPEG4LevelUnknown = 1862270975 # OMX_Video.h: 317

OMX_VIDEO_MPEG4LevelKhronosExtensions = 1862270976 # OMX_Video.h: 317

OMX_VIDEO_MPEG4LevelVendorStartUnused = 2130706432 # OMX_Video.h: 317

OMX_VIDEO_MPEG4LevelMax = 2147483647 # OMX_Video.h: 317

OMX_VIDEO_MPEG4LEVELTYPE = enum_OMX_VIDEO_MPEG4LEVELTYPE # OMX_Video.h: 317

# OMX_Video.h: 337
class struct_OMX_VIDEO_PARAM_MPEG4TYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_MPEG4TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nSliceHeaderSpacing',
    'bSVH',
    'bGov',
    'nPFrames',
    'nBFrames',
    'nIDCVLCThreshold',
    'bACPred',
    'nMaxPacketSize',
    'nTimeIncRes',
    'eProfile',
    'eLevel',
    'nAllowedPictureTypes',
    'nHeaderExtension',
    'bReversibleVLC',
]
struct_OMX_VIDEO_PARAM_MPEG4TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nSliceHeaderSpacing', OMX_U32),
    ('bSVH', OMX_BOOL),
    ('bGov', OMX_BOOL),
    ('nPFrames', OMX_U32),
    ('nBFrames', OMX_U32),
    ('nIDCVLCThreshold', OMX_U32),
    ('bACPred', OMX_BOOL),
    ('nMaxPacketSize', OMX_U32),
    ('nTimeIncRes', OMX_U32),
    ('eProfile', OMX_VIDEO_MPEG4PROFILETYPE),
    ('eLevel', OMX_VIDEO_MPEG4LEVELTYPE),
    ('nAllowedPictureTypes', OMX_U32),
    ('nHeaderExtension', OMX_U32),
    ('bReversibleVLC', OMX_BOOL),
]

OMX_VIDEO_PARAM_MPEG4TYPE = struct_OMX_VIDEO_PARAM_MPEG4TYPE # OMX_Video.h: 337

enum_OMX_VIDEO_WMVFORMATTYPE = c_int # OMX_Video.h: 348

OMX_VIDEO_WMVFormatUnused = 1 # OMX_Video.h: 348

OMX_VIDEO_WMVFormat7 = 2 # OMX_Video.h: 348

OMX_VIDEO_WMVFormat8 = 4 # OMX_Video.h: 348

OMX_VIDEO_WMVFormat9 = 8 # OMX_Video.h: 348

OMX_VIDEO_WMVFormatUnknown = 1862270975 # OMX_Video.h: 348

OMX_VIDEO_WMFFormatKhronosExtensions = 1862270976 # OMX_Video.h: 348

OMX_VIDEO_WMFFormatVendorStartUnused = 2130706432 # OMX_Video.h: 348

OMX_VIDEO_WMVFormatMax = 2147483647 # OMX_Video.h: 348

OMX_VIDEO_WMVFORMATTYPE = enum_OMX_VIDEO_WMVFORMATTYPE # OMX_Video.h: 348

enum_OMX_VIDEO_WMVPROFILETYPE = c_int # OMX_Video.h: 357

OMX_VIDEO_WMVProfileSimple = 0 # OMX_Video.h: 357

OMX_VIDEO_WMVProfileMain = (OMX_VIDEO_WMVProfileSimple + 1) # OMX_Video.h: 357

OMX_VIDEO_WMVProfileAdvanced = (OMX_VIDEO_WMVProfileMain + 1) # OMX_Video.h: 357

OMX_VIDEO_WMVProfileUnknown = 1862270975 # OMX_Video.h: 357

OMX_VIDEO_WMVProfileKhronosExtensions = 1862270976 # OMX_Video.h: 357

OMX_VIDEO_WMVProfileVendorStartUnused = 2130706432 # OMX_Video.h: 357

OMX_VIDEO_WMVPROFILETYPE = enum_OMX_VIDEO_WMVPROFILETYPE # OMX_Video.h: 357

enum_OMX_VIDEO_WMVLEVELTYPE = c_int # OMX_Video.h: 371

OMX_VIDEO_WMVLevelLow = 0 # OMX_Video.h: 371

OMX_VIDEO_WMVLevelMedium = (OMX_VIDEO_WMVLevelLow + 1) # OMX_Video.h: 371

OMX_VIDEO_WMVLevelHigh = (OMX_VIDEO_WMVLevelMedium + 1) # OMX_Video.h: 371

OMX_VIDEO_WMVLevelL0 = (OMX_VIDEO_WMVLevelHigh + 1) # OMX_Video.h: 371

OMX_VIDEO_WMVLevelL1 = (OMX_VIDEO_WMVLevelL0 + 1) # OMX_Video.h: 371

OMX_VIDEO_WMVLevelL2 = (OMX_VIDEO_WMVLevelL1 + 1) # OMX_Video.h: 371

OMX_VIDEO_WMVLevelL3 = (OMX_VIDEO_WMVLevelL2 + 1) # OMX_Video.h: 371

OMX_VIDEO_WMVLevelL4 = (OMX_VIDEO_WMVLevelL3 + 1) # OMX_Video.h: 371

OMX_VIDEO_WMVLevelUnknown = 1862270975 # OMX_Video.h: 371

OMX_VIDEO_WMVLevelKhronosExtensions = 1862270976 # OMX_Video.h: 371

OMX_VIDEO_WMVLevelVendorStartUnused = 2130706432 # OMX_Video.h: 371

OMX_VIDEO_WMVLEVELTYPE = enum_OMX_VIDEO_WMVLEVELTYPE # OMX_Video.h: 371

# OMX_Video.h: 378
class struct_OMX_VIDEO_PARAM_WMVTYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_WMVTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eFormat',
]
struct_OMX_VIDEO_PARAM_WMVTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eFormat', OMX_VIDEO_WMVFORMATTYPE),
]

OMX_VIDEO_PARAM_WMVTYPE = struct_OMX_VIDEO_PARAM_WMVTYPE # OMX_Video.h: 378

enum_OMX_VIDEO_RVFORMATTYPE = c_int # OMX_Video.h: 389

OMX_VIDEO_RVFormatUnused = 0 # OMX_Video.h: 389

OMX_VIDEO_RVFormat8 = (OMX_VIDEO_RVFormatUnused + 1) # OMX_Video.h: 389

OMX_VIDEO_RVFormat9 = (OMX_VIDEO_RVFormat8 + 1) # OMX_Video.h: 389

OMX_VIDEO_RVFormatG2 = (OMX_VIDEO_RVFormat9 + 1) # OMX_Video.h: 389

OMX_VIDEO_RVFormatUnknown = 1862270975 # OMX_Video.h: 389

OMX_VIDEO_RVFormatKhronosExtensions = 1862270976 # OMX_Video.h: 389

OMX_VIDEO_RVFormatVendorStartUnused = 2130706432 # OMX_Video.h: 389

OMX_VIDEO_RVFormatMax = 2147483647 # OMX_Video.h: 389

OMX_VIDEO_RVFORMATTYPE = enum_OMX_VIDEO_RVFORMATTYPE # OMX_Video.h: 389

# OMX_Video.h: 406
class struct_OMX_VIDEO_PARAM_RVTYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_RVTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eFormat',
    'nBitsPerPixel',
    'nPaddedWidth',
    'nPaddedHeight',
    'nFrameRate',
    'nBitstreamFlags',
    'nBitstreamVersion',
    'nMaxEncodeFrameSize',
    'bEnablePostFilter',
    'bEnableTemporalInterpolation',
    'bEnableLatencyMode',
]
struct_OMX_VIDEO_PARAM_RVTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eFormat', OMX_VIDEO_RVFORMATTYPE),
    ('nBitsPerPixel', OMX_U16),
    ('nPaddedWidth', OMX_U16),
    ('nPaddedHeight', OMX_U16),
    ('nFrameRate', OMX_U32),
    ('nBitstreamFlags', OMX_U32),
    ('nBitstreamVersion', OMX_U32),
    ('nMaxEncodeFrameSize', OMX_U32),
    ('bEnablePostFilter', OMX_BOOL),
    ('bEnableTemporalInterpolation', OMX_BOOL),
    ('bEnableLatencyMode', OMX_BOOL),
]

OMX_VIDEO_PARAM_RVTYPE = struct_OMX_VIDEO_PARAM_RVTYPE # OMX_Video.h: 406

enum_OMX_VIDEO_AVCPROFILETYPE = c_int # OMX_Video.h: 420

OMX_VIDEO_AVCProfileBaseline = 1 # OMX_Video.h: 420

OMX_VIDEO_AVCProfileMain = 2 # OMX_Video.h: 420

OMX_VIDEO_AVCProfileExtended = 4 # OMX_Video.h: 420

OMX_VIDEO_AVCProfileHigh = 8 # OMX_Video.h: 420

OMX_VIDEO_AVCProfileHigh10 = 16 # OMX_Video.h: 420

OMX_VIDEO_AVCProfileHigh422 = 32 # OMX_Video.h: 420

OMX_VIDEO_AVCProfileHigh444 = 64 # OMX_Video.h: 420

OMX_VIDEO_AVCProfileUnknown = 1862270975 # OMX_Video.h: 420

OMX_VIDEO_AVCProfileKhronosExtensions = 1862270976 # OMX_Video.h: 420

OMX_VIDEO_AVCProfileVendorStartUnused = 2130706432 # OMX_Video.h: 420

OMX_VIDEO_AVCProfileMax = 2147483647 # OMX_Video.h: 420

OMX_VIDEO_AVCPROFILETYPE = enum_OMX_VIDEO_AVCPROFILETYPE # OMX_Video.h: 420

enum_OMX_VIDEO_AVCLEVELTYPE = c_int # OMX_Video.h: 443

OMX_VIDEO_AVCLevel1 = 1 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel1b = 2 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel11 = 4 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel12 = 8 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel13 = 16 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel2 = 32 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel21 = 64 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel22 = 128 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel3 = 256 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel31 = 512 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel32 = 1024 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel4 = 2048 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel41 = 4096 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel42 = 8192 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel5 = 16384 # OMX_Video.h: 443

OMX_VIDEO_AVCLevel51 = 32768 # OMX_Video.h: 443

OMX_VIDEO_AVCLevelUnknown = 1862270975 # OMX_Video.h: 443

OMX_VIDEO_AVCLevelKhronosExtensions = 1862270976 # OMX_Video.h: 443

OMX_VIDEO_AVCLevelVendorStartUnused = 2130706432 # OMX_Video.h: 443

OMX_VIDEO_AVCLevelMax = 2147483647 # OMX_Video.h: 443

OMX_VIDEO_AVCLEVELTYPE = enum_OMX_VIDEO_AVCLEVELTYPE # OMX_Video.h: 443

enum_OMX_VIDEO_AVCLOOPFILTERTYPE = c_int # OMX_Video.h: 452

OMX_VIDEO_AVCLoopFilterEnable = 0 # OMX_Video.h: 452

OMX_VIDEO_AVCLoopFilterDisable = (OMX_VIDEO_AVCLoopFilterEnable + 1) # OMX_Video.h: 452

OMX_VIDEO_AVCLoopFilterDisableSliceBoundary = (OMX_VIDEO_AVCLoopFilterDisable + 1) # OMX_Video.h: 452

OMX_VIDEO_AVCLoopFilterKhronosExtensions = 1862270976 # OMX_Video.h: 452

OMX_VIDEO_AVCLoopFilterVendorStartUnused = 2130706432 # OMX_Video.h: 452

OMX_VIDEO_AVCLoopFilterMax = 2147483647 # OMX_Video.h: 452

OMX_VIDEO_AVCLOOPFILTERTYPE = enum_OMX_VIDEO_AVCLOOPFILTERTYPE # OMX_Video.h: 452

# OMX_Video.h: 482
class struct_OMX_VIDEO_PARAM_AVCTYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_AVCTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nSliceHeaderSpacing',
    'nPFrames',
    'nBFrames',
    'bUseHadamard',
    'nRefFrames',
    'nRefIdx10ActiveMinus1',
    'nRefIdx11ActiveMinus1',
    'bEnableUEP',
    'bEnableFMO',
    'bEnableASO',
    'bEnableRS',
    'eProfile',
    'eLevel',
    'nAllowedPictureTypes',
    'bFrameMBsOnly',
    'bMBAFF',
    'bEntropyCodingCABAC',
    'bWeightedPPrediction',
    'nWeightedBipredicitonMode',
    'bconstIpred',
    'bDirect8x8Inference',
    'bDirectSpatialTemporal',
    'nCabacInitIdc',
    'eLoopFilterMode',
]
struct_OMX_VIDEO_PARAM_AVCTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nSliceHeaderSpacing', OMX_U32),
    ('nPFrames', OMX_U32),
    ('nBFrames', OMX_U32),
    ('bUseHadamard', OMX_BOOL),
    ('nRefFrames', OMX_U32),
    ('nRefIdx10ActiveMinus1', OMX_U32),
    ('nRefIdx11ActiveMinus1', OMX_U32),
    ('bEnableUEP', OMX_BOOL),
    ('bEnableFMO', OMX_BOOL),
    ('bEnableASO', OMX_BOOL),
    ('bEnableRS', OMX_BOOL),
    ('eProfile', OMX_VIDEO_AVCPROFILETYPE),
    ('eLevel', OMX_VIDEO_AVCLEVELTYPE),
    ('nAllowedPictureTypes', OMX_U32),
    ('bFrameMBsOnly', OMX_BOOL),
    ('bMBAFF', OMX_BOOL),
    ('bEntropyCodingCABAC', OMX_BOOL),
    ('bWeightedPPrediction', OMX_BOOL),
    ('nWeightedBipredicitonMode', OMX_U32),
    ('bconstIpred', OMX_BOOL),
    ('bDirect8x8Inference', OMX_BOOL),
    ('bDirectSpatialTemporal', OMX_BOOL),
    ('nCabacInitIdc', OMX_U32),
    ('eLoopFilterMode', OMX_VIDEO_AVCLOOPFILTERTYPE),
]

OMX_VIDEO_PARAM_AVCTYPE = struct_OMX_VIDEO_PARAM_AVCTYPE # OMX_Video.h: 482

enum_OMX_VIDEO_VP84PROFILETYPE = c_int # OMX_Video.h: 491

OMX_VIDEO_VP8ProfileMain = 1 # OMX_Video.h: 491

OMX_VIDEO_VP8ProfileUnknown = 1862270975 # OMX_Video.h: 491

OMX_VIDEO_VP8ProfileKhronosExtensions = 1862270976 # OMX_Video.h: 491

OMX_VIDEO_VP8ProfileVendorStartUnused = 2130706432 # OMX_Video.h: 491

OMX_VIDEO_VP8ProfileMax = 2147483647 # OMX_Video.h: 491

OMX_VIDEO_VP8PROFILETYPE = enum_OMX_VIDEO_VP84PROFILETYPE # OMX_Video.h: 491

enum_OMX_VIDEO_VP8LEVELTYPE = c_int # OMX_Video.h: 502

OMX_VIDEO_VP8Level_Version0 = 1 # OMX_Video.h: 502

OMX_VIDEO_VP8Level_Version1 = 2 # OMX_Video.h: 502

OMX_VIDEO_VP8Level_Version2 = 4 # OMX_Video.h: 502

OMX_VIDEO_VP8Level_Version3 = 8 # OMX_Video.h: 502

OMX_VIDEO_VP8LevelUnknown = 1862270975 # OMX_Video.h: 502

OMX_VIDEO_VP8LevelKhronosExtensions = 1862270976 # OMX_Video.h: 502

OMX_VIDEO_VP8LevelVendorStartUnused = 2130706432 # OMX_Video.h: 502

OMX_VIDEO_VP8LevelMax = 2147483647 # OMX_Video.h: 502

OMX_VIDEO_VP8LEVELTYPE = enum_OMX_VIDEO_VP8LEVELTYPE # OMX_Video.h: 502

# OMX_Video.h: 512
class struct_OMX_VIDEO_PARAM_VP8TYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_VP8TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eProfile',
    'eLevel',
    'nDCTPartitions',
    'bErrorResilientMode',
]
struct_OMX_VIDEO_PARAM_VP8TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eProfile', OMX_VIDEO_VP8PROFILETYPE),
    ('eLevel', OMX_VIDEO_VP8LEVELTYPE),
    ('nDCTPartitions', OMX_U32),
    ('bErrorResilientMode', OMX_BOOL),
]

OMX_VIDEO_PARAM_VP8TYPE = struct_OMX_VIDEO_PARAM_VP8TYPE # OMX_Video.h: 512

# OMX_Video.h: 524
class struct_OMX_VIDEO_VP8REFERENCEFRAMETYPE(Structure):
    pass

struct_OMX_VIDEO_VP8REFERENCEFRAMETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nPreviousFrameRefresh',
    'bGoldenFrameRefresh',
    'bAlternateFrameRefresh',
    'bUsePreviousFrame',
    'bUseGoldenFrame',
    'bUseAlternateFrame',
]
struct_OMX_VIDEO_VP8REFERENCEFRAMETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nPreviousFrameRefresh', OMX_BOOL),
    ('bGoldenFrameRefresh', OMX_BOOL),
    ('bAlternateFrameRefresh', OMX_BOOL),
    ('bUsePreviousFrame', OMX_BOOL),
    ('bUseGoldenFrame', OMX_BOOL),
    ('bUseAlternateFrame', OMX_BOOL),
]

OMX_VIDEO_VP8REFERENCEFRAMETYPE = struct_OMX_VIDEO_VP8REFERENCEFRAMETYPE # OMX_Video.h: 524

# OMX_Video.h: 532
class struct_OMX_VIDEO_VP8REFERENCEFRAMEINFOTYPE(Structure):
    pass

struct_OMX_VIDEO_VP8REFERENCEFRAMEINFOTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bIsIntraFrame',
    'bIsGoldenOrAlternateFrame',
]
struct_OMX_VIDEO_VP8REFERENCEFRAMEINFOTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bIsIntraFrame', OMX_BOOL),
    ('bIsGoldenOrAlternateFrame', OMX_BOOL),
]

OMX_VIDEO_VP8REFERENCEFRAMEINFOTYPE = struct_OMX_VIDEO_VP8REFERENCEFRAMEINFOTYPE # OMX_Video.h: 532

# OMX_Video.h: 542
class struct_OMX_VIDEO_PARAM_PROFILELEVELTYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_PROFILELEVELTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eProfile',
    'eLevel',
    'nIndex',
    'eCodecType',
]
struct_OMX_VIDEO_PARAM_PROFILELEVELTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eProfile', OMX_U32),
    ('eLevel', OMX_U32),
    ('nIndex', OMX_U32),
    ('eCodecType', OMX_U32),
]

OMX_VIDEO_PARAM_PROFILELEVELTYPE = struct_OMX_VIDEO_PARAM_PROFILELEVELTYPE # OMX_Video.h: 542

# OMX_Video.h: 549
class struct_OMX_VIDEO_CONFIG_BITRATETYPE(Structure):
    pass

struct_OMX_VIDEO_CONFIG_BITRATETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nEncodeBitrate',
]
struct_OMX_VIDEO_CONFIG_BITRATETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nEncodeBitrate', OMX_U32),
]

OMX_VIDEO_CONFIG_BITRATETYPE = struct_OMX_VIDEO_CONFIG_BITRATETYPE # OMX_Video.h: 549

# OMX_Video.h: 556
class struct_OMX_CONFIG_FRAMERATETYPE(Structure):
    pass

struct_OMX_CONFIG_FRAMERATETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'xEncodeFramerate',
]
struct_OMX_CONFIG_FRAMERATETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('xEncodeFramerate', OMX_U32),
]

OMX_CONFIG_FRAMERATETYPE = struct_OMX_CONFIG_FRAMERATETYPE # OMX_Video.h: 556

# OMX_Video.h: 563
class struct_OMX_CONFIG_INTRAREFRESHVOPTYPE(Structure):
    pass

struct_OMX_CONFIG_INTRAREFRESHVOPTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'IntraRefreshVOP',
]
struct_OMX_CONFIG_INTRAREFRESHVOPTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('IntraRefreshVOP', OMX_BOOL),
]

OMX_CONFIG_INTRAREFRESHVOPTYPE = struct_OMX_CONFIG_INTRAREFRESHVOPTYPE # OMX_Video.h: 563

# OMX_Video.h: 571
class struct_OMX_CONFIG_MACROBLOCKERRORMAPTYPE(Structure):
    pass

struct_OMX_CONFIG_MACROBLOCKERRORMAPTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nErrMapSize',
    'ErrMap',
]
struct_OMX_CONFIG_MACROBLOCKERRORMAPTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nErrMapSize', OMX_U32),
    ('ErrMap', OMX_U8 * 1),
]

OMX_CONFIG_MACROBLOCKERRORMAPTYPE = struct_OMX_CONFIG_MACROBLOCKERRORMAPTYPE # OMX_Video.h: 571

# OMX_Video.h: 578
class struct_OMX_CONFIG_MBERRORREPORTINGTYPE(Structure):
    pass

struct_OMX_CONFIG_MBERRORREPORTINGTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnabled',
]
struct_OMX_CONFIG_MBERRORREPORTINGTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnabled', OMX_BOOL),
]

OMX_CONFIG_MBERRORREPORTINGTYPE = struct_OMX_CONFIG_MBERRORREPORTINGTYPE # OMX_Video.h: 578

# OMX_Video.h: 585
class struct_OMX_PARAM_MACROBLOCKSTYPE(Structure):
    pass

struct_OMX_PARAM_MACROBLOCKSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nMacroblocks',
]
struct_OMX_PARAM_MACROBLOCKSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nMacroblocks', OMX_U32),
]

OMX_PARAM_MACROBLOCKSTYPE = struct_OMX_PARAM_MACROBLOCKSTYPE # OMX_Video.h: 585

enum_OMX_VIDEO_AVCSLICEMODETYPE = c_int # OMX_Video.h: 594

OMX_VIDEO_SLICEMODE_AVCDefault = 0 # OMX_Video.h: 594

OMX_VIDEO_SLICEMODE_AVCMBSlice = (OMX_VIDEO_SLICEMODE_AVCDefault + 1) # OMX_Video.h: 594

OMX_VIDEO_SLICEMODE_AVCByteSlice = (OMX_VIDEO_SLICEMODE_AVCMBSlice + 1) # OMX_Video.h: 594

OMX_VIDEO_SLICEMODE_AVCKhronosExtensions = 1862270976 # OMX_Video.h: 594

OMX_VIDEO_SLICEMODE_AVCVendorStartUnused = 2130706432 # OMX_Video.h: 594

OMX_VIDEO_SLICEMODE_AVCLevelMax = 2147483647 # OMX_Video.h: 594

OMX_VIDEO_AVCSLICEMODETYPE = enum_OMX_VIDEO_AVCSLICEMODETYPE # OMX_Video.h: 594

# OMX_Video.h: 603
class struct_OMX_VIDEO_PARAM_AVCSLICEFMO(Structure):
    pass

struct_OMX_VIDEO_PARAM_AVCSLICEFMO.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nNumSliceGroups',
    'nSliceGroupMapType',
    'eSliceMode',
]
struct_OMX_VIDEO_PARAM_AVCSLICEFMO._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nNumSliceGroups', OMX_U8),
    ('nSliceGroupMapType', OMX_U8),
    ('eSliceMode', OMX_VIDEO_AVCSLICEMODETYPE),
]

OMX_VIDEO_PARAM_AVCSLICEFMO = struct_OMX_VIDEO_PARAM_AVCSLICEFMO # OMX_Video.h: 603

# OMX_Video.h: 611
class struct_OMX_VIDEO_CONFIG_AVCINTRAPERIOD(Structure):
    pass

struct_OMX_VIDEO_CONFIG_AVCINTRAPERIOD.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nIDRPeriod',
    'nPFrames',
]
struct_OMX_VIDEO_CONFIG_AVCINTRAPERIOD._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nIDRPeriod', OMX_U32),
    ('nPFrames', OMX_U32),
]

OMX_VIDEO_CONFIG_AVCINTRAPERIOD = struct_OMX_VIDEO_CONFIG_AVCINTRAPERIOD # OMX_Video.h: 611

# OMX_Video.h: 618
class struct_OMX_VIDEO_CONFIG_NALSIZE(Structure):
    pass

struct_OMX_VIDEO_CONFIG_NALSIZE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nNaluBytes',
]
struct_OMX_VIDEO_CONFIG_NALSIZE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nNaluBytes', OMX_U32),
]

OMX_VIDEO_CONFIG_NALSIZE = struct_OMX_VIDEO_CONFIG_NALSIZE # OMX_Video.h: 618

enum_OMX_NALUFORMATSTYPE = c_int # OMX_Video.h: 629

OMX_NaluFormatStartCodes = 1 # OMX_Video.h: 629

OMX_NaluFormatOneNaluPerBuffer = 2 # OMX_Video.h: 629

OMX_NaluFormatOneByteInterleaveLength = 4 # OMX_Video.h: 629

OMX_NaluFormatTwoByteInterleaveLength = 8 # OMX_Video.h: 629

OMX_NaluFormatFourByteInterleaveLength = 16 # OMX_Video.h: 629

OMX_NaluFormatKhronosExtensions = 1862270976 # OMX_Video.h: 629

OMX_NaluFormatVendorStartUnused = 2130706432 # OMX_Video.h: 629

OMX_NaluFormatCodingMax = 2147483647 # OMX_Video.h: 629

OMX_NALUFORMATSTYPE = enum_OMX_NALUFORMATSTYPE # OMX_Video.h: 629

# OMX_Video.h: 636
class struct_OMX_NALSTREAMFORMATTYPE(Structure):
    pass

struct_OMX_NALSTREAMFORMATTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eNaluFormat',
]
struct_OMX_NALSTREAMFORMATTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eNaluFormat', OMX_NALUFORMATSTYPE),
]

OMX_NALSTREAMFORMATTYPE = struct_OMX_NALSTREAMFORMATTYPE # OMX_Video.h: 636

enum_OMX_VIDEO_VC1PROFILETYPE = c_int # OMX_Video.h: 647

OMX_VIDEO_VC1ProfileUnused = 0 # OMX_Video.h: 647

OMX_VIDEO_VC1ProfileSimple = (OMX_VIDEO_VC1ProfileUnused + 1) # OMX_Video.h: 647

OMX_VIDEO_VC1ProfileMain = (OMX_VIDEO_VC1ProfileSimple + 1) # OMX_Video.h: 647

OMX_VIDEO_VC1ProfileAdvanced = (OMX_VIDEO_VC1ProfileMain + 1) # OMX_Video.h: 647

OMX_VIDEO_VC1ProfileUnknown = 1862270975 # OMX_Video.h: 647

OMX_VIDEO_VC1ProfileKhronosExtensions = 1862270976 # OMX_Video.h: 647

OMX_VIDEO_VC1ProfileVendorStartUnused = 2130706432 # OMX_Video.h: 647

OMX_VIDEO_VC1ProfileMax = (OMX_VIDEO_VC1ProfileVendorStartUnused + 1) # OMX_Video.h: 647

OMX_VIDEO_VC1PROFILETYPE = enum_OMX_VIDEO_VC1PROFILETYPE # OMX_Video.h: 647

enum_OMX_VIDEO_VC1LEVELTYPE = c_int # OMX_Video.h: 663

OMX_VIDEO_VC1LevelUnused = 0 # OMX_Video.h: 663

OMX_VIDEO_VC1LevelLow = (OMX_VIDEO_VC1LevelUnused + 1) # OMX_Video.h: 663

OMX_VIDEO_VC1LevelMedium = (OMX_VIDEO_VC1LevelLow + 1) # OMX_Video.h: 663

OMX_VIDEO_VC1LevelHigh = (OMX_VIDEO_VC1LevelMedium + 1) # OMX_Video.h: 663

OMX_VIDEO_VC1Level0 = (OMX_VIDEO_VC1LevelHigh + 1) # OMX_Video.h: 663

OMX_VIDEO_VC1Level1 = (OMX_VIDEO_VC1Level0 + 1) # OMX_Video.h: 663

OMX_VIDEO_VC1Level2 = (OMX_VIDEO_VC1Level1 + 1) # OMX_Video.h: 663

OMX_VIDEO_VC1Level3 = (OMX_VIDEO_VC1Level2 + 1) # OMX_Video.h: 663

OMX_VIDEO_VC1Level4 = (OMX_VIDEO_VC1Level3 + 1) # OMX_Video.h: 663

OMX_VIDEO_VC1LevelUnknown = 1862270975 # OMX_Video.h: 663

OMX_VIDEO_VC1LevelKhronosExtensions = 1862270976 # OMX_Video.h: 663

OMX_VIDEO_VC1LevelVendorStartUnused = 2130706432 # OMX_Video.h: 663

OMX_VIDEO_VC1LevelMax = (OMX_VIDEO_VC1LevelVendorStartUnused + 1) # OMX_Video.h: 663

OMX_VIDEO_VC1LEVELTYPE = enum_OMX_VIDEO_VC1LEVELTYPE # OMX_Video.h: 663

# OMX_Video.h: 671
class struct_OMX_VIDEO_PARAM_VC1TYPE(Structure):
    pass

struct_OMX_VIDEO_PARAM_VC1TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eProfile',
    'eLevel',
]
struct_OMX_VIDEO_PARAM_VC1TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eProfile', OMX_VIDEO_VC1PROFILETYPE),
    ('eLevel', OMX_VIDEO_VC1LEVELTYPE),
]

OMX_VIDEO_PARAM_VC1TYPE = struct_OMX_VIDEO_PARAM_VC1TYPE # OMX_Video.h: 671

# OMX_Video.h: 680
class struct_OMX_VIDEO_INTRAPERIODTYPE(Structure):
    pass

struct_OMX_VIDEO_INTRAPERIODTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nIDRPeriod',
    'nPFrames',
    'nBFrames',
]
struct_OMX_VIDEO_INTRAPERIODTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nIDRPeriod', OMX_U32),
    ('nPFrames', OMX_S32),
    ('nBFrames', OMX_S32),
]

OMX_VIDEO_INTRAPERIODTYPE = struct_OMX_VIDEO_INTRAPERIODTYPE # OMX_Video.h: 680

enum_OMX_IMAGE_CODINGTYPE = c_int # OMX_Image.h: 61

OMX_IMAGE_CodingUnused = 0 # OMX_Image.h: 61

OMX_IMAGE_CodingAutoDetect = (OMX_IMAGE_CodingUnused + 1) # OMX_Image.h: 61

OMX_IMAGE_CodingJPEG = (OMX_IMAGE_CodingAutoDetect + 1) # OMX_Image.h: 61

OMX_IMAGE_CodingJPEG2K = (OMX_IMAGE_CodingJPEG + 1) # OMX_Image.h: 61

OMX_IMAGE_CodingEXIF = (OMX_IMAGE_CodingJPEG2K + 1) # OMX_Image.h: 61

OMX_IMAGE_CodingTIFF = (OMX_IMAGE_CodingEXIF + 1) # OMX_Image.h: 61

OMX_IMAGE_CodingGIF = (OMX_IMAGE_CodingTIFF + 1) # OMX_Image.h: 61

OMX_IMAGE_CodingPNG = (OMX_IMAGE_CodingGIF + 1) # OMX_Image.h: 61

OMX_IMAGE_CodingLZW = (OMX_IMAGE_CodingPNG + 1) # OMX_Image.h: 61

OMX_IMAGE_CodingBMP = (OMX_IMAGE_CodingLZW + 1) # OMX_Image.h: 61

OMX_IMAGE_CodingWEBP = (OMX_IMAGE_CodingBMP + 1) # OMX_Image.h: 61

OMX_IMAGE_CodingKhronosExtensions = 1862270976 # OMX_Image.h: 61

OMX_IMAGE_CodingVendorStartUnused = 2130706432 # OMX_Image.h: 61

OMX_IMAGE_CodingMax = 2147483647 # OMX_Image.h: 61

OMX_IMAGE_CODINGTYPE = enum_OMX_IMAGE_CODINGTYPE # OMX_Image.h: 61

# OMX_Image.h: 73
class struct_OMX_IMAGE_PORTDEFINITIONTYPE(Structure):
    pass

struct_OMX_IMAGE_PORTDEFINITIONTYPE.__slots__ = [
    'pNativeRender',
    'nFrameWidth',
    'nFrameHeight',
    'nStride',
    'nSliceHeight',
    'bFlagErrorConcealment',
    'eCompressionFormat',
    'eColorFormat',
    'pNativeWindow',
]
struct_OMX_IMAGE_PORTDEFINITIONTYPE._fields_ = [
    ('pNativeRender', OMX_NATIVE_DEVICETYPE),
    ('nFrameWidth', OMX_U32),
    ('nFrameHeight', OMX_U32),
    ('nStride', OMX_S32),
    ('nSliceHeight', OMX_U32),
    ('bFlagErrorConcealment', OMX_BOOL),
    ('eCompressionFormat', OMX_IMAGE_CODINGTYPE),
    ('eColorFormat', OMX_COLOR_FORMATTYPE),
    ('pNativeWindow', OMX_NATIVE_WINDOWTYPE),
]

OMX_IMAGE_PORTDEFINITIONTYPE = struct_OMX_IMAGE_PORTDEFINITIONTYPE # OMX_Image.h: 73

# OMX_Image.h: 82
class struct_OMX_IMAGE_PARAM_PORTFORMATTYPE(Structure):
    pass

struct_OMX_IMAGE_PARAM_PORTFORMATTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nIndex',
    'eCompressionFormat',
    'eColorFormat',
]
struct_OMX_IMAGE_PARAM_PORTFORMATTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nIndex', OMX_U32),
    ('eCompressionFormat', OMX_IMAGE_CODINGTYPE),
    ('eColorFormat', OMX_COLOR_FORMATTYPE),
]

OMX_IMAGE_PARAM_PORTFORMATTYPE = struct_OMX_IMAGE_PARAM_PORTFORMATTYPE # OMX_Image.h: 82

enum_OMX_IMAGE_FLASHCONTROLTYPE = c_int # OMX_Image.h: 94

OMX_IMAGE_FlashControlOn = 0 # OMX_Image.h: 94

OMX_IMAGE_FlashControlOff = (OMX_IMAGE_FlashControlOn + 1) # OMX_Image.h: 94

OMX_IMAGE_FlashControlAuto = (OMX_IMAGE_FlashControlOff + 1) # OMX_Image.h: 94

OMX_IMAGE_FlashControlRedEyeReduction = (OMX_IMAGE_FlashControlAuto + 1) # OMX_Image.h: 94

OMX_IMAGE_FlashControlFillin = (OMX_IMAGE_FlashControlRedEyeReduction + 1) # OMX_Image.h: 94

OMX_IMAGE_FlashControlTorch = (OMX_IMAGE_FlashControlFillin + 1) # OMX_Image.h: 94

OMX_IMAGE_FlashControlKhronosExtensions = 1862270976 # OMX_Image.h: 94

OMX_IMAGE_FlashControlVendorStartUnused = 2130706432 # OMX_Image.h: 94

OMX_IMAGE_FlashControlMax = 2147483647 # OMX_Image.h: 94

OMX_IMAGE_FLASHCONTROLTYPE = enum_OMX_IMAGE_FLASHCONTROLTYPE # OMX_Image.h: 94

# OMX_Image.h: 101
class struct_OMX_IMAGE_PARAM_FLASHCONTROLTYPE(Structure):
    pass

struct_OMX_IMAGE_PARAM_FLASHCONTROLTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eFlashControl',
]
struct_OMX_IMAGE_PARAM_FLASHCONTROLTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eFlashControl', OMX_IMAGE_FLASHCONTROLTYPE),
]

OMX_IMAGE_PARAM_FLASHCONTROLTYPE = struct_OMX_IMAGE_PARAM_FLASHCONTROLTYPE # OMX_Image.h: 101

enum_OMX_IMAGE_FOCUSCONTROLTYPE = c_int # OMX_Image.h: 111

OMX_IMAGE_FocusControlOn = 0 # OMX_Image.h: 111

OMX_IMAGE_FocusControlOff = (OMX_IMAGE_FocusControlOn + 1) # OMX_Image.h: 111

OMX_IMAGE_FocusControlAuto = (OMX_IMAGE_FocusControlOff + 1) # OMX_Image.h: 111

OMX_IMAGE_FocusControlAutoLock = (OMX_IMAGE_FocusControlAuto + 1) # OMX_Image.h: 111

OMX_IMAGE_FocusControlKhronosExtensions = 1862270976 # OMX_Image.h: 111

OMX_IMAGE_FocusControlVendorStartUnused = 2130706432 # OMX_Image.h: 111

OMX_IMAGE_FocusControlMax = 2147483647 # OMX_Image.h: 111

OMX_IMAGE_FOCUSCONTROLTYPE = enum_OMX_IMAGE_FOCUSCONTROLTYPE # OMX_Image.h: 111

# OMX_Image.h: 120
class struct_OMX_IMAGE_CONFIG_FOCUSCONTROLTYPE(Structure):
    pass

struct_OMX_IMAGE_CONFIG_FOCUSCONTROLTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eFocusControl',
    'nFocusSteps',
    'nFocusStepIndex',
]
struct_OMX_IMAGE_CONFIG_FOCUSCONTROLTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eFocusControl', OMX_IMAGE_FOCUSCONTROLTYPE),
    ('nFocusSteps', OMX_U32),
    ('nFocusStepIndex', OMX_U32),
]

OMX_IMAGE_CONFIG_FOCUSCONTROLTYPE = struct_OMX_IMAGE_CONFIG_FOCUSCONTROLTYPE # OMX_Image.h: 120

# OMX_Image.h: 127
class struct_OMX_IMAGE_PARAM_QFACTORTYPE(Structure):
    pass

struct_OMX_IMAGE_PARAM_QFACTORTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nQFactor',
]
struct_OMX_IMAGE_PARAM_QFACTORTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nQFactor', OMX_U32),
]

OMX_IMAGE_PARAM_QFACTORTYPE = struct_OMX_IMAGE_PARAM_QFACTORTYPE # OMX_Image.h: 127

enum_OMX_IMAGE_QUANTIZATIONTABLETYPE = c_int # OMX_Image.h: 137

OMX_IMAGE_QuantizationTableLuma = 0 # OMX_Image.h: 137

OMX_IMAGE_QuantizationTableChroma = (OMX_IMAGE_QuantizationTableLuma + 1) # OMX_Image.h: 137

OMX_IMAGE_QuantizationTableChromaCb = (OMX_IMAGE_QuantizationTableChroma + 1) # OMX_Image.h: 137

OMX_IMAGE_QuantizationTableChromaCr = (OMX_IMAGE_QuantizationTableChromaCb + 1) # OMX_Image.h: 137

OMX_IMAGE_QuantizationTableKhronosExtensions = 1862270976 # OMX_Image.h: 137

OMX_IMAGE_QuantizationTableVendorStartUnused = 2130706432 # OMX_Image.h: 137

OMX_IMAGE_QuantizationTableMax = 2147483647 # OMX_Image.h: 137

OMX_IMAGE_QUANTIZATIONTABLETYPE = enum_OMX_IMAGE_QUANTIZATIONTABLETYPE # OMX_Image.h: 137

# OMX_Image.h: 145
class struct_OMX_IMAGE_PARAM_QUANTIZATIONTABLETYPE(Structure):
    pass

struct_OMX_IMAGE_PARAM_QUANTIZATIONTABLETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eQuantizationTable',
    'nQuantizationMatrix',
]
struct_OMX_IMAGE_PARAM_QUANTIZATIONTABLETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eQuantizationTable', OMX_IMAGE_QUANTIZATIONTABLETYPE),
    ('nQuantizationMatrix', OMX_U8 * 64),
]

OMX_IMAGE_PARAM_QUANTIZATIONTABLETYPE = struct_OMX_IMAGE_PARAM_QUANTIZATIONTABLETYPE # OMX_Image.h: 145

enum_OMX_IMAGE_HUFFMANTABLETYPE = c_int # OMX_Image.h: 157

OMX_IMAGE_HuffmanTableAC = 0 # OMX_Image.h: 157

OMX_IMAGE_HuffmanTableDC = (OMX_IMAGE_HuffmanTableAC + 1) # OMX_Image.h: 157

OMX_IMAGE_HuffmanTableACLuma = (OMX_IMAGE_HuffmanTableDC + 1) # OMX_Image.h: 157

OMX_IMAGE_HuffmanTableACChroma = (OMX_IMAGE_HuffmanTableACLuma + 1) # OMX_Image.h: 157

OMX_IMAGE_HuffmanTableDCLuma = (OMX_IMAGE_HuffmanTableACChroma + 1) # OMX_Image.h: 157

OMX_IMAGE_HuffmanTableDCChroma = (OMX_IMAGE_HuffmanTableDCLuma + 1) # OMX_Image.h: 157

OMX_IMAGE_HuffmanTableKhronosExtensions = 1862270976 # OMX_Image.h: 157

OMX_IMAGE_HuffmanTableVendorStartUnused = 2130706432 # OMX_Image.h: 157

OMX_IMAGE_HuffmanTableMax = 2147483647 # OMX_Image.h: 157

OMX_IMAGE_HUFFMANTABLETYPE = enum_OMX_IMAGE_HUFFMANTABLETYPE # OMX_Image.h: 157

# OMX_Image.h: 166
class struct_OMX_IMAGE_PARAM_HUFFMANTTABLETYPE(Structure):
    pass

struct_OMX_IMAGE_PARAM_HUFFMANTTABLETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eHuffmanTable',
    'nNumberOfHuffmanCodeOfLength',
    'nHuffmanTable',
]
struct_OMX_IMAGE_PARAM_HUFFMANTTABLETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eHuffmanTable', OMX_IMAGE_HUFFMANTABLETYPE),
    ('nNumberOfHuffmanCodeOfLength', OMX_U8 * 16),
    ('nHuffmanTable', OMX_U8 * 256),
]

OMX_IMAGE_PARAM_HUFFMANTTABLETYPE = struct_OMX_IMAGE_PARAM_HUFFMANTTABLETYPE # OMX_Image.h: 166

enum_OMX_FLICKERREJECTIONTYPE = c_int # OMX_Image.h: 176

OMX_FlickerRejectionOff = 0 # OMX_Image.h: 176

OMX_FlickerRejectionAuto = (OMX_FlickerRejectionOff + 1) # OMX_Image.h: 176

OMX_FlickerRejection50 = (OMX_FlickerRejectionAuto + 1) # OMX_Image.h: 176

OMX_FlickerRejection60 = (OMX_FlickerRejection50 + 1) # OMX_Image.h: 176

OMX_FlickerRejectionKhronosExtensions = 1862270976 # OMX_Image.h: 176

OMX_FlickerRejectionVendorStartUnused = 2130706432 # OMX_Image.h: 176

OMX_FlickerRejectionMax = 2147483647 # OMX_Image.h: 176

OMX_FLICKERREJECTIONTYPE = enum_OMX_FLICKERREJECTIONTYPE # OMX_Image.h: 176

# OMX_Image.h: 183
class struct_OMX_CONFIG_FLICKERREJECTIONTYPE(Structure):
    pass

struct_OMX_CONFIG_FLICKERREJECTIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eFlickerRejection',
]
struct_OMX_CONFIG_FLICKERREJECTIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eFlickerRejection', OMX_FLICKERREJECTIONTYPE),
]

OMX_CONFIG_FLICKERREJECTIONTYPE = struct_OMX_CONFIG_FLICKERREJECTIONTYPE # OMX_Image.h: 183

enum_OMX_HISTOGRAMTYPE = c_int # OMX_Image.h: 193

OMX_Histogram_Off = 0 # OMX_Image.h: 193

OMX_Histogram_RGB = (OMX_Histogram_Off + 1) # OMX_Image.h: 193

OMX_Histogram_Luma = (OMX_Histogram_RGB + 1) # OMX_Image.h: 193

OMX_Histogram_Chroma = (OMX_Histogram_Luma + 1) # OMX_Image.h: 193

OMX_HistogramKhronosExtensions = 1862270976 # OMX_Image.h: 193

OMX_HistogramVendorStartUnused = 2130706432 # OMX_Image.h: 193

OMX_HistogramMax = 2147483647 # OMX_Image.h: 193

OMX_HISTOGRAMTYPE = enum_OMX_HISTOGRAMTYPE # OMX_Image.h: 193

# OMX_Image.h: 201
class struct_OMX_IMAGE_HISTOGRAMTYPE(Structure):
    pass

struct_OMX_IMAGE_HISTOGRAMTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nBins',
    'eHistType',
]
struct_OMX_IMAGE_HISTOGRAMTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nBins', OMX_U32),
    ('eHistType', OMX_HISTOGRAMTYPE),
]

OMX_IMAGE_HISTOGRAMTYPE = struct_OMX_IMAGE_HISTOGRAMTYPE # OMX_Image.h: 201

# OMX_Image.h: 210
class struct_OMX_IMAGE_HISTOGRAMDATATYPE(Structure):
    pass

struct_OMX_IMAGE_HISTOGRAMDATATYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eHistType',
    'nBins',
    'data',
]
struct_OMX_IMAGE_HISTOGRAMDATATYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eHistType', OMX_HISTOGRAMTYPE),
    ('nBins', OMX_U32),
    ('data', OMX_U8 * 1),
]

OMX_IMAGE_HISTOGRAMDATATYPE = struct_OMX_IMAGE_HISTOGRAMDATATYPE # OMX_Image.h: 210

# OMX_Image.h: 219
class struct_OMX_IMAGE_HISTOGRAMINFOTYPE(Structure):
    pass

struct_OMX_IMAGE_HISTOGRAMINFOTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eHistType',
    'nBins',
    'nBitsPerBin',
]
struct_OMX_IMAGE_HISTOGRAMINFOTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eHistType', OMX_HISTOGRAMTYPE),
    ('nBins', OMX_U32),
    ('nBitsPerBin', OMX_U16),
]

OMX_IMAGE_HISTOGRAMINFOTYPE = struct_OMX_IMAGE_HISTOGRAMINFOTYPE # OMX_Image.h: 219

enum_OMX_OTHER_FORMATTYPE = c_int # OMX_Other.h: 56

OMX_OTHER_FormatTime = 0 # OMX_Other.h: 56

OMX_OTHER_FormatPower = (OMX_OTHER_FormatTime + 1) # OMX_Other.h: 56

OMX_OTHER_FormatStats = (OMX_OTHER_FormatPower + 1) # OMX_Other.h: 56

OMX_OTHER_FormatBinary = (OMX_OTHER_FormatStats + 1) # OMX_Other.h: 56

OMX_OTHER_FormatVendorReserved = 1000 # OMX_Other.h: 56

OMX_OTHER_FormatKhronosExtensions = 1862270976 # OMX_Other.h: 56

OMX_OTHER_FormatVendorStartUnused = 2130706432 # OMX_Other.h: 56

OMX_OTHER_FormatMax = 2147483647 # OMX_Other.h: 56

OMX_OTHER_FORMATTYPE = enum_OMX_OTHER_FORMATTYPE # OMX_Other.h: 56

enum_OMX_TIME_SEEKMODETYPE = c_int # OMX_Other.h: 64

OMX_TIME_SeekModeFast = 0 # OMX_Other.h: 64

OMX_TIME_SeekModeAccurate = (OMX_TIME_SeekModeFast + 1) # OMX_Other.h: 64

OMX_TIME_SeekModeKhronosExtensions = 1862270976 # OMX_Other.h: 64

OMX_TIME_SeekModeVendorStartUnused = 2130706432 # OMX_Other.h: 64

OMX_TIME_SeekModeMax = 2147483647 # OMX_Other.h: 64

OMX_TIME_SEEKMODETYPE = enum_OMX_TIME_SEEKMODETYPE # OMX_Other.h: 64

# OMX_Other.h: 70
class struct_OMX_TIME_CONFIG_SEEKMODETYPE(Structure):
    pass

struct_OMX_TIME_CONFIG_SEEKMODETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'eType',
]
struct_OMX_TIME_CONFIG_SEEKMODETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('eType', OMX_TIME_SEEKMODETYPE),
]

OMX_TIME_CONFIG_SEEKMODETYPE = struct_OMX_TIME_CONFIG_SEEKMODETYPE # OMX_Other.h: 70

# OMX_Other.h: 77
class struct_OMX_TIME_CONFIG_TIMESTAMPTYPE(Structure):
    pass

struct_OMX_TIME_CONFIG_TIMESTAMPTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nTimestamp',
]
struct_OMX_TIME_CONFIG_TIMESTAMPTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nTimestamp', OMX_TICKS),
]

OMX_TIME_CONFIG_TIMESTAMPTYPE = struct_OMX_TIME_CONFIG_TIMESTAMPTYPE # OMX_Other.h: 77

enum_OMX_TIME_UPDATETYPE = c_int # OMX_Other.h: 86

OMX_TIME_UpdateRequestFulfillment = 0 # OMX_Other.h: 86

OMX_TIME_UpdateScaleChanged = (OMX_TIME_UpdateRequestFulfillment + 1) # OMX_Other.h: 86

OMX_TIME_UpdateClockStateChanged = (OMX_TIME_UpdateScaleChanged + 1) # OMX_Other.h: 86

OMX_TIME_UpdateKhronosExtensions = 1862270976 # OMX_Other.h: 86

OMX_TIME_UpdateVendorStartUnused = 2130706432 # OMX_Other.h: 86

OMX_TIME_UpdateMax = 2147483647 # OMX_Other.h: 86

OMX_TIME_UPDATETYPE = enum_OMX_TIME_UPDATETYPE # OMX_Other.h: 86

enum_OMX_TIME_REFCLOCKTYPE = c_int # OMX_Other.h: 95

OMX_TIME_RefClockNone = 0 # OMX_Other.h: 95

OMX_TIME_RefClockAudio = (OMX_TIME_RefClockNone + 1) # OMX_Other.h: 95

OMX_TIME_RefClockVideo = (OMX_TIME_RefClockAudio + 1) # OMX_Other.h: 95

OMX_TIME_RefClockKhronosExtensions = 1862270976 # OMX_Other.h: 95

OMX_TIME_RefClockVendorStartUnused = 2130706432 # OMX_Other.h: 95

OMX_TIME_RefClockMax = 2147483647 # OMX_Other.h: 95

OMX_TIME_REFCLOCKTYPE = enum_OMX_TIME_REFCLOCKTYPE # OMX_Other.h: 95

enum_OMX_TIME_CLOCKSTATE = c_int # OMX_Other.h: 104

OMX_TIME_ClockStateRunning = 0 # OMX_Other.h: 104

OMX_TIME_ClockStateWaitingForStartTime = (OMX_TIME_ClockStateRunning + 1) # OMX_Other.h: 104

OMX_TIME_ClockStateStopped = (OMX_TIME_ClockStateWaitingForStartTime + 1) # OMX_Other.h: 104

OMX_TIME_ClockStateKhronosExtensions = 1862270976 # OMX_Other.h: 104

OMX_TIME_ClockStateVendorStartUnused = 2130706432 # OMX_Other.h: 104

OMX_TIME_ClockStateMax = 2147483647 # OMX_Other.h: 104

OMX_TIME_CLOCKSTATE = enum_OMX_TIME_CLOCKSTATE # OMX_Other.h: 104

# OMX_Other.h: 113
class struct_OMX_TIME_CONFIG_MEDIATIMEREQUESTTYPE(Structure):
    pass

struct_OMX_TIME_CONFIG_MEDIATIMEREQUESTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'pClientPrivate',
    'nMediaTimestamp',
    'nOffset',
]
struct_OMX_TIME_CONFIG_MEDIATIMEREQUESTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('pClientPrivate', OMX_PTR),
    ('nMediaTimestamp', OMX_TICKS),
    ('nOffset', OMX_TICKS),
]

OMX_TIME_CONFIG_MEDIATIMEREQUESTTYPE = struct_OMX_TIME_CONFIG_MEDIATIMEREQUESTTYPE # OMX_Other.h: 113

# OMX_Other.h: 125
class struct_OMX_TIME_MEDIATIMETYPE(Structure):
    pass

struct_OMX_TIME_MEDIATIMETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nClientPrivate',
    'eUpdateType',
    'nMediaTimestamp',
    'nOffset',
    'nWallTimeAtMediaTime',
    'xScale',
    'eState',
]
struct_OMX_TIME_MEDIATIMETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nClientPrivate', OMX_U32),
    ('eUpdateType', OMX_TIME_UPDATETYPE),
    ('nMediaTimestamp', OMX_TICKS),
    ('nOffset', OMX_TICKS),
    ('nWallTimeAtMediaTime', OMX_TICKS),
    ('xScale', OMX_S32),
    ('eState', OMX_TIME_CLOCKSTATE),
]

OMX_TIME_MEDIATIMETYPE = struct_OMX_TIME_MEDIATIMETYPE # OMX_Other.h: 125

# OMX_Other.h: 131
class struct_OMX_TIME_CONFIG_SCALETYPE(Structure):
    pass

struct_OMX_TIME_CONFIG_SCALETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'xScale',
]
struct_OMX_TIME_CONFIG_SCALETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('xScale', OMX_S32),
]

OMX_TIME_CONFIG_SCALETYPE = struct_OMX_TIME_CONFIG_SCALETYPE # OMX_Other.h: 131

# OMX_Other.h: 149
class struct_OMX_TIME_CONFIG_CLOCKSTATETYPE(Structure):
    pass

struct_OMX_TIME_CONFIG_CLOCKSTATETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'eState',
    'nStartTime',
    'nOffset',
    'nWaitMask',
]
struct_OMX_TIME_CONFIG_CLOCKSTATETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('eState', OMX_TIME_CLOCKSTATE),
    ('nStartTime', OMX_TICKS),
    ('nOffset', OMX_TICKS),
    ('nWaitMask', OMX_U32),
]

OMX_TIME_CONFIG_CLOCKSTATETYPE = struct_OMX_TIME_CONFIG_CLOCKSTATETYPE # OMX_Other.h: 149

# OMX_Other.h: 155
class struct_OMX_OTHER_CONFIG_POWERTYPE(Structure):
    pass

struct_OMX_OTHER_CONFIG_POWERTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'bEnablePM',
]
struct_OMX_OTHER_CONFIG_POWERTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('bEnablePM', OMX_BOOL),
]

OMX_OTHER_CONFIG_POWERTYPE = struct_OMX_OTHER_CONFIG_POWERTYPE # OMX_Other.h: 155

# OMX_Other.h: 161
class struct_OMX_OTHER_CONFIG_STATSTYPE(Structure):
    pass

struct_OMX_OTHER_CONFIG_STATSTYPE.__slots__ = [
    'nSize',
    'nVersion',
]
struct_OMX_OTHER_CONFIG_STATSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
]

OMX_OTHER_CONFIG_STATSTYPE = struct_OMX_OTHER_CONFIG_STATSTYPE # OMX_Other.h: 161

# OMX_Other.h: 165
class struct_OMX_OTHER_PORTDEFINITIONTYPE(Structure):
    pass

struct_OMX_OTHER_PORTDEFINITIONTYPE.__slots__ = [
    'eFormat',
]
struct_OMX_OTHER_PORTDEFINITIONTYPE._fields_ = [
    ('eFormat', OMX_OTHER_FORMATTYPE),
]

OMX_OTHER_PORTDEFINITIONTYPE = struct_OMX_OTHER_PORTDEFINITIONTYPE # OMX_Other.h: 165

# OMX_Other.h: 173
class struct_OMX_OTHER_PARAM_PORTFORMATTYPE(Structure):
    pass

struct_OMX_OTHER_PARAM_PORTFORMATTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nIndex',
    'eFormat',
]
struct_OMX_OTHER_PARAM_PORTFORMATTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nIndex', OMX_U32),
    ('eFormat', OMX_OTHER_FORMATTYPE),
]

OMX_OTHER_PARAM_PORTFORMATTYPE = struct_OMX_OTHER_PARAM_PORTFORMATTYPE # OMX_Other.h: 173

# OMX_Other.h: 180
class struct_OMX_TIME_CONFIG_ACTIVEREFCLOCKUPDATETYPE(Structure):
    pass

struct_OMX_TIME_CONFIG_ACTIVEREFCLOCKUPDATETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'bEnableRefClockUpdates',
    'nRefTimeUpdateInterval',
]
struct_OMX_TIME_CONFIG_ACTIVEREFCLOCKUPDATETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('bEnableRefClockUpdates', OMX_BOOL),
    ('nRefTimeUpdateInterval', OMX_TICKS),
]

OMX_TIME_CONFIG_ACTIVEREFCLOCKUPDATETYPE = struct_OMX_TIME_CONFIG_ACTIVEREFCLOCKUPDATETYPE # OMX_Other.h: 180

# OMX_Other.h: 187
class struct_OMX_TIME_CONFIG_RENDERINGDELAYTYPE(Structure):
    pass

struct_OMX_TIME_CONFIG_RENDERINGDELAYTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nRenderingDelay',
]
struct_OMX_TIME_CONFIG_RENDERINGDELAYTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nRenderingDelay', OMX_TICKS),
]

OMX_TIME_CONFIG_RENDERINGDELAYTYPE = struct_OMX_TIME_CONFIG_RENDERINGDELAYTYPE # OMX_Other.h: 187

enum_OMX_PORTDOMAINTYPE = c_int # OMX_Component.h: 58

OMX_PortDomainAudio = 0 # OMX_Component.h: 58

OMX_PortDomainVideo = (OMX_PortDomainAudio + 1) # OMX_Component.h: 58

OMX_PortDomainImage = (OMX_PortDomainVideo + 1) # OMX_Component.h: 58

OMX_PortDomainOther = (OMX_PortDomainImage + 1) # OMX_Component.h: 58

OMX_PortDomainKhronosExtensions = 1862270976 # OMX_Component.h: 58

OMX_PortDomainVendorStartUnused = 2130706432 # OMX_Component.h: 58

OMX_PortDomainMax = 134217727 # OMX_Component.h: 58

OMX_PORTDOMAINTYPE = enum_OMX_PORTDOMAINTYPE # OMX_Component.h: 58

# OMX_Component.h: 71
class union_anon_2(Union):
    pass

union_anon_2.__slots__ = [
    'audio',
    'video',
    'image',
    'other',
]
union_anon_2._fields_ = [
    ('audio', OMX_AUDIO_PORTDEFINITIONTYPE),
    ('video', OMX_VIDEO_PORTDEFINITIONTYPE),
    ('image', OMX_IMAGE_PORTDEFINITIONTYPE),
    ('other', OMX_OTHER_PORTDEFINITIONTYPE),
]

# OMX_Component.h: 79
class struct_OMX_PARAM_PORTDEFINITIONTYPE(Structure):
    pass

struct_OMX_PARAM_PORTDEFINITIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'eDir',
    'nBufferCountActual',
    'nBufferCountMin',
    'nBufferSize',
    'bEnabled',
    'bPopulated',
    'eDomain',
    'format',
    'bBuffersContiguous',
    'nBufferAlignment',
]
struct_OMX_PARAM_PORTDEFINITIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('eDir', OMX_DIRTYPE),
    ('nBufferCountActual', OMX_U32),
    ('nBufferCountMin', OMX_U32),
    ('nBufferSize', OMX_U32),
    ('bEnabled', OMX_BOOL),
    ('bPopulated', OMX_BOOL),
    ('eDomain', OMX_PORTDOMAINTYPE),
    ('format', union_anon_2),
    ('bBuffersContiguous', OMX_BOOL),
    ('nBufferAlignment', OMX_U32),
]

OMX_PARAM_PORTDEFINITIONTYPE = struct_OMX_PARAM_PORTDEFINITIONTYPE # OMX_Component.h: 79

# OMX_Component.h: 86
class struct_OMX_PARAM_U32TYPE(Structure):
    pass

struct_OMX_PARAM_U32TYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nU32',
]
struct_OMX_PARAM_U32TYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nU32', OMX_U32),
]

OMX_PARAM_U32TYPE = struct_OMX_PARAM_U32TYPE # OMX_Component.h: 86

enum_OMX_SUSPENSIONPOLICYTYPE = c_int # OMX_Component.h: 94

OMX_SuspensionDisabled = 0 # OMX_Component.h: 94

OMX_SuspensionEnabled = (OMX_SuspensionDisabled + 1) # OMX_Component.h: 94

OMX_SuspensionPolicyKhronosExtensions = 1862270976 # OMX_Component.h: 94

OMX_SuspensionPolicyStartUnused = 2130706432 # OMX_Component.h: 94

OMX_SuspensionPolicyMax = 2147483647 # OMX_Component.h: 94

OMX_SUSPENSIONPOLICYTYPE = enum_OMX_SUSPENSIONPOLICYTYPE # OMX_Component.h: 94

# OMX_Component.h: 100
class struct_OMX_PARAM_SUSPENSIONPOLICYTYPE(Structure):
    pass

struct_OMX_PARAM_SUSPENSIONPOLICYTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'ePolicy',
]
struct_OMX_PARAM_SUSPENSIONPOLICYTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('ePolicy', OMX_SUSPENSIONPOLICYTYPE),
]

OMX_PARAM_SUSPENSIONPOLICYTYPE = struct_OMX_PARAM_SUSPENSIONPOLICYTYPE # OMX_Component.h: 100

enum_OMX_SUSPENSIONTYPE = c_int # OMX_Component.h: 108

OMX_NotSuspended = 0 # OMX_Component.h: 108

OMX_Suspended = (OMX_NotSuspended + 1) # OMX_Component.h: 108

OMX_SuspensionKhronosExtensions = 1862270976 # OMX_Component.h: 108

OMX_SuspensionVendorStartUnused = 2130706432 # OMX_Component.h: 108

OMX_SuspendMax = 2147483647 # OMX_Component.h: 108

OMX_SUSPENSIONTYPE = enum_OMX_SUSPENSIONTYPE # OMX_Component.h: 108

# OMX_Component.h: 114
class struct_OMX_PARAM_SUSPENSIONTYPE(Structure):
    pass

struct_OMX_PARAM_SUSPENSIONTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'eType',
]
struct_OMX_PARAM_SUSPENSIONTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('eType', OMX_SUSPENSIONTYPE),
]

OMX_PARAM_SUSPENSIONTYPE = struct_OMX_PARAM_SUSPENSIONTYPE # OMX_Component.h: 114

# OMX_Component.h: 120
class struct_OMX_CONFIG_BOOLEANTYPE(Structure):
    pass

struct_OMX_CONFIG_BOOLEANTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'bEnabled',
]
struct_OMX_CONFIG_BOOLEANTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('bEnabled', OMX_BOOL),
]

OMX_CONFIG_BOOLEANTYPE = struct_OMX_CONFIG_BOOLEANTYPE # OMX_Component.h: 120

# OMX_Component.h: 126
class struct_OMX_PARAM_CONTENTURITYPE(Structure):
    pass

struct_OMX_PARAM_CONTENTURITYPE.__slots__ = [
    'nSize',
    'nVersion',
    'contentURI',
]
struct_OMX_PARAM_CONTENTURITYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('contentURI', OMX_U8 * 255),
]

OMX_PARAM_CONTENTURITYPE = struct_OMX_PARAM_CONTENTURITYPE # OMX_Component.h: 126

# OMX_Component.h: 132
class struct_OMX_RESOURCECONCEALMENTTYPE(Structure):
    pass

struct_OMX_RESOURCECONCEALMENTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'bResourceConcealmentForbidden',
]
struct_OMX_RESOURCECONCEALMENTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('bResourceConcealmentForbidden', OMX_BOOL),
]

OMX_RESOURCECONCEALMENTTYPE = struct_OMX_RESOURCECONCEALMENTTYPE # OMX_Component.h: 132

enum_OMX_METADATACHARSETTYPE = c_int # OMX_Component.h: 172

OMX_MetadataCharsetUnknown = 0 # OMX_Component.h: 172

OMX_MetadataCharsetASCII = (OMX_MetadataCharsetUnknown + 1) # OMX_Component.h: 172

OMX_MetadataCharsetBinary = (OMX_MetadataCharsetASCII + 1) # OMX_Component.h: 172

OMX_MetadataCharsetCodePage1252 = (OMX_MetadataCharsetBinary + 1) # OMX_Component.h: 172

OMX_MetadataCharsetUTF8 = (OMX_MetadataCharsetCodePage1252 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetJavaConformantUTF8 = (OMX_MetadataCharsetUTF8 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetUTF7 = (OMX_MetadataCharsetJavaConformantUTF8 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetImapUTF7 = (OMX_MetadataCharsetUTF7 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetUTF16LE = (OMX_MetadataCharsetImapUTF7 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetUTF16BE = (OMX_MetadataCharsetUTF16LE + 1) # OMX_Component.h: 172

OMX_MetadataCharsetGB12345 = (OMX_MetadataCharsetUTF16BE + 1) # OMX_Component.h: 172

OMX_MetadataCharsetHZGB2312 = (OMX_MetadataCharsetGB12345 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetGB2312 = (OMX_MetadataCharsetHZGB2312 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetGB18030 = (OMX_MetadataCharsetGB2312 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetGBK = (OMX_MetadataCharsetGB18030 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetBig5 = (OMX_MetadataCharsetGBK + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO88591 = (OMX_MetadataCharsetBig5 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO88592 = (OMX_MetadataCharsetISO88591 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO88593 = (OMX_MetadataCharsetISO88592 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO88594 = (OMX_MetadataCharsetISO88593 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO88595 = (OMX_MetadataCharsetISO88594 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO88596 = (OMX_MetadataCharsetISO88595 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO88597 = (OMX_MetadataCharsetISO88596 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO88598 = (OMX_MetadataCharsetISO88597 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO88599 = (OMX_MetadataCharsetISO88598 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO885910 = (OMX_MetadataCharsetISO88599 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO885913 = (OMX_MetadataCharsetISO885910 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO885914 = (OMX_MetadataCharsetISO885913 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO885915 = (OMX_MetadataCharsetISO885914 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetShiftJIS = (OMX_MetadataCharsetISO885915 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO2022JP = (OMX_MetadataCharsetShiftJIS + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISO2022JP1 = (OMX_MetadataCharsetISO2022JP + 1) # OMX_Component.h: 172

OMX_MetadataCharsetISOEUCJP = (OMX_MetadataCharsetISO2022JP1 + 1) # OMX_Component.h: 172

OMX_MetadataCharsetSMS7Bit = (OMX_MetadataCharsetISOEUCJP + 1) # OMX_Component.h: 172

OMX_MetadataCharsetKhronosExtensions = 1862270976 # OMX_Component.h: 172

OMX_MetadataCharsetVendorStartUnused = 2130706432 # OMX_Component.h: 172

OMX_MetadataCharsetTypeMax = 2147483647 # OMX_Component.h: 172

OMX_METADATACHARSETTYPE = enum_OMX_METADATACHARSETTYPE # OMX_Component.h: 172

enum_OMX_METADATASCOPETYPE = c_int # OMX_Component.h: 183

OMX_MetadataScopeAllLevels = 0 # OMX_Component.h: 183

OMX_MetadataScopeTopLevel = (OMX_MetadataScopeAllLevels + 1) # OMX_Component.h: 183

OMX_MetadataScopePortLevel = (OMX_MetadataScopeTopLevel + 1) # OMX_Component.h: 183

OMX_MetadataScopeNodeLevel = (OMX_MetadataScopePortLevel + 1) # OMX_Component.h: 183

OMX_MetadataScopeKhronosExtensions = 1862270976 # OMX_Component.h: 183

OMX_MetadataScopeVendorStartUnused = 2130706432 # OMX_Component.h: 183

OMX_MetadataScopeTypeMax = 2147483647 # OMX_Component.h: 183

OMX_METADATASCOPETYPE = enum_OMX_METADATASCOPETYPE # OMX_Component.h: 183

enum_OMX_METADATASEARCHMODETYPE = c_int # OMX_Component.h: 193

OMX_MetadataSearchValueSizeByIndex = 0 # OMX_Component.h: 193

OMX_MetadataSearchItemByIndex = (OMX_MetadataSearchValueSizeByIndex + 1) # OMX_Component.h: 193

OMX_MetadataSearchNextItemByKey = (OMX_MetadataSearchItemByIndex + 1) # OMX_Component.h: 193

OMX_MetadataSearchKhronosExtensions = 1862270976 # OMX_Component.h: 193

OMX_MetadataSearchVendorStartUnused = 2130706432 # OMX_Component.h: 193

OMX_MetadataSearchTypeMax = 2147483647 # OMX_Component.h: 193

OMX_METADATASEARCHMODETYPE = enum_OMX_METADATASEARCHMODETYPE # OMX_Component.h: 193

# OMX_Component.h: 202
class struct_OMX_CONFIG_METADATAITEMCOUNTTYPE(Structure):
    pass

struct_OMX_CONFIG_METADATAITEMCOUNTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'eScopeMode',
    'nScopeSpecifier',
    'nMetadataItemCount',
]
struct_OMX_CONFIG_METADATAITEMCOUNTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('eScopeMode', OMX_METADATASCOPETYPE),
    ('nScopeSpecifier', OMX_U32),
    ('nMetadataItemCount', OMX_U32),
]

OMX_CONFIG_METADATAITEMCOUNTTYPE = struct_OMX_CONFIG_METADATAITEMCOUNTTYPE # OMX_Component.h: 202

# OMX_Component.h: 220
class struct_OMX_CONFIG_METADATAITEMTYPE(Structure):
    pass

struct_OMX_CONFIG_METADATAITEMTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'eScopeMode',
    'nScopeSpecifier',
    'nMetadataItemIndex',
    'eSearchMode',
    'eKeyCharset',
    'nKeySizeUsed',
    'nKey',
    'eValueCharset',
    'sLanguageCountry',
    'nValueMaxSize',
    'nValueSizeUsed',
    'nValue',
]
struct_OMX_CONFIG_METADATAITEMTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('eScopeMode', OMX_METADATASCOPETYPE),
    ('nScopeSpecifier', OMX_U32),
    ('nMetadataItemIndex', OMX_U32),
    ('eSearchMode', OMX_METADATASEARCHMODETYPE),
    ('eKeyCharset', OMX_METADATACHARSETTYPE),
    ('nKeySizeUsed', OMX_U8),
    ('nKey', OMX_U8 * 128),
    ('eValueCharset', OMX_METADATACHARSETTYPE),
    ('sLanguageCountry', OMX_U8 * 128),
    ('nValueMaxSize', OMX_U32),
    ('nValueSizeUsed', OMX_U32),
    ('nValue', OMX_U8 * 1),
]

OMX_CONFIG_METADATAITEMTYPE = struct_OMX_CONFIG_METADATAITEMTYPE # OMX_Component.h: 220

# OMX_Component.h: 229
class struct_OMX_CONFIG_CONTAINERNODECOUNTTYPE(Structure):
    pass

struct_OMX_CONFIG_CONTAINERNODECOUNTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'bAllKeys',
    'nParentNodeID',
    'nNumNodes',
]
struct_OMX_CONFIG_CONTAINERNODECOUNTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('bAllKeys', OMX_BOOL),
    ('nParentNodeID', OMX_U32),
    ('nNumNodes', OMX_U32),
]

OMX_CONFIG_CONTAINERNODECOUNTTYPE = struct_OMX_CONFIG_CONTAINERNODECOUNTTYPE # OMX_Component.h: 229

# OMX_Component.h: 241
class struct_OMX_CONFIG_CONTAINERNODEIDTYPE(Structure):
    pass

struct_OMX_CONFIG_CONTAINERNODEIDTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'bAllKeys',
    'nParentNodeID',
    'nNodeIndex',
    'nNodeID',
    'cNodeName',
    'bIsLeafType',
]
struct_OMX_CONFIG_CONTAINERNODEIDTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('bAllKeys', OMX_BOOL),
    ('nParentNodeID', OMX_U32),
    ('nNodeIndex', OMX_U32),
    ('nNodeID', OMX_U32),
    ('cNodeName', OMX_U8 * 128),
    ('bIsLeafType', OMX_BOOL),
]

OMX_CONFIG_CONTAINERNODEIDTYPE = struct_OMX_CONFIG_CONTAINERNODEIDTYPE # OMX_Component.h: 241

# OMX_Component.h: 254
class struct_OMX_PARAM_METADATAFILTERTYPE(Structure):
    pass

struct_OMX_PARAM_METADATAFILTERTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'bAllKeys',
    'eKeyCharset',
    'nKeySizeUsed',
    'nKey',
    'nLanguageCountrySizeUsed',
    'nLanguageCountry',
    'bEnabled',
]
struct_OMX_PARAM_METADATAFILTERTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('bAllKeys', OMX_BOOL),
    ('eKeyCharset', OMX_METADATACHARSETTYPE),
    ('nKeySizeUsed', OMX_U32),
    ('nKey', OMX_U8 * 128),
    ('nLanguageCountrySizeUsed', OMX_U32),
    ('nLanguageCountry', OMX_U8 * 128),
    ('bEnabled', OMX_BOOL),
]

OMX_PARAM_METADATAFILTERTYPE = struct_OMX_PARAM_METADATAFILTERTYPE # OMX_Component.h: 254

# OMX_Component.h: 360
class struct_OMX_COMPONENTTYPE(Structure):
    pass

struct_OMX_COMPONENTTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'pComponentPrivate',
    'pApplicationPrivate',
    'GetComponentVersion',
    'SendCommand',
    'GetParameter',
    'SetParameter',
    'GetConfig',
    'SetConfig',
    'GetExtensionIndex',
    'GetState',
    'ComponentTunnelRequest',
    'UseBuffer',
    'AllocateBuffer',
    'FreeBuffer',
    'EmptyThisBuffer',
    'FillThisBuffer',
    'SetCallbacks',
    'ComponentDeInit',
    'UseEGLImage',
    'ComponentRoleEnum',
]
struct_OMX_COMPONENTTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('pComponentPrivate', OMX_PTR),
    ('pApplicationPrivate', OMX_PTR),
    ('GetComponentVersion', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, OMX_STRING, POINTER(OMX_VERSIONTYPE), POINTER(OMX_VERSIONTYPE), POINTER(OMX_UUIDTYPE))),
    ('SendCommand', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, OMX_COMMANDTYPE, OMX_U32, OMX_PTR)),
    ('GetParameter', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, OMX_INDEXTYPE, OMX_PTR)),
    ('SetParameter', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, OMX_INDEXTYPE, OMX_PTR)),
    ('GetConfig', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, OMX_INDEXTYPE, OMX_PTR)),
    ('SetConfig', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, OMX_INDEXTYPE, OMX_PTR)),
    ('GetExtensionIndex', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, OMX_STRING, POINTER(OMX_INDEXTYPE))),
    ('GetState', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, POINTER(OMX_STATETYPE))),
    ('ComponentTunnelRequest', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, OMX_U32, OMX_HANDLETYPE, OMX_U32, POINTER(OMX_TUNNELSETUPTYPE))),
    ('UseBuffer', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, POINTER(POINTER(OMX_BUFFERHEADERTYPE)), OMX_U32, OMX_PTR, OMX_U32, POINTER(OMX_U8))),
    ('AllocateBuffer', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, POINTER(POINTER(OMX_BUFFERHEADERTYPE)), OMX_U32, OMX_PTR, OMX_U32)),
    ('FreeBuffer', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, OMX_U32, POINTER(OMX_BUFFERHEADERTYPE))),
    ('EmptyThisBuffer', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, POINTER(OMX_BUFFERHEADERTYPE))),
    ('FillThisBuffer', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, POINTER(OMX_BUFFERHEADERTYPE))),
    ('SetCallbacks', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, POINTER(OMX_CALLBACKTYPE), OMX_PTR)),
    ('ComponentDeInit', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE)),
    ('UseEGLImage', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, POINTER(POINTER(OMX_BUFFERHEADERTYPE)), OMX_U32, OMX_PTR, POINTER(None))),
    ('ComponentRoleEnum', CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE, POINTER(OMX_U8), OMX_U32)),
]

OMX_COMPONENTTYPE = struct_OMX_COMPONENTTYPE # OMX_Component.h: 360

# OMX_Component.h: 366
class struct_OMX_CONFIG_COMMITMODETYPE(Structure):
    pass

struct_OMX_CONFIG_COMMITMODETYPE.__slots__ = [
    'nSize',
    'nVersion',
    'bDeferred',
]
struct_OMX_CONFIG_COMMITMODETYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('bDeferred', OMX_BOOL),
]

OMX_CONFIG_COMMITMODETYPE = struct_OMX_CONFIG_COMMITMODETYPE # OMX_Component.h: 366

# OMX_Component.h: 371
class struct_OMX_CONFIG_COMMITTYPE(Structure):
    pass

struct_OMX_CONFIG_COMMITTYPE.__slots__ = [
    'nSize',
    'nVersion',
]
struct_OMX_CONFIG_COMMITTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
]

OMX_CONFIG_COMMITTYPE = struct_OMX_CONFIG_COMMITTYPE # OMX_Component.h: 371

enum_OMX_MEDIACONTAINER_FORMATTYPE = c_int # OMX_Component.h: 411

OMX_FORMAT_RAW = 0 # OMX_Component.h: 411

OMX_FORMAT_MP4 = (OMX_FORMAT_RAW + 1) # OMX_Component.h: 411

OMX_FORMAT_3GP = (OMX_FORMAT_MP4 + 1) # OMX_Component.h: 411

OMX_FORMAT_3G2 = (OMX_FORMAT_3GP + 1) # OMX_Component.h: 411

OMX_FORMAT_AMC = (OMX_FORMAT_3G2 + 1) # OMX_Component.h: 411

OMX_FORMAT_SKM = (OMX_FORMAT_AMC + 1) # OMX_Component.h: 411

OMX_FORMAT_K3G = (OMX_FORMAT_SKM + 1) # OMX_Component.h: 411

OMX_FORMAT_VOB = (OMX_FORMAT_K3G + 1) # OMX_Component.h: 411

OMX_FORMAT_AVI = (OMX_FORMAT_VOB + 1) # OMX_Component.h: 411

OMX_FORMAT_ASF = (OMX_FORMAT_AVI + 1) # OMX_Component.h: 411

OMX_FORMAT_RM = (OMX_FORMAT_ASF + 1) # OMX_Component.h: 411

OMX_FORMAT_MPEG_ES = (OMX_FORMAT_RM + 1) # OMX_Component.h: 411

OMX_FORMAT_DIVX = (OMX_FORMAT_MPEG_ES + 1) # OMX_Component.h: 411

OMX_FORMAT_MPEG_TS = (OMX_FORMAT_DIVX + 1) # OMX_Component.h: 411

OMX_FORMAT_QT = (OMX_FORMAT_MPEG_TS + 1) # OMX_Component.h: 411

OMX_FORMAT_M4A = (OMX_FORMAT_QT + 1) # OMX_Component.h: 411

OMX_FORMAT_MP3 = (OMX_FORMAT_M4A + 1) # OMX_Component.h: 411

OMX_FORMAT_WAVE = (OMX_FORMAT_MP3 + 1) # OMX_Component.h: 411

OMX_FORMAT_XMF = (OMX_FORMAT_WAVE + 1) # OMX_Component.h: 411

OMX_FORMAT_AMR = (OMX_FORMAT_XMF + 1) # OMX_Component.h: 411

OMX_FORMAT_AAC = (OMX_FORMAT_AMR + 1) # OMX_Component.h: 411

OMX_FORMAT_EVRC = (OMX_FORMAT_AAC + 1) # OMX_Component.h: 411

OMX_FORMAT_QCP = (OMX_FORMAT_EVRC + 1) # OMX_Component.h: 411

OMX_FORMAT_SMF = (OMX_FORMAT_QCP + 1) # OMX_Component.h: 411

OMX_FORMAT_OGG = (OMX_FORMAT_SMF + 1) # OMX_Component.h: 411

OMX_FORMAT_BMP = (OMX_FORMAT_OGG + 1) # OMX_Component.h: 411

OMX_FORMAT_JPG = (OMX_FORMAT_BMP + 1) # OMX_Component.h: 411

OMX_FORMAT_JPG2000 = (OMX_FORMAT_JPG + 1) # OMX_Component.h: 411

OMX_FORMAT_MKV = (OMX_FORMAT_JPG2000 + 1) # OMX_Component.h: 411

OMX_FORMAT_FLV = (OMX_FORMAT_MKV + 1) # OMX_Component.h: 411

OMX_FORMAT_M4V = (OMX_FORMAT_FLV + 1) # OMX_Component.h: 411

OMX_FORMAT_F4V = (OMX_FORMAT_M4V + 1) # OMX_Component.h: 411

OMX_FORMAT_WEBM = (OMX_FORMAT_F4V + 1) # OMX_Component.h: 411

OMX_FORMAT_WEBP = (OMX_FORMAT_WEBM + 1) # OMX_Component.h: 411

OMX_FORMATKhronosExtensions = 1862270976 # OMX_Component.h: 411

OMX_FORMATVendorStartUnused = 2130706432 # OMX_Component.h: 411

OMX_FORMATMax = 2147483647 # OMX_Component.h: 411

OMX_MEDIACONTAINER_FORMATTYPE = enum_OMX_MEDIACONTAINER_FORMATTYPE # OMX_Component.h: 411

# OMX_Component.h: 417
class struct_OMX_MEDIACONTAINER_INFOTYPE(Structure):
    pass

struct_OMX_MEDIACONTAINER_INFOTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'eFmtType',
]
struct_OMX_MEDIACONTAINER_INFOTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('eFmtType', OMX_MEDIACONTAINER_FORMATTYPE),
]

OMX_MEDIACONTAINER_INFOTYPE = struct_OMX_MEDIACONTAINER_INFOTYPE # OMX_Component.h: 417

# OMX_Component.h: 427
class struct_OMX_CONFIG_TUNNELEDPORTSTATUSTYPE(Structure):
    pass

struct_OMX_CONFIG_TUNNELEDPORTSTATUSTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'nTunneledPortStatus',
]
struct_OMX_CONFIG_TUNNELEDPORTSTATUSTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('nTunneledPortStatus', OMX_U32),
]

OMX_CONFIG_TUNNELEDPORTSTATUSTYPE = struct_OMX_CONFIG_TUNNELEDPORTSTATUSTYPE # OMX_Component.h: 427

# OMX_Component.h: 434
class struct_OMX_CONFIG_PORTBOOLEANTYPE(Structure):
    pass

struct_OMX_CONFIG_PORTBOOLEANTYPE.__slots__ = [
    'nSize',
    'nVersion',
    'nPortIndex',
    'bEnabled',
]
struct_OMX_CONFIG_PORTBOOLEANTYPE._fields_ = [
    ('nSize', OMX_U32),
    ('nVersion', OMX_VERSIONTYPE),
    ('nPortIndex', OMX_U32),
    ('bEnabled', OMX_BOOL),
]

OMX_CONFIG_PORTBOOLEANTYPE = struct_OMX_CONFIG_PORTBOOLEANTYPE # OMX_Component.h: 434

# OMX_Types.h: 76
try:
    OMX_ALL = 4294967295L
except:
    pass

# OMX_Types.h: 173
try:
    OMX_TICKS_PER_SECOND = 1000000
except:
    pass

# OMX_Types.h: 204
try:
    OMX_VERSION_MAJOR = 1
except:
    pass

# OMX_Types.h: 205
try:
    OMX_VERSION_MINOR = 2
except:
    pass

# OMX_Types.h: 206
try:
    OMX_VERSION_REVISION = 0
except:
    pass

# OMX_Types.h: 207
try:
    OMX_VERSION_STEP = 0
except:
    pass

# OMX_Types.h: 209
try:
    OMX_VERSION = ((((OMX_VERSION_STEP << 24) | (OMX_VERSION_REVISION << 16)) | (OMX_VERSION_MINOR << 8)) | OMX_VERSION_MAJOR)
except:
    pass

# OMX_Core.h: 185
try:
    OMX_MAX_STRINGNAME_SIZE = 128
except:
    pass

# OMX_Core.h: 193
try:
    OMX_BUFFERFLAG_EOS = 1
except:
    pass

# OMX_Core.h: 194
try:
    OMX_BUFFERFLAG_STARTTIME = 2
except:
    pass

# OMX_Core.h: 195
try:
    OMX_BUFFERFLAG_DECODEONLY = 4
except:
    pass

# OMX_Core.h: 196
try:
    OMX_BUFFERFLAG_DATACORRUPT = 8
except:
    pass

# OMX_Core.h: 197
try:
    OMX_BUFFERFLAG_ENDOFFRAME = 16
except:
    pass

# OMX_Core.h: 198
try:
    OMX_BUFFERFLAG_SYNCFRAME = 32
except:
    pass

# OMX_Core.h: 199
try:
    OMX_BUFFERFLAG_EXTRADATA = 64
except:
    pass

# OMX_Core.h: 200
try:
    OMX_BUFFERFLAG_CODECCONFIG = 128
except:
    pass

# OMX_Core.h: 201
try:
    OMX_BUFFERFLAG_TIMESTAMPINVALID = 256
except:
    pass

# OMX_Core.h: 202
try:
    OMX_BUFFERFLAG_READONLY = 512
except:
    pass

# OMX_Core.h: 203
try:
    OMX_BUFFERFLAG_ENDOFSUBFRAME = 1024
except:
    pass

# OMX_Core.h: 204
try:
    OMX_BUFFERFLAG_SKIPFRAME = 2048
except:
    pass

# OMX_Core.h: 309
try:
    OMX_PORTTUNNELFLAG_READONLY = 1
except:
    pass

# OMX_Core.h: 317
def OMX_GetComponentVersion(hComponent, pComponentName, pComponentVersion, pSpecVersion, pComponentUUID):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.GetComponentVersion) (hComponent, pComponentName, pComponentVersion, pSpecVersion, pComponentUUID))

# OMX_Core.h: 330
def OMX_SendCommand(hComponent, Cmd, nParam, pCmdData):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.SendCommand) (hComponent, Cmd, nParam, pCmdData))

# OMX_Core.h: 341
def OMX_GetParameter(hComponent, nParamIndex, pComponentParameterStructure):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.GetParameter) (hComponent, nParamIndex, pComponentParameterStructure))

# OMX_Core.h: 350
def OMX_SetParameter(hComponent, nParamIndex, pComponentParameterStructure):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.SetParameter) (hComponent, nParamIndex, pComponentParameterStructure))

# OMX_Core.h: 359
def OMX_GetConfig(hComponent, nConfigIndex, pComponentConfigStructure):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.GetConfig) (hComponent, nConfigIndex, pComponentConfigStructure))

# OMX_Core.h: 368
def OMX_SetConfig(hComponent, nConfigIndex, pComponentConfigStructure):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.SetConfig) (hComponent, nConfigIndex, pComponentConfigStructure))

# OMX_Core.h: 377
def OMX_GetExtensionIndex(hComponent, cParameterName, pIndexType):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.GetExtensionIndex) (hComponent, cParameterName, pIndexType))

# OMX_Core.h: 386
def OMX_GetState(hComponent, pState):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.GetState) (hComponent, pState))

# OMX_Core.h: 393
def OMX_UseBuffer(hComponent, ppBufferHdr, nPortIndex, pAppPrivate, nSizeBytes, pBuffer):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.UseBuffer) (hComponent, ppBufferHdr, nPortIndex, pAppPrivate, nSizeBytes, pBuffer))

# OMX_Core.h: 408
def OMX_AllocateBuffer(hComponent, ppBuffer, nPortIndex, pAppPrivate, nSizeBytes):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.AllocateBuffer) (hComponent, ppBuffer, nPortIndex, pAppPrivate, nSizeBytes))

# OMX_Core.h: 421
def OMX_FreeBuffer(hComponent, nPortIndex, pBuffer):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.FreeBuffer) (hComponent, nPortIndex, pBuffer))

# OMX_Core.h: 430
def OMX_EmptyThisBuffer(hComponent, pBuffer):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.EmptyThisBuffer) (hComponent, pBuffer))

# OMX_Core.h: 437
def OMX_FillThisBuffer(hComponent, pBuffer):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.FillThisBuffer) (hComponent, pBuffer))

# OMX_Core.h: 444
def OMX_UseEGLImage(hComponent, ppBufferHdr, nPortIndex, pAppPrivate, eglImage):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.UseEGLImage) (hComponent, ppBufferHdr, nPortIndex, pAppPrivate, eglImage))

# OMX_Core.h: 457
def OMX_SetCallbacks(hComponent, pCallbacks, pAppData):
    return ((cast(hComponent, POINTER(OMX_COMPONENTTYPE)).contents.SetCallbacks) (hComponent, pCallbacks, pAppData))

# OMX_Audio.h: 130
try:
    OMX_AUDIO_MAXCHANNELS = 36
except:
    pass

# OMX_Audio.h: 131
try:
    OMX_MIN_PCMPAYLOAD_MSEC = 5
except:
    pass

# OMX_Audio.h: 210
try:
    OMX_AUDIO_AACToolNone = 0
except:
    pass

# OMX_Audio.h: 211
try:
    OMX_AUDIO_AACToolMS = 1
except:
    pass

# OMX_Audio.h: 212
try:
    OMX_AUDIO_AACToolIS = 2
except:
    pass

# OMX_Audio.h: 213
try:
    OMX_AUDIO_AACToolTNS = 4
except:
    pass

# OMX_Audio.h: 214
try:
    OMX_AUDIO_AACToolPNS = 8
except:
    pass

# OMX_Audio.h: 215
try:
    OMX_AUDIO_AACToolLTP = 16
except:
    pass

# OMX_Audio.h: 216
try:
    OMX_AUDIO_AACToolAll = 2147483647
except:
    pass

# OMX_Audio.h: 218
try:
    OMX_AUDIO_AACERNone = 0
except:
    pass

# OMX_Audio.h: 219
try:
    OMX_AUDIO_AACERVCB11 = 1
except:
    pass

# OMX_Audio.h: 220
try:
    OMX_AUDIO_AACERRVLC = 2
except:
    pass

# OMX_Audio.h: 221
try:
    OMX_AUDIO_AACERHCR = 4
except:
    pass

# OMX_Audio.h: 222
try:
    OMX_AUDIO_AACERAll = 2147483647
except:
    pass

# OMX_IVCommon.h: 594
try:
    OMX_InterlaceFrameProgressive = 1
except:
    pass

# OMX_IVCommon.h: 595
try:
    OMX_InterlaceInterleaveFrameTopFieldFirst = 2
except:
    pass

# OMX_IVCommon.h: 596
try:
    OMX_InterlaceInterleaveFrameBottomFieldFirst = 4
except:
    pass

# OMX_IVCommon.h: 597
try:
    OMX_InterlaceFrameTopFieldFirst = 8
except:
    pass

# OMX_IVCommon.h: 598
try:
    OMX_InterlaceFrameBottomFieldFirst = 16
except:
    pass

# OMX_IVCommon.h: 599
try:
    OMX_InterlaceInterleaveFieldTop = 32
except:
    pass

# OMX_IVCommon.h: 600
try:
    OMX_InterlaceInterleaveFieldBottom = 64
except:
    pass

# OMX_Other.h: 133
try:
    OMX_CLOCKPORT0 = 1
except:
    pass

# OMX_Other.h: 134
try:
    OMX_CLOCKPORT1 = 2
except:
    pass

# OMX_Other.h: 135
try:
    OMX_CLOCKPORT2 = 4
except:
    pass

# OMX_Other.h: 136
try:
    OMX_CLOCKPORT3 = 8
except:
    pass

# OMX_Other.h: 137
try:
    OMX_CLOCKPORT4 = 16
except:
    pass

# OMX_Other.h: 138
try:
    OMX_CLOCKPORT5 = 32
except:
    pass

# OMX_Other.h: 139
try:
    OMX_CLOCKPORT6 = 64
except:
    pass

# OMX_Other.h: 140
try:
    OMX_CLOCKPORT7 = 128
except:
    pass

# OMX_Component.h: 419
try:
    OMX_PORTSTATUS_ACCEPTUSEBUFFER = 1
except:
    pass

# OMX_Component.h: 420
try:
    OMX_PORTSTATUS_ACCEPTBUFFEREXCHANGE = 2
except:
    pass

# OMX_RoleNames.h: 38
try:
    OMX_ROLE_AUDIO_DECODER_AAC = 'audio_decoder.aac'
except:
    pass

# OMX_RoleNames.h: 39
try:
    OMX_ROLE_AUDIO_DECODER_AMRNB = 'audio_decoder.amrnb'
except:
    pass

# OMX_RoleNames.h: 40
try:
    OMX_ROLE_AUDIO_DECODER_AMRWB = 'audio_decoder.amrwb'
except:
    pass

# OMX_RoleNames.h: 41
try:
    OMX_ROLS_AUDIO_DEXODER_AMRPLUS = 'audio_decoder.amrwb+'
except:
    pass

# OMX_RoleNames.h: 42
try:
    OMX_ROLE_AUDIO_DECODER_MP3 = 'audio_decoder.mp3'
except:
    pass

# OMX_RoleNames.h: 43
try:
    OMX_ROLE_AUDIO_DECODER_RA = 'audio_decoder.ra'
except:
    pass

# OMX_RoleNames.h: 44
try:
    OMX_ROLE_AUDIO_DECODER_WMA = 'audio_decoder.wma'
except:
    pass

# OMX_RoleNames.h: 47
try:
    OMX_ROLE_AUDIO_ENCODER_AAC = 'audio_encoder.aac'
except:
    pass

# OMX_RoleNames.h: 48
try:
    OMX_ROLE_AUDIO_ENCODER_AMRNB = 'audio_encoder.amrnb'
except:
    pass

# OMX_RoleNames.h: 49
try:
    OMX_ROLE_AUDIO_ENCODER_AMRWB = 'audio_encoder.amrwb'
except:
    pass

# OMX_RoleNames.h: 50
try:
    OMX_ROLS_AUDIO_ENCODER_AMRPLUS = 'audio_encoder.amrwb+'
except:
    pass

# OMX_RoleNames.h: 51
try:
    OMX_ROLE_AUDIO_ENCODER_MP3 = 'audio_encoder.mp3'
except:
    pass

# OMX_RoleNames.h: 54
try:
    OMX_ROLE_AUDIO_MIXER_PCM = 'audio_mixer.pcm'
except:
    pass

# OMX_RoleNames.h: 57
try:
    OMX_ROLE_AUDIO_READER_BINARY = 'audio_reader.binary'
except:
    pass

# OMX_RoleNames.h: 60
try:
    OMX_ROLE_AUDIO_RENDERER_PCM = 'audio_renderer.pcm'
except:
    pass

# OMX_RoleNames.h: 63
try:
    OMX_ROLE_AUDIO_WRITER_BINARY = 'audio_writer.binary'
except:
    pass

# OMX_RoleNames.h: 66
try:
    OMX_ROLE_AUDIO_CAPTURER_PCM = 'audio_capturer.pcm'
except:
    pass

# OMX_RoleNames.h: 69
try:
    OMX_ROLE_AUDIO_PROCESSOR_PCM_STEREO_WIDENING_LOUDSPEAKERS = 'audio_processor.pcm.stereo_widening_loudspeakers'
except:
    pass

# OMX_RoleNames.h: 70
try:
    OMX_ROLE_AUDIO_PROCESSOR_PCM_STEREO_WIDENING_HEADPHONES = 'audio_processor.pcm.stereo_widening_headphones'
except:
    pass

# OMX_RoleNames.h: 71
try:
    OMX_ROLE_AUDIO_PROCESSOR_PCM_REVERBERATION = 'audio_processor.pcm.reverberation'
except:
    pass

# OMX_RoleNames.h: 72
try:
    OMX_ROLE_AUDIO_PROCESSOR_PCM_CHORUS = 'audio_processor.pcm.chorus'
except:
    pass

# OMX_RoleNames.h: 73
try:
    OMX_ROLE_AUDIO_PROCESSOR_PCM_EQUALIZER = 'audio_processor.pcm.equalizer'
except:
    pass

# OMX_RoleNames.h: 76
try:
    OMX_ROLE_AUDIO_3D_MIXER_PCM_HEADPHONES = 'audio_3D_mixer.pcm.headphones'
except:
    pass

# OMX_RoleNames.h: 77
try:
    OMX_ROLE_AUDIO_3D_MIXER_PCM_LOUDSPEAKERS = 'audio_3D_mixer.pcm.loudspeakers'
except:
    pass

# OMX_RoleNames.h: 80
try:
    OMX_ROLE_IMAGE_DECODER_JPEG = 'image_decoder.JPEG'
except:
    pass

# OMX_RoleNames.h: 83
try:
    OMX_ROLE_IMAGE_ENCODER_JPEG = 'image_encoder.JPEG'
except:
    pass

# OMX_RoleNames.h: 86
try:
    OMX_ROLE_IMAGE_READER_BINARY = 'image_reader.binary'
except:
    pass

# OMX_RoleNames.h: 89
try:
    OMX_ROLE_IMAGE_WRITER_BINARY = 'image_writer.binary'
except:
    pass

# OMX_RoleNames.h: 92
try:
    OMX_ROLE_VIDEO_DECODER_H263 = 'video_decoder.h263'
except:
    pass

# OMX_RoleNames.h: 93
try:
    OMX_ROLE_VIDEO_DECODER_AVC = 'video_decoder.avc'
except:
    pass

# OMX_RoleNames.h: 94
try:
    OMX_ROLE_VIDEO_DECODER_MPEG4 = 'video_decoder.mpeg4'
except:
    pass

# OMX_RoleNames.h: 95
try:
    OMX_ROLE_VIDEO_DECODER_RV = 'video_decoder.rv'
except:
    pass

# OMX_RoleNames.h: 96
try:
    OMX_ROLE_VIDEO_DECODER_WMV = 'video_decoder.wmv'
except:
    pass

# OMX_RoleNames.h: 97
try:
    OMX_ROLE_VIDEO_DECODER_VC1 = 'video_decoder.vc1'
except:
    pass

# OMX_RoleNames.h: 100
try:
    OMX_ROLE_VIDEO_ENCODER_H263 = 'video_encoder.h263'
except:
    pass

# OMX_RoleNames.h: 101
try:
    OMX_ROLE_VIDEO_ENCODER_AVC = 'video_encoder.avc'
except:
    pass

# OMX_RoleNames.h: 102
try:
    OMX_ROLE_VIDEO_ENCODER_MPEG4 = 'video_encoder.mpeg4'
except:
    pass

# OMX_RoleNames.h: 105
try:
    OMX_ROLE_VIDEO_READER_BINARY = 'video_reader.binary'
except:
    pass

# OMX_RoleNames.h: 108
try:
    OMX_ROLE_VIDEO_SCHEDULER_BINARY = 'video_scheduler.binary'
except:
    pass

# OMX_RoleNames.h: 111
try:
    OMX_ROLE_VIDEO_WRITER_BINARY = 'video_writer.binary'
except:
    pass

# OMX_RoleNames.h: 114
try:
    OMX_ROLE_CAMERA_YUV = 'camera.yuv'
except:
    pass

# OMX_RoleNames.h: 117
try:
    OMX_ROLE_CLOCK_BINARY = 'clock.binary'
except:
    pass

# OMX_RoleNames.h: 120
try:
    OMX_ROLE_CONTAINER_DEMUXER_3GP = 'container_demuxer_3gp'
except:
    pass

# OMX_RoleNames.h: 121
try:
    OMX_ROLE_CONTAINER_DEMUXER_ASF = 'container_demuxer_asf'
except:
    pass

# OMX_RoleNames.h: 122
try:
    OMX_ROLE_CONTAINER_DEMUXER_REAL = 'container_demuxer_real'
except:
    pass

# OMX_RoleNames.h: 125
try:
    OMX_ROLE_CONTAINER_MUXER_3GP = 'container_muxer_3gp'
except:
    pass

# OMX_RoleNames.h: 128
try:
    OMX_ROLE_IV_PROCESSOR_YUV = 'iv_processor.yuv'
except:
    pass

# OMX_RoleNames.h: 131
try:
    OMX_ROLE_IV_RENDERER_YUV_OVERLAY = 'iv_renderer.yuv.overlay'
except:
    pass

# OMX_RoleNames.h: 132
try:
    OMX_ROLE_IV_RENDERER_YUV_BLTER = 'iv_renderer.yuv.blter'
except:
    pass

# OMX_RoleNames.h: 133
try:
    OMX_ROLE_IV_RENDERER_RGB_OVERLAY = 'iv_renderer.rgb.overlay'
except:
    pass

# OMX_RoleNames.h: 134
try:
    OMX_ROLE_IV_RENDERER_RGB_BLTER = 'iv_renderer.rgb.blter'
except:
    pass

OMX_BU32 = struct_OMX_BU32 # OMX_Types.h: 154

OMX_BS32 = struct_OMX_BS32 # OMX_Types.h: 161

OMX_MARKTYPE = struct_OMX_MARKTYPE # OMX_Types.h: 188

OMX_VERSIONTYPE = union_OMX_VERSIONTYPE # OMX_Types.h: 236

OMX_COMPONENTREGISTERTYPE = struct_OMX_COMPONENTREGISTERTYPE # OMX_Core.h: 174

OMX_PRIORITYMGMTTYPE = struct_OMX_PRIORITYMGMTTYPE # OMX_Core.h: 183

OMX_PARAM_COMPONENTROLETYPE = struct_OMX_PARAM_COMPONENTROLETYPE # OMX_Core.h: 191

OMX_BUFFERHEADERTYPE = struct_OMX_BUFFERHEADERTYPE # OMX_Core.h: 225

OMX_OTHER_EXTRADATATYPE = struct_OMX_OTHER_EXTRADATATYPE # OMX_Core.h: 244

OMX_PORT_PARAM_TYPE = struct_OMX_PORT_PARAM_TYPE # OMX_Core.h: 251

OMX_CALLBACKTYPE = struct_OMX_CALLBACKTYPE # OMX_Core.h: 290

OMX_PARAM_BUFFERSUPPLIERTYPE = struct_OMX_PARAM_BUFFERSUPPLIERTYPE # OMX_Core.h: 307

OMX_TUNNELSETUPTYPE = struct_OMX_TUNNELSETUPTYPE # OMX_Core.h: 315

OMX_CONFIG_CALLBACKREQUESTTYPE = struct_OMX_CONFIG_CALLBACKREQUESTTYPE # OMX_Core.h: 512

OMX_AUDIO_PORTDEFINITIONTYPE = struct_OMX_AUDIO_PORTDEFINITIONTYPE # OMX_Audio.h: 83

OMX_AUDIO_PARAM_PORTFORMATTYPE = struct_OMX_AUDIO_PARAM_PORTFORMATTYPE # OMX_Audio.h: 91

OMX_AUDIO_PARAM_PCMMODETYPE = struct_OMX_AUDIO_PARAM_PCMMODETYPE # OMX_Audio.h: 145

OMX_AUDIO_PARAM_MP3TYPE = struct_OMX_AUDIO_PARAM_MP3TYPE # OMX_Audio.h: 177

OMX_AUDIO_PARAM_AACPROFILETYPE = struct_OMX_AUDIO_PARAM_AACPROFILETYPE # OMX_Audio.h: 238

OMX_AUDIO_PARAM_VORBISTYPE = struct_OMX_AUDIO_PARAM_VORBISTYPE # OMX_Audio.h: 253

OMX_AUDIO_PARAM_WMATYPE = struct_OMX_AUDIO_PARAM_WMATYPE # OMX_Audio.h: 306

OMX_AUDIO_PARAM_RATYPE = struct_OMX_AUDIO_PARAM_RATYPE # OMX_Audio.h: 335

OMX_AUDIO_PARAM_SBCTYPE = struct_OMX_AUDIO_PARAM_SBCTYPE # OMX_Audio.h: 358

OMX_AUDIO_PARAM_ADPCMTYPE = struct_OMX_AUDIO_PARAM_ADPCMTYPE # OMX_Audio.h: 368

OMX_AUDIO_PARAM_G723TYPE = struct_OMX_AUDIO_PARAM_G723TYPE # OMX_Audio.h: 388

OMX_AUDIO_PARAM_G726TYPE = struct_OMX_AUDIO_PARAM_G726TYPE # OMX_Audio.h: 407

OMX_AUDIO_PARAM_G729TYPE = struct_OMX_AUDIO_PARAM_G729TYPE # OMX_Audio.h: 426

OMX_AUDIO_PARAM_AMRTYPE = struct_OMX_AUDIO_PARAM_AMRTYPE # OMX_Audio.h: 561

OMX_AUDIO_PARAM_GSMFRTYPE = struct_OMX_AUDIO_PARAM_GSMFRTYPE # OMX_Audio.h: 569

OMX_AUDIO_PARAM_GSMHRTYPE = struct_OMX_AUDIO_PARAM_GSMHRTYPE # OMX_Audio.h: 577

OMX_AUDIO_PARAM_GSMEFRTYPE = struct_OMX_AUDIO_PARAM_GSMEFRTYPE # OMX_Audio.h: 585

OMX_AUDIO_PARAM_TDMAFRTYPE = struct_OMX_AUDIO_PARAM_TDMAFRTYPE # OMX_Audio.h: 594

OMX_AUDIO_PARAM_TDMAEFRTYPE = struct_OMX_AUDIO_PARAM_TDMAEFRTYPE # OMX_Audio.h: 603

OMX_AUDIO_PARAM_PDCFRTYPE = struct_OMX_AUDIO_PARAM_PDCFRTYPE # OMX_Audio.h: 612

OMX_AUDIO_PARAM_PDCEFRTYPE = struct_OMX_AUDIO_PARAM_PDCEFRTYPE # OMX_Audio.h: 621

OMX_AUDIO_PARAM_PDCHRTYPE = struct_OMX_AUDIO_PARAM_PDCHRTYPE # OMX_Audio.h: 630

OMX_AUDIO_PARAM_QCELP8TYPE = struct_OMX_AUDIO_PARAM_QCELP8TYPE # OMX_Audio.h: 653

OMX_AUDIO_PARAM_QCELP13TYPE = struct_OMX_AUDIO_PARAM_QCELP13TYPE # OMX_Audio.h: 663

OMX_AUDIO_PARAM_EVRCTYPE = struct_OMX_AUDIO_PARAM_EVRCTYPE # OMX_Audio.h: 677

OMX_AUDIO_PARAM_SMVTYPE = struct_OMX_AUDIO_PARAM_SMVTYPE # OMX_Audio.h: 691

OMX_AUDIO_PARAM_MIDITYPE = struct_OMX_AUDIO_PARAM_MIDITYPE # OMX_Audio.h: 716

OMX_AUDIO_PARAM_MIDILOADUSERSOUNDTYPE = struct_OMX_AUDIO_PARAM_MIDILOADUSERSOUNDTYPE # OMX_Audio.h: 748

OMX_AUDIO_CONFIG_MIDIIMMEDIATEEVENTTYPE = struct_OMX_AUDIO_CONFIG_MIDIIMMEDIATEEVENTTYPE # OMX_Audio.h: 756

OMX_AUDIO_CONFIG_MIDISOUNDBANKPROGRAMTYPE = struct_OMX_AUDIO_CONFIG_MIDISOUNDBANKPROGRAMTYPE # OMX_Audio.h: 766

OMX_AUDIO_CONFIG_MIDICONTROLTYPE = struct_OMX_AUDIO_CONFIG_MIDICONTROLTYPE # OMX_Audio.h: 784

OMX_AUDIO_CONFIG_MIDISTATUSTYPE = struct_OMX_AUDIO_CONFIG_MIDISTATUSTYPE # OMX_Audio.h: 810

OMX_AUDIO_CONFIG_MIDIMETAEVENTTYPE = struct_OMX_AUDIO_CONFIG_MIDIMETAEVENTTYPE # OMX_Audio.h: 821

OMX_AUDIO_CONFIG_MIDIMETAEVENTDATATYPE = struct_OMX_AUDIO_CONFIG_MIDIMETAEVENTDATATYPE # OMX_Audio.h: 830

OMX_AUDIO_CONFIG_VOLUMETYPE = struct_OMX_AUDIO_CONFIG_VOLUMETYPE # OMX_Audio.h: 838

OMX_AUDIO_CONFIG_CHANNELVOLUMETYPE = struct_OMX_AUDIO_CONFIG_CHANNELVOLUMETYPE # OMX_Audio.h: 848

OMX_AUDIO_CONFIG_BALANCETYPE = struct_OMX_AUDIO_CONFIG_BALANCETYPE # OMX_Audio.h: 855

OMX_AUDIO_CONFIG_MUTETYPE = struct_OMX_AUDIO_CONFIG_MUTETYPE # OMX_Audio.h: 862

OMX_AUDIO_CONFIG_CHANNELMUTETYPE = struct_OMX_AUDIO_CONFIG_CHANNELMUTETYPE # OMX_Audio.h: 871

OMX_AUDIO_CONFIG_LOUDNESSTYPE = struct_OMX_AUDIO_CONFIG_LOUDNESSTYPE # OMX_Audio.h: 878

OMX_AUDIO_CONFIG_BASSTYPE = struct_OMX_AUDIO_CONFIG_BASSTYPE # OMX_Audio.h: 886

OMX_AUDIO_CONFIG_TREBLETYPE = struct_OMX_AUDIO_CONFIG_TREBLETYPE # OMX_Audio.h: 894

OMX_AUDIO_CONFIG_EQUALIZERTYPE = struct_OMX_AUDIO_CONFIG_EQUALIZERTYPE # OMX_Audio.h: 904

OMX_AUDIO_CONFIG_STEREOWIDENINGTYPE = struct_OMX_AUDIO_CONFIG_STEREOWIDENINGTYPE # OMX_Audio.h: 921

OMX_AUDIO_CONFIG_CHORUSTYPE = struct_OMX_AUDIO_CONFIG_CHORUSTYPE # OMX_Audio.h: 932

OMX_AUDIO_CONFIG_REVERBERATIONTYPE = struct_OMX_AUDIO_CONFIG_REVERBERATIONTYPE # OMX_Audio.h: 950

OMX_AUDIO_CONFIG_ECHOCANCELATIONTYPE = struct_OMX_AUDIO_CONFIG_ECHOCANCELATIONTYPE # OMX_Audio.h: 967

OMX_AUDIO_CONFIG_NOISEREDUCTIONTYPE = struct_OMX_AUDIO_CONFIG_NOISEREDUCTIONTYPE # OMX_Audio.h: 974

OMX_AUDIO_CONFIG_3DOUTPUTTYPE = struct_OMX_AUDIO_CONFIG_3DOUTPUTTYPE # OMX_Audio.h: 987

OMX_AUDIO_CONFIG_3DLOCATIONTYPE = struct_OMX_AUDIO_CONFIG_3DLOCATIONTYPE # OMX_Audio.h: 996

OMX_AUDIO_PARAM_3DDOPPLERMODETYPE = struct_OMX_AUDIO_PARAM_3DDOPPLERMODETYPE # OMX_Audio.h: 1003

OMX_AUDIO_CONFIG_3DDOPPLERSETTINGSTYPE = struct_OMX_AUDIO_CONFIG_3DDOPPLERSETTINGSTYPE # OMX_Audio.h: 1012

OMX_AUDIO_CONFIG_3DLEVELSTYPE = struct_OMX_AUDIO_CONFIG_3DLEVELSTYPE # OMX_Audio.h: 1020

OMX_AUDIO_CONFIG_3DDISTANCEATTENUATIONTYPE = struct_OMX_AUDIO_CONFIG_3DDISTANCEATTENUATIONTYPE # OMX_Audio.h: 1038

OMX_AUDIO_CONFIG_3DDIRECTIVITYSETTINGSTYPE = struct_OMX_AUDIO_CONFIG_3DDIRECTIVITYSETTINGSTYPE # OMX_Audio.h: 1047

OMX_AUDIO_CONFIG_3DDIRECTIVITYORIENTATIONTYPE = struct_OMX_AUDIO_CONFIG_3DDIRECTIVITYORIENTATIONTYPE # OMX_Audio.h: 1056

OMX_AUDIO_CONFIG_3DMACROSCOPICORIENTATIONTYPE = struct_OMX_AUDIO_CONFIG_3DMACROSCOPICORIENTATIONTYPE # OMX_Audio.h: 1068

OMX_AUDIO_CONFIG_3DMACROSCOPICSIZETYPE = struct_OMX_AUDIO_CONFIG_3DMACROSCOPICSIZETYPE # OMX_Audio.h: 1077

OMX_AUDIO_PARAM_CHANNELMAPPINGTYPE = struct_OMX_AUDIO_PARAM_CHANNELMAPPINGTYPE # OMX_Audio.h: 1085

OMX_AUDIO_SBCBITPOOLTYPE = struct_OMX_AUDIO_SBCBITPOOLTYPE # OMX_Audio.h: 1092

OMX_AUDIO_AMRMODETYPE = struct_OMX_AUDIO_AMRMODETYPE # OMX_Audio.h: 1100

OMX_AUDIO_CONFIG_BITRATETYPE = struct_OMX_AUDIO_CONFIG_BITRATETYPE # OMX_Audio.h: 1107

OMX_AUDIO_CONFIG_AMRISFTYPE = struct_OMX_AUDIO_CONFIG_AMRISFTYPE # OMX_Audio.h: 1114

OMX_AUDIO_FIXEDPOINTTYPE = struct_OMX_AUDIO_FIXEDPOINTTYPE # OMX_Audio.h: 1124

OMX_CONFIG_COLORCONVERSIONTYPE = struct_OMX_CONFIG_COLORCONVERSIONTYPE # OMX_IVCommon.h: 120

OMX_CONFIG_SCALEFACTORTYPE = struct_OMX_CONFIG_SCALEFACTORTYPE # OMX_IVCommon.h: 128

OMX_CONFIG_IMAGEFILTERTYPE = struct_OMX_CONFIG_IMAGEFILTERTYPE # OMX_IVCommon.h: 163

OMX_CONFIG_COLORENHANCEMENTTYPE = struct_OMX_CONFIG_COLORENHANCEMENTTYPE # OMX_IVCommon.h: 172

OMX_CONFIG_COLORKEYTYPE = struct_OMX_CONFIG_COLORKEYTYPE # OMX_IVCommon.h: 180

OMX_CONFIG_COLORBLENDTYPE = struct_OMX_CONFIG_COLORBLENDTYPE # OMX_IVCommon.h: 201

OMX_FRAMESIZETYPE = struct_OMX_FRAMESIZETYPE # OMX_IVCommon.h: 209

OMX_CONFIG_ROTATIONTYPE = struct_OMX_CONFIG_ROTATIONTYPE # OMX_IVCommon.h: 216

OMX_CONFIG_MIRRORTYPE = struct_OMX_CONFIG_MIRRORTYPE # OMX_IVCommon.h: 233

OMX_CONFIG_POINTTYPE = struct_OMX_CONFIG_POINTTYPE # OMX_IVCommon.h: 241

OMX_CONFIG_RECTTYPE = struct_OMX_CONFIG_RECTTYPE # OMX_IVCommon.h: 251

OMX_PARAM_DEBLOCKINGTYPE = struct_OMX_PARAM_DEBLOCKINGTYPE # OMX_IVCommon.h: 258

OMX_CONFIG_FRAMESTABTYPE = struct_OMX_CONFIG_FRAMESTABTYPE # OMX_IVCommon.h: 265

OMX_CONFIG_WHITEBALCONTROLTYPE = struct_OMX_CONFIG_WHITEBALCONTROLTYPE # OMX_IVCommon.h: 288

OMX_CONFIG_EXPOSURECONTROLTYPE = struct_OMX_CONFIG_EXPOSURECONTROLTYPE # OMX_IVCommon.h: 311

OMX_PARAM_SENSORMODETYPE = struct_OMX_PARAM_SENSORMODETYPE # OMX_IVCommon.h: 320

OMX_CONFIG_CONTRASTTYPE = struct_OMX_CONFIG_CONTRASTTYPE # OMX_IVCommon.h: 327

OMX_CONFIG_BRIGHTNESSTYPE = struct_OMX_CONFIG_BRIGHTNESSTYPE # OMX_IVCommon.h: 334

OMX_CONFIG_BACKLIGHTTYPE = struct_OMX_CONFIG_BACKLIGHTTYPE # OMX_IVCommon.h: 342

OMX_CONFIG_GAMMATYPE = struct_OMX_CONFIG_GAMMATYPE # OMX_IVCommon.h: 349

OMX_CONFIG_SATURATIONTYPE = struct_OMX_CONFIG_SATURATIONTYPE # OMX_IVCommon.h: 356

OMX_CONFIG_LIGHTNESSTYPE = struct_OMX_CONFIG_LIGHTNESSTYPE # OMX_IVCommon.h: 363

OMX_CONFIG_PLANEBLENDTYPE = struct_OMX_CONFIG_PLANEBLENDTYPE # OMX_IVCommon.h: 371

OMX_PARAM_INTERLEAVETYPE = struct_OMX_PARAM_INTERLEAVETYPE # OMX_IVCommon.h: 379

OMX_CONFIG_TRANSITIONEFFECTTYPE = struct_OMX_CONFIG_TRANSITIONEFFECTTYPE # OMX_IVCommon.h: 399

OMX_PARAM_DATAUNITTYPE = struct_OMX_PARAM_DATAUNITTYPE # OMX_IVCommon.h: 426

OMX_CONFIG_DITHERTYPE = struct_OMX_CONFIG_DITHERTYPE # OMX_IVCommon.h: 443

OMX_CONFIG_CAPTUREMODETYPE = struct_OMX_CONFIG_CAPTUREMODETYPE # OMX_IVCommon.h: 452

OMX_CONFIG_EXPOSUREVALUETYPE = struct_OMX_CONFIG_EXPOSUREVALUETYPE # OMX_IVCommon.h: 475

OMX_SHARPNESSTYPE = struct_OMX_SHARPNESSTYPE # OMX_IVCommon.h: 493

OMX_CONFIG_ZOOMFACTORTYPE = struct_OMX_CONFIG_ZOOMFACTORTYPE # OMX_IVCommon.h: 500

OMX_IMAGE_CONFIG_LOCKTYPE = struct_OMX_IMAGE_CONFIG_LOCKTYPE # OMX_IVCommon.h: 516

OMX_CONFIG_FOCUSRANGETYPE = struct_OMX_CONFIG_FOCUSRANGETYPE # OMX_IVCommon.h: 535

OMX_IMAGE_CONFIG_FLASHSTATUSTYPE = struct_OMX_IMAGE_CONFIG_FLASHSTATUSTYPE # OMX_IVCommon.h: 554

OMX_CONFIG_EXTCAPTUREMODETYPE = struct_OMX_CONFIG_EXTCAPTUREMODETYPE # OMX_IVCommon.h: 562

OMX_CONFIG_NDFILTERCONTROLTYPE = struct_OMX_CONFIG_NDFILTERCONTROLTYPE # OMX_IVCommon.h: 577

OMX_CONFIG_AFASSISTANTLIGHTTYPE = struct_OMX_CONFIG_AFASSISTANTLIGHTTYPE # OMX_IVCommon.h: 592

OMX_INTERLACEFORMATTYPE = struct_OMX_INTERLACEFORMATTYPE # OMX_IVCommon.h: 608

OMX_DEINTERLACETYPE = struct_OMX_DEINTERLACETYPE # OMX_IVCommon.h: 615

OMX_STREAMINTERLACEFORMATTYPE = struct_OMX_STREAMINTERLACEFORMATTYPE # OMX_IVCommon.h: 623

OMX_FROITYPE = struct_OMX_FROITYPE # OMX_IVCommon.h: 632

OMX_CONFIG_FOCUSREGIONSTATUSTYPE = struct_OMX_CONFIG_FOCUSREGIONSTATUSTYPE # OMX_IVCommon.h: 641

OMX_MANUALFOCUSRECTTYPE = struct_OMX_MANUALFOCUSRECTTYPE # OMX_IVCommon.h: 658

OMX_CONFIG_FOCUSREGIONCONTROLTYPE = struct_OMX_CONFIG_FOCUSREGIONCONTROLTYPE # OMX_IVCommon.h: 666

OMX_VIDEO_PORTDEFINITIONTYPE = struct_OMX_VIDEO_PORTDEFINITIONTYPE # OMX_Video.h: 75

OMX_VIDEO_PARAM_PORTFORMATTYPE = struct_OMX_VIDEO_PARAM_PORTFORMATTYPE # OMX_Video.h: 85

OMX_VIDEO_PARAM_QUANTIZATIONTYPE = struct_OMX_VIDEO_PARAM_QUANTIZATIONTYPE # OMX_Video.h: 94

OMX_VIDEO_PARAM_VIDEOFASTUPDATETYPE = struct_OMX_VIDEO_PARAM_VIDEOFASTUPDATETYPE # OMX_Video.h: 104

OMX_VIDEO_PARAM_BITRATETYPE = struct_OMX_VIDEO_PARAM_BITRATETYPE # OMX_Video.h: 123

OMX_VIDEO_PARAM_MOTIONVECTORTYPE = struct_OMX_VIDEO_PARAM_MOTIONVECTORTYPE # OMX_Video.h: 144

OMX_VIDEO_PARAM_INTRAREFRESHTYPE = struct_OMX_VIDEO_PARAM_INTRAREFRESHTYPE # OMX_Video.h: 163

OMX_VIDEO_PARAM_ERRORCORRECTIONTYPE = struct_OMX_VIDEO_PARAM_ERRORCORRECTIONTYPE # OMX_Video.h: 174

OMX_VIDEO_PARAM_VBSMCTYPE = struct_OMX_VIDEO_PARAM_VBSMCTYPE # OMX_Video.h: 187

OMX_VIDEO_PARAM_H263TYPE = struct_OMX_VIDEO_PARAM_H263TYPE # OMX_Video.h: 245

OMX_VIDEO_PARAM_MPEG2TYPE = struct_OMX_VIDEO_PARAM_MPEG2TYPE # OMX_Video.h: 279

OMX_VIDEO_PARAM_MPEG4TYPE = struct_OMX_VIDEO_PARAM_MPEG4TYPE # OMX_Video.h: 337

OMX_VIDEO_PARAM_WMVTYPE = struct_OMX_VIDEO_PARAM_WMVTYPE # OMX_Video.h: 378

OMX_VIDEO_PARAM_RVTYPE = struct_OMX_VIDEO_PARAM_RVTYPE # OMX_Video.h: 406

OMX_VIDEO_PARAM_AVCTYPE = struct_OMX_VIDEO_PARAM_AVCTYPE # OMX_Video.h: 482

OMX_VIDEO_PARAM_VP8TYPE = struct_OMX_VIDEO_PARAM_VP8TYPE # OMX_Video.h: 512

OMX_VIDEO_VP8REFERENCEFRAMETYPE = struct_OMX_VIDEO_VP8REFERENCEFRAMETYPE # OMX_Video.h: 524

OMX_VIDEO_VP8REFERENCEFRAMEINFOTYPE = struct_OMX_VIDEO_VP8REFERENCEFRAMEINFOTYPE # OMX_Video.h: 532

OMX_VIDEO_PARAM_PROFILELEVELTYPE = struct_OMX_VIDEO_PARAM_PROFILELEVELTYPE # OMX_Video.h: 542

OMX_VIDEO_CONFIG_BITRATETYPE = struct_OMX_VIDEO_CONFIG_BITRATETYPE # OMX_Video.h: 549

OMX_CONFIG_FRAMERATETYPE = struct_OMX_CONFIG_FRAMERATETYPE # OMX_Video.h: 556

OMX_CONFIG_INTRAREFRESHVOPTYPE = struct_OMX_CONFIG_INTRAREFRESHVOPTYPE # OMX_Video.h: 563

OMX_CONFIG_MACROBLOCKERRORMAPTYPE = struct_OMX_CONFIG_MACROBLOCKERRORMAPTYPE # OMX_Video.h: 571

OMX_CONFIG_MBERRORREPORTINGTYPE = struct_OMX_CONFIG_MBERRORREPORTINGTYPE # OMX_Video.h: 578

OMX_PARAM_MACROBLOCKSTYPE = struct_OMX_PARAM_MACROBLOCKSTYPE # OMX_Video.h: 585

OMX_VIDEO_PARAM_AVCSLICEFMO = struct_OMX_VIDEO_PARAM_AVCSLICEFMO # OMX_Video.h: 603

OMX_VIDEO_CONFIG_AVCINTRAPERIOD = struct_OMX_VIDEO_CONFIG_AVCINTRAPERIOD # OMX_Video.h: 611

OMX_VIDEO_CONFIG_NALSIZE = struct_OMX_VIDEO_CONFIG_NALSIZE # OMX_Video.h: 618

OMX_NALSTREAMFORMATTYPE = struct_OMX_NALSTREAMFORMATTYPE # OMX_Video.h: 636

OMX_VIDEO_PARAM_VC1TYPE = struct_OMX_VIDEO_PARAM_VC1TYPE # OMX_Video.h: 671

OMX_VIDEO_INTRAPERIODTYPE = struct_OMX_VIDEO_INTRAPERIODTYPE # OMX_Video.h: 680

OMX_IMAGE_PORTDEFINITIONTYPE = struct_OMX_IMAGE_PORTDEFINITIONTYPE # OMX_Image.h: 73

OMX_IMAGE_PARAM_PORTFORMATTYPE = struct_OMX_IMAGE_PARAM_PORTFORMATTYPE # OMX_Image.h: 82

OMX_IMAGE_PARAM_FLASHCONTROLTYPE = struct_OMX_IMAGE_PARAM_FLASHCONTROLTYPE # OMX_Image.h: 101

OMX_IMAGE_CONFIG_FOCUSCONTROLTYPE = struct_OMX_IMAGE_CONFIG_FOCUSCONTROLTYPE # OMX_Image.h: 120

OMX_IMAGE_PARAM_QFACTORTYPE = struct_OMX_IMAGE_PARAM_QFACTORTYPE # OMX_Image.h: 127

OMX_IMAGE_PARAM_QUANTIZATIONTABLETYPE = struct_OMX_IMAGE_PARAM_QUANTIZATIONTABLETYPE # OMX_Image.h: 145

OMX_IMAGE_PARAM_HUFFMANTTABLETYPE = struct_OMX_IMAGE_PARAM_HUFFMANTTABLETYPE # OMX_Image.h: 166

OMX_CONFIG_FLICKERREJECTIONTYPE = struct_OMX_CONFIG_FLICKERREJECTIONTYPE # OMX_Image.h: 183

OMX_IMAGE_HISTOGRAMTYPE = struct_OMX_IMAGE_HISTOGRAMTYPE # OMX_Image.h: 201

OMX_IMAGE_HISTOGRAMDATATYPE = struct_OMX_IMAGE_HISTOGRAMDATATYPE # OMX_Image.h: 210

OMX_IMAGE_HISTOGRAMINFOTYPE = struct_OMX_IMAGE_HISTOGRAMINFOTYPE # OMX_Image.h: 219

OMX_TIME_CONFIG_SEEKMODETYPE = struct_OMX_TIME_CONFIG_SEEKMODETYPE # OMX_Other.h: 70

OMX_TIME_CONFIG_TIMESTAMPTYPE = struct_OMX_TIME_CONFIG_TIMESTAMPTYPE # OMX_Other.h: 77

OMX_TIME_CONFIG_MEDIATIMEREQUESTTYPE = struct_OMX_TIME_CONFIG_MEDIATIMEREQUESTTYPE # OMX_Other.h: 113

OMX_TIME_MEDIATIMETYPE = struct_OMX_TIME_MEDIATIMETYPE # OMX_Other.h: 125

OMX_TIME_CONFIG_SCALETYPE = struct_OMX_TIME_CONFIG_SCALETYPE # OMX_Other.h: 131

OMX_TIME_CONFIG_CLOCKSTATETYPE = struct_OMX_TIME_CONFIG_CLOCKSTATETYPE # OMX_Other.h: 149

OMX_OTHER_CONFIG_POWERTYPE = struct_OMX_OTHER_CONFIG_POWERTYPE # OMX_Other.h: 155

OMX_OTHER_CONFIG_STATSTYPE = struct_OMX_OTHER_CONFIG_STATSTYPE # OMX_Other.h: 161

OMX_OTHER_PORTDEFINITIONTYPE = struct_OMX_OTHER_PORTDEFINITIONTYPE # OMX_Other.h: 165

OMX_OTHER_PARAM_PORTFORMATTYPE = struct_OMX_OTHER_PARAM_PORTFORMATTYPE # OMX_Other.h: 173

OMX_TIME_CONFIG_ACTIVEREFCLOCKUPDATETYPE = struct_OMX_TIME_CONFIG_ACTIVEREFCLOCKUPDATETYPE # OMX_Other.h: 180

OMX_TIME_CONFIG_RENDERINGDELAYTYPE = struct_OMX_TIME_CONFIG_RENDERINGDELAYTYPE # OMX_Other.h: 187

OMX_PARAM_PORTDEFINITIONTYPE = struct_OMX_PARAM_PORTDEFINITIONTYPE # OMX_Component.h: 79

OMX_PARAM_U32TYPE = struct_OMX_PARAM_U32TYPE # OMX_Component.h: 86

OMX_PARAM_SUSPENSIONPOLICYTYPE = struct_OMX_PARAM_SUSPENSIONPOLICYTYPE # OMX_Component.h: 100

OMX_PARAM_SUSPENSIONTYPE = struct_OMX_PARAM_SUSPENSIONTYPE # OMX_Component.h: 114

OMX_CONFIG_BOOLEANTYPE = struct_OMX_CONFIG_BOOLEANTYPE # OMX_Component.h: 120

OMX_PARAM_CONTENTURITYPE = struct_OMX_PARAM_CONTENTURITYPE # OMX_Component.h: 126

OMX_RESOURCECONCEALMENTTYPE = struct_OMX_RESOURCECONCEALMENTTYPE # OMX_Component.h: 132

OMX_CONFIG_METADATAITEMCOUNTTYPE = struct_OMX_CONFIG_METADATAITEMCOUNTTYPE # OMX_Component.h: 202

OMX_CONFIG_METADATAITEMTYPE = struct_OMX_CONFIG_METADATAITEMTYPE # OMX_Component.h: 220

OMX_CONFIG_CONTAINERNODECOUNTTYPE = struct_OMX_CONFIG_CONTAINERNODECOUNTTYPE # OMX_Component.h: 229

OMX_CONFIG_CONTAINERNODEIDTYPE = struct_OMX_CONFIG_CONTAINERNODEIDTYPE # OMX_Component.h: 241

OMX_PARAM_METADATAFILTERTYPE = struct_OMX_PARAM_METADATAFILTERTYPE # OMX_Component.h: 254

OMX_COMPONENTTYPE = struct_OMX_COMPONENTTYPE # OMX_Component.h: 360

OMX_CONFIG_COMMITMODETYPE = struct_OMX_CONFIG_COMMITMODETYPE # OMX_Component.h: 366

OMX_CONFIG_COMMITTYPE = struct_OMX_CONFIG_COMMITTYPE # OMX_Component.h: 371

OMX_MEDIACONTAINER_INFOTYPE = struct_OMX_MEDIACONTAINER_INFOTYPE # OMX_Component.h: 417

OMX_CONFIG_TUNNELEDPORTSTATUSTYPE = struct_OMX_CONFIG_TUNNELEDPORTSTATUSTYPE # OMX_Component.h: 427

OMX_CONFIG_PORTBOOLEANTYPE = struct_OMX_CONFIG_PORTBOOLEANTYPE # OMX_Component.h: 434

def get_il_enum_from_string(string):
    from skema import omxil12
    for name, val in omxil12.__dict__.iteritems():
        if name == string:
            return val
    raise AttributeError

def get_string_from_il_enum(enum, hint):
    from skema import omxil12
    for name, val in omxil12.__dict__.iteritems():
        if enum == val:
            if name.startswith(hint):
                return name
    raise AttributeError

__all_indexes__ = dict([
('OMX_IndexParamPriorityMgmt',             OMX_PRIORITYMGMTTYPE),
('OMX_IndexParamAudioInit',                OMX_PORT_PARAM_TYPE),
('OMX_IndexParamImageInit',                OMX_PORT_PARAM_TYPE),
('OMX_IndexParamVideoInit',                OMX_PORT_PARAM_TYPE),
('OMX_IndexParamOtherInit',                OMX_PORT_PARAM_TYPE),
('OMX_IndexParamNumAvailableStreams',      OMX_PARAM_U32TYPE),
('OMX_IndexParamActiveStream',             OMX_PARAM_U32TYPE),
('OMX_IndexParamSuspensionPolicy',         OMX_PARAM_SUSPENSIONPOLICYTYPE),
('OMX_IndexParamComponentSuspended',       OMX_PARAM_SUSPENSIONTYPE),
('OMX_IndexConfigCapturing',               OMX_CONFIG_BOOLEANTYPE),
('OMX_IndexConfigCaptureMode',             OMX_CONFIG_CAPTUREMODETYPE),
('OMX_IndexAutoPauseAfterCapture',         OMX_CONFIG_BOOLEANTYPE),
('OMX_IndexParamContentURI',               OMX_PARAM_CONTENTURITYPE),
('OMX_IndexParamDisableResourceConcealment', OMX_RESOURCECONCEALMENTTYPE),
('OMX_IndexConfigMetadataItemCount',       OMX_CONFIG_METADATAITEMCOUNTTYPE),
('OMX_IndexConfigContainerNodeCount',      OMX_CONFIG_CONTAINERNODECOUNTTYPE),
('OMX_IndexConfigMetadataItem',            OMX_CONFIG_METADATAITEMTYPE),
('OMX_IndexConfigCounterNodeID',           OMX_CONFIG_CONTAINERNODEIDTYPE),
('OMX_IndexParamMetadataFilterType',       OMX_PARAM_METADATAFILTERTYPE),
('OMX_IndexParamMetadataKeyFilter',        OMX_PARAM_METADATAFILTERTYPE),
('OMX_IndexConfigPriorityMgmt',            OMX_PRIORITYMGMTTYPE),
('OMX_IndexParamStandardComponentRole',    OMX_PARAM_COMPONENTROLETYPE),
('OMX_IndexConfigContentURI',              OMX_PARAM_CONTENTURITYPE),
('OMX_IndexConfigCommonCapturing',         OMX_CONFIG_PORTBOOLEANTYPE),
('OMX_IndexConfigCommonPortCapturing',     OMX_CONFIG_PORTBOOLEANTYPE),
('OMX_IndexConfigTunneledPortStatus',      OMX_CONFIG_TUNNELEDPORTSTATUSTYPE),
('OMX_IndexParamPortDefinition',           OMX_PARAM_PORTDEFINITIONTYPE),
('OMX_IndexParamCompBufferSupplier',       OMX_PARAM_BUFFERSUPPLIERTYPE),
('OMX_IndexParamAudioPortFormat',          OMX_AUDIO_PARAM_PORTFORMATTYPE),
('OMX_IndexParamAudioPcm',                 OMX_AUDIO_PARAM_PCMMODETYPE),
('OMX_IndexParamAudioAac',                 OMX_AUDIO_PARAM_AACPROFILETYPE),
('OMX_IndexParamAudioRa',                  OMX_AUDIO_PARAM_RATYPE),
('OMX_IndexParamAudioMp3',                 OMX_AUDIO_PARAM_MP3TYPE),
('OMX_IndexParamAudioAdpcm',               OMX_AUDIO_PARAM_ADPCMTYPE),
('OMX_IndexParamAudioG723',                OMX_AUDIO_PARAM_G723TYPE),
('OMX_IndexParamAudioG729',                OMX_AUDIO_PARAM_G729TYPE),
('OMX_IndexParamAudioAmr',                 OMX_AUDIO_PARAM_AMRTYPE),
('OMX_IndexParamAudioWma',                 OMX_AUDIO_PARAM_WMATYPE),
('OMX_IndexParamAudioSbc',                 OMX_AUDIO_PARAM_SBCTYPE),
('OMX_IndexParamAudioMidi',                OMX_AUDIO_PARAM_MIDITYPE),
('OMX_IndexParamAudioGsm_FR',              OMX_AUDIO_PARAM_GSMFRTYPE),
('OMX_IndexParamAudioMidiLoadUserSound',   OMX_AUDIO_PARAM_MIDILOADUSERSOUNDTYPE),
('OMX_IndexParamAudioG726',                OMX_AUDIO_PARAM_G726TYPE),
('OMX_IndexParamAudioGsm_EFR',             OMX_AUDIO_PARAM_GSMEFRTYPE),
('OMX_IndexParamAudioGsm_HR',              OMX_AUDIO_PARAM_GSMHRTYPE),
('OMX_IndexParamAudioPdc_FR',              OMX_AUDIO_PARAM_PDCFRTYPE),
('OMX_IndexParamAudioPdc_EFR',             OMX_AUDIO_PARAM_PDCEFRTYPE),
('OMX_IndexParamAudioPdc_HR',              OMX_AUDIO_PARAM_PDCHRTYPE),
('OMX_IndexParamAudioTdma_FR',             OMX_AUDIO_PARAM_TDMAFRTYPE),
('OMX_IndexParamAudioTdma_EFR',            OMX_AUDIO_PARAM_TDMAEFRTYPE),
('OMX_IndexParamAudioQcelp8',              OMX_AUDIO_PARAM_QCELP8TYPE),
('OMX_IndexParamAudioQcelp13',             OMX_AUDIO_PARAM_QCELP13TYPE),
('OMX_IndexParamAudioEvrc',                OMX_AUDIO_PARAM_EVRCTYPE),
('OMX_IndexParamAudioSmv',                 OMX_AUDIO_PARAM_SMVTYPE),
('OMX_IndexParamAudioVorbis',              OMX_AUDIO_PARAM_VORBISTYPE),
('OMX_IndexConfigAudioMidiImmediateEvent', OMX_AUDIO_CONFIG_MIDIIMMEDIATEEVENTTYPE),
('OMX_IndexConfigAudioMidiControl',        OMX_AUDIO_CONFIG_MIDICONTROLTYPE),
('OMX_IndexConfigAudioMidiSoundBankProgram', OMX_AUDIO_CONFIG_MIDISOUNDBANKPROGRAMTYPE),
('OMX_IndexConfigAudioMidiStatus',         OMX_AUDIO_CONFIG_MIDISTATUSTYPE),
('OMX_IndexConfigAudioMidiMetaEvent',      OMX_AUDIO_CONFIG_MIDIMETAEVENTTYPE),
('OMX_IndexConfigAudioMidiMetaEventData',  OMX_AUDIO_CONFIG_MIDIMETAEVENTDATATYPE),
('OMX_IndexConfigAudioVolume',             OMX_AUDIO_CONFIG_VOLUMETYPE),
('OMX_IndexConfigAudioBalance',            OMX_AUDIO_CONFIG_BALANCETYPE),
('OMX_IndexConfigAudioChannelMute',        OMX_AUDIO_CONFIG_CHANNELMUTETYPE),
('OMX_IndexConfigAudioMute',               OMX_AUDIO_CONFIG_MUTETYPE),
('OMX_IndexConfigAudioLoudness',           OMX_AUDIO_CONFIG_LOUDNESSTYPE),
('OMX_IndexConfigAudioEchoCancelation',    OMX_AUDIO_CONFIG_ECHOCANCELATIONTYPE),
('OMX_IndexConfigAudioNoiseReduction',     OMX_AUDIO_CONFIG_NOISEREDUCTIONTYPE),
('OMX_IndexConfigAudioBass',               OMX_AUDIO_CONFIG_BASSTYPE),
('OMX_IndexConfigAudioTreble',             OMX_AUDIO_CONFIG_TREBLETYPE),
('OMX_IndexConfigAudioStereoWidening',     OMX_AUDIO_CONFIG_STEREOWIDENINGTYPE),
('OMX_IndexConfigAudioChorus',             OMX_AUDIO_CONFIG_CHORUSTYPE),
('OMX_IndexConfigAudioEqualizer',          OMX_AUDIO_CONFIG_EQUALIZERTYPE),
('OMX_IndexConfigAudioReverberation',      OMX_AUDIO_CONFIG_REVERBERATIONTYPE),
('OMX_IndexConfigAudioChannelVolume',      OMX_AUDIO_CONFIG_CHANNELVOLUMETYPE),
('OMX_IndexConfigAudio3DOutput',           OMX_AUDIO_CONFIG_3DOUTPUTTYPE),
('OMX_IndexConfigAudio3DLocation',         OMX_AUDIO_CONFIG_3DLOCATIONTYPE),
('OMX_IndexParamAudio3DDopplerMode',       OMX_AUDIO_PARAM_3DDOPPLERMODETYPE),
('OMX_IndexConfigAudio3DDopplerSettings',  OMX_AUDIO_CONFIG_3DDOPPLERSETTINGSTYPE),
('OMX_IndexConfigAudio3DLevels',           OMX_AUDIO_CONFIG_3DLEVELSTYPE),
('OMX_IndexConfigAudio3DDistanceAttenuation',    OMX_AUDIO_CONFIG_3DDISTANCEATTENUATIONTYPE),
('OMX_IndexConfigAudio3DDirectivitySettings',    OMX_AUDIO_CONFIG_3DDIRECTIVITYSETTINGSTYPE),
('OMX_IndexConfigAudio3DDirectivityOrientation', OMX_AUDIO_CONFIG_3DDIRECTIVITYORIENTATIONTYPE),
('OMX_IndexConfigAudio3DMacroscopicOrientation', OMX_AUDIO_CONFIG_3DMACROSCOPICORIENTATIONTYPE),
('OMX_IndexConfigAudio3DMacroscopicSize',  OMX_AUDIO_CONFIG_3DMACROSCOPICSIZETYPE),
('OMX_IndexParamAudioQueryChannelMapping', OMX_AUDIO_PARAM_CHANNELMAPPINGTYPE),
('OMX_IndexConfigAudioSbcBitpool',         OMX_AUDIO_SBCBITPOOLTYPE),
('OMX_IndexConfigAudioAmrMode',            OMX_AUDIO_AMRMODETYPE),
('OMX_IndexConfigAudioBitrate',            OMX_AUDIO_CONFIG_BITRATETYPE),
('OMX_IndexParamImagePortFormat',          OMX_IMAGE_PARAM_PORTFORMATTYPE),
('OMX_IndexParamFlashControl',             OMX_IMAGE_PARAM_FLASHCONTROLTYPE),
('OMX_IndexConfigFocusControl',            OMX_IMAGE_CONFIG_FOCUSCONTROLTYPE),
('OMX_IndexParamQFactor',                  OMX_IMAGE_PARAM_QFACTORTYPE),
('OMX_IndexParamQuantizationTable',        OMX_IMAGE_PARAM_QUANTIZATIONTABLETYPE),
('OMX_IndexParamHuffmanTable',             OMX_IMAGE_PARAM_HUFFMANTTABLETYPE),
('OMX_IndexConfigFlashControl',            OMX_IMAGE_PARAM_FLASHCONTROLTYPE),
('OMX_IndexConfigFlickerRejection',        OMX_CONFIG_FLICKERREJECTIONTYPE),
('OMX_IndexConfigImageHistogram',          OMX_IMAGE_HISTOGRAMTYPE),
('OMX_IndexConfigImageHistogramData',      OMX_IMAGE_HISTOGRAMDATATYPE),
('OMX_IndexConfigImageHistogramInfo',      OMX_IMAGE_HISTOGRAMINFOTYPE),
('OMX_IndexConfigImageCaptureStarted',     OMX_PARAM_U32TYPE),
('OMX_IndexConfigImageCaptureEnded',       OMX_PARAM_U32TYPE),
('OMX_IndexParamVideoPortFormat',          OMX_VIDEO_PARAM_PORTFORMATTYPE),
('OMX_IndexParamVideoQuantization',        OMX_VIDEO_PARAM_QUANTIZATIONTYPE),
('OMX_IndexParamVideoFastUpdate',          OMX_VIDEO_PARAM_VIDEOFASTUPDATETYPE),
('OMX_IndexParamVideoBitrate',             OMX_VIDEO_PARAM_BITRATETYPE),
('OMX_IndexParamVideoMotionVector',        OMX_VIDEO_PARAM_MOTIONVECTORTYPE),
('OMX_IndexParamVideoIntraRefresh',        OMX_VIDEO_PARAM_INTRAREFRESHTYPE),
('OMX_IndexParamVideoErrorCorrection',     OMX_VIDEO_PARAM_ERRORCORRECTIONTYPE),
('OMX_IndexParamVideoVBSMC',               OMX_VIDEO_PARAM_VBSMCTYPE),
('OMX_IndexParamVideoMpeg2',               OMX_VIDEO_PARAM_MPEG2TYPE),
('OMX_IndexParamVideoMpeg4',               OMX_VIDEO_PARAM_MPEG4TYPE),
('OMX_IndexParamVideoWmv',                 OMX_VIDEO_PARAM_WMVTYPE),
('OMX_IndexParamVideoRv',                  OMX_VIDEO_PARAM_RVTYPE),
('OMX_IndexParamVideoAvc',                 OMX_VIDEO_PARAM_AVCTYPE),
('OMX_IndexParamVideoH263',                OMX_VIDEO_PARAM_H263TYPE),
('OMX_IndexParamVideoProfileLevelQuerySupported', OMX_VIDEO_PARAM_PROFILELEVELTYPE),
('OMX_IndexParamVideoProfileLevelCurrent', OMX_VIDEO_PARAM_PROFILELEVELTYPE),
('OMX_IndexConfigVideoBitrate',            OMX_VIDEO_CONFIG_BITRATETYPE),
('OMX_IndexConfigVideoFramerate',          OMX_CONFIG_FRAMERATETYPE),
('OMX_IndexConfigVideoIntraVOPRefresh',    OMX_CONFIG_INTRAREFRESHVOPTYPE),
('OMX_IndexConfigVideoIntraMBRefresh',     OMX_CONFIG_MACROBLOCKERRORMAPTYPE),
('OMX_IndexConfigVideoMBErrorReporting',   OMX_CONFIG_MBERRORREPORTINGTYPE),
('OMX_IndexParamVideoMacroblocksPerFrame', OMX_PARAM_MACROBLOCKSTYPE),
('OMX_IndexConfigVideoMacroBlockErrorMap', OMX_CONFIG_MACROBLOCKERRORMAPTYPE),
('OMX_IndexParamVideoSliceFMO',            OMX_VIDEO_PARAM_AVCSLICEFMO),
('OMX_IndexConfigVideoAVCIntraPeriod',     OMX_VIDEO_CONFIG_AVCINTRAPERIOD),
('OMX_IndexConfigVideoNalSize',            OMX_VIDEO_CONFIG_NALSIZE),
('OMX_IndexParamNalStreamFormatSupported', OMX_NALSTREAMFORMATTYPE),
('OMX_IndexParamNalStreamFormat',          OMX_NALSTREAMFORMATTYPE),
('OMX_IndexParamNalStreamFormatSelect',    OMX_NALSTREAMFORMATTYPE),
('OMX_IndexParamVideoVC1',                 OMX_VIDEO_PARAM_VC1TYPE),
('OMX_IndexConfigVideoIntraPeriod',        OMX_VIDEO_INTRAPERIODTYPE),
('OMX_IndexConfigVideoIntraRefresh',       OMX_VIDEO_PARAM_INTRAREFRESHTYPE),
('OMX_IndexParamCommonDeblocking',         OMX_PARAM_DEBLOCKINGTYPE),
('OMX_IndexParamCommonSensorMode',         OMX_PARAM_SENSORMODETYPE),
('OMX_IndexParamCommonInterleave',         OMX_PARAM_INTERLEAVETYPE),
('OMX_IndexConfigCommonColorFormatConversion', OMX_CONFIG_COLORCONVERSIONTYPE),
('OMX_IndexConfigCommonScale',             OMX_CONFIG_SCALEFACTORTYPE),
('OMX_IndexConfigCommonImageFilter',       OMX_CONFIG_IMAGEFILTERTYPE),
('OMX_IndexConfigCommonColorEnhancement',  OMX_CONFIG_COLORENHANCEMENTTYPE),
('OMX_IndexConfigCommonColorKey',          OMX_CONFIG_COLORKEYTYPE),
('OMX_IndexConfigCommonColorBlend',        OMX_CONFIG_COLORBLENDTYPE),
('OMX_IndexConfigCommonFrameStabilisation',OMX_CONFIG_FRAMESTABTYPE),
('OMX_IndexConfigCommonRotate',            OMX_CONFIG_ROTATIONTYPE),
('OMX_IndexConfigCommonMirror',            OMX_CONFIG_MIRRORTYPE),
('OMX_IndexConfigCommonOutputPosition',    OMX_CONFIG_POINTTYPE),
('OMX_IndexConfigCommonInputCrop',         OMX_CONFIG_RECTTYPE),
('OMX_IndexConfigCommonOutputCrop',        OMX_CONFIG_RECTTYPE),
('OMX_IndexConfigCommonDigitalZoom',       OMX_CONFIG_SCALEFACTORTYPE),
('OMX_IndexConfigCommonOpticalZoom',       OMX_CONFIG_SCALEFACTORTYPE),
('OMX_IndexConfigCommonWhiteBalance',      OMX_CONFIG_WHITEBALCONTROLTYPE),
('OMX_IndexConfigCommonExposure',          OMX_CONFIG_EXPOSURECONTROLTYPE),
('OMX_IndexConfigCommonContrast',          OMX_CONFIG_CONTRASTTYPE),
('OMX_IndexConfigCommonBrightness',        OMX_CONFIG_BRIGHTNESSTYPE),
('OMX_IndexConfigCommonBacklight',         OMX_CONFIG_BACKLIGHTTYPE),
('OMX_IndexConfigCommonGamma',             OMX_CONFIG_GAMMATYPE),
('OMX_IndexConfigCommonSaturation',        OMX_CONFIG_SATURATIONTYPE),
('OMX_IndexConfigCommonLightness',         OMX_CONFIG_LIGHTNESSTYPE),
('OMX_IndexConfigCommonExclusionRect',     OMX_CONFIG_RECTTYPE),
('OMX_IndexConfigCommonDithering',         OMX_CONFIG_DITHERTYPE),
('OMX_IndexConfigCommonPlaneBlend',        OMX_CONFIG_PLANEBLENDTYPE),
('OMX_IndexConfigCommonExposureValue',     OMX_CONFIG_EXPOSUREVALUETYPE),
('OMX_IndexConfigCommonOutputSize',        OMX_FRAMESIZETYPE),
('OMX_IndexParamCommonExtraQuantData',     OMX_OTHER_EXTRADATATYPE),
('OMX_IndexConfigCommonTransitionEffect',  OMX_CONFIG_TRANSITIONEFFECTTYPE),
('OMX_IndexConfigSharpness',               OMX_SHARPNESSTYPE),
('OMX_IndexConfigCommonExtDigitalZoom',    OMX_CONFIG_ZOOMFACTORTYPE),
('OMX_IndexConfigCommonExtOpticalZoom',    OMX_CONFIG_ZOOMFACTORTYPE),
('OMX_IndexConfigCommonCenterFieldOfView', OMX_CONFIG_POINTTYPE),
('OMX_IndexConfigImageExposureLock',       OMX_IMAGE_CONFIG_LOCKTYPE),
('OMX_IndexConfigImageWhiteBalanceLock',   OMX_IMAGE_CONFIG_LOCKTYPE),
('OMX_IndexConfigImageFocusLock',          OMX_IMAGE_CONFIG_LOCKTYPE),
('OMX_IndexConfigCommonFocusRange',        OMX_CONFIG_FOCUSRANGETYPE),
('OMX_IndexConfigImageFlashStatus',        OMX_IMAGE_CONFIG_FLASHSTATUSTYPE),
('OMX_IndexConfigCommonExtCaptureMode',    OMX_CONFIG_EXTCAPTUREMODETYPE),
('OMX_IndexConfigCommonNDFilterControl',   OMX_CONFIG_NDFILTERCONTROLTYPE),
('OMX_IndexConfigCommonAFAssistantLight',  OMX_CONFIG_AFASSISTANTLIGHTTYPE),
('OMX_IndexConfigCommonFocusRegionStatus', OMX_CONFIG_FOCUSREGIONSTATUSTYPE),
('OMX_IndexConfigCommonFocusRegionControl',OMX_CONFIG_FOCUSREGIONCONTROLTYPE),
('OMX_IndexParamInterlaceFormat',          OMX_INTERLACEFORMATTYPE),
('OMX_IndexConfigDeInterlace',             OMX_DEINTERLACETYPE),
('OMX_IndexConfigStreamInterlaceFormats',  OMX_STREAMINTERLACEFORMATTYPE),
('OMX_IndexParamOtherPortFormat',          OMX_OTHER_PARAM_PORTFORMATTYPE),
('OMX_IndexConfigOtherPower',              OMX_OTHER_CONFIG_POWERTYPE),
('OMX_IndexConfigOtherStats',              OMX_OTHER_CONFIG_STATSTYPE),
('OMX_IndexConfigTimeScale',               OMX_TIME_CONFIG_SCALETYPE),
('OMX_IndexConfigTimeClockState',          OMX_TIME_CONFIG_CLOCKSTATETYPE),
('OMX_IndexConfigTimeCurrentMediaTime',    OMX_TIME_CONFIG_TIMESTAMPTYPE),
('OMX_IndexConfigTimeCurrentWallTime',     OMX_TIME_CONFIG_TIMESTAMPTYPE),
('OMX_IndexConfigTimeMediaTimeRequest',    OMX_TIME_CONFIG_MEDIATIMEREQUESTTYPE),
('OMX_IndexConfigTimeClientStartTime',     OMX_TIME_CONFIG_TIMESTAMPTYPE),
('OMX_IndexConfigTimePosition',            OMX_TIME_CONFIG_TIMESTAMPTYPE),
('OMX_IndexConfigTimeSeekMode',            OMX_TIME_CONFIG_SEEKMODETYPE),
('OMX_IndexConfigTimeCurrentReference',    OMX_TIME_CONFIG_TIMESTAMPTYPE),
('OMX_IndexConfigTimeActiveRefClockUpdate',OMX_TIME_CONFIG_ACTIVEREFCLOCKUPDATETYPE),
('OMX_IndexConfigTimeUpdate',              OMX_TIME_MEDIATIMETYPE),
('OMX_IndexConfigCommitMode',              OMX_CONFIG_COMMITMODETYPE),
('OMX_IndexConfigCommit',                  OMX_CONFIG_COMMITTYPE),
('OMX_IndexConfigCallbackRequest',         OMX_CONFIG_CALLBACKREQUESTTYPE),
('OMX_IndexParamMediaContainer',           OMX_MEDIACONTAINER_INFOTYPE),
])

# No inserted files

