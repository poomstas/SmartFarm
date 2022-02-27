import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.LCD()

# mylcd.lcd_display_string("1234567890123456", 1) # Allows up to 16 characters per line
mylcd.lcd_display_string("Neither Smart,", 1)
mylcd.lcd_display_string("nor a Farm. Yet.", 2)