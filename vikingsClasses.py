#!/usr/bin/python
import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength
    
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength) 
        self.name = name

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
 
    def vikingAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        saxon_status = random_saxon.receiveDamage(random_viking.strength)

        # remove dead saxon from the army
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        
        return saxon_status
    
    def saxonAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        viking_status = random_viking.receiveDamage(random_saxon.strength)

        # remove dead saxon from the army
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)

        return viking_status

    def showStatus(self):
        # your code here
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."

