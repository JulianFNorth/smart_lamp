from dataclasses import dataclass, field

@dataclass
class SmartLamp:
    name: str
    color: str
    brightness: int = field(default=0, init=True)
    is_on: bool = field(default=False, init=False)

    def turn_on(self):
        self.is_on = True
        print("Lamp turned on.")
    
    def turn_off(self):
        self.is_on = False
        print("Lamp turned off.")
    
    def set_brightness(self, percent:int):
        self.brightness = int(percent)
        print("Brightness set.")
    
    def set_color(self, new_color:str):
        self.color = new_color
        print("Color set.")

    def status(self):
        print(f"Your SmartLamp {self.name} is: {self.color} and is {'on' if self.is_on else 'off'} with {self.brightness} brightness.")

def main():
    my_lampy = SmartLamp("Lampy", "Blue", 50)
    my_lampy.status()
    my_lampy.turn_on()
    my_lampy.set_brightness(70)
    my_lampy.status()

    our_limpy = SmartLamp("Limpy", "Green", 90)
    our_limpy.status()
    our_limpy.turn_on()
    our_limpy.set_brightness(85)
    our_limpy.status()

if __name__ == "__main__":
    main()