import digitalio
import board
import displayio
import time
import xpt2046_circuitpython
from adafruit_rgb_display import color565
import adafruit_rgb_display.ili9341 as ili9341

# Release any previously configured displays
displayio.release_displays()

# Set up the display
display = ili9341.ILI9341(
    board.SPI(),
    cs=digitalio.DigitalInOut(board.LCD_CS),
    dc=digitalio.DigitalInOut(board.LCD_DC),
    rotation=270
)

# Fill the display with a color
display.fill(color565(0xff, 0x11, 0x22))

# Create the touch controller
touch = xpt2046_circuitpython.Touch(
    board.SPI(), 
    cs = digitalio.DigitalInOut(board.TOUCH_CS)
)

while(True):
    # Get the coordinates for this touch
    x, y = touch.get_coordinates()
    # Check if coordinates are valid
    if x is not None and y is not None:
        display.pixel(x, y, color565(255, 255, 255))
        # print((x, y))
    # Optional delay to reduce CPU usage
    # time.sleep(0.1)


