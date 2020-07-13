def moveset(self,name):
        dog_moves = []
        def Scratch(self,name):
            move_name = "Scratch"
            Power = 30
            MoveType = "Brawler"
            move_statement = name+" scratched the enemy.\n"
            Scratch = (move_name, Power, MoveType,move_statement)
            return Scratch
        def Bite(self,name):
            move_name = "Bite"
            Power = 35
            MoveType = "Brawler"
            move_statement = name+" bit the enemy.\n"
            Bite = (move_name, Power, MoveType,move_statement)
            return Bite
        def Tackle(self,name):
            move_name = "Tackle"
            Power = 40
            MoveType = "Brawler"
            move_statement = name+" ran at full speed and tackled the opponent.\n"
            Tackle = (move_name, Power, MoveType,move_statement)
            return Tackle
        def Gnaw(self,name):
            move_name = "Gnaw"
            Power = 45
            MoveType = "Brawler"
            move_statement = name+" sank it's jaws into the enemy and gnawed away at them.\n"
            Gnaw = (move_name, Power, MoveType,move_statement)
            return Gnaw
        def Nocturnus(self,name):
            move_name = "Nocturnus"
            Power = 120
            MoveType = "All-Around Type"
            move_statement = "An ominous night swallowed the battlefield "+name+" howled at the full moon and transformed into a feral werewolf. Along with her partner she launched an remorseless all-out massacre with claws, fangs, punches, kicks and tackles.\n"
            Nocturnus = (move_name, Power, MoveType,move_statement)
            return Nocturnus
        Scratch = Scratch(self,name)
        Bite = Bite(self,name)
        Tackle = Tackle(self,name)
        Gnaw = Gnaw(self,name)
        Nocturnus = Nocturnus(self,name)
        dog_moves.append(Scratch)
        dog_moves.append(Bite)
        dog_moves.append(Tackle)
        dog_moves.append(Gnaw)
        dog_moves.append(Nocturnus)
        return dog_moves