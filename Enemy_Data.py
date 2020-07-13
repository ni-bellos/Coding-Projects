import time, random, math, turtle, ctypes, CharacterBuilder, Login_Welcome, tkinter, Dog_Profile
"""all of the name of the enemies are linked to computer science."""
def Full_Adder(name):
    enemy_name = "Full Adder"
    enemy_attack = 15
    enemy_defence = 10
    enemy_hp = 250
    enemy_speed = 45
    enemy_type = "Projectile Based"
    attack_statement = ("\nUsing its internal AND & XOR gates "+enemy_name+" spat out a carry bit at "+name+"!\n")
    Full_Adder = [enemy_name, enemy_attack, enemy_defence, enemy_hp, enemy_speed, enemy_type,attack_statement]
    return Full_Adder

def Web_Goat(name):
    enemy_name = "Web Goat"
    enemy_attack = 25
    enemy_defence = 15
    enemy_hp = 340
    enemy_speed = 30
    enemy_type = "Psychic"
    attack_statement = ("\n"+enemy_name+" used a server-side attack on "+name+"!\n")
    Web_Goat = [enemy_name, enemy_attack, enemy_defence, enemy_hp, enemy_speed, enemy_type, attack_statement]
    return Web_Goat

def Oracle_Raptor(name):
    enemy_name = "Oracle Raptor"
    enemy_attack = 50
    enemy_defence = 18
    enemy_hp = 225
    enemy_speed = 75
    enemy_type = "Brawler"
    attack_statement = ("\n"+enemy_name+" searched through its database. \nThrough SQL injection it dropped a table on "+name+"!\n")
    Oracle_Raptor = [enemy_name, enemy_attack, enemy_defence, enemy_hp, enemy_speed, enemy_type, attack_statement]
    return Oracle_Raptor

def Apache_Pig(name):
    enemy_name = "Apache Pig"
    enemy_attack = 1
    enemy_defence = 25
    enemy_hp = 500
    enemy_speed = 0
    enemy_type = "All-Around Type"
    attack_statement = ("\n"+enemy_name+" threw some mortar data at "+name+"!\n")
    Apache_Pig = [enemy_name, enemy_attack, enemy_defence, enemy_hp, enemy_speed, enemy_type, attack_statement]
    return Apache_Pig

def Shark_Search(name):
    enemy_name = "Shark Search"
    enemy_attack = 50
    enemy_defence = 65
    enemy_hp = 250
    enemy_speed = 100
    enemy_type = "Sword Fighter"
    attack_statement = ("\n"+enemy_name+" used the Shark Search Algorithm.\n "+enemy_name+" found "+name+" and took a large chomp!\n")
    Shark_Search = [enemy_name, enemy_attack, enemy_defence, enemy_hp, enemy_speed, enemy_type, attack_statement]
    return Shark_Search