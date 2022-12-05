#!/bin/bash

case $1 in
up)
  # Unmute
  pamixer -u
  # Increase volume by 5
  pamixer -i 5
  # Get current volume
  curr_volume=$(pamixer --get-volume-human)
  # Send notification
  dunstify -a "changevolume" -u normal -r 6969 -h int:value:"$curr_volume" -i /usr/share/icons/breeze-dark/status/24/audio-volume-high.svg "Volume: $curr_volume" -t 3000
  ;;
down)
  # Unmute
  pamixer -u
  # Decrease volume by 5
  pamixer -d 5
  # Get current volume
  curr_volume=$(pamixer --get-volume-human)
  # Send notification
  dunstify -a "changevolume" -u normal -r 6969 -h int:value:"$curr_volume" -i /usr/share/icons/breeze-dark/status/24/audio-volume-medium.svg "Volume: $curr_volume"
  ;;
toggle)
  pamixer -t
  if $(pamixer --get-mute); then
    dunstify -a "changevolume" -u normal -r 6969 -i /usr/share/icons/breeze-dark/status/24/audio-off.svg "Volume Off" -t 3000
  else
    dunstify -a "changevolume" -u normal -r 6969 -i /usr/share/icons/breeze-dark/status/24/audio-on.svg "Volume On" -t 3000
  fi
  ;;
esac
