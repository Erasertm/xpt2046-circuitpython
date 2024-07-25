import xpt2046_circuitpython
import time
import digitalio
import board
import displayio

displayio.release_displays()

# Create touch controller
touch = xpt2046_circuitpython.Touch(
    board.SPI(), 
    cs = digitalio.DigitalInOut(board.TOUCH_CS)
)

while(True):
    # Get the coordinates for this touch
    x, y = touch.get_coordinates()
    # Check if coordinates are valid
    if x is not None and y is not None:
        print(x, y)
    time.sleep(0.1)
