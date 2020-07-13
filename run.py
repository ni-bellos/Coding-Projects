import time, random, math, CharacterBuilder, Login_Welcome, Dog_Profile, moves, json, questions, Elixir_Game,sys
ElixirGame = Elixir_Game.Elixir_Game
characterData = Login_Welcome.Character_check()
Login_Welcome.delete_user()
name = characterData[0][0]
find_file = open(name+"'s moves.txt" , "r")
save = find_file.read()
charactermoves = json.loads(save)
dogname = characterData[1][0]
find_file = open(dogname + ".txt" , "r")
save = find_file.read()
dogdata = json.loads(save)
dogname = dogdata[0][0]
find_file = open(dogname + "'s moves.txt" , "r")
save = find_file.read()
dogmoves = json.loads(save)
StorageIncorrect = int()
DataRepIncorrect = int()
RobustProgIncorrect = int()
SysArchIncorrect = int()
NetworksIncorrect = int()
Game = ElixirGame.__init__(ElixirGame,characterData,name,charactermoves,dogname,dogdata,dogmoves,StorageIncorrect,DataRepIncorrect,RobustProgIncorrect,SysArchIncorrect,NetworksIncorrect)
StorageQs = ElixirGame.StorageQuestions
DataRepQs = ElixirGame.DataRepQuestions
RoProgQs = ElixirGame.RobustProgrammingQuestions
SysArchQs = ElixirGame.SysArchQuestions
NetQs = ElixirGame.NetworkQuestions
total = ElixirGame.total
HP = ElixirGame.HP
dogattack = ElixirGame.dogattack
Attack = ElixirGame.Attack

def Level_One(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves):
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
            print("\n")
        ElixirGame.START(ElixirGame,name,dogname)
        ElixirGame.FirstChapter(ElixirGame,name)
        Questions = ElixirGame.getFirstQuestions(ElixirGame)
        progress = ElixirGame.askQuestions(ElixirGame,Questions,total)
        while progress > 2:
            type("\n"+name+" answered too many questions wrong and the entrance to the cave was sealed shut. \n"+name+" needs to try again.\n")
            progress = ElixirGame.askQuestions(ElixirGame,Questions,total)
            continue
        weakestsubject = ElixirGame.DetermineWeakestSubject(ElixirGame,characterData)
###stop = ElixirGame.checkHP(ElixirGame,characterData)
##HP = ElixirGame.HP

##dogattack = ElixirGame.dogattack
##Attack = ElixirGame.Attack
##dogmoves = ElixirGame.dog_moves
##dogname = ElixirGame.dogname



