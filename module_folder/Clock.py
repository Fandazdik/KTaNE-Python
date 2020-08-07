import random
import ClockRoman
from datetime import datetime



class Clock:
        
    def __init__(self, serial_parse = ''): # serial parse if necessary
        
        self.details = {}
        
        self.displayed = ''
        self.correct = ''
        self.is_defused = False
        
        Clock.create_new(self)
        Clock.parse(self, self.details)
        
    # MECHANICS HERE
    def rand_bool():
        return bool(random.randrange(2))
    
    
    def create_new(self):
        
        # Create random details
        details_dict = {}
        #Symbols - 0:Arabic, 1:Roman, 2:Alpha
        details_dict['symbols'] = random.randrange(2)
        details_dict['spacer_is_dash'] = Clock.rand_bool()
        details_dict['brackets'] = Clock.rand_bool()
        
        details_dict['pretext'] = random.randrange(3)
        details_dict['pretext_capitals'] = Clock.rand_bool()
        details_dict['padding'] = random.randrange(5)
        details_dict['24hour'] = Clock.rand_bool()
        details_dict['seconds'] = Clock.rand_bool()
        
        self.details = details_dict
        
        # Figure out hours
        hours = 0
        hours += details_dict['symbols'] * 4
        if details_dict['spacer_is_dash']:
            hours += 2
        
        if not details_dict['brackets']:
            hours += 1
        
        # Figure out minutes
        minutes = 0
        minutes += details_dict['pretext'] * 20
        minutes += details_dict['padding'] * 4
        if details_dict['24hour']:
            minutes += 2
        
        if details_dict['seconds']:
            minutes += 1
        
        # Figure out extras
        
        if details_dict['pretext_capitals']:
            
            hours += 12 #MAKE TIME PM
        
        # Namely converting the text
        
        # Check if one digit
        if hours/10 < 1:
            hours = '0' + str(hours)
            
        if minutes/10 < 1:
            minutes = '0' + str(minutes)
        
        self.correct = str(hours) + ':' + str(minutes)
    
    
    def parse(self, details_dict):
        
        suffix = 'PM'
        
        time_now = datetime.now()
        hours = time_now.hour
        minutes = time_now.minute
        seconds = time_now.second
        
        '''
        details_dict['24hour'] = Clock.rand_bool()
        '''
        
        # Check if 12 or 24 hour before (Note that it's already given in 12 hour
        if not details_dict['24hour']:
            if hours >= 12:
                suffix = 'PM'
                hours -= 12
            else:
                suffix = 'AM'
            
        
        final_string = ''
        baseline_list = [hours, minutes]

            
        
        # Add seconds if seconds is True
        if details_dict['seconds']:
            
            baseline_list.append(seconds)
            
            
        # Create symbols for time
        if details_dict['symbols'] == 1:
            baseline_list = [ClockRoman.toRoman(time) for time in baseline_list]
            
        elif details_dict['symbols'] == 2:
            baseline_list = [[chr(int(i) + 65) for i in str(element)] for element in baseline_list]
            
        else:
            baseline_list = [str(i) for i in baseline_list]
        
        # Add spacer
        if details_dict['spacer_is_dash']:
            spacer = '-'
        else:
            spacer = ':'
            
        final_string = spacer.join(baseline_list)
        
        # Check if 12 or 24 hour (Note that it's already given in 12 hour
        if not details_dict['24hour']:
            final_string += ' ' + suffix
        
        # Check for brackets
        if details_dict['brackets']:
            final_string = '[' + final_string + ']'
        
        # Add padding around time
        pad_level = details_dict['padding']
        while pad_level != 0:
            final_string = '#' + final_string + '#'
            pad_level -= 1
            
        # Create pretext
        if details_dict['pretext'] == 0:
            pretext = 'time:'
        elif details_dict['pretext'] == 1:
            pretext = 'the time is:'
        else:
            pretext = 'the time is now:'
        
        if details_dict['pretext_capitals']:
            pretext = pretext.upper()
        
        final_string = pretext + '\n' + final_string
        
        self.displayed = final_string
            
        
    def correct_XXX():
        pass
    
    
    def defused(self):
        self.is_defused = True
