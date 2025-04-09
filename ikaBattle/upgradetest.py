
def forgeDamage(lvl):
    if lvl==1:
        return 1.1
    elif lvl==2:
        return 1.1
    elif lvl==3:
        return 1.15
    elif lvl==4:
        return 1.15
    elif lvl==5:
        return 1.2
    else:
        return 1.0

def forgeArmor(lvl):
    if lvl==1:
        return 0
    elif lvl==2:
        return 1
    elif lvl==3:
        return 1
    elif lvl==4:
        return 2
    elif lvl==5:
        return 2
    else:
        return 0

def getSlotSize(Class,portLevel=30):
    if portLevel > 29:
        if Class == "Heavy":
            return 25
        elif Class == "Light":
            return 20
        elif Class == "LongRange":
            return 25
        elif Class == "Artillery":
            return 15
        elif Class == "AntiBomb":
            return 15
        elif Class == "Bomb":
            return 15
        else:
            return -1
    
def getSlotNum(Class,portLevel=30):
    if portLevel > 29:
        if Class == "Heavy":
            return 7
        elif Class == "Light":
            return 6
        elif Class == "LongRange":
            return 7
        elif Class == "Artillery":
            return 5
        elif Class == "AntiBomb":
            return 2
        elif Class == "Bomb":
            return 2
        else:
            return -1

def round(defender: dict, attacker: dict, defForgeLvl, atkForgeLvl, defUpLvl, atkUpLvl, verbose=False, estloss=0):
    def_hp = defender["hp"]
    def_armor = defender["armor"]
    def_unit_size = defender["size"]
    def_forge_armor = forgeArmor(defForgeLvl)
    def_armor_bonus = defUpLvl*2


    off_dmg = attacker["damage"]
    off_dmg_bonus = atkUpLvl*2
    off_forge_dmg = forgeDamage(atkForgeLvl)
    off_unit_size = attacker["size"]
    


    def_field_num = getSlotNum(defender["class"])
    def_field_size = getSlotSize(defender["class"])
    
    off_field_num = getSlotNum(attacker["class"])
    off_field_size = getSlotSize(attacker["class"])
    
    if(verbose):
        deff_slots = [[] for _ in range(def_field_num)]

    def_slots = []
    for s in range(def_field_num):
        slot = []
        for unit in range(int(def_field_size/def_unit_size)):
            slot.append(def_hp)
        def_slots.append(slot)
        if(verbose):
            deff_slots[s]=len(slot)
    #print(def_slots)



    if(verbose):
        atk_slots = [[] for _ in range(off_field_num)]


    off_slots = []
    for s in range(off_field_num):
        slot = []
        for unit in range(int(off_field_size/off_unit_size)):
            slot.append((off_dmg+off_dmg_bonus)*off_forge_dmg)
        
        off_slots.append(slot)

        if(verbose):
            atk_slots[s]=len(slot)

    #print(off_slots)

    if verbose:

        print("\n\tDefender line:\n",deff_slots)
        print("\n\tAttacker line:\n",atk_slots)


    atk_matrix = [[] for _ in range(def_field_num)]

    for os in off_slots:
        for idx,u in enumerate(os):
            atk_matrix[idx%def_field_num].append(u)


    for idx,i in enumerate(atk_matrix):
        #print(i,len(i))
        for dmg in i:
            consumed = False
            for t_idx, target in enumerate(def_slots[idx]):
                if consumed: break
                #print(t_idx,target)
                if target > 0:
                    
                    def_slots[idx][t_idx] = target - (dmg-(def_armor+def_armor_bonus+def_forge_armor))
                    #print(target,def_slots[idx][t_idx],dmg,def_armor+def_armor_bonus+def_forge_armor)
                    consumed = True
                    break

    #print(def_slots)

    losses= [0 for _ in range(def_field_num)]
    for idx,slot in enumerate(def_slots):
        for surv in slot:
            if(surv < 1):
                losses[idx]+=1
            


    print("losses:",losses," - total:",sum(losses))

    if sum(losses) < estloss:
        print("\n\t!!!REDUCED LOSSES!!!")
        return True
    else: return False





ram = {
    "hp":3080,
    "armor":180,
    "damage":1500,
    "size":3,
    "class":"Light"
}

ballista = {
    "hp":3080,
    "armor":280,
    "damage":560,
    "size":2,
    "class":"LongRange"
}

fires = {
    "hp":4380,
    "armor":160,
    "damage":1640,
    "size":2,
    "class":"Heavy"
}

cata = {
    "hp":2960,
    "armor":200,
    "damage":900,
    "size":3,
    "class":"LongRange"
}

mortar = {
    "hp":3080,
    "armor":120,
    "damage":1380,
    "size":4,
    "class":"LongRange"
}

steam = {
    "hp":11520,
    "armor":320,
    "damage":3320,
    "size":5,
    "class":"Heavy"
}

rocket = {
    "hp":1300,
    "armor":120,
    "damage":7600,
    "size":4,
    "class":"Artillery"
}

dive = {
    "hp":2200,
    "armor":120,
    "damage":2460,
    "size":3,
    "class":"Artillery"
}

paddle = {
    "hp":400,
    "armor":0,
    "damage":240,
    "size":1,
    "class":"AntiBomb"
}

carrier = {
    "hp":2800,
    "armor":0,
    "damage":2000,
    "size":5,
    "class":"Bomb"
}


print("\nSteams (DEF)vs(ATK) Steams")
for off_level in range(0,9):
    for deff_level in range(0,9):
        print("\n--------------------------------")
        print("Attacker bonus damage:",off_level*2,"\tDefender bonus armor:",deff_level*2)

        round(carrier,paddle,5,5,deff_level,off_level,True,2)
            








print("--------------------------------")


