import random
import sys
import os
import time

monst_names=['Aarakocra','Aboleth','Abominable Yeti','Acolyte','Air Elemental','Allosaurus','Androsphinx','Animated Armor','Ankheg','Ankylosaurus','Ape','Arcanaloth','Archmage','Assassin','Awakened Shrub','Awakened Tree','Axe Beak','Azer','Baboon','Badger','Balor','Bandit','Bandit Captain','Banshee','Barbed Devil','Barlgura','Basilisk','Bat','Bearded Devil','Behir','Beholder','Beholder Zombie','Berserker','Black Bear','Black Dragon Adult','Black Dragon Ancient','Black Dragon Wyrmling','Black Dragon Young','Black Pudding','Blink Dog','Blood Hawk','Blue Dragon Adult','Blue Dragon Ancient','Blue Dragon Wyrmling','Blue Dragon Young','Blue Slaad','Boar','Bone Devil','Bone Naga','Brass Dragon Adult','Brass Dragon Ancient','Brass Dragon Wyrmling','Brass Dragon Young','Bronze Dragon Adult','Bronze Dragon Ancient','Bronze Dragon Wyrmling','Bronze Dragon Young','Brown Bear','Bugbear','Bugbear Chief','Bulette','Bullywug','Cambion','Camel','Carrion Crawler','Cat','Centaur','Chain Devil','Chasme','Chimera','Chuul','Clay Golem','Cloaker','Cloud Giant','Cockatrice','Commoner','Constrictor Snake','Copper Dragon Adult','Copper Dragon Ancient','Copper Dragon Wyrmling','Copper Dragon Young','Couatl','Crab','Crawling Claw','Crocodile','Cult Fanatic','Cultist','Cyclops','Dao','Darkmantle','Death Dog','Death Knight','Death Slaad','Death Tyrant','Deer','Demilich','Deva','Dire Wolf','Displacer Beast','Djinni','Doppelganger','Dracolich','Draft Horse','Dragon Turtle','Dretch','Drider','Drow','Drow Elite Warrior','Drow Mage','Drow Priestess of Lolth','Druid','Dryad','Duergar','Duodrone','Dust Mephit','Eagle','Earth Elemental','Efreeti','Elephant','Elk','Empyrean','Erinyes','Ettercap','Ettin','Faerie Dragon','Fire Elemental','Fire Giant','Fire Snake','Flameskull','Flesh Golem','Flumph','Flying Snake','Flying Sword','Fomorian','Frog','Frost Giant','Galeb Duhr','Gargoyle','Gas Spore','Gelatinous Cube','Ghast','Ghost','Ghoul','Giant Ape','Giant Badger','Giant Bat','Giant Boar','Giant Centipede','Giant Constrictor Snake','Giant Crab','Giant Crocodile','Giant Eagle','Giant Elk','Giant Fire Beetle','Giant Frog','Giant Goat','Giant Hyena','Giant Lizard','Giant Octopus','Giant Owl','Giant Poisonous Snake','Giant Rat','Giant Scorpion','Giant Sea Horse','Giant Shark','Giant Spider','Giant Toad','Giant Vulture','Giant Wasp','Giant Weasel','Giant Wolf Spider','Gibbering Mouther','Githyanki Knight','Githyanki Warrior','Githzerai Monk','Githzerai Zerth','Glabrezu','Gladiator','Gnoll','Gnoll Fang of Yeenoghu','Gnoll Pack Lord','Gnome Deep','Goat','Goblin','Goblin Boss','Gold Dragon Adult','Gold Dragon Ancient','Gold Dragon Wyrmling','Gold Dragon Young','Gorgon','Goristro','Gray Ooze','Gray Slaad','Green Dragon Adult','Green Dragon Ancient','Green Dragon Wyrmling','Green Dragon Young','Green Hag','Green Slaad','Grell','Grick','Grick Alpha','Griffon','Grimlock','Guard','Guardian Naga','Gynosphinx','Half Ogre','Half-Red Dragon Veteran','Harpy','Hawk','Hell Hound','Helmed Horror','Hezrou','Hill Giant','Hippogriff','Hobgoblin','Hobgoblin Captain','Hobgoblin Warlord','Homunculus','Hook Horror','Horned Devil','Hunter Shark','Hydra','Hyena','Ice Devil','Ice Mephit','Imp','Intellect Devourer','Invisible Stalker','Iron Golem','Jackal','Jackalwere','Kenku','Killer Whale','Knight','Kobold','Kraken','Kuo-Toa','Kuo-Toa Archpriest','Kuo-Toa Whip','Lamia','Lemure','Lich','Lion','Lizard','Lizard King/Queen','Lizardfolk','Lizardfolk Shaman','Mage','Magma Mephit','Magmin','Mammoth','Manes','Manticore','Marid','Marilith','Mastiff','Medusa','Merfolk','Merrow','Mezzoloth','Mimic','Mind Flayer','Minotaur','Minotaur Skeleton','Monodrone','Mud Mephit','Mule','Mummy','Mummy Lord','Myconid Adult','Myconid Sovereign','Myconid Sprout','Nalfeshnee','Needle Blight','Night Hag','Nightmare','Noble','Nothic','Nycaloth','Ochre Jelly','Octopus','Ogre','Ogre Zombie','Oni','Orc','Orc Eye of Gruumsh','Orc War Chief','Orog','Otyugh','Owl','Owlbear','Panther','Pegasus','Pentadrone','Peryton','Phase Spider','Piercer','Pit Fiend','Pixie','Planetar','Plesiosaurus','Poisonous Snake','Polar Bear','Pony','Priest','Pseudodragon','Pteranodon','Purple Worm','Quadrone','Quaggoth','Quaggoth Spore Servant','Quasit','Quipper','Rakshasa','Rat','Raven','Red Dragon Adult','Red Dragon Ancient','Red Dragon Wyrmling','Red Dragon Young','Red Slaad','Reef Shark','Remorhaz','Revenant','Rhinoceros','Riding Horse','Roc','Roper','Rug o Smothering','Rust Monster','Saber-Toothed Tiger','Sahuagin','Sahuagin Baron','Sahuagin Priestess','Salamander','Satyr','Scarecrow','Scorpion','Scout','Sea Hag','Sea Horse','Shadow','Shadow Demon','Shadow Dragon','Shambling Mound','Shield Guardian','Shrieker','Silver Dragon Adult','Silver Dragon Ancient','Silver Dragon Wyrmling','Silver Dragon Young','Skeleton','Slaad Tadpole','Smoke Mephit','Solar','Spectator','Specter','Spider','Spined Devil','Spirit Naga','Sprite','Spy','Steam Mephit','Stirge','Stone Giant','Stone Golem','Storm Giant','Succubus/Incubus','Swarm of Bats','Swarm of Insects','Swarm of Poisonous Snakes','Swarm of Quippers','Swarm of Rats','Swarm of Ravens','Tarrasque','Thri-Kreen','Thug','Tiger','Treant','Tribal Warrior','Triceratops','Tridrone','Troglodyte','Troll','Twig Blight','Tyrannosaurus Rex','Ultroloth','Umber Hulk','Unicorn','Vampire','Vampire Spawn','Veteran','Vine Blight','Violet Fungus','Vrock','Vulture','Warhorse','Warhorse Skeleton','Water Elemental','Water Weird','Weasel','Werebear','Wereboar','Wererat','Weretiger','Werewolf','White Dragon Adult','White Dragon Ancient','White Dragon Wyrmling','White Dragon Young','Wight','Will-O-Wisp','Winged Kobold','Winter Wolf','Wolf','Worg','Wraith','Wyvern','Xorn','Yeti','Yochlol','Young Remorhaz','Yuan-Ti Abomination','Yuan-Ti Malison','Yuan-Ti Pureblood','Zombie']
armor_class=[12,17,15,10,15,13,17,18,14,15,12,17,12,15,9,13,11,17,12,10,19,12,15,12,15,15,15,12,13,17,18,15,13,11,19,22,17,18,7,13,12,19,22,17,18,15,11,19,15,18,20,16,17,19,22,17,18,11,16,17,17,15,19,9,13,12,12,16,15,14,16,14,14,14,11,10,12,18,21,16,17,19,11,12,12,13,12,14,18,11,12,20,18,19,13,20,17,14,13,17,14,19,10,20,11,19,15,18,12,16,11,11,16,15,12,12,17,17,12,10,22,18,13,12,15,13,18,14,13,9,12,14,17,14,11,15,16,15,5,6,13,11,12,12,10,13,12,13,12,15,14,13,14,13,11,11,12,12,11,12,14,12,15,13,13,14,11,10,12,13,13,9,18,17,14,17,17,16,15,14,15,15,10,15,17,19,22,17,18,19,19,8,18,19,21,17,18,17,16,12,14,18,12,11,16,18,17,12,18,11,13,15,20,16,13,11,18,17,20,13,15,18,12,15,11,18,11,13,12,14,20,12,12,13,12,18,12,18,13,13,11,13,7,17,12,10,15,15,13,12,11,14,13,9,14,17,18,12,15,11,13,18,12,15,14,12,15,11,10,11,17,12,13,10,18,12,17,13,15,15,18,8,12,11,8,16,13,16,16,18,14,11,13,12,12,16,13,13,15,19,15,19,13,13,12,10,13,13,13,18,16,13,13,13,13,16,10,12,19,22,17,18,14,12,17,13,11,10,15,20,12,14,12,12,16,12,15,14,11,11,13,14,11,12,13,18,15,17,5,19,22,17,18,13,12,12,21,14,12,12,15,15,15,12,10,14,17,17,16,15,12,12,14,13,10,12,25,15,11,12,16,12,13,15,11,15,13,13,19,18,12,16,15,17,12,5,15,10,11,13,14,13,13,11,11,12,12,12,18,20,16,14,14,19,13,13,13,13,13,13,19,12,15,14,15,12,11,8]
monst_hit_points=[13,135,137,9,90,51,199,33,39,68,19,104,99,78,10,59,19,39,3,3,262,11,65,58,110,68,52,1,52,168,180,93,67,19,195,367,33,127,85,22,7,225,481,52,152,123,11,142,58,172,297,16,110,212,444,32,142,34,27,65,94,11,82,15,51,2,45,85,84,114,93,133,78,200,27,4,13,184,350,22,119,97,2,2,19,33,9,138,187,22,39,180,170,187,4,80,136,37,85,161,52,225,19,341,18,123,13,71,45,71,27,22,26,11,17,3,126,200,76,13,313,153,44,85,14,102,162,22,40,93,7,5,17,149,1,138,85,52,1,84,36,45,22,157,13,22,42,4,60,13,85,26,42,4,18,19,45,19,52,19,11,7,52,16,126,26,39,22,13,9,11,67,91,46,38,84,157,112,22,65,49,16,4,7,21,256,546,60,178,114,310,22,127,207,385,38,136,82,127,55,27,75,59,11,11,127,136,30,65,38,11,45,60,136,105,19,11,39,97,5,75,178,45,172,5,180,21,10,21,104,210,3,18,13,90,52,5,472,18,97,65,97,13,135,26,2,78,22,27,40,22,9,126,9,68,229,189,5,127,11,45,75,58,71,76,67,5,27,11,58,97,22,60,7,184,11,112,68,9,45,123,45,3,59,85,110,15,45,93,42,114,1,59,13,59,32,33,32,22,300,1,200,68,2,42,11,27,7,13,247,22,45,45,7,1,110,1,1,256,546,75,178,93,22,195,136,45,13,248,93,33,27,52,22,76,33,90,31,36,1,16,52,1,16,66,178,136,142,13,243,487,45,168,13,10,22,243,39,22,1,110,75,2,27,21,2,126,178,230,66,22,22,36,28,24,24,676,33,32,37,138,11,95,16,13,84,4,136,153,93,67,144,82,58,26,18,104,5,19,22,114,58,1,135,78,35,120,58,200,333,32,135,45,22,7,75,11,26,67,110,73,51,136,93,127,66,40,22]
die_num=[1,2,4,1,2,2,2,1,3,4,1,2,1,1,1,3,1,1,1,1,3,1,1,3,1,2,4,1,1,3,4,4,1,1,2,2,1,2,4,1,1,3,4,1,3,2,1,1,5,2,2,1,2,2,2,1,2,1,2,2,4,1,1,1,1,1,1,2,11,2,2,2,2,3,1,1,1,2,2,1,2,1,1,1,1,1,1,3,2,1,1,1,1,4,1,6,4,2,2,2,1,3,2,3,1,2,1,4,1,6,1,1,1,1,1,1,2,2,3,1,6,3,2,2,1,2,6,1,3,2,2,3,1,3,0,3,2,1,1,3,2,4,2,3,1,1,10,1,2,1,3,1,2,1,1,2,2,1,2,2,1,1,1,1,3,1,2,2,1,1,1,5,5,4,3,2,2,2,1,1,1,1,1,1,1,2,2,1,2,2,3,3,1,2,2,1,2,2,2,1,2,1,2,1,1,2,2,1,2,1,1,1,1,2,3,1,1,2,1,1,2,2,2,1,1,5,2,1,2,2,3,1,1,1,5,2,1,3,1,5,1,2,1,3,1,1,1,1,1,1,2,2,4,2,1,2,2,1,1,1,1,2,1,2,2,2,1,1,1,5,9,4,6,2,5,2,2,2,1,1,2,3,1,2,2,1,1,2,1,1,2,1,1,1,2,1,1,1,0,4,0,4,3,1,1,2,1,1,2,3,1,1,1,1,1,2,0,1,2,2,1,2,2,1,6,2,2,2,4,4,2,1,1,1,2,1,2,2,2,1,1,2,0,2,2,2,2,2,0,2,2,1,2,1,1,1,4,1,1,1,1,1,1,1,2,1,3,3,6,1,0,0,0,0,0,0,4,1,1,1,3,1,4,1,1,1,1,4,1,1,2,4,2,1,2,1,2,1,2,2,2,2,1,2,2,1,1,1,2,2,1,2,1,2,1,2,2,2,4,2,1,2,7,3,4,0,1,1]
die_side=[4,6,6,4,8,10,10,6,6,6,6,4,4,6,4,6,8,8,4,1,8,6,6,6,6,6,6,18,1,0,6,6,12,6,14,14,14,14,9,6,4,10,10,16,10,6,6,8,6,10,10,10,10,10,10,10,10,8,8,8,12,4,14,4,4,1,10,6,6,6,6,10,6,8,4,4,6,10,10,10,10,6,1,4,10,4,6,8,8,6,6,34,20,6,4,6,10,6,6,6,6,10,4,12,6,10,6,6,14,6,8,8,8,4,4,4,8,6,8,6,6,11,8,8,1,6,6,10,6,8,4,4,8,8,0,12,6,6,1,6,8,6,6,10,6,6,6,4,6,6,10,6,6,6,6,4,6,8,6,6,4,4,8,6,10,8,10,4,6,4,6,6,6,6,8,18,10,8,4,6,4,8,4,6,6,10,10,10,10,12,8,6,6,16,19,16,16,8,6,10,6,6,8,4,6,8,8,10,10,4,1,20,10,10,8,10,10,6,10,1,6,8,8,10,6,6,4,4,4,6,8,4,4,6,6,6,4,8,4,6,4,10,4,6,8,1,6,6,6,4,4,6,8,4,8,8,8,6,7,8,8,4,8,10,12,12,4,6,4,6,6,4,4,4,10,4,8,14,8,6,6,6,1,8,8,8,12,8,20,12,8,1,10,6,6,6,8,10,0,6,0,16,6,1,8,4,6,4,4,8,4,6,6,4,1,6,0,1,16,22,16,23,4,8,13,6,8,4,8,8,6,8,10,4,4,4,11,4,4,1,6,6,0,6,6,13,8,6,0,10,10,10,10,6,4,4,18,6,6,1,6,6,1,6,4,4,8,8,6,6,0,0,0,0,0,0,8,6,6,10,6,8,8,4,4,6,4,12,10,8,6,6,4,10,6,8,6,4,6,6,8,6,1,10,6,4,10,8,14,18,14,14,6,8,4,6,4,6,8,6,6,6,6,12,6,0,6,6]
die_bonus=[2,5,7,0,5,4,6,2,3,4,3,3,2,3,-1,4,2,3,-1,0,8,1,3,2,3,4,3,0,2,6,0,0,3,2,7,10,3,5,3,1,2,7,9,4,5,5,1,4,3,6,8,2,4,7,9,3,5,4,2,3,4,1,12,4,2,0,4,4,2,4,4,5,3,8,1,4,2,6,8,2,4,5,0,1,2,2,1,6,6,3,2,9,4,0,0,0,5,3,4,5,4,7,4,7,6,4,2,4,0,2,8,4,2,4,2,2,5,6,5,3,10,5,2,5,0,3,7,2,0,4,2,1,1,6,0,6,5,2,4,6,3,3,2,6,1,2,3,2,4,1,5,3,4,1,1,3,3,2,3,1,4,2,2,1,6,3,2,4,2,3,1,6,6,2,2,7,5,4,2,3,3,3,1,2,2,8,10,4,6,5,7,1,3,8,11,3,6,4,4,2,2,4,4,3,1,4,4,3,3,1,0,5,4,4,5,3,1,2,3,0,4,6,4,5,6,5,1,3,2,3,7,1,2,3,4,3,2,10,1,3,2,3,4,6,3,0,3,2,2,2,1,6,7,4,3,6,4,1,6,8,4,4,3,4,4,4,1,1,2,3,4,4,1,1,5,1,4,6,1,3,5,2,0,4,6,4,3,3,5,4,3,0,5,2,4,2,3,2,0,8,0,12,4,0,5,2,0,2,1,9,1,3,3,3,0,2,0,4,10,14,4,7,3,2,10,4,5,3,9,4,3,1,5,1,4,1,4,1,1,0,2,3,0,2,3,7,4,4,0,8,10,4,6,2,2,2,14,-1,6,0,3,4,0,2,4,3,6,6,9,3,0,0,0,0,0,0,10,1,2,3,6,1,6,1,2,4,1,7,3,5,4,4,3,3,2,8,3,4,4,4,4,3,0,4,3,2,3,2,7,10,3,5,2,0,3,4,4,3,3,4,3,4,2,6,4,0,1,1]

