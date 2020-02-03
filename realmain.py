from classes import opforUnit as opforUnit
from classes import myUnit as myUnit
from classes import opforUnitCombatRatios as opforUnitCombatRatios
from classes import myUnitCombatRatios as myUnitCombatRatios
from classes import myUnitCombatStats as myUnitCombatStats
from classes import opforUnitCombatStats as opforUnitCombatStats
import random

iAmAttacking = True

if iAmAttacking is True:
    myUnitCombatStats.defenses = myUnit.breakthrough*0.1
    opforUnitCombatStats.defenses = opforUnit.defense*0.1
elif iAmAttacking is False:
    myUnitCombatStats.defenses = myUnit.defense * 0.1
    opforUnitCombatStats.defenses = opforUnit.breakthrough * 0.1

if myUnitCombatStats.defenses >= opforUnitCombatStats.attacks:
    opforADRatio = 0.1
elif myUnitCombatStats.defenses < opforUnitCombatStats.attacks:
    opforAD = (opforUnitCombatStats.attacks-myUnitCombatStats.defenses)/opforUnitCombatStats.attacks
    opforADRatio = opforAD*0.4+(1-opforAD)*0.1
else:
    opforADRatio = 0.1

if opforUnitCombatStats.defenses >= myUnitCombatStats.attacks:
    myADRatio = 0.1
elif opforUnitCombatStats.defenses < myUnitCombatStats.attacks:
    myAD = (myUnitCombatStats.attacks-opforUnitCombatStats.defenses)/myUnitCombatStats.attacks
    myADRatio = myAD*0.4+(1-myAD)*0.1
else:
    myADRatio = 0.1

opforBattleHp = opforUnit.hp
opforBattleOrg = opforUnit.org
myBattleHp = myUnit.hp
myBattleOrg = myUnit.org


if myUnit.piercing < opforUnit.armor:
    myUnitCombatRatios.damageRatio = 0.5
    iCanPierce = False
else:
    myUnitCombatRatios.damageRatio = 1.0
    iCanPierce = True
if opforUnit.piercing < myUnit.armor:
    opforUnitCombatRatios.damageRatio = 0.5
    opforCanPierce = False
else:
    opforUnitCombatRatios.damageRatio = 1.0
    opforCanPierce = True
battleStatus = True

while battleStatus is True:
    myDamageDealtHp = random.randint(1, 2) * 0.05 * myUnitCombatStats.attacks * myADRatio * myUnitCombatRatios.damageRatio
    if opforCanPierce is True:
        myDamageDealtOrg = random.randint(1, 4) * 0.05 * myUnitCombatStats.attacks * myADRatio * myUnitCombatRatios.damageRatio
    else:
        myDamageDealtOrg = random.randint(1, 6) * 0.05 * myUnitCombatStats.attacks * myADRatio * myUnitCombatRatios.damageRatio
    opforBattleHp -= myDamageDealtHp
    opforBattleOrg -= myDamageDealtOrg

    opforDamageDealtHp = random.randint(1, 2) * 0.05 * opforUnitCombatStats.attacks * opforADRatio * opforUnitCombatRatios.damageRatio
    if iCanPierce is True:
        opforDamageDealtOrg = random.randint(1, 4) * 0.05 * opforUnitCombatStats.attacks * opforADRatio * opforUnitCombatRatios.damageRatio
    else:
        opforDamageDealtOrg = random.randint(1, 6) * 0.05 * opforUnitCombatStats.attacks * opforADRatio * opforUnitCombatRatios.damageRatio
    myBattleHp -= opforDamageDealtHp
    myBattleOrg -= opforDamageDealtOrg

    if myBattleOrg < 0 or opforBattleOrg < 0 or myBattleHp <= 1 or opforBattleHp <= 1:
        battleStatus = False
    else:
        battleStatus = True


myCasualtiesRaw = ((myUnit.hp-myBattleHp)/myUnit.hp)*myUnit.manpower
opforCasualtiesRaw = ((opforUnit.hp-opforBattleHp)/opforUnit.hp)*opforUnit.manpower
myCasualties = round(myCasualtiesRaw)
opforCasualties = round(opforCasualtiesRaw)

if myBattleOrg > 0:
    print("we won the battle")
else:
    print("we lost the battle")
print("debug opforUnit.hp, opforUnit.org, opforBattleOrg, opforBattleHp:", opforUnit.hp, opforUnit.org, opforBattleOrg, opforBattleHp)
print("debug myUnit.hp, myUnit.org, myBattleOrg, myBattleHp:", myUnit.hp, myUnit.org, myBattleOrg, myBattleHp)
print("debug: opforUnitCombatStats.attacks, opforADRatio,opforUnitCombatRatios.damageRatio", opforUnitCombatStats.attacks, opforADRatio, opforUnitCombatRatios.damageRatio)
print("We took", myCasualties, "casualties")
print("They took", opforCasualties, "casualties")