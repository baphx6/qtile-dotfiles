from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from typing import Optional
from libqtile.widget.textbox import TextBox
from libqtile.widget.spacer import Spacer

from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration 

import os

import netifaces as ni

mod = "mod4"
#terminal = guess_terminal()
terminal = "alacritty" 
 
################################################################################################
###################################### KEYBINDS ################################################
################################################################################################

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Keybind for rofi
    Key([mod], "m", lazy.spawn("rofi -show run -show-icons"), desc="Launch Rofi"),

    # Growing and shrinking windows
    Key([mod, "shift"], "plus", lazy.layout.grow()),
    Key([mod, "shift"], "minus", lazy.layout.shrink()),

    # Audio 
    Key([mod], "plus", lazy.spawn("bash /home/faust/.config/scripts/volume-notif.sh up"), desc="vol +5%"),
    Key([mod], "minus", lazy.spawn("bash /home/faust/.config/scripts/volume-notif.sh down"), desc="vol -5%"),
    Key([mod], "v", lazy.spawn("bash /home/faust/.config/scripts/volume-notif.sh toggle"), desc="toggle mute"),

    # BetterLockScreen
    Key([mod], "l", lazy.spawn("betterlockscreen -l dim -q"), desc="Locks Screen"),

    # Flameshot
    Key([mod], "s", lazy.spawn("flameshot gui"), desc="Flameshot gui screenshot"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot screen"), desc="Flameshot fullscreenshot")
]

################################################################################################
###################################### GROUPS ##################################################
################################################################################################

groups = [Group(i, label="") for i in "1234567"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

################################################################################################
###################################### COLORS ##################################################
################################################################################################

background = "#1F1C19"
white = "#eeeeee"
disabled = "#707880"
transparent = "#00"
alert = "#A54242"

# Palette 1
aquamarine = "#8ABEB7"
purple = "#8e7cc3" 
blue = "#6fa8dc"
silver = "#AEC6CF"

# Hellkitty Palette
hk_whitesmoke = "#fff5f5"
hk_red = "#d95151"
hk_gold = "#d8b049"
hk_blue = "#508abb"
hk_black = "#2d2929"

# Ramen bowl colors
pumpkin_orange = "#fb7a09"
neon_fucsia = "#fd4165"

# False god
gold = "#fb980e"
space_cadet = "#1f2543ff"
bittersweet_shimmer = "#cc444bff"
medium_slate_blue = "#6b7bf3ff"
carolina_blue = "#6daedbff"
battleship_gray = "#909590"

################################################################################################
###################################### LAYOUTS #################################################
################################################################################################

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_normal=battleship_gray,
        border_focus=medium_slate_blue,
        border_width=3,
        margin=6,
        single_border_width=3,
        single_margin=4
        ),
    layout.MonadWide(
        border_normal=battleship_gray,
        border_focus=medium_slate_blue,
        border_width=3,
        margin=6,
        single_border_width=3,
        single_margin=4
        ),
    layout.Floating(
        border_normal=battleship_gray,
        border_focus=medium_slate_blue,
        border_width=3,
        margin=6,
        single_border_width=3,
        single_margin=4
        ),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

################################################################################################
##################################### FUNCTIONS ################################################
################################################################################################

def get_vpn_ip():
    try:
        addrs = ni.ifaddresses('tun0')
        ip = addrs[ni.AF_INET][0]['addr']
    except:
        ip = "Off"
    return ip

################################################################################################
######################################## BAR ###################################################
################################################################################################

powerline_left = {
    "decorations": [
        PowerLineDecoration(path="rounded_left")
    ]
}
powerline_right = {
    "decorations": [
        PowerLineDecoration(path="rounded_right")
    ]
}


