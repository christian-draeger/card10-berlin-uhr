import utime
import leds
import display

WIDTH = 160
HEIGHT = 80
OFFSET = 1

SEGMENT_WIDTH = 40
SEGMENT_HEIGHT = 20

COLOR_BG = (80, 80, 80)
COLOR_RED_ACTIVE = (255, 0, 0)
COLOR_RED_INACTIVE = (150, 0, 0)
COLOR_YELLOW_ACTIVE = (255, 255, 0)
COLOR_YELLOW_INACTIVE = (150, 150, 0)


def render_bg(disp):
    disp.rect(0, 0, 160, 80, col=COLOR_BG, filled=True)


def render_hour_x5(disp, pos, col):
    disp.rect(SEGMENT_WIDTH * pos + OFFSET,
              OFFSET,
              SEGMENT_WIDTH * (pos + 1) - OFFSET,
              SEGMENT_HEIGHT - OFFSET,
              col=col,
              filled=True)


def render_hour_x1(disp, pos, col):
    disp.rect(SEGMENT_WIDTH * pos + OFFSET,
              SEGMENT_HEIGHT,
              SEGMENT_WIDTH * (pos + 1) - OFFSET,
              SEGMENT_HEIGHT * 2 - OFFSET,
              col=col,
              filled=True)


def render_minute_x5(disp, pos, col):
    disp.rect(SEGMENT_WIDTH * pos + OFFSET,
              SEGMENT_HEIGHT,
              SEGMENT_WIDTH * (pos + 1) - OFFSET,
              SEGMENT_HEIGHT * 3 - OFFSET,
              col=col,
              filled=True)


def render_minute_x1(disp, pos, col):
    disp.rect(SEGMENT_WIDTH * pos + OFFSET,
              SEGMENT_HEIGHT * 3,
              SEGMENT_WIDTH * (pos + 1) - OFFSET,
              SEGMENT_HEIGHT * 4 - OFFSET,
              col=col,
              filled=True)


def render_hours_x5(disp):
    # localtime = utime.localtime()
    # hours = localtime[3]
    for i in range(4):
        render_hour_x5(disp, i, COLOR_RED_ACTIVE)


def render_hours_x1(disp):
    # localtime = utime.localtime()
    # hours = localtime[3]
    for i in range(4):
        render_hour_x1(disp, i, COLOR_RED_INACTIVE)


def render_minutes_x1(disp):
    # localtime = utime.localtime()
    # mins = localtime[4]
    for i in range(4):
        render_minute_x1(disp, i, COLOR_RED_INACTIVE)


def render(disp):
    render_bg(disp)
    render_hours_x5(disp)
    render_hours_x1(disp)

    render_minutes_x1(disp)
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
