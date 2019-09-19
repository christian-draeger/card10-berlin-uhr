import utime
import leds
import display
import buttons
import light_sensor
import simple_menu
import sys
sys.path.append('/apps/berlin_uhr/')

import segement as _segment
import render as _render


def brightness():
    light = light_sensor.get_reading()
    display_brightness = int(light // 4) if light >= 4 else 1
    display_brightness = 100 if light > 300 else display_brightness
    led_brightness = int(light // 10) if light >= 10 else 1
    led_brightness = 31 if light > 300 else led_brightness
    return display_brightness, led_brightness


def render_type(disp, type, top_unit, bottom_unit):
    it = _segment.DESCRIPTION.get(type)
    _render.unit(disp, it.get("top"), top_unit)
    _render.unit(disp, it.get("bottom"), bottom_unit)

    if WITH_HINTS:
        disp.print('{:02}'.format(top_unit), posx=70, posy=10, font=display.FONT20)
        disp.print('{:02}'.format(bottom_unit), posx=70, posy=50, font=display.FONT20)


def render_seconds(disp, seconds):
    if WITH_SECONDS:
        _render.second_markers(disp)
        secs = 60 if seconds is 0 else seconds
        start_x = 80

        if secs > 0:
            length = (secs - 0) * 8 if secs < 10 else 80
            disp.rect(start_x, 0, length + start_x, 0, col=_segment.Colors.orange, filled=True)

        if secs > 10:
            length = (secs - 10) * 8 if secs < 20 else 80
            disp.rect(159, 0, 160, length, col=_segment.Colors.orange, filled=True)

        if secs > 20:
            length = 160 - (secs - 20) * 8 if secs < 30 else 80
            disp.rect(length, 79, 160, 80, col=_segment.Colors.orange, filled=True)

        if secs > 30:
            length = 80 - (secs - 30) * 8 if secs < 40 else 0
            disp.rect(length, 79, 160, 80, col=_segment.Colors.orange, filled=True)

        if secs > 40:
            length = 80 - (secs - 40) * 8 if secs < 50 else 0
            disp.rect(0, length, 0, 80, col=_segment.Colors.orange, filled=True)

        if secs > 50:
            length = (secs - 50) * 8 if secs < 60 else 80
            disp.rect(0, 0, length, 0, col=_segment.Colors.orange, filled=True)


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

        display_brightness, led_brightness = brightness()
        if WITH_BRIGHTNESS_ADJUST:
            disp.backlight(display_brightness)

        if WITH_SECONDS_LED:
            display_seconds(secs, led_brightness)

        render_seconds(disp, secs)

        render_type(disp, MODE, first_unit, second_unit)

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
WITH_HINTS = False
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
    light_sensor.start()
    while True:
        load_config()
        # setting_menu()
        with display.open() as _display:
            render_gui(_display)


main()
