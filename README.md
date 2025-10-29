# 🖥️ ESP8266 OLED Graphics Display (SSD1306) — MicroPython

## 🧠 Overview
This project demonstrates how to use an **SSD1306 128x64 OLED display** with an **ESP8266** board using **MicroPython**.  
It covers **text display**, **pixel plotting**, and **basic graphics drawing** (lines, boxes, and shapes) using the `ssd1306` library.

---

## ⚙️ Hardware Setup

| Component | ESP8266 Pin | Description |
|------------|-------------|--------------|
| OLED SDA   | GPIO4 (D2)  | I2C Data line |
| OLED SCL   | GPIO5 (D1)  | I2C Clock line |
| VCC        | 3.3V        | Power supply |
| GND        | GND         | Common ground |

🪛 **Connections:**
- OLED **VCC → 3.3V**
- OLED **GND → GND**
- OLED **SDA → GPIO4 (D2)**
- OLED **SCL → GPIO5 (D1)**

---

## 🧩 Code

```python
from machine import Pin, I2C
import ssd1306

# D1 = SCL = GPIO5
# D2 = SDA = GPIO4

# Initialize I2C and OLED display
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Function to display text easily
def oled_string(x, y, z, c):
    display.fill(0)  # Clear display
    display.text(x, y, z, c)
    display.show()

# --- Drawing individual pixels (vertical line example) ---
for y in range(0, 11):
    display.pixel(0, y, 1)  # Draw pixel column from y=0 to 10

# --- Drawing lines to form a rectangle ---
display.hline(0, 0, 10, 1)   # Top edge
display.vline(0, 0, 10, 1)   # Left edge
display.vline(10, 0, 10, 1)  # Right edge
display.hline(0, 10, 11, 1)  # Bottom edge

display.show()
