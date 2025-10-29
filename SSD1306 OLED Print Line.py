from machine import Pin
from machine import I2C
import ssd1306

#D1 = scl = GPIO5
#D2 = sda = GPIO4

i2c = I2C(sda=Pin(4), scl=Pin(5))

display = ssd1306.SSD1306_I2C(128, 64, i2c)

def oled_string(x,y,z,c):
    display.fill(0) #Empty the display
    display.text(x, y, z, c)
    display.show()

display.pixel(0,0,1)
display.pixel(0,1,1)
display.pixel(0,2,1)
display.pixel(0,3,1)
display.pixel(0,4,1)
display.pixel(0,5,1)
display.pixel(0,6,1)
display.pixel(0,7,1)
display.pixel(0,8,1)
display.pixel(0,9,1)
display.pixel(0,10,1)
display.show()

