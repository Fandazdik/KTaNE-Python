import random
from module_folder import SimpleWires
from module_folder import Keypad
from module_folder import WhosOnFirst
from module_folder import Clock

class Modules:
    
    def __init__(self):
        
        # Local assignments
        self.simpleWires = SimpleWires.SimpleWires
        self.keypad = Keypad.Keypad
        self.whosOnFirst = WhosOnFirst.WhosOnFirst
        self.clock = Clock.Clock
    
    
    # Global assignments
    simpleWires = SimpleWires.simpleWires
    keypad = Keypad.Keypad
    whosOnFirst = WhosOnFirst.WhosOnFirst
    clock = Clock.Clock
    
    module_list = [simpleWires, keypad, whosOnFirst, clock]
    
    def create_modules(amount):
    
        
        final_modules = []
        while amount != 0:
            final_modules.append(random.choice(Modules.module_list))
            amount -= 1
            
        return final_modules
        
    