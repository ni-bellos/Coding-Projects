import CharacterBuilder, json
import Dog_Moves
class Dog():
    Attack = int()
    Defence = int()
    HP = int()
    Speed = int()
    name = str()
    Type = str()
    def __init__(self, Attack, Defence, HP, Speed, name):
        CharacterBuilder.__init__(self)
        self.Attack = Attack
        self.Defence = Defence
        self.HP = HP
        self.Speed = Speed
        self.name = name
        self.Type = Type
    def dog_profile(self, name, Attack, Defence, HP, Speed, Type):
        name = input("What is your dog's name going to be?")
        print("")
        Attack = 90
        Defence = 50
        HP = 150
        Speed = 105
        Type = "All-Around Type"
        print("Your dog's name is: ", name)
        print("Your dog's attack is: ", Attack)
        print("Your dog's defence is: ", Defence)
        print("Your dog's HP is: ", HP)
        print("Your dog's Speed is: ", Speed)
        print("Your dog's type is: ", Type)
        dog_profile = [[name,HP,Attack,Defence,Speed,Type],[5]]
        dog_moves = Dog_Moves.moveset(self,name)
        """Saving the dog's details"""
        details = json.dumps(dog_profile)
        name = dog_profile[0][0]
        name = str(name)
        file_name = (name)
        open_file = open(file_name + ".txt" , "w")
        open_file.write(details)
        open_file.close()
        """opening the file"""
        find_file = open(name + ".txt" , "r")
        save = find_file.read()
        saveV2 = json.loads(save)
        """Saving the dog's moves"""
        details = json.dumps(dog_moves)
        name = dog_profile[0][0]+"'s moves"
        name = str(name)
        file_name = (name)
        open_file = open(file_name + ".txt" , "w")
        open_file.write(details)
        open_file.close()
        """opening the file"""
        find_file = open(name + ".txt" , "r")
        save = find_file.read()
        saveV2 = json.loads(save)
        return dog_profile
Attack = int()
Defence = int()
HP = int()
Speed = int()
name = str()
Type = "Brawler"
