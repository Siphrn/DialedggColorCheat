# 0, 100, 100
# 360, 0, 0
HUE_POSITION = [(686, 447), (686, 834)]
SATURATION_POSITION = [(720, 837), (720, 447)]
BRIGHTNESS_POSITION = [(762, 837), (762, 447)]

import pyautogui
import time
from pynput import keyboard

def wait_for_key(target=keyboard.Key.shift_r):
    with keyboard.Listener(on_press=lambda k: False if k == target else None) as listener:
        listener.join()

def rgb_to_hsl(rgb: tuple) -> tuple[int, int, int]:
    r, g, b = rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0

    max_c = max(r, g, b)
    min_c = min(r, g, b)
    l = (max_c + min_c) / 2.0

    if max_c == min_c:
        h = s = 0.0
    else:
        d = max_c - min_c
        s = d / (1 - abs(2 * l - 1))
        if max_c == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_c == g:
            h = (b - r) / d + 2
        else:
            h = (r - g) / d + 4
        h /= 6

    return round(h * 360), round(s * 100), round(l * 100)

def pickColor(hsl, hue_position, saturation_position, brightness_position):
    hue_starting = hue_position[0]
    hue_ending = hue_position[1]
    saturation_starting = saturation_position[0]
    saturation_ending = saturation_position[1]
    brightness_starting = brightness_position[0]
    brightness_ending = brightness_position[1]

    hue = hsl[0]
    saturation = hsl[1]
    brightness = hsl[2]

    hue_y = hue / 360 * (hue_ending[1] - hue_starting[1]) + hue_starting[1]
    saturation_y = saturation / 100 * (saturation_ending[1] - saturation_starting[1]) + saturation_starting[1]
    brightness_y = brightness / 100 * (brightness_ending[1] - brightness_starting[1]) + brightness_starting[1]

    wait_for_key()

    pyautogui.moveTo(hue_starting[0], hue_y)
    pyautogui.click()
    pyautogui.moveTo(saturation_starting[0], saturation_y)
    pyautogui.click()
    pyautogui.moveTo(brightness_starting[0], brightness_y)
    pyautogui.click()


    

def main():
    for i in range(0, 4):
        wait_for_key()
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")

        rgb_color = pyautogui.pixel(1821, 1304)
        hsl = rgb_to_hsl(rgb_color)

        pickColor(hsl, HUE_POSITION, SATURATION_POSITION, BRIGHTNESS_POSITION)



if __name__ == "__main__":    main()