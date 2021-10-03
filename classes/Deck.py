import json
import random

class Deck:
    def __init__(self, active_deck="", id_list=[]):
        self.active_deck = active_deck
        self.id_list = id_list
    
    def __str__(self):
        return f"active deck: {self.active_deck}\n{self.id_list}"

    def add_card():
        pass

    def remove_card():
        pass

    def get_cards():
        #for card object in list print card details
        pass
    
    def get_decks(self, filename):
        print("Available Decks: ")
        file = open(filename,encoding='utf-8')
        data = json.load(file)
        decks = []
        for i in data:
            decks.append(i['name'])
        file.close()
        return decks

    def get_active_deck(self):
        return self.active_deck

    def set_active_deck(self, list):
        for decks in list:
            print(decks)
        print("Enter the name of the deck you want to select: ")
        active_deck = ""
        while active_deck not in list:
            active_deck = input("Enter deck name: ")
            try:
                active_deck = str(active_deck)
            except ValueError:
                print("You entered an invalid value!")
        self.active_deck = active_deck

    def load_deck(self, filename):
        file = open(filename,encoding='utf-8')
        data = json.load(file)
        for set in data:
            if set['name'] == self.active_deck:
                for x in set['cards']:
                    count = int(x['count'])
                    for n in range(count):
                        self.id_list.append(x['id'])
        file.close()

    def shuffle_deck(self):
        random.shuffle(self.id_list)

    def pop_card(self):
        return self.id_list.pop(0)

    def append_to_deck(self, card):
        self.id_list.append(card)

    def draw_number_of_cards(self, number):
        cards = []
        for x in range(number):
            cards.append(self.id_list.pop(0))
        return cards

            
        
    


    '''
    f = open('set1.json',encoding='utf-8')
    data = json.load(f)
    for i in data:
        #print(i['name]) gets the names of the sets in this file
        #if i['name] == 'setname':
            #get info
        print(i['cards'])
    f.close()
    '''