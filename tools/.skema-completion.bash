_skema()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # The basic skema commands to complete
    opts=" list_installed_suites list_installed_tags help list_suites
    uninstall_tag version install_suite run_suite list_tags uninstall_suite
    install_tag"

    #
    #  Complete the arguments to some of the basic commands.
    #
    case "${prev}" in
        run_suite)
            local suites=$(for x in `./skema list_installed_suites`; do echo ${x} ; done )
            COMPREPLY=( $(compgen -W "${suites}" -- ${cur}) )
            return 0
            ;;

        install_suite)
            local suites=$(for x in `./skema list_suites`; do echo ${x} ; done )
            COMPREPLY=( $(compgen -W "${suites}" -- ${cur}) )
            return 0
            ;;

        uninstall_suite)
            local suites=$(for x in `./skema list_installed_suites`; do echo ${x} ; done )
            COMPREPLY=( $(compgen -W "${suites}" -- ${cur}) )
            return 0
            ;;

        install_tag)
            local tags=$(for x in `./skema list_tags`; do echo ${x} ; done )
            COMPREPLY=( $(compgen -W "${tags}" -- ${cur}) )
            return 0
            ;;

        uninstall_tag)
            local tags=$(for x in `./skema list_installed_tags`; do echo ${x} ; done )
            COMPREPLY=( $(compgen -W "${tags}" -- ${cur}) )
            return 0
            ;;
        *)
        ;;
    esac

    if [[ ${cur} == * ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi
}
complete -F _skema skema
