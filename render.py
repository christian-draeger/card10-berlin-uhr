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
