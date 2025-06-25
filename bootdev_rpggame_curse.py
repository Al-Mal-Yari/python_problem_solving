"""
Curse
An enemy's weapons can be cursed so that they don't deal as much damage.

Assignment
Complete the curse function. It accepts a weapon_damage parameter and returns two values:

The lesser_cursed damage: reduce the input weapon_damage from 100% to 50% (50% reduction).
The greater_cursed damage: reduce the input weapon_damage from 100% to 25% (75% reduction).
A greater curse is more powerful than a lesser curse, so it reduces the damage more.
"""

def curse(weapon_damage: int) -> int:
    lesser_cursed = weapon_damage * 0.50
    greater_cursed = weapon_damage * 0.75
    return curse

# Don't modify below this line

def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")

def main():
    test(100)
    test(500)
    test(1000)

main()
