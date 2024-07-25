import xpt2046_circuitpython
import time
import digitalio
import board
import displayio

displayio.release_displays()

# Create touch controller
touch = xpt2046_circuitpython.Touch(
    board.SPI(), 
    cs = digitalio.DigitalInOut(board.TOUCH_CS),
    interrupt = digitalio.DigitalInOut(board.TOUCH_IRQ)
)

while(True):
    # Check if we have an interrupt signal
    if touch.is_pressed():
        # Get the coordinates for this touch
        print(touch.get_coordinates())
    time.sleep(0.1)
