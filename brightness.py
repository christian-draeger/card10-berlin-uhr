import light_sensor


def start_light_sensor():
    light_sensor.start()


def calculated():
    light = light_sensor.get_reading()
    display_brightness = int(light // 4) if light >= 4 else 1
    display_brightness = 100 if light > 300 else display_brightness
    led_brightness = int(light // 10) if light >= 10 else 1
    led_brightness = 31 if light > 300 else led_brightness
    return display_brightness, led_brightness
