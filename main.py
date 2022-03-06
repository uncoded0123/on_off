import time, http1
from machine import Pin, reset

http1.connect_router(user_name1='<enter_wifi_username1>', password1='<enter_wifi_password1>',
					 user_name2='<enter_wifi_username2>', password2='<enter_wifi_password2>')
def on_off_function():
    led_blue = Pin(2, Pin.OUT)
    pin_D1 = Pin(5, Pin.OUT)
    if http1.http_get_request('<enter url>')['test'] == 'Turn On': # enter url, retrieve key, value, check if true
        led_blue.on() #off=on esp8266
        pin_D1.on()
    else:
        pin_D1.off()
        led_blue.off()

def loop1():
    while True:
        try:
            on_off_function()
        except:
            reset()
        time.sleep(0.3)
loop1()