def Battle(stop,HP,dogattack,Attack,dogmoves,dogname):
    enemy = ElixirGame.getEnemy(ElixirGame,name)
    enemyHP = enemy[3]
    def type(str):
        for letter in str:
            print(letter, end='')
            time.sleep(0.035)
        print("\n")
    type("\nA hostile "+enemy[0]+" appeared out of nowhere! The "+enemy[0]+" launched an attack!\n")
    while stop == False:
        character_speed = ElixirGame.Speed
        enemy_speed = enemy[4]
        if character_speed >= enemy_speed:
            damage_dealer = "user"
            move = ElixirGame.pick_dog_move(ElixirGame,dogmoves)
            dogattack = ElixirGame.Type_Properties(ElixirGame,dogdata,enemy,dogname)
            move_statement = ElixirGame.getMoveStatement(ElixirGame,move)
            type(move_statement)
            damage = ElixirGame.damage_calculator(ElixirGame,enemy,dogattack,dogdata,damage_dealer,move)
            enemyHP = ElixirGame.deal_damage(ElixirGame,damage,enemyHP)
            stop = ElixirGame.checkHP(ElixirGame,enemyHP)
            if stop == True:
                continue
            move = ElixirGame.pick_move(ElixirGame,charactermoves)
            Attack = ElixirGame.Type_Properties(ElixirGame,characterData,enemy,name)
            move_statement = ElixirGame.getMoveStatement(ElixirGame,move)
            type(move_statement)
            damage = ElixirGame.damage_calculator(ElixirGame,enemy,Attack,characterData,damage_dealer,move)
            enemyHP = ElixirGame.deal_damage(ElixirGame,damage,enemyHP)
            stop = ElixirGame.checkHP(ElixirGame,enemyHP)
            if stop == True:
                continue
            damage_dealer = "enemy"
            SPmove = 0
            damage = ElixirGame.damage_calculator(ElixirGame,enemy,Attack,characterData,damage_dealer,SPmove)
            type(enemy[6])
            HP = ElixirGame.deal_damage(ElixirGame,damage,HP)
            stop = ElixirGame.checkHP(ElixirGame,enemyHP)
            continue
        else:
            damage_dealer = "enemy"
            SPmove = 0
            damage = ElixirGame.damage_calculator(ElixirGame,enemy,Attack,characterData,damage_dealer,SPmove)
            type(enemy[6])
            HP = ElixirGame.deal_damage(ElixirGame,damage,HP)
            stop = ElixirGame.checkHP(ElixirGame,enemyHP)
            if stop == True:
                continue
            damage_dealer = "user"
            move = ElixirGame.pick_dog_move(ElixirGame,dogmoves)
            dogattack = ElixirGame.Type_Properties(ElixirGame,dogdata,enemy,dogname)
            move_statement = ElixirGame.getMoveStatement(ElixirGame,move)
            type(move_statement)
            damage = ElixirGame.damage_calculator(ElixirGame,enemy,dogattack,dogdata,damage_dealer,move)
            enemyHP = ElixirGame.deal_damage(ElixirGame,damage,enemyHP)
            stop = ElixirGame.checkHP(ElixirGame,enemyHP)
            if stop == True:
                continue
            move = ElixirGame.pick_move(ElixirGame,charactermoves)
            Attack = ElixirGame.Type_Properties(ElixirGame,characterData,enemy,name)
            move_statement = ElixirGame.getMoveStatement(ElixirGame,move)
            type(move_statement)
            damage = ElixirGame.damage_calculator(ElixirGame,enemy,Attack,characterData,damage_dealer,move)
            enemyHP = ElixirGame.deal_damage(ElixirGame,damage,enemyHP)
            stop = ElixirGame.checkHP(ElixirGame,enemyHP)
            continue
    if HP == 0:
        type("\n"+name+" and "+dogname+" have been defeated!\n")
        type("..........")
        type("\n"+name+" and "+dogname+" mustered up the courage to get up and try again!\n")
        stop = False
        HP = ElixirGame.HP
        enemyHP = enemy[3]
        dogattack = ElixirGame.dogattack
        Attack = ElixirGame.Attack
        dogmoves = ElixirGame.dog_moves
        dogname = ElixirGame.dogname
        Battle(stop,HP,dogattack,Attack,dogmoves,dogname)
    else:
        type("\n"+name+" and "+dogname+" have defeated the "+enemy[0]+"!\n")
        type("\nOnwards to the next location!\n")






def Level_Two(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves):
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
            print("\n")
        ElixirGame.SecondChapter(ElixirGame,name)
        Questions = ElixirGame.getNextQuestions(ElixirGame,characterData)
        progress = ElixirGame.askQuestions(ElixirGame,Questions,total)
        while progress > 2:
            type("\n"+name+" answered too many questions wrong and fell out of the binary tree. \n"+name+" needs to try again.\n")
            progress = ElixirGame.askQuestions(ElixirGame,Questions,total)
            continue
        weakestsubject = ElixirGame.DetermineWeakestSubject(ElixirGame,characterData)




