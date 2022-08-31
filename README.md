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

## Polybar

The battery module has not been tested yet since I'm building this from a VM and don't have access to a laptop. It's literally the same as the one they suggest in their repo though (https://github.com/polybar/polybar/wiki/Module:-battery), so I assume it should work right off the bat if you specify your battery and adapter. I will tweak it once I get my hands on a laptop to keep labbing.

If you do have a laptop and want to try it, you will need to add it to the modules-right variable in the config.ini file.

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
