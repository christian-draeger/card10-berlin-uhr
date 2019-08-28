import utime
import leds
import display


class Colors(object):
    background = (20, 20, 20)
    red_on = (255, 0, 0)
    red_off = (60, 0, 0)
    yellow_on = (255, 255, 0)
    yellow_off = (60, 60, 0)


def render_bg(disp):
    disp.rect(0, 0, 160, 80, col=Colors.background, filled=True)


def render_segment(disp, row, pos, color, thin=False):
    width = 14 if thin else 40
    offset = 1
    extra_offset = 3 if thin else 0
    height = 20
    disp.rect(width * pos + offset + extra_offset,
              height * (row - 1),
              width * (pos + 1) - offset + extra_offset,
              height * row - offset,
              col=color,
              filled=True)


def render_hour_x5(disp, pos):
    localtime = utime.localtime()
    hours = localtime[3]
    active_segments = int(hours // 5)

    color = Colors.red_on if active_segments > pos else Colors.red_off
    render_segment(disp, 1, pos, color)


def render_hour_x1(disp, pos):
    localtime = utime.localtime()
    hours = localtime[3]
    active_segments = hours % 5

    color = Colors.red_on if active_segments > pos else Colors.red_off
    render_segment(disp, 2, pos, color)


def render_minute_x5(disp, pos):
    localtime = utime.localtime()
    mins = localtime[4]
    active_segments = int(mins // 5) > pos
    is_quarter = (pos + 1) % 3 is 0
    color = Colors.yellow_on if active_segments > pos else Colors.yellow_off

    if active_segments and is_quarter:
        color = Colors.red_on

    if not active_segments and is_quarter:
        color = Colors.red_off

    render_segment(disp, 3, pos, color, True)


def render_minute_x1(disp, pos):
    localtime = utime.localtime()
    mins = localtime[4]
    active_segments = mins % 5

    color = Colors.yellow_on if active_segments > pos else Colors.yellow_off
    render_segment(disp, 4, pos, color)


def render_hours(disp):
    for i in range(4):
        render_hour_x5(disp, i)
        render_hour_x1(disp, i)


def render_minutes(disp):
    for i in range(11):
        render_minute_x5(disp, i)

    for i in range(4):
        render_minute_x1(disp, i)


def render(disp):
    render_bg(disp)
    render_hours(disp)
    render_minutes(disp)
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
