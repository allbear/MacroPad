import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio


btn1_pin = board.GP12
btn2_pin = board.GP13
btn3_pin = board.GP14
memory_switch = board.GP19

mode = 1
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

switch = digitalio.DigitalInOut(memory_switch)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN

def btn_maker(btn_num):#マクロのセット
    if btn_num == 1:
        if mode == 1:
            keyboard.send(Keycode.O,Keycode.U,Keycode.B)
            keyboard.send(Keycode.O,Keycode.SPACE,Keycode.S,Keycode.I,Keycode.M,Keycode.A)
            keyboard.send(Keycode.S,Keycode.U,Keycode.ENTER)
        else:
            keyboard.send(Keycode.K,Keycode.A,Keycode.M,Keycode.I)
            keyboard.send(Keycode.Y,Keycode.A)
            keyboard.send(Keycode.N,Keycode.A,Keycode.O,Keycode.SPACE,Keycode.ENTER)

keyboard = Keyboard(usb_hid.devices)
while True:
    if btn1.value:
        btn_maker(1)
        time.sleep(0.1)
    if btn2.value:
        btn_maker(2)
        time.sleep(0.1)
    if btn3.value:
        btn_maker(3)
        time.sleep(0.1)
    if switch.value:
        if mode == 1:
            mode = 2
        else:
            mode = 1
        time.sleep(0.1)
    time.sleep(0.1)
