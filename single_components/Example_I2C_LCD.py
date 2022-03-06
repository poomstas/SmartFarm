import I2C_LCD_driver

mylcd = I2C_LCD_driver.LCD()

mylcd.lcd_display_string("Neither Smart,", 1)
mylcd.lcd_display_string("nor a Farm. Yet.", 2)
