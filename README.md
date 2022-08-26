# Qtile dotfiles

My first Arch Linux custom desktop, made from scratch with QtileWM.
If you want to use these dotfiles, please keep in mind that you need every package installed.
I will keep on adding commits to this repo as I change stuff in my personal desktop.
Feel free to change any config file to your heart's content.


## Packages needed

Fonts used are JetBrains Mono Nerd Font for Alacritty and Fira Code Nerd Font for Polybar.
Assuming you are using Arch, you can install these packages directly using pacman or from the AUR:
  - qtile
  - alacritty
  - rofi
  - pulseaudio-ctl
  - feh
  - picom
  - polybar
  - betterlockscreen

## BetterLockScreen

In order to use betterlockscreen you will need to update its cache with the image you want to use.
You can also specify a directory with a few images in it and betterlockscreen will randomly choose one to update.
To do this use this command:
```bash
betterlockscreen -u <path>
```
To lock the screen from a terminal you can use:
```bash
betterlockscreen -l <effect> -q
```
But I already set a keybind in config.py. Just do [mod] + l

You will also need to enable the service if you want it to lock the screen when the system sleeps/suspends.
First copy the .service file to /usr/lib/systemd/system/ (The AUR package does this for you)
```bash
cp betterlockscreen@.service /usr/lib/systemd/system/
```
Then enable the service:
```bash
sudo systemctl enable betterlockscreen@$USER.service
```

For more info check their repository: https://github.com/betterlockscreen/betterlockscreen

## Shoutouts
rofi-wifi.sh made by ericmurphy: https://github.com/ericmurphyxyz/rofi-wifi-menu
