class Colors(object):
    black = (0, 0, 0)
    red_on = (255, 0, 0)
    red_off = (51, 0, 0)
    yellow_on = (255, 255, 0)
    yellow_off = (51, 51, 0)
    orange = (255, 128, 0)


DESCRIPTION = {
    "time": {
        "top": {
            "color_on": Colors.red_on,
            "color_off": Colors.red_off,
            "x5": {
                "row": 1,
                "offset": 0,
                "amount": 4,
                "width": 39
            },
            "x1": {
                "row": 2,
                "offset": 0,
                "amount": 4,
                "width": 39
            }
        },
        "bottom": {
            "color_on": Colors.yellow_on,
            "color_off": Colors.yellow_off,
            "x5": {
                "row": 3,
                "offset": 0,
                "amount": 11,
                "width": 14
            },
            "x1": {
                "row": 4,
                "offset": 0,
                "amount": 4,
                "width": 39
            }
        }
    },
    "date": {
        "top": {
            "color_on": Colors.yellow_on,
            "color_off": Colors.yellow_off,
            "x5": {
                "row": 1,
                "offset": 0,
                "amount": 6,
                "width": 26
            },
            "x1": {
                "row": 2,
                "offset": 0,
                "amount": 4,
                "width": 39
            }
        },
        "bottom": {
            "color_on": Colors.red_on,
            "color_off": Colors.red_off,
            "x5": {
                "row": 3,
                "offset": 0,
                "amount": 2,
                "width": 79
            },
            "x1": {
                "row": 4,
                "offset": 0,
                "amount": 4,
                "width": 39
            }
        }
    }
}
