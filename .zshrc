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
#################################### 
####################################

# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/faust/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall


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
####################################
