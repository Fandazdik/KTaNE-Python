import random
from colorama import Fore, Back
class ColorMath:
        
    def __init__(self, serial_parse): # serial parse if necessary

        self.symbol_dict = ColorMath.create_symbol_dict(serial_parse)             
        temp_colors = ColorMath.create_colors(self, serial_parse)
        self.displayed = temp_colors[1]
        self.correct = str(temp_colors[2])
        self.is_defused = False

    
    RED, YELLOW, BLUE, GREEN = range(4)
    colors = [RED, YELLOW, BLUE, GREEN]
    
    def create_symbol_dict(serial_parse):
        symbol_dict = {}
        if int(serial_parse[-1]) % 2 == 1: #last symbol is odd
            symbol_dict = {0:'+', 1:'-', 2:'*', 3:'/'}
            
        elif int(serial_parse[1]) > 500: #First two digits are larger than 50
            symbol_dict = {0:'-', 1:'+', 2:'/', 3:'*'}
            
        elif serial_parse[-2] in ['a', 'e', 'i', 'o', 'u']:
            symbol_dict = {0:'/', 1:'*', 2:'-', 3:'+'}
            
        else:
            symbol_dict = {0:'*', 1:'/', 2:'+', 3:'-'}
        
        return symbol_dict
            
        
    
    # MECHANICS HERE
    def create_colors(self, serial_parse):
        num_length = random.randrange(3,8)
        
        # Create random colors and numbers
        display_num_list = [(random.randrange(1, 10), random.choice(ColorMath.colors)) for i in range(num_length)]
        
        print(display_num_list)
        
        # Create Coloured display
        color_display = ''
        for item in display_num_list:
            if item[1] == 0:
                color_display += Back.RED + ' ' + str(item[0]) + ' ' + Back.RESET
            if item[1] == 1:
                color_display += Back.YELLOW + ' ' + str(item[0]) + ' ' + Back.RESET
            if item[1] == 2:
                color_display += Back.BLUE + ' ' + str(item[0]) + ' ' + Back.RESET
            if item[1] == 3:
                color_display += Back.GREEN + ' ' + str(item[0]) + ' ' + Back.RESET
        
        # Parse the random list
        final_num = []
        no_color_display = ''
        for item in display_num_list:
            # Add first number to no color display
            no_color_display += str(item[0])
            
            final_num.append(str(item[0]))
            final_num.append(self.symbol_dict[item[1]])
        final_num.append(serial_parse[-1])
        
        
        
        eval_statement = ''.join(final_num)
        print(eval_statement)
        
        answer = eval(eval_statement)
        
        if answer < 0:
            answer *= -1
        
        answer = round(answer)
        
        print(color_display)
        print(answer)
        
        return no_color_display, color_display, answer
    
    
    def defused(self):
        self.is_defused = True