screens = [

    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=16,
                    borderwidth=3,
                    highlight_method='line',
                    active=medium_slate_blue,
                    block_highlight_text_color=bittersweet_shimmer,
                    highlight_color=hk_black,
                    inactive=battleship_gray,
                    foreground=background,
                    background=hk_black,
                    this_current_screen_border=hk_black,
                    rounded=True,
                    disable_drag=True,
                    **powerline_left,
                ),
                widget.CurrentLayoutIcon(
                    padding = 0,
                    scale = 0.5,
                    background=carolina_blue,
                ),

                widget.CurrentLayout(
                    font= 'JetBrains Mono Bold',
                    background=carolina_blue,
                    **powerline_left,
                ),
                widget.TextBox(
                    text="",
                    font="JetBrains Mono Bold",
                    fontsize=47,
                    padding=7,
                    background=battleship_gray,
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show drun -show-icons")},
                    **powerline_left,
                ),

                widget.Systray(
                    padding=7,
                    fontsize=2,
                    background=hk_black,
                ),

                widget.WindowName(
                    format = "{name}",
                    #format = "{ }",
                    font='JetBrains Mono Bold',
                    empty_group_string = 'Desktop',
                    padding=7,
                    background=hk_black,
                    **powerline_right
                ),
                # widget.CheckUpdates(
                #     distro='Arch_Sup',
                #     #colour_have_updates=white,
                #     #colour_no_updates=blue,
                #     display_format= 'Updates 祝  {updates}',
                #     no_update_string='Updates 祝  0',
                #     #execute= '',
                #     update_interval= 300,
                #     fontsize=12,
                #     padding=10,
                #     font="JetBrains Mono Bold",
                #     background=aquamarine,
                #     mouse_callbacks={"Button1": lazy.spawn("alacritty --class float -e sudo pacman -Syyu")},
                #     **powerline_right,
                # ),
                widget.TextBox(
                    text=f'HTB VPN: {get_vpn_ip()}',
                    font="JetBrains Mono Bold",
                    fontsize=12,
                    padding=10,
                    background=battleship_gray,
                    **powerline_right
                ),
                # widget.TextBox(text=get_vpn_ip()),
                widget.TextBox(
                    text="",
                    font="JetBrains Mono Bold",
                    fontsize=25,
                    padding=0,
                    background=carolina_blue,
                    mouse_callbacks={"Button1": lazy.spawn("alacritty --class float -e htop")},
                ),
                widget.CPU(
                    format='{load_percent}%',
                    fontsize=12,
                    padding=10,
                    font="JetBrains Mono Bold",
                    background=carolina_blue,
                    mouse_callbacks={"Button1": lazy.spawn("alacritty --class float -e htop")},
                ),
                widget.TextBox(
                    text="﬙",
                    font="JetBrains Mono Bold",
                    fontsize=25,
                    padding=0,
                    background=carolina_blue,
                    mouse_callbacks={"Button1": lazy.spawn("alacritty --class float -e htop")},
                ),
                widget.Memory(
                    #format='{SwapUsed: .0f}{mm}',
                    format='{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                    measure_mem='G',
                    font="JetBrains Mono Bold",
                    fontsize=12,
                    padding=10,
                    background=carolina_blue,
                    mouse_callbacks={"Button1": lazy.spawn("alacritty --class float -e htop")},
                    **powerline_right
                ),
                # widget.UPowerWidget(

                # ),
                # widget.WifiIcon(),
                widget.TextBox(
                    text="",
                    font="JetBrains Mono Bold",
                    fontsize=15,
                    padding=0,
                    background=medium_slate_blue,
                    mouse_callbacks={"Button1": lazy.spawn("alacritty --class float -e nmtui")},
                ),
                widget.Net(
                    font='JetBrains Mono Bold',
                    fontsize=12,
                    padding=10,
                    background=medium_slate_blue,
                    format="Wired Connection",
                    mouse_callbacks={"Button1": lazy.spawn("alacritty --class float -e nmtui")},
                ),

                # widget.TextBox(
                #     text="",
                #     font="JetBrains Mono Bold",
                #     fontsize=25,
                #     padding=0,
                #     background=medium_slate_blue,
                # ),
                # widget.PulseVolume(
                #     font='JetBrains Mono Bold',
                #     fontsize=12,
                #     padding=10,
                #     background=medium_slate_blue,
                #     volume_app="pamixer",
                #     update_interval=0.05,
                # ),

                widget.TextBox(
                    text="",
                    font="JetBrains Mono Bold",
                    fontsize=24,
                    padding=0,
                    background=medium_slate_blue,
                ),
                widget.Clock(
                    format='%d/%m/%y %H:%M',
                    font="JetBrains Mono Bold",
                    background=medium_slate_blue,
                    padding=7,
                    **powerline_right
                ),
                widget.TextBox(
                    text="",
                    font="JetBrains Mono Bold",
                    fontsize=24,
                    padding=0,
                    background=bittersweet_shimmer,
                    mouse_callbacks={"Button1": lazy.spawn("bash /home/baphx6/.config/scripts/rofi-powermenu.sh")},
                    **powerline_left
                ),
            ],
            size=32,
            margin=[10, 10, 5, 10],
            background='#00000000',
            opacity=1,
        ),
    ),
]

################################################################################################
######################################## MOUSE #################################################
################################################################################################

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry

        Match(wm_class="float"),  # Custom rule to float windows spawned from widgets 
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#List of commands to run when Qtile starts

autostart = [
        "xrandr --output Virtual-1 --mode 1920x1080",
        "feh --bg-fill ~/.config/wallpapers/false_god.jpg",
        "picom --no-vsync &",
        ]

for i in autostart:
    os.system(i)
