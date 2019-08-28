import utime
import leds
import display

WIDTH = 160
HEIGHT = 80
OFFSET = 1

SEGMENT_WIDTH = 40
SEGMENT_WIDTH_THIN = 14
SEGMENT_HEIGHT = 20

COLOR_BG = (80, 80, 80)
COLOR_RED_ACTIVE = (255, 0, 0)
COLOR_RED_INACTIVE = (150, 0, 0)
COLOR_YELLOW_ACTIVE = (255, 255, 0)
COLOR_YELLOW_INACTIVE = (150, 150, 0)


def render_bg(disp):
    disp.rect(0, 0, 160, 80, col=COLOR_BG, filled=True)


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
    on = int(hours // 5) > pos
    color = COLOR_RED_ACTIVE if on else COLOR_RED_INACTIVE
    render_segment(disp, 1, pos, color)


def render_hour_x1(disp, pos):
    color = COLOR_RED_INACTIVE
    render_segment(disp, 2, pos, color)


def render_minute_x5(disp, pos):
    localtime = utime.localtime()
    mins = localtime[4]
    on = int(mins // 5) > pos
    is_quarter = (pos + 1) % 3 is 0
    color = COLOR_RED_ACTIVE if is_quarter else COLOR_YELLOW_ACTIVE

    render_segment(disp, 3, pos, color, True)


def render_minute_x1(disp, pos):
    color = COLOR_YELLOW_ACTIVE
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
