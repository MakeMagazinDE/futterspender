import monitor

const SERVO_PIN = C_PIN_01      # Servo on IO01
setPWMFrequency(50)             # Servo runs on 50Hz

monitor.pushc("Ready for you.",MONITOR_GREEN )

def comment(id) ->byte[]
    if id == 0: return "Enjoy your meal"
    elif id == 1: return "Savor the taste"
    elif id == 2: return "Bon appétit"
    elif id == 3: return "Treat yourself"
    elif id == 4: return "Delicious bites"
    elif id == 5: return "Tasty and fresh"
    elif id == 6: return "Have fun eating"
    elif id == 7: return "Feast with joy"
    elif id == 8: return "More flavors?"
    return "Craving more?"

def downState():
    writePWM(SERVO_PIN, 102)
    delay(400)

def upState():
    writePWM(SERVO_PIN, 512)
    delay(400)

def resetState():
    downState()

def onClick():
    monitor.push(comment(random(0,9)))
    downState()
    upState()
    downState()
    
resetState()