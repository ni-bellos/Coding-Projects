import time, random, math, turtle, ctypes, tkinter, json
class moves():
    def __init__(self):
        self.name = name
        self.enemy_name = enemy_name
    def psychic_moveset(self,name):
        psychic_moves = []
        def Psykick(self,name):
            move_name = "PsyKick"
            Power = 40
            MoveType = "Psychic"
            move_statement = name+" gave the enemy a quick kick to the head full of psychic energy.\n"
            cost = 0
            Psykick = (move_name,name,Power,MoveType,move_statement,cost)
            return Psykick
        def Brainwave(self,name):
            move_name = "Brainwave"
            Power = 60
            MoveType = "Psychic"
            move_statement = name+" released a powerful brainwave.\n"
            cost = 5
            Brainwave = (move_name,Power,MoveType,move_statement,cost)

            return Brainwave
        def PsychicSurge(self,name):
            move_name = "Psychic Surge"
            Power = 80
            MoveType = "Psychic"
            move_statement = name+" used telekinesis gave the enemy an excruciating migraine.\n"
            cost = 10
            PsychicSurge = (move_name,Power,MoveType,move_statement,cost)
            return PsychicSurge
        def MindOverMatter(self,name):
            move_name = "Mind Over Matter"
            Power = 100
            MoveType = "Psychic"
            move_statement = name+" used their brain to levitate then enemy whilst encasing them in rock and then proceeded to violently slam them down.\n"
            cost = 15
            MindOverMatter = (move_name,Power,MoveType,move_statement,cost)
            return MindOverMatter
        def BrainStorm(self,name):
            move_name = "Brain Storm"
            Power = 120
            MoveType = "Psychic"
            move_statement = name+" unleashed powerful surges of energy in the form of a storm from their brain.\n"
            cost = 20
            BrainStorm = (move_name,Power,MoveType,move_statement,cost)
            return BrainStorm
        Psykick = Psykick(self,name)
        Brainwave = Brainwave(self,name)
        PsychicSurge = PsychicSurge(self,name)
        MindOverMatter = MindOverMatter(self,name)
        BrainStorm = BrainStorm(self, name)
        psychic_moves.append(Psykick)
        psychic_moves.append(Brainwave)
        psychic_moves.append(PsychicSurge)
        psychic_moves.append(MindOverMatter)
        psychic_moves.append(BrainStorm)
        return psychic_moves

    def brawler_moveset(self,name):
        brawler_moves = []
        def RapidJab(self,name):
            move_name = "Rapid Jab"
            Power = 40
            MoveType = "Brawler"
            move_statement = name+" punched his opponent continuously at a high speed.\n"
            cost = 0
            RapidJab = (move_name,Power,MoveType,move_statement,cost)
            return RapidJab
        def HardKnuckle(self,name):
            move_name = "Hard Knuckle"
            Power = 60
            MoveType = "Brawler"
            move_statement = name+" struck the enemy in the gut with a hard reinforced knuckle.\n"
            cost = 5
            HardKnuckle = (move_name,Power,MoveType,move_statement,cost)
            return HardKnuckle
        def MeteorPunch(self,name):
            move_name = "Meteor Punch"
            Power = 80
            MoveType = "Brawler"
            move_statement = name+" took to the sky and struck his opponent in the skull with the force of a meteor.\n"
            cost = 10
            MeteorPunch = (move_name,Power,MoveType,move_statement,cost)
            return MeteorPunch
        def SwiftCounter(self,name):
            move_name = "Swift Counter"
            Power = 100
            MoveType = "Brawler"
            move_statement = name+" performed a powerful yet quick counter with perfect timing.\n"
            cost = 15
            SwiftCounter = (move_name,Power,MoveType,move_statement,cost)
            return SwiftCounter
        def BruteForceBarrage(self,name):
            move_name = "Brute Force Barrage"
            Power = 120
            MoveType = "Brawler"
            move_statement = name+" used their full power to perform a vigorous all-out attack bombarding the enemy with a flurry of strenuous kicks, punches, elbows, knees and headbutts.\n"
            cost = 20
            BruteForceBarrage = (move_name,Power,MoveType,move_statement,cost)
            return BruteForceBarrage
        RapidJab = RapidJab(self,name)
        HardKnuckle = HardKnuckle(self,name)
        MeteorPunch = MeteorPunch(self,name)
        SwiftCounter = SwiftCounter(self,name)
        BruteForceBarrage = BruteForceBarrage(self, name)
        brawler_moves.append(RapidJab)
        brawler_moves.append(HardKnuckle)
        brawler_moves.append(MeteorPunch)
        brawler_moves.append(SwiftCounter)
        brawler_moves.append(BruteForceBarrage)
        return brawler_moves

    def Projectile_Based_moveset(self,name):
        projectile_based_moves = []
        def RapidFire(self,name):
            move_name = "Rapid Fire"
            Power = 40
            MoveType = "Projectile Based"
            move_statement = name+" fired shots in rapid succession at the enemy.\n"
            cost = 0
            RapidFire = (move_name,Power,MoveType,move_statement,cost)
            return RapidFire
        def PlasmaBall(self,name):
            move_name = "Plasma Ball"
            Power = 60
            MoveType = "Projectile Based"
            move_statement = name+" charged up energy and released it in the form of a large spherical projectile.\n"
            cost = 5
            PlasmaBall= (move_name,Power,MoveType,move_statement,cost)
            return PlasmaBall
        def BulletStorm(self,name):
            move_name = "Bullet Storm"
            Power = 80
            MoveType = "Projectile Based"
            move_statement = name+" sprayed a multitude of bullets into the air that rained down like torrential rain.\n"
            cost = 10
            BulletStorm = (move_name,Power,MoveType,move_statement,cost)
            return BulletStorm
        def AmmunitionPrison(self,name):
            move_name = "Ammunition Prison"
            Power= 100
            MoveType = "Projectile Based"
            move_statement = name+" released swarms of bullets attatched to strings which wrapped around the enemy restraining them.\n"
            cost = 15
            AmmunitionPrison = (move_name,Power,MoveType,move_statement,cost)
            return AmmunitionPrison
        def AcidDownpour(self,name):
            move_name = "Acid Downpour"
            Power = 120
            MoveType = "Projectile Based"
            move_statement = name+" lept into the sky and charged up their cannon. When fully charged "+name+"'s cannon unleashed an immense beam of corrosive acid.\n"
            cost = 20
            AcidDownpour = (move_name,Power,MoveType,move_statement,cost)
            return AcidDownpour
        RapidFire = RapidFire(self,name)
        PlasmaBall = PlasmaBall(self,name)
        BulletStorm = BulletStorm(self,name)
        AmmunitionPrison = AmmunitionPrison(self,name)
        AcidDownpour = AcidDownpour(self, name)
        projectile_based_moves.append(RapidFire)
        projectile_based_moves.append(PlasmaBall)
        projectile_based_moves.append(BulletStorm)
        projectile_based_moves.append(AmmunitionPrison)
        projectile_based_moves.append(AcidDownpour)
        return projectile_based_moves

    def Sword_Fighter_Moveset(self,name):
        sword_fighter_moves = []
        def SliceAndDice(self,name):
            move_name = "Slice and Dice"
            Power = 40
            MoveType = "Sword Fighter"
            move_statement = name+" drew their sword and slashed the enemy twice.\n"
            cost = 0
            SliceAndDice = (move_name,Power,MoveType,move_statement,cost)
            return SliceAndDice
        def MetalScreech(self,name):
            move_name = "Metal Screech"
            Power = 60
            MoveType = "Sword Fighter"
            move_statement = name+" dragged their blades across each other and created an unbearable screech.\n"
            cost = 5
            MetalScreech = (move_name,Power,MoveType,move_statement,cost)
            return MetalScreech
        def SplitSecondSlash(self,name):
            move_name = "Split Second Slash"
            Power = 80
            MoveType = "Sword Fighter"
            move_statement = name+" drew their sword and instantly deposited it back in the holster their movements were too fast to follow.\n"
            cost = 10
            SplitSecondSlash = (move_name,Power,MoveType,move_statement,cost)
            return SplitSecondSlash
        def CrescentMoonKatana(self,name):
            move_name = "Cresent Moon Katana"
            Power = 100
            MoveType = "Sword Fighter"
            move_statement = "An ominous night smothered the battlefield as "+name+" held their blade up in the air and carved through their opponent slicing them with a cresent motion and the force of a falling moon.\n"
            cost = 15
            CresentMoonKatana = (move_name,Power,MoveType,move_statement,cost)
            return CresentMoonKatana
        def RealmWrecker(self,name):
            move_name = "Realm Wrecker"
            Power = 120
            MoveType = "Sword Fighter"
            move_statement = name+" drew all their and concentrated all their energy into them unleashing a large unified slash tearing through the air and ground as far as the eye could see.\n"
            cost = 20
            RealmWrecker = (move_name,Power,MoveType,move_statement,cost)
            return RealmWrecker
        SliceAndDice = SliceAndDice(self,name)
        MetalScreech = MetalScreech(self,name)
        SplitSecondSlash = SplitSecondSlash(self,name)
        CrescentMoonKatana = CrescentMoonKatana(self,name)
        RealmWrecker = RealmWrecker(self, name)
        sword_fighter_moves.append(SliceAndDice)
        sword_fighter_moves.append(MetalScreech)
        sword_fighter_moves.append(SplitSecondSlash)
        sword_fighter_moves.append(CrescentMoonKatana)
        sword_fighter_moves.append(RealmWrecker)
        return sword_fighter_moves

    def all_around_type_moveset(self,name):
        all_around_moves = []
        def AuraBeam(self,name):
            move_name = "Aura Beam"
            Power = 40
            MoveType = "All-Around Type"
            move_statement = name+" released a blast of energy from their palms.\n"
            cost = 0
            AuraBeam = (move_name,Power,MoveType,move_statement,cost)
            return AuraBeam
        def RoadRoller(self,name):
            move_name = "Road Roller"
            Power = 60
            MoveType = "All-Around Type"
            move_statement = name+" rushed head first into the enemy like an enraged bull and steamrolled over them.\n"
            cost = 5
            RoadRoller = (move_name,Power,MoveType,move_statement,cost)
            return RoadRoller
        def RollingThunder(self,name):
            move_name = "Rolling Thunder"
            Power = 80
            MoveType = "All-Around Type"
            move_statement = "Impulses of electricity shot around "+name+"'s body. "+name+" leapt high into the air and descended onto the enemy like a cannonball.\n"
            cost = 10
            RollingThunder = (move_name,Power,MoveType,move_statement,cost)
            return RollingThunder
        def SoulBlade(self,name):
            move_name = "Soul Blade"
            Power = 100
            MoveType = "All-Around Type"
            move_statement = name+" channeled all his energy into his hand and materialised a gargantuan sword and brought it down tearing through the surroundings.\n"
            cost = 15
            SoulBlade = (move_name,Power,MoveType,move_statement,cost)
            return SoulBlade
        def FightingSpirit(self,name):
            move_name = "Fighting Spirit"
            Power = 120
            MoveType = "All-Around Type"
            move_statement = name+" summoned all his strength into his chest and unleashed a large warrior resembling an Angel which brought down a beam of blinding light that scorched the surrounding expanse of land as far as the eye could see.\n"
            cost = 20
            FightingSpirit = (move_name,Power,MoveType,move_statement,cost)
            return FightingSpirit
        AuraBeam = AuraBeam(self,name)
        RoadRoller = RoadRoller(self,name)
        RollingThunder = RollingThunder(self, name)
        SoulBlade = SoulBlade(self,name)
        FightingSpirit = FightingSpirit(self,name)
        all_around_moves.append(AuraBeam)
        all_around_moves.append(RoadRoller)
        all_around_moves.append(RollingThunder)
        all_around_moves.append(SoulBlade)
        all_around_moves.append(FightingSpirit)
        return all_around_moves