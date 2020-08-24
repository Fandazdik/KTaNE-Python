import random
from colorama import Fore, Back
class afg:
    # What species (0 (Rabbit), 1(Feline), 2(Canine))
    # Animal name in name
    # Reference to quality of animal
    # Reference to food animal eats

    species_dict = {
        0: 'LEPOR',
        1: 'FEL',
        2: 'CAN',
        3: 'MUR'
    }

    animal_names = [
                         {   
                            # Leporines
                            
                            'Peter Rabbit': (0, True, False, False),
                            'Bunnicula': (0, True, False, False),
                            'March Hare': (0, True, False, False),
                            'Buster Bunny': (0, True, False, False),
                            'Bugs Bunny': (0, True, False, False),
                            'Lola Bunny': (0, True, False, False),
                            'Judy Hopps': (0, True, True, False),
                            'Hopsalot': (0, False, True, False),
                            'Buster Baxter': (0, False, False, False),
                            'Lille Skutt': (0, False, False, False),
                            'Pupu Tupuna': (0, False, False, False),
                            'Jaxxon': (0, False, False, False),
                            'Schnuffel': (0, False, False, False),
                            'Anais Watterson': (0, False, False, False),
                            'Richard Watterson': (0, False, False, False),
                            'Mr Herriman': (0, False, False, False),
                            'Barnaby Screwloose': (0, False, False, False),
                            'Monomi': (0, False, False, False),
                            'The Noid': (0, False, False, False),
                            'Trix': (0, False, False, False)
                            },
                            
                            # Felines
                            {
                            'MC Scat Cat': (1, True, False, False),
                            'Bubsy Bobcat': (1, True, False, False),
                            'Tigger': (1, True, False, False),
                            'Cheshire Cat': (1, True, False, False),
                            'Topcat': (1, True, False, False),
                            'Pink Panther': (1, True, False, False),
                            'Chester Cheetah': (1, True, False, False),
                            'Tony Tiger': (1, True, False, False),
                            'Scratchy': (1, False, True, False),
                            'Garfield': (1, False, False, False),
                            'Gumball Watterson': (1, False, False, False),
                            'Nicole Watterson': (1, False, False, False),
                            'Blinx': (1, False, False, False),
                            'Shere Khan': (1, False, False, False),
                            'Bagheera': (1, False, False, False),
                            'Richard Parker': (1, False, False, False),
                            'Nermal': (1, False, False, False),
                            'Stimpy': (1, False, False, False),
                            'Pusheen': (1, False, False, False)
                            },
                            
                            # Canines
                        {
                            'Muttley': (2, True, False, False),
                            'Puppycorn': (2, True, False, False),
                            'Duggee': (2, True, False, False),
                            'Mr Peanutbutter': (2, False, False, True),
                            'Huckleberry Hound': (2, True, False, False),
                            'Sam the Sheepdog': (2, True, False, False),
                            'Droopy': (2, False, True, False),
                            'Snoopy': (2, False, True, False),
                            'Hong Kong Phooey': (2, False, False, False),
                            'Scooby Doo': (2, False, False, False),
                            'Balto': (2, False, False, False),
                            'Gromit': (2, False, False, False),
                            'Mr Peabody': (2, False, False, False),
                            'Akamaru': (2, False, False, False),
                            'Brian Griffin': (2, False, False, False),
                            'Ren Hoek': (2, False, False, False),
                            'Ottoperotto': (2, False, False, False),
                            'Bitzer': (2, False, False, False),
                            'Max Goof': (2, False, False, False)
                         },
                            
                            # Murines
                        {
                            'Sally Acorn': (3, False, False, True),
                            'Biggie Cheese': (3, False, False, True),
                            'Mickey Mouse': (3, True, False, False),
                            'Chuck E Cheese': (3, False, False, True),
                            'Danger Mouse': (3, True, False, False),
                            'Geronimo Stilton': (3, False, False, True),
                            'Mortimer Mouse': (3, True, False, False),
                            'Ratigan': (3, True, False, False),
                            'Nigel Ratburn': (3, True, False, False),
                            'Ratbert': (3, True, False, False),
                            'Itchy': (3, False, True, False),
                            'Stuart Little': (3, False, False, False),
                            'Marcel Toing': (3, False, False, False),
                            'Speedy Gonzales': (3, False, False, False),
                            'Master Splinter': (3, False, False, False),
                            'Mappy': (3, False, False, False),
                            'Slowpoke Rodriguez': (3, False, False, False),
                            'Pikachu': (3, False, False, False),
                            'Jaq': (3, False, False, False),
                            'Werner Werman': (3, False, False, False),
                        }
                    ]

    verb_dict = [
        ['FIGHTS', 'CONSUMES', 'NOTICES', 'BITES'],
        ['JUDGES', 'FIGHTS', 'CHASES', 'AVOIDS'],
        ['IGNORES', 'RUNS FROM', 'FIGHTS', 'BEFRIENDS'],
        ['RUNS FROM', 'CHASES', 'BEFRIENDS', 'FIGHTS'],
    ]


        
        

    
    
    
    
    
    
    
