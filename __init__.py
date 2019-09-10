import utime
import leds
import display
import buttons
import light_sensor
import simple_menu


class Colors(object):
    background = (0, 0, 0)
    red_on = (255, 0, 0)
    red_off = (60, 0, 0)
    yellow_on = (255, 255, 0)
    yellow_off = (60, 60, 0)
    seconds = (255, 128, 0)
    white = (255, 255, 255)


class Segment(object):
    # value is representing the width in px
    half = 79
    quarter = 39
    sixth = 26
    eleventh = 14


def brightness():
    light = light_sensor.get_reading()
    display_brightness = int(light // 4) if light >= 4 else 1
    display_brightness = 100 if light > 300 else display_brightness
    led_brightness = int(light // 10) if light >= 10 else 1
    led_brightness = 31 if light > 300 else led_brightness
    return display_brightness, led_brightness, light


def render_segment(disp, row, pos, color, dimension):
    width = dimension
    extra_offset = 1 if dimension == Segment.eleventh else 0
    height = 19
    # hint: coordinate 0, 0 is on top left corner of display
    disp.rect(width * pos + 2 + extra_offset,       # X-start coordinate
              height * (row - 1) + 2,               # Y-start coordinate
              width * (pos + 1) + extra_offset,     # X-End coordinate
              height * row,                         # Y-End coordinate
              col=color,
              filled=True)


def on_off_color_calc(active_segments, pos):
    return Colors.red_on if active_segments > pos else Colors.red_off


def render_minute_x5(disp, pos, minutes):
    active_segments = int(minutes // 5) > pos
    is_quarter = (pos + 1) % 3 is 0
    color = Colors.yellow_on if active_segments else Colors.yellow_off

    if active_segments and is_quarter:
        color = Colors.red_on

    if not active_segments and is_quarter:
        color = Colors.red_off

    render_segment(disp, 3, pos, color, Segment.eleventh)


def render_minute_x1(disp, pos, minutes):
    active_segments = minutes % 5

    color = Colors.yellow_on if active_segments > pos else Colors.yellow_off
    render_segment(disp, 4, pos, color, Segment.quarter)


def render_hours(disp, hours):
    for index in range(4):
        row1_segment_color = on_off_color_calc(int(hours // 5), index)
        row2_segment_color = on_off_color_calc(hours % 5, index)
        render_segment(disp, 1, index, row1_segment_color, Segment.quarter)
        render_segment(disp, 2, index, row2_segment_color, Segment.quarter)

    if WITH_HINTS:
        disp.print(str(hours), posx=70, posy=10, font=display.FONT20)


def render_minutes(disp, minutes):
    for index in range(11):
        render_minute_x5(disp, index, minutes)

    for index in range(4):
        render_minute_x1(disp, index, minutes)

    if WITH_HINTS:
        disp.print(str(minutes), posx=70, posy=50, font=display.FONT20)


def render_months(disp, months):
    for index in range(4):
        row1_segment_color = on_off_color_calc(int(months // 5), index)
        row2_segment_color = on_off_color_calc(months % 5, index)
        render_segment(disp, 1, index, row1_segment_color, Segment.quarter)
        render_segment(disp, 2, index, row2_segment_color, Segment.quarter)

    if WITH_HINTS:
        disp.print(str(months), posx=70, posy=10, font=display.FONT20)


def render_days(disp, days):
    for index in range(11):
        render_minute_x5(disp, index, days)

    for index in range(4):
        render_minute_x1(disp, index, days)

    if WITH_HINTS:
        disp.print(str(days), posx=70, posy=50, font=display.FONT20)


def render_seconds(disp, seconds):
    render_second_hints(disp)
    secs = 60 if seconds is 0 else seconds
    start_x = 80

    if secs > 0:
        length = (secs - 0) * 8 if secs < 10 else 80
        disp.rect(start_x, 0, length + start_x, 0, col=Colors.seconds, filled=True)

    if secs > 10:
        length = (secs - 10) * 8 if secs < 20 else 80
        disp.rect(159, 0, 160, length, col=Colors.seconds, filled=True)

    if secs > 20:
        length = 160 - (secs - 20) * 8 if secs < 30 else 80
        disp.rect(length, 79, 160, 80, col=Colors.seconds, filled=True)

    if secs > 30:
        length = 80 - (secs - 30) * 8 if secs < 40 else 0
        disp.rect(length, 79, 160, 80, col=Colors.seconds, filled=True)

    if secs > 40:
        length = 80 - (secs - 40) * 8 if secs < 50 else 0
        disp.rect(0, length, 0, 80, col=Colors.seconds, filled=True)

    if secs > 50:
        length = (secs - 50) * 8 if secs < 60 else 80
        disp.rect(0, 0, length, 0, col=Colors.seconds, filled=True)


def render_second_hints(disp):
    for i in range(0, 161, 8):
        is_5er = i // 8 % 5 == 0
        color = Colors.seconds

        if is_5er:
            disp.circ(i, 0, 2, col=color, filled=True)
            disp.circ(i, 79, 2, col=color, filled=True)
        else:
            disp.pixel(i, 0, col=color)
            disp.pixel(i, 79, col=color)

        if i <= 80:
            if is_5er:
                disp.circ(0, i, 2, col=color, filled=True)
                disp.circ(159, i, 2, col=color, filled=True)
            else:
                disp.pixel(0, i, col=color)
                disp.pixel(159, i, col=color)


def render(disp, display_brightness, led_brightness):

    if WITH_BRIGHTNESS_ADJUST:
        disp.backlight(display_brightness)

    year, month, day, hours, mins, secs, _, _ = utime.localtime()

    if WITH_SECONDS:
        render_seconds(disp, secs)
    if WITH_SECONDS_LED:
        display_seconds(secs, led_brightness)

    if DATE_MODE:
        render_months(disp, month)
        render_days(disp, day)
    else:
        render_hours(disp, hours)
        render_minutes(disp, mins)


def display_seconds(sec, intensity):
    leds.set_rocket(1, intensity) if sec % 2 == 0 else leds.set_rocket(1, 0)


# ==== configuration ==== #

WITH_SECONDS = True
WITH_SECONDS_LED = True
DATE_MODE = False
WITH_HINTS = False
WITH_BRIGHTNESS_ADJUST = True
DEV_MODE = False


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
    global DATE_MODE
    DATE_MODE = not DATE_MODE


def brightness_adjust_toggle():
    global WITH_BRIGHTNESS_ADJUST
    WITH_BRIGHTNESS_ADJUST = not WITH_BRIGHTNESS_ADJUST


class SettingsMenu(simple_menu.Menu):
    color_1 = Colors.background
    color_2 = Colors.background
    color_text = Colors.yellow_on
    color_sel = Colors.red_on

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
        display_brightness, led_brightness, light = brightness()
        load_config()
        # setting_menu()
        with display.open() as _display:
            _display.clear(col=Colors.background)
            render(_display, display_brightness, led_brightness)
            if DEV_MODE:
                _display.print("light sensor: " + str(light), posx=0, posy=0, font=display.FONT8)
            _display.update()
        utime.sleep_ms(400)


main()
