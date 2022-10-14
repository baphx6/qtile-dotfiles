# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from typing import Optional
from libqtile.widget.textbox import TextBox
from libqtile.widget.spacer import Spacer

import os

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
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Keybind for rofi
    Key([mod], "m", lazy.spawn("rofi -show drun -show-icons"), desc="Launch Rofi"),
    # Growing and shrinking windows
    Key([mod], "plus", lazy.layout.grow()),
    Key([mod], "minus", lazy.layout.shrink()),
    # Pulseaudio
    Key([mod, "shift"], "plus", lazy.spawn("pulseaudio-ctl up"), desc="vol +5%"),
    Key([mod, "shift"], "minus", lazy.spawn("pulseaudio-ctl down"), desc="vol -5%"),
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
        border_normal=blue,
        border_focus=purple,
        border_width=3,
        margin=6,
        single_border_width=3,
        single_margin=4
        ),
    layout.MonadWide(
        border_normal=blue,
        border_focus=purple,
        border_width=3,
        margin=6,
        single_border_width=3,
        single_margin=4
        ),
    layout.Floating(
        border_normal=blue,
        border_focus=purple,
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
###################################### UNICODE #################################################
################################################################################################

def left_half_circle(fg_color):
    return TextBox(
        text='\uE0B6',
        fontsize=28,
        foreground=fg_color,
        padding=0)


def right_half_circle(fg_color, bg_color: Optional['str'] = None):
    return TextBox(
        text='\uE0B4',
        fontsize=28,
        background=bg_color,
        foreground=fg_color,
        padding=0)


def lower_left_triangle(bg_color, fg_color):
    return TextBox(
        text='\u25e2',
        padding=0,
        fontsize=50,
        background=bg_color,
        foreground=fg_color)


def left_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B2',
        padding=0,
        fontsize=24,
        background=bg_color,
        foreground=fg_color)


def right_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B0',
        padding=0,
        fontsize=24,
        background=bg_color,
        foreground=fg_color)

################################################################################################
######################################## BAR ###################################################
################################################################################################

screens = [

    Screen(
        top=bar.Bar(
            [
                left_half_circle(hk_black),
                widget.GroupBox(
                    fontsize=16,
                    borderwidth=3,
                    highlight_method='line',
                    active=blue,
                    block_highlight_text_color=blue,
                    highlight_color=hk_black,
                    inactive=aquamarine,
                    foreground=background,
                    background=hk_black,
                    this_current_screen_border=purple,
                    rounded=True,
                    disable_drag=True,
                 ),
                right_half_circle(hk_black),

                Spacer(length=10),

                left_half_circle(hk_blue),
                widget.CurrentLayoutIcon(
                    padding = 0,
                    scale = 0.5,
                    background=hk_blue,
                ),

                    widget.CurrentLayout(
                    font= 'JetBrains Mono Bold',
                    background=hk_blue,
                ),
                right_half_circle(hk_blue),

                Spacer(length=10),

                left_half_circle(hk_black),
                widget.WindowName(
                    format = "{name}",
                    #format = "{ }",
                    font='JetBrains Mono Bold',
                    empty_group_string = 'Desktop',
                    background=hk_black,
                ),
                right_half_circle(hk_black),

                Spacer(length=10),

                #widget.Systray(
                #    fontsize=2,
                #    background=background,
                #),

                #widget.TextBox(
                #    text=' ',
                #    background=background,
                #),

                #widget.TextBox(
                #    text='',
                #    size=20,
                #    font='JetBrains Mono Bold',
                #    background=background,
                #),
                 
                #widget.Battery(
                #    format=' {percent:2.0%}',
                #    font="JetBrains Mono ExtraBold",
                #    fontsize=12,
                #    padding=10,
                #    background=background,
                #),                     

                left_half_circle(aquamarine),
                widget.CheckUpdates(
                    distro='Arch_Sup',
                    #colour_have_updates=white,
                    #colour_no_updates=blue,
                    display_format= 'Updates 祝  {updates}',
                    no_update_string='Updates 祝  0',
                    #execute= '',
                    update_interval= 3600,
                    fontsize=12,
                    padding=10,
                    font="JetBrains Mono Bold",
                    background=aquamarine,
                ),
                right_half_circle(aquamarine),

                Spacer(length=10),

                left_half_circle(hk_blue),
                widget.TextBox(
                    text="",
                    font="JetBrains Mono Bold",
                    fontsize=25,
                    padding=0,
                    background=hk_blue,
                ),
                widget.CPU(
                    format='{load_percent}%',
                    fontsize=12,
                    padding=10,
                    font="JetBrains Mono Bold",
                    background=hk_blue,
                    mouse_callbacks={"Button1": lazy.spawn("alacritty -e htop")},
                ),

                widget.TextBox(
                    text="﬙",
                    font="JetBrains Mono Bold",
                    fontsize=25,
                    padding=0,
                    background=hk_blue,
                ),
                widget.Memory(
                    #format='{SwapUsed: .0f}{mm}',
                    format='{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                    measure_mem='G',
                    font="JetBrains Mono Bold",
                    fontsize=12,
                    padding=10,
                    background=hk_blue,
                    mouse_callbacks={"Button1": lazy.spawn("alacritty -e htop")},
                ),
                right_half_circle(hk_blue),

                Spacer(length=10),

                left_half_circle(purple),
                widget.TextBox(
                    text="",
                    font="JetBrains Mono Bold",
                    fontsize=25,
                    padding=0,
                    background=purple,
                ),
                widget.PulseVolume(
                    font='JetBrains Mono Bold',
                    fontsize=12,
                    padding=10,
                    background=purple,
                ),

                widget.TextBox(
                    text="",
                    font="JetBrains Mono Bold",
                    fontsize=24,
                    padding=0,
                    background=purple,
                ),
                widget.Clock(
                    format='%d/%m/%y %H:%M',
                    font="JetBrains Mono Bold",
                    background=purple,
                ),
                right_half_circle(purple),

                Spacer(length=10),

                left_half_circle(hk_red),
                widget.TextBox(
                    text="",
                    font="JetBrains Mono Bold",
                    fontsize=24,
                    padding=0,
                    background=hk_red,
                    mouse_callbacks={"Button1": lazy.spawn("bash ~/.config/scripts/rofi-powermenu.sh")},
                ),

                right_half_circle(hk_red),

                widget.Spacer(
                    length=18,
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
        "feh --bg-fill ../wallpapers/ramen-bowl-godzilla-v-kong-1920×1080.jpg",
        "picom --no-vsync &",
        ]

for i in autostart:
    os.system(i)
