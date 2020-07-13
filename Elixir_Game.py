import time, random, math, turtle,CharacterBuilder, Login_Welcome, Dog_Profile, moves,json, questions, Enemy_Data

class Elixir_Game():
####    characterData = Login_Welcome.Character_check()
##    name = characterData[0][0]
##    find_file = open(name+"'s moves.txt" , "r")
##    save = find_file.read()
##    charactermoves = json.loads(save)
##    dogname = characterData[1][0]
##    find_file = open(dogname + ".txt" , "r")
##    save = find_file.read()
##    dogdata = json.loads(save)
##    dogname = dogdata[0][0]
##    find_file = open(dogname + "'s moves.txt" , "r")
##    save = find_file.read()
##    dogmoves = json.loads(save)
##    StorageIncorrect = int()
##    DataRepIncorrect = int()
##    RobustProgIncorrect = int()
##    SysArchIncorrect = int()
##    NetworksIncorrect = int()
    def __init__(self,characterData,name,charactermoves,dogname,dogdata,dogmoves,StorageIncorrect,DataRepIncorrect,RobustProgIncorrect,SysArchIncorrect,NetworksIncorrect):
        self.characterData = characterData
        self.name = characterData[0][0]
        self.HP = characterData[0][1]
        self.Attack = characterData[0][2]
        self.Defence = characterData[0][3]
        self.Speed = characterData[0][4]
        self.Type = characterData[0][5]
        self.weakest_subject = characterData[0][6]
        self.character_moves = charactermoves
        self.dogdata = dogdata
        self.dogname = dogdata[0][0]
        self.dogHP = dogdata[0][1]
        self.dogattack = dogdata[0][2]
        self.dogdefence = dogdata[0][3]
        self.dogspeed = dogdata[0][4]
        self.dogtype = dogdata[0][5]
        self.dog_moves = dogmoves
        self.StorageQuestions = questions.Storage()
        self.DataRepQuestions = questions.DataRep()
        self.RobustProgrammingQuestions = questions.RobustProgramming()
        self.SysArchQuestions = questions.SystemsArchitecture()
        self.NetworkQuestions = questions.Networks()
        self.StorageIncorrect = 0
        self.DataRepIncorrect = 0
        self.RobustProgIncorrect = 0
        self.SysArchIncorrect = 0
        self.NetworksIncorrect = 0
        self.total = 0
    def type(str):
        for letter in str:
            print(letter, end='')
            time.sleep(0.035)
        print("\n")
    def START(self,name,dogname):
        print("")
        print("____________________________________________________")
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
            print("\n")
        type("Intro:\n"+self.name+"'s Village has been bedridden with a mysterious virus. A perilous task was bestowed upon "+self.name+": In order to rid the village of suffering, "+self.name+" needs to find the 5 ingredients required to create an elixir that will act as an antidote to counteract the virus. Without hesitation "+self.name+" set off accompanied by their dog named "+self.dogname+", to find the ingredients.")
    def FirstChapter(self,name):
        print("____________________________________________________")
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
            print("\n")
        type("Location 1: Binary Berry Cave")
        type("...")
        type(self.name+" arrived at the first location. A cave containing Binary Berries guarded by an enemy.\nHowever, the entrance was blocked off by multiple walls.\nEach wall contains a lock that can only be opened by answering the questions that are specified on each wall.")
    def SecondChapter(self,name):
        print("____________________________________________________")
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
            print("\n")
        type("Location 2: Binary Tree Forest")
        type("...")
        type(self.name+" arrived at the second location. A large forest containing many binary trees which are the prime location to find the raspberries needed to make a Raspberry Pi. \nHowever the raspberries are found on the highest point of the binary trees. \nIn order to get to the raspberries "+self.name+" needs to climb the binary trees, each binary tree has a computer science problem located at it's peak. If answered corretly the berries will detach, if too many are answered incorrectly "+name+" will fall out of the tree.")
    def ThirdChapter(self,name):
        print("____________________________________________________")
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
            print("\n")
        type("Location 3: World Wide Spider Web")
        type("...")
        type(self.name+" arrived at the third location. The root of the large web that covers the globe. \nThe webs that the spiders produce contain proteins and amino acids. To find the nodes on each web that contain the highest volume of amino acids "+self.name+" needs to do a breadth-first search and then traverse to the nodes. \nHowever, on each node their is a spider that is present, which will ask "+self.name+" a question.")
    def FourthChapter(self,name):
        print("____________________________________________________")
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
            print("\n")
        type("Location 4: The Cloud")
        type("...")
        type(self.name+" & "+self.dogname+" have taken to the skies at the penultimate location. The cloud storage system is a large warehouse in the clouds that holds the data of every citizen. \nThe storage system is kept cool by hydro cooling pads. Within each cooling pad is a chemical needed to create the elixir. \nIn order to disable the cooling pads a series of questions needs to be answered.")
    def FifthChapter(self,name):
        print("____________________________________________________")
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
            print("\n")
        type("Location 5: Central Processing Square")
        type("...")
        type(self.name+" is almost at their final location. Central Processing Square is the busiest place in the globe, people and data commute in from the Memory Address Bus to RAM street, as well as the Memory Data Bus from RAM's square. \nThe last ingredient is by far the most difficult to get. The ingredient requires "+self.name+" to get to ACC Ltd. To get to ACC Ltd. "+self.name+" Program Counter Lane then to Memory Address Road, to RAM street by the Memory Address Bus. The to Memory Data Road by the Memory Data Bus. And finally to ACC Ltd. by the Current Instruction Register Train.\nHowever to board the buses and the train a number of questions will need to be answered.")
    def getFirstQuestions(self):
        Q1 = self.StorageQuestions[random.randint(0,5)]
        Q2 = self.DataRepQuestions[random.randint(0,5)]
        Q3 = self.RobustProgrammingQuestions[random.randint(0,5)]
        Q4 = self.SysArchQuestions[random.randint(0,5)]
        Q5 = self.NetworkQuestions[random.randint(0,5)]
        Questions = [Q1,Q2,Q3,Q4,Q5]
        return Questions
    def totalQuestions(self,total):
        self.total = total + 1
    def askQuestions(self,Questions,total):
        self.total = self.totalQuestions(self,total)
        flag = True
        user_answers = []
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
            print("\n")
        stepper = 0
        StorageIncorrect = 0
        DataRepIncorrect = 0
        RobustProgIncorrect = 0
        SysArchIncorrect = 0
        NetworksIncorrect = 0

        for each in range(5):
            flag = True
            while flag:
                    type(Questions[each][0])
                    type(Questions[each][3])
                    type(Questions[each][4])
                    type(Questions[each][5])
                    type(Questions[each][6])
                    print("")
                    user_response = input("Which is the correct answer?").lower()
                    while user_response != "a" and user_response != "b" and user_response != "c" and user_response != "d":
                        user_response = input("Enter a valid response. Which is the correct answer?").lower()
                        continue
                    flag = False
                    user_answers.append(user_response)
                    continue
        for each in range(len(user_answers)):
                        if user_answers[each] != Questions[each][1]:
                            topic = Questions[each][2]
                            if topic == "Storage":
                                StorageIncorrect = StorageIncorrect + 1
                                continue
                            elif topic == "Data Representation":
                                DataRepIncorrect = DataRepIncorrect + 1
                                continue
                            elif topic == "Robust Programming":
                                RobustProgIncorrect = RobustProgIncorrect + 1
                                continue
                            elif topic == "Systems Architecture":
                                SysArchIncorrect = SysArchIncorrect + 1
                                continue
                            elif topic == "Networks":
                                NetworksIncorrect = NetworksIncorrect + 1
                                continue
        self.totalQuestions(self,total)
        progress = StorageIncorrect + DataRepIncorrect + RobustProgIncorrect + SysArchIncorrect + NetworksIncorrect
        self.StorageIncorrect = self.StorageIncorrect + StorageIncorrect
        self.DataRepIncorrect = self.DataRepIncorrect + DataRepIncorrect
        self.RobustProgIncorrect = self.RobustProgIncorrect + RobustProgIncorrect
        self.SysArchIncorrect = self.SysArchIncorrect + SysArchIncorrect
        self.NetworksIncorrect = self.NetworksIncorrect + NetworksIncorrect
        return progress
    def DetermineWeakestSubject(self,characterData):
        if characterData[0][7] > 1:
            for each in range(5):
                if characterData[2][each][0] == "Storage":
                    self.StorageIncorrect = self.StorageIncorrect + characterData[2][each][1]
                    continue
                elif characterData[2][each][0] == "Data Representation":
                    self.DataRepIncorrect = self.DataRepIncorrect + characterData[2][each][1]
                    continue
                elif characterData[2][each][0] == "Robust Programming":
                    self.RobustProgIncorrect = self.RobustProgIncorrect + characterData[2][each][1]
                    continue
                elif characterData[2][each][0] == "Systems Architecture":
                    self.SysArchIncorrect = self.SysArchIncorrect + characterData[2][each][1]
                    continue
                elif characterData[2][each][0] == "Networks":
                    self.NetworksIncorrect = self.NetworksIncorrect + characterData[2][each][1]
                    continue

        topics = [["Robust Programming",self.RobustProgIncorrect],["Systems Architecture",self.SysArchIncorrect],["Data Representation",self.DataRepIncorrect],["Storage",self.StorageIncorrect],["Networks",self.NetworksIncorrect]]
        topics.sort(key=lambda x: x[1])#this determines the subject that the target is the weakest and strongest in by ordering the nested array.
        #The array with the lowest number of incorrect questions will be their strongest subject and will be at the index "3".
        #The array that has the highest number of incorrect questions will be their strongest subject and will be at the index "0".
        topics[4].append(0.35)
        topics[3].append(0.25)
        topics[2].append(0.2)
        topics[1].append(0.1)
        topics[0].append(0.1)
        #The four lines of code above are adjusting the probabilities of questions from each subject occuring based on how they have performed with their previous questions
        WeakestSubject = topics[4][0]
        StrongestSubject = topics[0][0]
        characterData[2] = topics
        characterData[0][6] = WeakestSubject
        details = json.dumps(characterData)
        name = characterData[0][0]
        name = str(name)
        file_name = (name)
        open_file = open(file_name + ".txt" , "w")
        open_file.write(details)
        open_file.close()
        return WeakestSubject
    def getNextQuestions(self,characterData):
        name = characterData[0][0]
        find_file = open(name + ".txt" , "r")
        file = find_file.read()
        fileData = json.loads(file)
        PossibleQuestions = []
        for each in range(len(fileData[2])):
            probability = fileData[2][each][2]
            prob = int(probability * 100)
            topic = fileData[2][each][0]
            for each in range(prob):
                if topic == "Storage":
                    Question = self.StorageQuestions[random.randint(0,5)]
                    PossibleQuestions.append(Question)
                elif topic == "Robust Programming":
                    Question = self.RobustProgrammingQuestions[random.randint(0,5)]
                    PossibleQuestions.append(Question)
                elif topic == "Data Representation":
                    Question = self.DataRepQuestions[random.randint(0,5)]
                    PossibleQuestions.append(Question)
                elif topic == "Systems Architecture":
                    Question = self.SysArchQuestions[random.randint(0,5)]
                    PossibleQuestions.append(Question)
                elif topic == "Networks":
                    Question = self.NetworkQuestions[random.randint(0,5)]
                    PossibleQuestions.append(Question)
        Questions = []
        for each in range(5):
            Question = PossibleQuestions[random.randint(0,99)]
            Questions.append(Question)
        return Questions
    def getEnemy(self,name):
        FullAdder = Enemy_Data.Full_Adder(name)
        ApachePig = Enemy_Data.Apache_Pig(name)
        OracleRaptor = Enemy_Data.Oracle_Raptor(name)
        SharkSearch = Enemy_Data.Shark_Search(name)
        WebGoat = Enemy_Data.Web_Goat(name)
        enemies = [FullAdder, ApachePig, OracleRaptor, SharkSearch, WebGoat]
        enemy = enemies[random.randint(0,4)]
        return enemy
    def Type_Properties(self,stats,enemy,name):
             def type(str):
                for letter in str:
                 print(letter, end='')
                 time.sleep(0.035)
             print("\n")
             Attack = stats[0][2]
             name = stats[0][0]
             if stats[0][5]== "Psychic":
                if enemy[5] == "Brawler":
                    Attack = 1.25*(Attack)
                    type(name + " has the type advantage. Their attack has increased\n")
                elif enemy[5] == "Sword Fighter":
                    Attack = 0.75*(Attack)
                    type(name + " has the type disadvantage. Their attack has decreased\n")
                return Attack

             elif stats[0][5] == "Brawler":
                if enemy[5] == "Projectile Based":
                    Attack = 1.25*(Attack)
                    type(name + " has the type advantage. Their attack has increased\n")
                if enemy[5] == "Psychic":
                    Attack = 0.75*(Attack)
                    type(name + " has the type disadvantage. Their attack has decreased\n")
                return Attack

             elif stats[0][5] == "Projectile Based":
                if enemy[5] == "Sword Fighter":
                    Attack = 1.25*(Attack)
                    type(name + " has the type advantage. Their attack has increased\n")
                if enemy[5] == "Brawler":
                    Attack = 0.75*(Attack)
                    type(name + " has the type disadvantage. Their attack has decreased\n")
                return Attack

             elif stats[0][5] == "Sword Fighter":
                if enemy[5] == "Psychic":
                    Attack= 1.25*(Attack)
                    type(name + " has the type advantage. Their attack has increased\n")
                if enemy[5] == "Projectile Based":
                    Attack = 0.75*(Attack)
                    type(name + " has the type disadvantage. Their attack has decreased\n")
                return Attack
             else:
                tempAttack = Attack
                return tempAttack
    def pick_move(self,moves):
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
            print("\n")
        letters = ["A.)","B.)","C.)","D.)","E.)"]
        print("\n")
        for each in range(len(moves)):
            print(letters[each]+moves[each][0])
        type("\nWhich move would you like to use?")
        move_choice = input("Which move would you like to use?").lower()
        while move_choice != "a" and move_choice != "b" and move_choice != "c" and move_choice != "d" and move_choice != "e":
            print("Please choose a valid move option.")
            move_choice = self.pick_move(self,moves)
        if move_choice == "a":
            move = moves[0]
            return move
        elif move_choice == "b":
            move = moves[1]
            return move
        elif move_choice == "c":
            move = moves[2]
            return move
        elif move_choice == "d":
            move = moves[3]
            return move
        elif move_choice == "e":
            move = moves[4]
            return move
    def pick_dog_move(self,dog_moves):
        move = dog_moves[random.randint(0,4)]
        return move
    def getMoveStatement(self,move):
        move_statement = move[3]
        return move_statement
    def damage_calculator(self,enemy,AttackBoosted,characterData,damage_dealer,move):
        if damage_dealer == "enemy":
            defence = self.characterData[0][3]
            offence = enemy[1]
            damage = (((2*10*offence)/defence)+2)
            return damage
        elif damage_dealer == "user":
            defence = enemy[2]
            offence = AttackBoosted
            Power = move[1]
            damage = ((((offence+Power)*10)/defence)+10)
            return damage
    def deal_damage(self,damage,HP):
        HP = HP - damage
        if HP <= 0:
            HP = 0
        return HP
    def checkHP(self,HP):
        if HP == 0:
            return True
        else:
            return False
