# You import all the IOs of your board
import board 

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.mouse_jiggler import MouseJiggler
from kmk.extensions.LED import LED
import board

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

#Adds mouse jiggler module
keyboard.modules.append(MouseJiggler())

# Define your pins here!
PINS = [board.D7, board.D8, board.D9, board.D10]

led = LED(led_pin=[board.D3])
keyboard.extensions.append(led)

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        KC.Macro(Tap(KC.LGUI), "vs code", Tap(KC.ENTER)),
        KC.MJ_TOGGLE,
        KC.LED_TOG(),
        KC.Macro(Press(KC.LCTL), Tap(KC.S), Release(KC.LCTL))
        ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