def Level_Three(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves):
        def type(str):
                for letter in str:
                    print(letter, end='')
                    time.sleep(0.035)
                print("\n")
        ElixirGame.ThirdChapter(ElixirGame,name)
        Questions = ElixirGame.getNextQuestions(ElixirGame,characterData)
        progress = ElixirGame.askQuestions(ElixirGame,Questions,total)
        while progress > 2:
            type("\n"+name+" answered too many questions wrong and fell out of the web. \n"+name+" needs to try again.\n")
            progress = ElixirGame.askQuestions(ElixirGame,Questions,total)
            continue
        weakestsubject = ElixirGame.DetermineWeakestSubject(ElixirGame,characterData)




def Level_Four(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves):
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
            print("\n")
        ElixirGame.FourthChapter(ElixirGame,name)
        Questions = ElixirGame.getNextQuestions(ElixirGame,characterData)
        progress = ElixirGame.askQuestions(ElixirGame,Questions,total)
        while progress > 2:
            type("\n"+name+" answered too many questions wrong and the system malfunctioned. \n"+name+" needs to try again.\n")
            progress = ElixirGame.askQuestions(ElixirGame,Questions,total)
            continue
        weakestsubject = ElixirGame.DetermineWeakestSubject(ElixirGame,characterData)



def Level_Five(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves):
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
            print("\n")
        ElixirGame.FifthChapter(ElixirGame,name)
        Questions = ElixirGame.getNextQuestions(ElixirGame,characterData)
        progress = ElixirGame.askQuestions(ElixirGame,Questions,total)
        while progress > 2:
            type("\n"+name+" answered too many questions wrong and was kicked off. \n"+name+" needs to try again.\n")
            progress = ElixirGame.askQuestions(ElixirGame,Questions,total)
            continue
        weakestsubject = ElixirGame.DetermineWeakestSubject(ElixirGame,characterData)
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
        print("\n")
        type("\n"+name+"has successfully gathered all the ingredients needed to make the elixir and returned home. Along with "+name+" they combined the ingredients and fed the medicine to the village people, restoring peace to the village.\n")
        type("\n.....\n")
        time.sleep(1)
        type("\nCongratulations! You have completed the game!\n")



stop = ElixirGame.checkHP(ElixirGame,characterData)
##HP = ElixirGame.HP
##enemyHP = enemy[3]
##dogattack = ElixirGame.dogattack
##Attack = ElixirGame.Attack
##dogmoves = ElixirGame.dog_moves
##dogname = ElixirGame.dognamed

if characterData[0][7] == 1:
    Level_One(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves)
    Battle(stop,HP,dogattack,Attack,dogmoves,dogname)
    characterData[0][7] = 2
    details = json.dumps(characterData)
    name = str(name)
    file_name = (name)
    open_file = open(file_name + ".txt" , "w")
    open_file.write(details)
    open_file.close()
    next_level = input("Would you like to start the next level or would you like to save and quit? If you would like to start the next level enter 'next' or to save and quit enter 'quit'").lower()
    while next_level != "next" and next_level != "quit":
        print("Enter a valid response")
        next_level = input("Would you like to start the next level or would you like to save and quit? If you would like to start the next level enter 'next' or to save and quit enter 'quit'").lower()
        continue
    if next_level == "quit":
        sys.exit()
if characterData[0][7] == 2:
    Level_Two(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves)
    Battle(stop,HP,dogattack,Attack,dogmoves,dogname)
    characterData[0][7] = 3
    details = json.dumps(characterData)
    name = str(name)
    file_name = (name)
    open_file = open(file_name + ".txt" , "w")
    open_file.write(details)
    open_file.close()
    next_level = input("Would you like to start the next level or would you like to save and quit? If you would like to start the next level enter 'next' or to save and quit enter 'quit'").lower()
    while next_level != "next" and next_level != "quit":
        print("Enter a valid response")
        next_level = input("Would you like to start the next level or would you like to save and quit? If you would like to start the next level enter 'next' or to save and quit enter 'quit'").lower()
        continue
    if next_level == "quit":
        sys.exit()

