#!/bin/bash

chosen=$(printf "Power Off  \nReboot  \nLock  \nSuspend 鈴 \nExit  " | rofi -dmenu -window-title PowerMenu) 

case "$chosen" in
  "Power Off  ") shutdown 0 ;;
  "Reboot  ") reboot ;;
  "Lock  ") betterlockscreen -l dim -q ;;
  "Suspend 鈴 ") systemctl suspend ;;
  "Exit  ") exit 1 ;;
esac
