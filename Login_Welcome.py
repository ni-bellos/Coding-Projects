import json, os
from CharacterBuilder import CharacterBuilder
def Character_check():
    repeat = True
    while repeat:
        begin = input("Do you already have a character?").lower()
        if begin == "yes" or begin == "y":
            name = input("Enter the name of your character:")
            try:
                open(name + ".txt" , "r")
                print("Character Data Found")
                repeat = False
            except IOError:
                print("Character Not Found")
                continue
            find_file = open(name + ".txt" , "r")
            save = find_file.read()
            saveV2 = json.loads(save)
            print("Your character's name is " + saveV2[0][0])
            print("Your character's HP is", saveV2[0][1])
            print("Your character's Attack is", saveV2[0][2])
            print("Your character's Defense is", saveV2[0][3])
            print("Your character's Speed is", saveV2[0][4])
            print("Your character's type is " + saveV2[0][5])
            print("Your weakest subject is " + saveV2[0][6])
            print("Your dog's name is ", saveV2[1][0])
            check = input("Is the data above correct?").lower()
            print("____________________________________________________")
            if check == "yes" or check == "y":
                return saveV2
            else:
                Character_check()
                return saveV2

        elif begin == "no" or begin == "n":
            name = str()
            start = True
            Character = []
            Type = ""
            Stat_points = 0
            Attack = int()
            Defence = int()
            HP = int()
            Speed = int()
            Assignment_Choice = ""
            name = str()
            weakest_subject = ""
            newCharacter = CharacterBuilder(name)
            newCharacter = CharacterBuilder.CharacterCustomisation(name,Attack,Defence,HP,Speed,Type,Character,start,Stat_points,weakest_subject)
            newCharacter[0].append(1)
            """This is saving the users details"""
            details = json.dumps(newCharacter)
            name = newCharacter[0][0]
            name = str(name)
            file_name = (name)
            open_file = open(file_name + ".txt" , "w")
            open_file.write(details)
            open_file.close()
            """opening the file"""
            find_file = open(name + ".txt" , "r")
            save = find_file.read()
            saveV2 = json.loads(save)
            return saveV2
        else:
            print("Enter a valid response.")
            print("")
            Character_check()

def delete_user():
    delete = input("Would you like to delete a user?").lower()
    if delete == "yes" or delete == "y" or delete == "yeah":
        name = input("Enter the name of the user you would like to delete (keep in mind that the names are case sensitive).")
        confirmation = input("Are you sure you would like to delete the character "+name).lower()
        if confirmation == "yes" or confirmation == "y" or confirmation == "yeah":
            os.remove(name+".txt")
            os.remove(name+"'s moves.txt")
        else:
            delete_user()