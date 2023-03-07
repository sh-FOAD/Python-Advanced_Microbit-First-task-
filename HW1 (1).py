
from microbit import *
x = 0
    
while True:
    if button_a.was_pressed():
        x = x + 1
    elif button_b.was_pressed():
        x = 0
    if button_a.is_pressed() and button_b.is_pressed():
        break
    if x == 0:
        display.show("0")
        pin0.write_analog(0)
            
    if x == 1:
        display.show("1")
        pin0.write_analog(50)
                
    if x == 2:
        display.show("2")
        pin0.write_analog(100)

    if x == 3:
        display.show("3")
        pin0.write_analog(150)
        
    if x == 4:
        display.show("4")
        pin0.write_analog(200)
        
    if x == 5:
        display.show("5")
        pin0.write_analog(250)

display.scroll("off")