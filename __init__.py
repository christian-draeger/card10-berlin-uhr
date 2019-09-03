import utime
import leds
import display


class Colors(object):
    background = (0, 0, 0)
    red_on = (255, 0, 0)
    red_off = (60, 0, 0)
    yellow_on = (255, 255, 0)
    yellow_off = (60, 60, 0)
    seconds = (255, 128, 0)
    white = (255, 255, 255)


def render_bg(disp):
    disp.rect(0, 0, 160, 80, col=Colors.background, filled=True)


def render_segment(disp, row, pos, color, thin=False):
    width = 14 if thin else 39
    extra_offset = 1 if thin else 0
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

    render_segment(disp, 3, pos, color, True)


def render_minute_x1(disp, pos, minutes):
    active_segments = minutes % 5

    color = Colors.yellow_on if active_segments > pos else Colors.yellow_off
    render_segment(disp, 4, pos, color)


def render_hours(disp):
    localtime = utime.localtime()
    hours = localtime[3]
    for index in range(4):
        row1_segment_color = on_off_color_calc(int(hours // 5), index)
        row2_segment_color = on_off_color_calc(hours % 5, index)
        render_segment(disp, 1, index, row1_segment_color)
        render_segment(disp, 2, index, row2_segment_color)


def render_minutes(disp):
    localtime = utime.localtime()
    minutes = localtime[4]
    for index in range(11):
        render_minute_x5(disp, index, minutes)

    for index in range(4):
        render_minute_x1(disp, index, minutes)


def render_seconds(disp):
    localtime = utime.localtime()
    seconds = localtime[5]
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
        color = Colors.white if i // 8 % 5 == 0 else Colors.seconds
        disp.pixel(i, 0, col=color)
        disp.pixel(i, 79, col=color)

    for i in range(0, 81, 8):
        color = Colors.white if i // 8 % 5 == 0 else Colors.seconds
        disp.pixel(0, i, col=color)
        disp.pixel(159, i, col=color)


def render(disp):
    render_bg(disp)
    render_hours(disp)
    render_minutes(disp)
    render_seconds(disp)
    render_second_hints(disp)
    disp.update()
    disp.close()


def display_seconds():
    localtime = utime.localtime()
    secs = localtime[5]
    # second value is brightness of led (0 - 31)
    leds.set_rocket(1, 31) if secs % 2 == 0 else leds.set_rocket(1, 0)


def main():
    while True:
        display_seconds()
        with display.open() as disp:
            render(disp)


main()
