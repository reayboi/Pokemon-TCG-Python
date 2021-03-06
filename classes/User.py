from datetime import date
from classes.Deck import *
from classes.Deck_UI import *
from misc_functions import *
from classes.config import *

class User():
    def __init__(self, username="", matches_won=0, matches_lost=0, date_joined=00-00-00, favourite_pokemon="", email_addr="", active_deck=""):
        self.username = username
        self.matches_won = matches_won
        self.matches_lost = matches_lost
        self.date_joined = date_joined
        self.favourite_pokemon = favourite_pokemon
        self.email_addr = email_addr
        self.active_deck = active_deck
    
    def __str__(self):
        return f"username: {self.username}\nmatches won: {self.matches_won}\nmatches lost: {self.matches_lost}\ndate joined: {self.date_joined}\nfavourite pokemon: {self.favourite_pokemon}\nemail address: {self.email_addr}\nactive deck: {self.active_deck}\n"

    def get_username(self):
        return self.username
    
    def set_username(self, username):
        self.username = username

    def update_wins(self):
        self.matches_won += 1

    def update_losses(self):
        self.matches_lost += 1 
    
    def update(self):
        #TO DO
        pass

    def load_user_data(self):
            file = open("data/player_data.txt", "r")
            lines = file.readlines()
            for line in lines:
                username, matches_won, matches_lost, date_joined, favourite_pokemon, email_addr, active_deck = line.strip().split(",")
                if (self.username in username):
                    self.matches_won = matches_won
                    self.matches_lost = matches_lost
                    self.date_joined = date_joined
                    self.favourite_pokemon = favourite_pokemon
                    self.email_addr = email_addr
                    self.active_deck = active_deck
                    break
                else:
                    print("username not found")
            file.close()


    def create_user_data(self, fav_poke, email):
        today = date.today()
        self.date_joined = today.strftime("%d-%m-%Y")
        self.favourite_pokemon = fav_poke
        self.email_addr = email
    
    def update_to_file(self):
        file = open("data/player_data.txt", "wr")
        lines = file.readlines()
        for line in lines:
            username, matches_won, matches_lost, date_joined, favourite_pokemon, email_addr, active_deck = line.strip().split(",")
            if (self.username in username):
                username = self.username
                matches_won = self.matches_won
                matches_lost = self.matches_lost
                date_joined = self.date_joined
                favourite_pokemon = self.favourite_pokemon
                email_addr = self.email_addr
                active_deck = self.active_deck
                file.write(f"{username},{matches_won},{matches_lost},{date_joined},{favourite_pokemon},{email_addr},{active_deck}")
            else:
                print("username not found")
            file.close()