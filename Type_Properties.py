import Login_Welcome, Enemy_Data, Login_Welcome
def Type_Properties(characterData,specified_enemy):
            characterData[0][2] = Attack
            tempAttack = Attack
            if characterData[][]== "Psychic":
                if Enemy_Data.enemies.enemies_list[specicfied_enemy][5] == "Brawler":
                    Attack = 1.25*(Attack)
                    print(name + "has the type advantage. Their attack has increased")
                elif Enemy_Data.enemies.enemies_list[specicfied_enemy][5] == "Sword Fighter":
                    Attack = 0.75*(Attack)

            elif Type == "Brawler":
                if Enemy_Data.enemies.enemies_list[specicfied_enemy][5] == "Projectile Based":
                    Attack = 1.25*(Attack)
                if Enemy_Data.enemies.enemies_list[specicfied_enemy][5] == "Psychic":
                    Attack = 0.75(Attack)

            elif Type == "Projectile Based":
                if Enemy_Data.enemies.enemies_list[specicfied_enemy][5] == "Sword Fighter":
                    Attack = 1.25*(Attack)
                if Enemy_Data.enemies.enemies_list[specicfied_enemy][5] == "Brawler":
                    SimulatorGame.characterData[0][2] = 0.75*(Attack)

            elif Type == "Sword Fighter":
                if Enemy_Data.enemies.enemies_list[specicfied_enemy][5] == "Psychic":
                    Attack= 1.25*(Attack)
                if Enemy_Data.enemies.enemies_list[specicfied_enemy][5] == "Projectile Based":
                    Attack = 0.75*(Attack)
            return tempAttack

"""add else for all around types"""
"""redesign this in order to make it applicable to multiple characters"""
"""replace attacks with tempAttacks where necessary"""