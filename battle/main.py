from classes.game import Person, bcolors
from classes.magic import Spell

# Create Black Magic
fire = Spell("Fire", 10, 100,"black")
thunder = Spell("Thunder", 10, 100,"black")
blizzard = Spell("Blizzard", 10, 100,"black")
meteor = Spell("Meteor", 20, 200,"black")
quake = Spell("Quake", 14, 140,"black")

# Create White Magic
cure = Spell("Cure", 12, 120, "White Magic")
cura = Spell("Cura", 18, 200, "White Magic")

# Instantiate People
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure,cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0


# Old Code for Player Magic
'''
magic = [{"name": "Fire", "cost":10, "dmg": 60},
         {"name": "Thunder", "cost":12, "dmg": 80},
         {"name": "Blizzard", "cost":10, "dmg": 60}]
'''


print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("========================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("choose magic:")) - 1

        # magic_dmg = player.generate_spell_damage(magic_choice)
        # spell = player.get_spell_name(magic_choice)
        # cost = player.get_spell_mp_cost(magic_choice)

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "White Magic":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKGREEN + "\n" + spell.name + " deals ", str(magic_dmg), " points of damage " + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy Attacked for", enemy_dmg, "Player HP", player.get_hp())

    print("---------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC )
    print("Player HP", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)

    print("Player MP", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC )

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False

    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You Lost" + bcolors.ENDC)
        running = False


#print("You chose", player.get_spell_name(index))

#running = False

# Code for generate_spell_damage#
'''
print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
print(player.generate_spell_damage(2))
'''

# Code for generate_damage#
''' 
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
'''