e_1={'HP':0}
e_2={'HP':0}
turn=1
def battle_initiation():
    global e_1
    global e_2
    en_num=2
    while en_num==2:
        e= input('Creature 1 type: ')
        try:
            a=monst_names.index(e) 
            e_2={'name':monst_names[a],'AC':armor_class[a],'HP':monst_hit_points[a],'DN':die_num[a],'DS':die_side[a],'BA':die_bonus[a]}
            en_num= en_num-1
            print('Creature Recorded')
            cls()
        except:
            print('That creature does not exist!')
    while en_num==1:
        e= input('Creature 2 type: ')
        try:
            a=monst_names.index(e) 
            e_1={'name':monst_names[a],'AC':armor_class[a],'HP':monst_hit_points[a],'DN':die_num[a],'DS':die_side[a],'BA':die_bonus[a]}
            en_num= en_num-1
            print('Creature Recorded')
            cls()
        except:
            print('That creature does not exist!')
    total_hp=e_1['HP']+e_2['HP']
            
def battle_simulator():
    turn=1
    first = random.randint(1,2)
    if first==1:
        first=e_1['name']
        turn=int(turn)+1
    first=e_2['name']
    global total_hp
    action='attack'
    def battle():
        global wait
        global turn
        if turn == 1:
            wait = input("How many seconds would you like to read turns? ")
        if turn % 2 == 0:
            print ("Here come the stats...")
            display_stats()
            print (e_1['name'],"will be attacking now! Here comes the swing...")
            if turn % 2 == 0:
                if e_1['HP']>0:
                    hitdie=random.randint(1,20)
                    print(e_1['name'],' rolled a: ', hitdie)
                    if hitdie>=e_2['AC']:
                        en_damage=e_1['BA']
                        rolls=e_1['DN']
                        while rolls>0:
                            die_roll=random.randint(1,e_1['DS'])
                            en_damage+=die_roll
                            rolls-=1
                        print("It's a hit! ",e_1['name']," hit for ", en_damage)
                        e_2['HP']=e_2['HP']-en_damage
                        time.sleep(int(wait))
                        cls()
                        turn=turn+1
                        battle()
                    else:
                        print("It's a miss! The turn passes to",e_2['name'])
                        time.sleep(int(wait))
                        cls()
                        turn=turn+1
                        battle()
                else:
                    print('It appears that',e_1['name'],' no longer has hitpoints!',e_2['name'],'wins the match!')
                    time.sleep(int(wait))
                    cls()
        if turn % 2 != 0:
            print ("Here come the stats...")
            display_stats()
            print (e_2['name'],"will be attacking now! Here comes the swing...")
            if turn % 2 != 0:
                if e_2['HP']>0:
                    hitdie=random.randint(1,20)
                    print(e_2['name'],' rolled a: ', hitdie)
                    if hitdie>=e_1['AC']:
                        en_damage=e_2['BA']
                        rolls=e_2['DN']
                        while rolls>0:
                            die_roll=random.randint(1,e_2['DS'])
                            en_damage+=die_roll
                            rolls-=1
                        print("It's a hit! ",e_2['name']," hit for ", en_damage)
                        e_1['HP']=e_1['HP']-en_damage
                        time.sleep(int(wait))
                        cls()
                        turn=turn+1
                        battle()
                    else:
                        print("It's a miss! The turn passes to",e_1['name'])
                        time.sleep(int(wait))
                        cls()
                        turn=turn+1
                        battle()
                else:
                    print('It appears that',e_2['name'],' no longer has hitpoints!',e_1['name'],'wins the match!')
                    time.sleep(int(wait))
                    cls()
    total_hp=e_1['HP']+e_2['HP']
    battle()

def display_stats():
    print(e_2)
    print(e_1)
def end():
    print ("That's the battle! Thanks for watching!")
def cls():
    cls()           

print ("Welcome to the D&D pit, where you can pit your favorite D&D creatures against each other in a battle to the death!")

battle_initiation()
battle_simulator()


