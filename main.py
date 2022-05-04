import pydirectinput as pdi
import keyboard
import time
import random
from win32gui import GetWindowText, GetForegroundWindow


pdi.PAUSE = 0

class Timer:
    timeStamp = 0

    def Timer(self):
        Time = max(0, self.timeStamp - time.time())
        if 0 == Time:
            return 1
        return 0

    def SetTimer(self, t):
        self.timeStamp = time.time() + t
    
    def RemainingTime(self):
        return max(0, self.timeStamp - time.time())

class StateMachine:
    state = None
    previous_state = None

RowTimer = Timer()
States = StateMachine()


toggled = False
while True:
    if GetWindowText(GetForegroundWindow()) == "Sea of Thieves":
        if keyboard.is_pressed('['):
            toggled = False
            States.state = None
            pdi.keyUp('a')
            pdi.keyUp('d')
            print("Toggled off")
        if keyboard.is_pressed(']'):
            toggled = True
        if toggled:
            if States.state == None:
                print("Rowing the boat...")
                pdi.keyDown('a')
                pdi.keyDown('d')
                RowTimer.SetTimer(2+random.uniform(-0.1, 0.25))
                States.state = "Rowing"
            if States.state == "Rowing":
                if RowTimer.Timer():
                    pdi.keyUp('a')
                    pdi.keyUp('d')
                    States.state = "Waiting"
                    RowTimer.SetTimer(0.47 + random.uniform(0, 0.3))
            if States.state == "Waiting":
                if RowTimer.Timer():
                    States.state = None
