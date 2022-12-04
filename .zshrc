# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000

####################################
############# Vi mode ##############
####################################
bindkey -v

# Remove mode switching delay.
    KEYTIMEOUT=5

    # Change cursor shape for different vi modes.
    function zle-keymap-select {
      if [[ ${KEYMAP} == vicmd ]] ||
         [[ $1 = 'block' ]]; then
        echo -ne '\e[1 q'

      elif [[ ${KEYMAP} == main ]] ||
           [[ ${KEYMAP} == viins ]] ||
           [[ ${KEYMAP} = '' ]] ||
           [[ $1 = 'line' ]]; then
        echo -ne '\e[5 q'
      fi
    }
    zle -N zle-keymap-select

    # Use beam shape cursor on startup.
    echo -ne '\e[5 q'

    # Use beam shape cursor for each new prompt.
    preexec() {
       echo -ne '\e[5 q'
    }

####################################

# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/faust/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

####################################
############### GIT ################
####################################

autoload -Uz vcs_info
precmd_vcs_info() { vcs_info }
precmd_functions+=( precmd_vcs_info )
setopt prompt_subst
RPROMPT='${vcs_info_msg_0_}'
# PROMPT='${vcs_info_msg_0_}%# '
zstyle ':vcs_info:git:*' formats '%b'

####################################
############# PROMPT ###############
####################################

autoload -Uz promptinit
promptinit
PROMPT="%F{141}[%f%B%F{68}%n%f%b%F{141}]%f🪐%F{141}[%f%B%F{68}%~%f%b%F{141}]%f%F{68}$%f "
# 👽
# 🪐
####################################


####################################
############# PLUGINS ##############
####################################

source ~/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.plugin.zsh
source ~/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.plugin.zsh

####################################


####################################
############# ALIASES ##############
####################################

alias ls='ls --color'
LS_COLORS="di=1;35:*.py=32:*.sh=32:*.odt=36:*.docx=36:*.doc=36:*.html=36:*.png=36:*.jpg=36:*.rb=31:*.vbs=31:*.js=33:*.css=34:*.git=34:*.txt=29"
export LS_COLORS
alias ls="/usr/bin/lsd"
alias cat="/usr/bin/bat"

####################################

