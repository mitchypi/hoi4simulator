import random

class Equipment:
    def __init__(self, softAttack,
                 hardAttack, defense, breakthrough,
                 piercing, hardness, armor):  # soft atk, hard atk, defense, brkthrough, piercing, hardness, armor
        # set attributes
        self.softAttack = softAttack
        self.hardAttack = hardAttack
        self.defense = defense
        self.breakthrough = breakthrough
        self.piercing = piercing
        self.hardness = hardness
        self.armor = armor


# soft atk, hard atk, defense, brkthrough, piercing, hardness, armor
infEquipment = Equipment(14, 3, 41, 6, 30.0, 0.1, 0.0)
tankEquipment = Equipment(40, 32, 10, 84, 131.0, 0.98, 130.0)


class Battalion:
    def __init__(self, hp, org, manpowerOptimal, supplyOptimal, manpower, supply):
        self.hp = hp
        self.org = org
        self.manpowerOptimal = manpowerOptimal
        self.supplyOptimal = supplyOptimal
        self.manpower = manpower
        self.supply = supply


friendlySupplyInf = [1000, 500]
friendlySupplyTank = [500, 100]
# org, hp, manpower, supply
infBat = Battalion(25, 60, 1000, 500, friendlySupplyInf[0], friendlySupplyInf[1])
tankBat = Battalion(2, 10, 500, 100, friendlySupplyTank[0], friendlySupplyTank[1])


class Unit:
    def __init__(self, hp, org, manpower, supply, softAttack, hardAttack, defense,
                 breakthrough, piercing, hardness, armor, infBatCount, tankBatCount, manpowerStatus, supplyStatus, experience):
        self.hp = hp
        self.org = org
        self.manpower = manpower
        self.supply = supply
        self.softAttack = softAttack
        self.hardAttack = hardAttack
        self.defense = defense
        self.breakthrough = breakthrough
        self.piercing = piercing
        self.hardness = hardness
        self.armor = armor
        self.infBatCount = infBatCount
        self.tankBatCount = tankBatCount
        self.manpowerStatus = manpowerStatus
        self.supplyStatus = supplyStatus
        self.experience = experience

batCount = [12, 1]
opforBatCount = [12, 0]

myUnit = Unit(infBat.hp*batCount[0]+tankBat.hp*batCount[1],# hp
              (infBat.org*batCount[0]+tankBat.org*batCount[1])/(batCount[0]+batCount[1]),  # org
              infBat.manpower*batCount[0]+tankBat.manpower*batCount[1],  # manpower
              infBat.supply*batCount[0]+tankBat.supply*batCount[1],  # supply
              infEquipment.softAttack*batCount[0]+tankEquipment.softAttack*batCount[1],  # soft attack
              infEquipment.hardAttack*batCount[0]+tankEquipment.hardAttack*batCount[1],  # hard attack
              infEquipment.defense*batCount[0]+tankEquipment.defense*batCount[1],  # defense
              infEquipment.breakthrough*batCount[0]+tankEquipment.breakthrough*batCount[1],  # breakthrough
              (0.4*(infEquipment.piercing+tankEquipment.piercing*batCount[1])/(batCount[0]+batCount[1]))+tankEquipment.piercing*0.6,  # piercing
              (infEquipment.hardness * batCount[0] + tankEquipment.hardness * batCount[1]) / (batCount[0] + batCount[1]),  # hardness
              tankEquipment.armor*0.3+((infEquipment.armor*batCount[0]+tankEquipment.armor*batCount[1])/(batCount[0]+batCount[1]))*0.7,  # armor
              batCount[0], batCount[1],  # infBatCount, tankBatCount
              (infBat.manpower*batCount[0]+tankBat.manpower*batCount[1])/(infBat.manpowerOptimal*batCount[0]+tankBat.manpowerOptimal*batCount[1]),  # manpower Status
              (infBat.supply*batCount[0]+tankBat.supply*batCount[1])/(infBat.supplyOptimal*batCount[0]+tankBat.supplyOptimal*batCount[1]),  # supply status
              0)  # experience