if characterData[0][7] == 3:
    Level_Three(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves)
    Battle(stop,HP,dogattack,Attack,dogmoves,dogname)
    characterData[0][7] = 4
    details = json.dumps(characterData)
    name = str(name)
    file_name = (name)
    open_file = open(file_name + ".txt" , "w")
    open_file.write(details)
    open_file.close()
    next_level = input("Would you like to start the next level or would you like to save and quit? If you would like to start the next level enter 'next' or to save and quit enter 'quit'").lower()
    while next_level != "next" and next_level != "quit":
        print("Enter a valid response")
        next_level = input("Would you like to start the next level or would you like to save and quit? If you would like to start the next level enter 'next' or to save and quit enter 'quit'").lower()
        continue
    if next_level == "quit":
        sys.exit()

if characterData[0][7] == 4:
    Level_Four(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves)
    Battle(stop,HP,dogattack,Attack,dogmoves,dogname)
    characterData[0][7] = 5
    details = json.dumps(characterData)
    name = str(name)
    file_name = (name)
    open_file = open(file_name + ".txt" , "w")
    open_file.write(details)
    open_file.close()
    next_level = input("Would you like to start the next level or would you like to save and quit? If you would like to start the next level enter 'next' or to save and quit enter 'quit'").lower()
    while next_level != "next" and next_level != "quit":
        print("Enter a valid response")
        next_level = input("Would you like to start the next level or would you like to save and quit? If you would like to start the next level enter 'next' or to save and quit enter 'quit'").lower()
        continue
    if next_level == "quit":
        sys.exit()

if characterData[0][7] == 5:
    Level_Five(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves)
    Battle(stop,HP,dogattack,Attack,dogmoves,dogname)
    characterData[0][7] = 6
    details = json.dumps(characterData)
    name = str(name)
    file_name = (name)
    open_file = open(file_name + ".txt" , "w")
    open_file.write(details)
    open_file.close()
    next_level = input("Would you like to start the next level or would you like to save and quit? If you would like to start the next level enter 'next' or to save and quit enter 'quit'").lower()
    while next_level != "next" and next_level != "quit":
        print("Enter a valid response")
        next_level = input("Would you like to start the next level or would you like to save and quit? If you would like to start the next level enter 'next' or to save and quit enter 'quit'").lower()
        continue
    if next_level == "quit":
        sys.exit()

if characterData[0][7] == 6:
    flag = True
    while flag:
        def type(str):
            for letter in str:
                print(letter, end='')
                time.sleep(0.035)
        print("\n")
        type("You have completed the game.\nNow you have the ability to choose any level and battle two enemies after completing the level.\n")
        time.sleep(0.75)
        print("A.)Level One")
        time.sleep(0.75)
        print("B.)Level Two")
        time.sleep(0.75)
        print("C.)Level Three")
        time.sleep(0.75)
        print("D.)Level Four")
        time.sleep(0.75)
        print("E.)Level Five")
        time.sleep(2)
        level = input("Input the letter that corresponds with the level that you would like to play.").lower()
        while level != "a" and level != "b" and level != "c" and level != "d" and level != "e":
            print("Enter a valid letter.")
            level = input("Input the letter that corresponds with the level that you would like to play.").lower()
            continue
        if level == "a":
            Level_One(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves)
        elif level == "b":
            Level_Two(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves)
        elif level == "c":
            Level_Three(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves)
        elif level == "d":
            Level_Four(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves)
        elif level == "e":
            Level_Five(name,dogname,StorageQs, DataRepQs, RoProgQs, SysArchQs, NetQs,total,charactermoves)
        Battle(stop,HP,dogattack,Attack,dogmoves,dogname)
        Battle(stop,HP,dogattack,Attack,dogmoves,dogname)
        next_level = input("Would you like to continue playing or would you like to save and quit? If you would like to start the next level enter 'next' or to save and quit enter 'quit'").lower()
        while next_level != "next" and next_level != "quit":
            print("Enter a valid response")
            next_level = input("Would you like continue playing or would you like to save and quit? If you would like to start the next level enter 'next' or to save and quit enter 'quit'").lower()
            continue
        if next_level == "quit":
            flag = False
            continue
    sys.exit()#