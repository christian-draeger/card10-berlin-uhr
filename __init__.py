import utime
import leds
import display
import buttons
import simple_menu
import sys

sys.path.append('/apps/berlin_uhr/')

import segement as _segment
import render as _render
import brightness as _brightness


def render_gui(disp):
    _, month, day, hours, mins, secs, _, _ = utime.localtime()

    first_unit = hours
    second_unit = mins

    if MODE is "date":
        first_unit = day
        second_unit = month

    global PREV_SECOND
    if PREV_SECOND < secs:
        disp.clear(col=_segment.Colors.black)

        display_brightness, led_brightness = _brightness.calculated()
        if WITH_BRIGHTNESS_ADJUST:
            disp.backlight(display_brightness)

        if WITH_SECONDS_LED:
            display_seconds(secs, led_brightness)

        if WITH_SECONDS:
            _render.second(disp, secs)

        _render.type(disp, MODE, first_unit, second_unit)

        if WITH_HINTS:
            _render.hint(disp, first_unit, second_unit)

        disp.update()

        if secs is 59:
            PREV_SECOND = -1
        else:
            PREV_SECOND += 1


def display_seconds(sec, intensity):
    leds.set_rocket(1, intensity) if sec % 2 == 0 else leds.set_rocket(1, 0)


# ==== configuration ==== #

WITH_SECONDS = True
WITH_SECONDS_LED = True
MODE = "time"
WITH_HINTS = True
WITH_BRIGHTNESS_ADJUST = True
DEV_MODE = False
PREV_SECOND = 0


def load_config():
    toggle_seconds_mode()
    toggle_date_mode()
    toggle_hint_mode()


def toggle_date_mode():
    button = buttons.read(buttons.TOP_RIGHT)
    pressed = button != 0
    if pressed:
        date_mode_toggle()


def toggle_seconds_mode():
    button = buttons.read(buttons.BOTTOM_LEFT)
    pressed = button != 0
    if pressed:
        seconds_toggle()


def toggle_hint_mode():
    button = buttons.read(buttons.BOTTOM_RIGHT)
    pressed = button != 0
    if pressed:
        hints_toggle()


def state_2_str(state):
    if state:
        return "[Y]"
    else:
        return "[N]"


def seconds_toggle():
    global WITH_SECONDS
    WITH_SECONDS = not WITH_SECONDS


def seconds_led_toggle():
    global WITH_SECONDS_LED
    WITH_SECONDS_LED = not WITH_SECONDS_LED


def hints_toggle():
    global WITH_HINTS
    WITH_HINTS = not WITH_HINTS


def dev_mode_toggle():
    global DEV_MODE
    DEV_MODE = not DEV_MODE


def date_mode_toggle():
    global MODE
    if MODE is "time":
        MODE = "date"
    else:
        MODE = "time"


def brightness_adjust_toggle():
    global WITH_BRIGHTNESS_ADJUST
    WITH_BRIGHTNESS_ADJUST = not WITH_BRIGHTNESS_ADJUST


class SettingsMenu(simple_menu.Menu):
    color_1 = _segment.Colors.black
    color_2 = _segment.Colors.black
    color_text = _segment.Colors.yellow_on
    color_sel = _segment.Colors.red_on

    def on_select(self, name, index):
        self.exit()


def setting_menu():
    if WITH_HINTS:
        SettingsMenu([
            state_2_str(WITH_SECONDS) + " show seconds",
            state_2_str(WITH_SECONDS_LED) + " seconds LED",
            state_2_str(WITH_HINTS) + " show hints",
            state_2_str(DEV_MODE) + " date mode",
            state_2_str(WITH_BRIGHTNESS_ADJUST) + " auto brightness",
            state_2_str(DEV_MODE) + " dev mode"
        ]).run()


# ==== execution ==== #

def main():
    _brightness.start_light_sensor()
    while True:
        load_config()
        # setting_menu()
        with display.open() as _display:
            render_gui(_display)


main()
