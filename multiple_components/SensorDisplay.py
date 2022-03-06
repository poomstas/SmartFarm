'''
Takes readings from BME680 and displays it in the I2C LCD display.
'''

import sys
import time
from single_components import I2C_LCD_driver
import bme680

# Initialize I2C LCD Driver
try:
    mylcd = I2C_LCD_driver.LCD()
    print('LCD Driver Loaded\n')
except:
    print('LCD Driver Load Failed')
    sys.exit()

# Initialize BME680 Driver
try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    print('BME680 Driver Loaded\n')
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
    print('BME680 Driver Loaded\n')
except:
    print('BME680 Driver Load Failed')
    sys.exit()

# Can be omitted, if desired. 
print('Calibration data: ')
for name in dir(sensor.calibration_data):
    if not name.startswith('_'):
        value = getattr(sensor.calibration_data, name)
        if isinstance(value, int):
            print('\t{}: {}'.format(name, value))

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

print('\n\nInitial reading:')
for name in dir(sensor.data):
    value = getattr(sensor.data, name)
    if not name.startswith('_'):
        print('\t{}: {}'.format(name, value))

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

# Up to 10 heater profiles can be configured, each
# with their own temperature and duration.
# sensor.set_gas_heater_profile(200, 150, nb_profile=1)
# sensor.select_gas_heater_profile(1)

print('\n\nPolling: ')
try:
    while True:
        if sensor.get_sensor_data():
            temp, pressure, humidity = sensor.data.temperature, sensor.data.pressure, sensor.data.humidity
            temp, pressure, humidity = round(temp, 1), round(pressure, 1), round(humidity, 1)
            output = '\t{0:.1f} C,\t{1:.1f} hPa,\t{2:.1f} %RH'.format(temp, pressure, humidity)

            output1 = '{0:.1f}C {1:.1f}hPa'.format(temp, pressure)
            output2 = '{0:.1f}%RH '.format(humidity)

            if sensor.data.heat_stable:
                output2 += '{:4.1f}kOhms'.format(round(sensor.data.gas_resistance/1000, 1))
                print("\t" + output1 + " " + output2)
            else:
                print(output)

            mylcd.lcd_display_string(output1, 1) # 1st line on display
            mylcd.lcd_display_string(output2, 2) # 2nd line on display

        time.sleep(1)

except KeyboardInterrupt:
    pass
