import random
class simpleWires:
        
    def __init__(self, serial_parse):
             
        self.displayed_code = simpleWires.create_wires()
        self.displayed = '\n'.join([simpleWires.COLOR_DICT[i] for i in self.displayed_code])
        self.correct = str(simpleWires.wire_to_cut(self.displayed_code, serial_parse))
        self.is_defused = False
    
    
    RED, WHITE, BLUE, YELLOW, BLACK = range(5)
    COLORS = [RED, WHITE, BLUE, YELLOW, BLACK]
    COLOR_DICT = {
        0: 'Red',
        1: 'White',
        2: 'Blue',
        3: 'Yellow',
        4: 'Black'
    }
    
    
    def is_odd(num):
        return int(num) % 2 == 1
    
    def create_wires():
        wire_list = []
        wire_num = random.randrange(3, 6)
        
        while wire_num != 0:
            wire_list.append(random.choice(simpleWires.COLORS))
            wire_num -= 1
        
        return wire_list
    
    def wire_to_cut(wire_list, serial_parse):
        
        last_digit_odd = simpleWires.is_odd(serial_parse[-1])
        
        # 3 to 6 wires
        
        # 3 Wires ---------------------
        if len(wire_list) == 3:
            
            if 0 not in wire_list: #no red wires
                return 2 #cut second
            
            elif wire_list[-1] == 1: #last wire white
                return 3 #cut last wire
                
                # You can't return a negative index since
                # it wont be intuitive for the user
                
                # Also these will return the 'nth' wire,
                # not the 'nth' position of wire_list
                
            elif wire_list.count(2) > 1: #more than one blue wire
                # THIS FINDS EVERY OCCURENCE OF BLUE (2) AND RETURNS LAST ONE
                return [i for i,val in enumerate(wire_list) if val == 2][-1] #cut last blue wire
            
            else:
                return 3 #cut last wire
        
        
        # 4 Wires ---------------------
        if len(wire_list) == 4:
             
            if wire_list.count(0) > 1 and last_digit_odd: #more that one red wire and last digit of serial odd:
                return [i for i,val in enumerate(wire_list) if val == 0][-1]  #cut last red wire
            
            elif wire_list[-1] == 3 and wire_list.count(0) == 0: #last wire yellow and no red wires
                return 1 #cut first wire
            
            elif wire_list.count(2) == 1: #one blue wire
                return 1 #cut first wire
            
            elif wire_list.count(3) > 1: #more than one yellow wire
                return 4 #cut last wire
            
            else:
                return 2 #cut second wire

        
        # 5 Wires ---------------------
        if len(wire_list) == 5:

            
            if wire_list[-1] == 4 and last_digit_odd: #last wire black and last digit of serial odd:
                return 4 #cut fourth wire
            
            elif wire_list.count(0) == 1 and wire_list.count(3) > 1: #one red wire and more than one yellow wire:
                return 1 #cut first wire
            
            elif wire_list.count(4): #no black wires:
                return 2
            
            else:
                return 1


        # 6 Wires ---------------------        
        if len(wire_list) == 6:

            
            if wire_list.count(3) == 0 and last_digit_odd: # no yellow wires and last digit of serial odd:
                return 3 #cut third wire
            
            elif wire_list.count(3) == 1 and wire_list.count(1) > 1:# one yellow wire and more than one white wire:
                return 4
            
            elif wire_list.count(0) == 0: # no red wires
                return 5
            
            else:
                return 4
        
    def defused(self):
        self.is_defused = True