class AnimalFight:
        
    def __init__(self, serial_parse): # serial parse if necessary
            
        temp_headline = AnimalFight.create_headline()
        self.displayed = Back.WHITE + Fore.GREEN + ' ' + temp_headline[0][0] + ' ' + Fore.RESET + Back.RESET + '\n' + Back.WHITE + Fore.GREEN + ' ' +temp_headline[0][1] + ' ' + Fore.RESET + Back.RESET
        self.correct = temp_headline[1]
        self.is_defused = False
    
    # MECHANICS HERE
    def create_headline():
        # 0:lepor 1:fel etc.
        two_animals = (random.randrange(0, 4), random.randrange(0, 4))
        
        # Get two random names from keys of animal_names
        two_names = random.choice(list(afg.animal_names[two_animals[0]].keys())), random.choice(list(afg.animal_names[two_animals[1]].keys()))
        
        # Get the detail dicts for each character
        attacker_name = two_names[0]
        defender_name = two_names[1]
        
        # a convoluted way to get the dicts
        attacker_details = afg.animal_names[two_animals[0]][attacker_name]
        defender_details = afg.animal_names[two_animals[1]][defender_name]
        
#        print(attacker_name, defender_name)
#        print(attacker_details, defender_details)
        
        # NOW ADD THE QUALITY NAME FOOD TO CHANGE THE VERB
        
        up = down = left = right = 0
        
        # name
        up = up + 1 if attacker_details[1] else up
        up = up + 1 if defender_details[1] else up
#        print(up)
        
        # quality
        down = down + 1 if attacker_details[2] else down
        down = down + 1 if defender_details[2] else down
#        print(down)
        
        # food
        right = right + 1 if attacker_details[3] else right
        right = right + 1 if defender_details[3] else right
#        print(right)
        
        # wild
        is_wild = random.randrange(2)
        left = 1 if is_wild else 0
        #print(left)
        
        # Account for overflow
        vertical_offset = attacker_details[0] - up + down
        if vertical_offset < 0:
            vertical_offset += 4
        elif vertical_offset > 3:
            vertical_offset -= 4
            
        horizontal_offset = defender_details[0] + right - left
        if horizontal_offset < 0:
            horizontal_offset += 4
        elif horizontal_offset > 3:
            horizontal_offset -= 4
        
        
        correct_verb = afg.verb_dict[vertical_offset][horizontal_offset]
        
         
        # Create display
        correct_answer = defender_name.upper() + ' ' + correct_verb + ' ' + attacker_name.upper()
    
        
        display = [f'{attacker_name} appears!', f'> What will {defender_name} do?']
        if is_wild:
            display[0] = '> A wild ' + display[0]
        else:
            display[0] = '> ' + display[0]
         
        return display, correct_answer
        
    def correct_XXX():
        pass
    
    
    def defused(self):
        self.is_defused = True

