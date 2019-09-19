import display
import segement as _segment


def seg(disp, pos, color, seg_conf):
    height = 19
    width = seg_conf.get("width")
    offset = seg_conf.get("offset")
    row = seg_conf.get("row")
    x_start = width * pos + 2 + offset
    y_start = height * (row - 1) + 2
    x_end = width * (pos + 1) + offset
    y_end = height * row
    disp.rect(x_start, y_start, x_end, y_end, col=color, filled=True)


def unit(disp, unit_conf, amount):
    color_on = unit_conf.get("color_on")
    color_off = unit_conf.get("color_off")
    x5 = unit_conf.get("x5")
    x1 = unit_conf.get("x1")

    for index in range(x5.get("amount")):
        active_segments = int(amount // 5) > index
        is_quarter = (index + 1) % 3 is 0
        color = color_on if active_segments else color_off

        if active_segments and is_quarter:
            color = _segment.Colors.red_on

        if not active_segments and is_quarter:
            color = _segment.Colors.red_off
        seg(disp, index, color, x5)

    for index in range(x1.get("amount")):
        active_segments = amount % 5 > index
        color = color_on if active_segments else color_off
        seg(disp, index, color, x1)


def second(disp, seconds):
    second_markers(disp)
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


def second_markers(disp):
    for i in range(0, 161, 8):
        is_5er = i // 8 % 5 == 0
        color = _segment.Colors.orange

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


def type(disp, type, top_unit, bottom_unit):
    it = _segment.DESCRIPTION.get(type)
    unit(disp, it.get("top"), top_unit)
    unit(disp, it.get("bottom"), bottom_unit)


def hint(disp, top_unit, bottom_unit):
    disp.print('{:02}'.format(top_unit), posx=70, posy=10, font=display.FONT20)
    disp.print('{:02}'.format(bottom_unit), posx=70, posy=50, font=display.FONT20)