if batCount[1] == 0:
    myUnit.piercing = infEquipment.piercing
    myUnit.armor = infEquipment.armor

opforUnit = Unit(infBat.hp*opforBatCount[0]+tankBat.hp*opforBatCount[1],# hp
              (infBat.org*opforBatCount[0]+tankBat.org*opforBatCount[1])/(opforBatCount[0]+opforBatCount[1]),  # org
              infBat.manpower*opforBatCount[0]+tankBat.manpower*opforBatCount[1],  # manpower
              infBat.supply*opforBatCount[0]+tankBat.supply*opforBatCount[1],  # supply
              infEquipment.softAttack*opforBatCount[0]+tankEquipment.softAttack*opforBatCount[1],  # soft attack
              infEquipment.hardAttack*opforBatCount[0]+tankEquipment.hardAttack*opforBatCount[1],  # hard attack
              infEquipment.defense*opforBatCount[0]+tankEquipment.defense*opforBatCount[1],  # defense
              infEquipment.breakthrough*opforBatCount[0]+tankEquipment.breakthrough*opforBatCount[1],  # breakthrough
              (0.4*(infEquipment.piercing+tankEquipment.piercing*opforBatCount[1])/(opforBatCount[0]+opforBatCount[1]))+tankEquipment.piercing*0.6,  # piercing
              (infEquipment.hardness * opforBatCount[0] + tankEquipment.hardness * opforBatCount[1]) / (opforBatCount[0] + opforBatCount[1]),  # hardness
              tankEquipment.armor*0.3+((infEquipment.armor*opforBatCount[0]+tankEquipment.armor*opforBatCount[1])/(opforBatCount[0]+opforBatCount[1]))*0.7,  # armor
              opforBatCount[0], opforBatCount[1],  # infopforBatCount, tankopforBatCount
              (infBat.manpower*opforBatCount[0]+tankBat.manpower*opforBatCount[1])/(infBat.manpowerOptimal*opforBatCount[0]+tankBat.manpowerOptimal*opforBatCount[1]),  # manpower Status
              (infBat.supply*opforBatCount[0]+tankBat.supply*opforBatCount[1])/(infBat.supplyOptimal*opforBatCount[0]+tankBat.supplyOptimal*opforBatCount[1]),  # supply status
              0)  # experience
if opforBatCount[1] == 0:
    opforUnit.piercing = infEquipment.piercing
    opforUnit.armor = infEquipment.armor


class CombatStatRatios:
    def __init__(self, hardnessModifiedAttack, attackRatio, damageRatio):
        self.hardnessModifiedAttack = hardnessModifiedAttack
        self.attackRatio = attackRatio
        self.damageRatio = damageRatio


myUnitCombatRatios = CombatStatRatios(opforUnit.hardness*myUnit.hardAttack+(1-opforUnit.hardness)*myUnit.softAttack, #hardness modified attack
                                      ((random.gauss(1, 0.1))+(myUnit.experience*0.01)), 1.0)  # attackRatio, damageRatio

opforUnitCombatRatios = CombatStatRatios(myUnit.hardness*opforUnit.hardAttack+(1-myUnit.hardness)*opforUnit.softAttack, #hardness modified attack
                                         ((random.gauss(1, 0.1))+(opforUnit.experience*0.01)), 1.0)  # attackRatio, damageRatio

class CombatStats:
    def __init__(self, attacks, defenses):
        self.attacks = attacks
        self.defenses = defenses


myUnitCombatStats = CombatStats((myUnitCombatRatios.hardnessModifiedAttack*0.1)*myUnitCombatRatios.attackRatio,
                                myUnit.defense*0.1)

opforUnitCombatStats = CombatStats((opforUnitCombatRatios.hardnessModifiedAttack*0.1)*opforUnitCombatRatios.attackRatio,
                                   opforUnit.defense*0.1)


opforBattleHp = opforUnit.hp
opforBattleOrg = opforUnit.org
myBattleHp = myUnit.hp
myBattleOrg = myUnit.org




