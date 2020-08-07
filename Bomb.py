import random
import Modules
import inspect

class Bomb:
    
    def __init__(self, module_count):

        temp_serial = Bomb.random_serial()
        self.serial = temp_serial[0]
        self.serial_parse = temp_serial[1]
        
        self.strikes = 0
        
        # for modules on bomb
        self.bomb_modules = Bomb.make_modules(self, amount = module_count, serial_parse = self.serial_parse)
        
        # Make a defused dictionary
        self.defused = Bomb.update_defused(self)
    
    
        
    Modules = Modules.Modules
        
        
    UPPERCASE, LOWERCASE, NUMBERCASE = range(3)
    
    
    # case_mode should be a list of symbols to include
    def random_string(length = 1, case_mode = [UPPERCASE, LOWERCASE, NUMBERCASE], numbers = False):
        
        # Define the ord()s for the possible chars
        numbers_ord = list(range(48, 58))
        upper_ord = list(range(65, 91))
        lower_ord = list(range(97, 123))
        
        # Create a final list to choose characters from
        final_choice_list = []
        
        if Bomb.UPPERCASE in case_mode:
            final_choice_list += upper_ord
            
        if Bomb.LOWERCASE in case_mode:
            final_choice_list += lower_ord
            
        if Bomb.NUMBERCASE in case_mode:
            final_choice_list += numbers_ord
        
        final_string = ''
        while length != 0:
            final_string += chr(random.choice(final_choice_list))
            length -= 1
        
        return final_string
    
    def random_serial():
        serial = ''
        
        # Should have list of serial elements to make it easier to parse
        parse_list = []
        
        # Format: '15.01.2-1a (ver. NCQ)'
        # I'd make a function to do this but it likely not be used often
        to_add = Bomb.random_string(2, [Bomb.NUMBERCASE])
        serial += to_add  + '.'
        parse_list.append(to_add)
        
        to_add = Bomb.random_string(3, [Bomb.NUMBERCASE])
        serial += to_add + '.'
        parse_list.append(to_add)
        
        to_add = Bomb.random_string(case_mode = [Bomb.NUMBERCASE])
        serial += to_add + '-'
        parse_list.append(to_add)
        
        to_add = Bomb.random_string(case_mode = [Bomb.LOWERCASE])
        serial += to_add
        parse_list.append(to_add)
        
        to_add = Bomb.random_string(case_mode = [Bomb.NUMBERCASE])
        serial += to_add
        parse_list.append(to_add)
        
        return serial, parse_list
    
    def update_defused(self):
        
        temp_dict = {}
        for module in self.bomb_modules:
            temp_dict[module[0]] = module[1].is_defused
        
        return temp_dict
    
    def add_strike(self):
        self.strikes += 1
    
    def make_modules(self, amount, serial_parse):
        module_list = []
        
        counter = 0
        
        # FOR ONE OF EACH
        no_index_list = random.sample(Modules.Modules.module_list, k = 4)
        
        index_list = []
        for module in no_index_list:
            index_list.append((counter, module(serial_parse)))
            counter += 1
            
        return index_list
        
        
        
        # FOR RANDOM
        '''
        while amount != 0:
            
            module = random.choice(Modules.Modules.module_list)
            
            if inspect.getfullargspec(module).args == ['self', 'serial_parse']:
                module_list.append((counter, module(self.serial_parse)))
            else:
                module_list.append((counter, module()))
            
            counter += 1
            amount -= 1
            
        return module_list
        '''
            