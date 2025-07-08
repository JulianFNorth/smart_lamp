import time
from dataclasses import dataclass, field

@dataclass
class SmartLamp:
    name: str
    color: str
    brightness: int = field(default=0, init=True)
    is_on: bool = field(default=False, init=False)
    _registry = []

    def __post_init__(self): #Chat helped
        SmartLamp._registry.append(self)

    @classmethod
    def power_outage(cls):
        print("Wait....")
        time.sleep(0.5)
        print("Earthquake...POWER OUTAGE!!@#@>d.wd.....")
        time.sleep(1)
        for lamp in cls._registry: #Chat helped
            lamp.is_on = False
        print("All lamps turned off.")

    def turn_on(self):
        self.is_on = True
        print("Lamp turned on.")
    
    def turn_off(self):
        self.is_on = False
        print("Lamp turned off.")

    def toggle(self):
        if self.is_on:
            self.is_on = False
            print("Lamp turned off (toggled).")
        else:
            self.is_on = True
            print("Lamp turned on (toggled).")
    
    def set_brightness(self, percent:int):
        try:
            if not 0 <= int(percent) <= 100:
                print("Invalid brightness level.")
            else:
                self.brightness = int(percent)
                print("Brightness set.")
        except:
            print("Invalid brightness level.")
    
    def set_color(self, new_color:str):
        self.color = new_color
        print("Color set.")

    def status(self):
        print(f"Your SmartLamp {self.name} is: {self.color} and is {'on' if self.is_on else 'off'} with {self.brightness} brightness.")

def main():
    my_lampy = SmartLamp("Lampy", "Blue", 50)
    my_lampy.status()
    my_lampy.turn_on()
    my_lampy.set_brightness(10)
    my_lampy.status()

    our_limpy = SmartLamp("Limpy", "Green", 90)
    our_limpy.status()
    our_limpy.turn_on()
    our_limpy.set_brightness(85)
    our_limpy.status()
    our_limpy.power_outage()

    our_limpy.status()
    my_lampy.status()

    my_lampy.toggle()
    my_lampy.status()

if __name__ == "__main__":
    main()