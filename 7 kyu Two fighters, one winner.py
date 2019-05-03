
# 7 kyu Two fighters, one winner.

class fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack


def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here
    
  if fighter2 == first_attacker:
     fightera = fighter2
     fighterb = fighter1
  else:
     fightera = fighter1
     fighterb = fighter2
 
  
  x = fighter1.health/fighter2.damage_per_attack
  y = fighter2.health/fighter1.damage_per_attack
  
  if x == y:
     return first_attacker
  elif x > y:
     return fightera.name
  else:
     return fighterb.name