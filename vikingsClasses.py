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

'''# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here

    def battleCry(self):
        # your code here

    def receiveDamage(self, damage):
        # your code here

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here

    def receiveDamage(self, damage):
        # your code here

# Davicente

class War():
    def __init__(self):
        # your code here

    def addViking(self, viking):
        # your code here
    
    def addSaxon(self, saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here
    
    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here
    pass'''


