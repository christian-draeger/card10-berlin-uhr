import utime
import leds
import display

WIDTH = 160
HEIGHT = 80
OFFSET = 2

SEGMENT_WIDTH = 13
SEGMENT_HEIGHT = 20

COLOR_BG = (180, 180, 180)
COLOR_RED_ACTIVE = (255, 0, 0)
COLOR_RED_INACTIVE = (150, 0, 0)
COLOR_YELLOW_ACTIVE = (255, 255, 0)
COLOR_YELLOW_INACTIVE = (150, 150, 0)


#
# def display_minutes():
#     localtime = utime.localtime()
#     mins = localtime[4]
#

def render_bg(disp):
    disp.rect(0, 0, 160, 80, col=COLOR_BG, filled=True)


def render_hours(disp):
    localtime = utime.localtime()
    hours = localtime[3]
    disp.rect(OFFSET, OFFSET, (WIDTH // 4) - (OFFSET * 2), HEIGHT // 4, col=COLOR_RED_ACTIVE, filled=True)


def render(disp):
    render_bg(disp)
    render_hours(disp)
    disp.update()
    disp.close()


def display_seconds():
    localtime = utime.localtime()
    secs = localtime[5]
    if secs % 2 == 0:
        # second value is brightness of led (0 - 31)
        leds.set_rocket(1, 31)
    else:
        leds.set_rocket(1, 0)


def main():
    while True:
        display_seconds()
        with display.open() as disp:
            render(disp)


main()
