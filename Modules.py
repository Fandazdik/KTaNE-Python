import random
from module_folder import SimpleWires
from module_folder import Keypad
from module_folder import WhosOnFirst
from module_folder import Clock
from module_folder import CrazyTalk
from module_folder import ColorMath
from module_folder import AnimalFight
from module_folder import Colorblindness

class Modules:
    
    def __init__(self):
        
        # Local assignments
        self.simpleWires = SimpleWires.SimpleWires
        self.keypad = Keypad.Keypad
        self.whosOnFirst = WhosOnFirst.WhosOnFirst
        self.clock = Clock.Clock
        self.crazyTalk = CrazyTalk.CrazyTalk
        self.colorMath = ColorMath.Colormath
        self.animalFight = AnimalFight.AnimalFight
        self.colorblindness = Colorblindness.Colorblindness
    
    
    # Global assignments
    simpleWires = SimpleWires.simpleWires
    keypad = Keypad.Keypad
    whosOnFirst = WhosOnFirst.WhosOnFirst
    clock = Clock.Clock
    crazyTalk = CrazyTalk.CrazyTalk
    colorMath = ColorMath.ColorMath
    animalFight = AnimalFight.AnimalFight
    colorblindness = Colorblindness.Colorblindness
    
    module_list = [
        simpleWires,
        keypad,
        whosOnFirst,
        clock,
        crazyTalk,
        colorMath,
        animalFight,
        colorblindness
        ]
    
    def create_modules(amount):
    
        
        final_modules = []
        while amount != 0:
            final_modules.append(random.choice(Modules.module_list))
            amount -= 1
            
        return final_modules
        
    