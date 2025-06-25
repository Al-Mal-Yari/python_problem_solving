"""
Assignment
Complete the get_punched and get_slashed functions. They both take 2 integers as arguments, health and armor.

Complete the get_punched function:
Change the armor parameter to have a default value of 0
Create a damage variable equal to 50 minus the armor - the armor reduces the damage
Create a new_health variable equal to the input health minus damage - we apply the damage
Return new_health
Complete the get_slashed function
Change the armor parameter to have a default value of 0
Create a damage variable equal to 100 minus the armor
Create a new_health variable equal to the input health minus damage
Return new_health
"""

def get_punched(health: int, armor: int = 0) -> int:
  damage = max(50 - armor, 0)
  new_health = max(health - damage, 0)
  return new_health
  
def get_slashed(health: int, armor: int = 0) -> int:
  damage = max(100 - armor, 0)
  new_health = max(health - damage, 0)
  return new_health

# Don't touch below this line


def test(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")


test(400, 5)
test(300, 3)
test(200, 1)

