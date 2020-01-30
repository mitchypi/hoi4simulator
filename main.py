import random

# [hp,org,soft attack,hard attack,defense,breakthrough,piercing,hardness,manpower,armor]
infStats = [25,60,12,2,34,5,10.0,0.1,1000,0.0]
medTankStats = [2,10,40,32,10,84,131.0,0.98,500,130.0]



#number of friendly and opfor batallions
friendlyStrength = 1.0
opforStrength = 1.0
infBatCountOptimalInput = input ("How many infantry battalions does your unit contain: ")
isInt1 = False
while isInt1 is False:
    try:
        int(infBatCountOptimalInput)
        isInt1 = True
    except ValueError:
        infBatCountOptimalInput = input("Please enter a integer value: ")
infBatCountOptimal = float(infBatCountOptimalInput)
infBatCount = infBatCountOptimal*friendlyStrength
medTankBatCountOptimalInput = input ("How many tank battalions does your unit contain: ")
isInt2 = False
while isInt2 is False:
    try:
        int(medTankBatCountOptimalInput)
        isInt2 = True
    except ValueError:
        medTankBatCountOptimalInput = input("Please enter a integer value: ")
medTankBatCountOptimal = float(medTankBatCountOptimalInput)
medTankBatCount = medTankBatCountOptimal*friendlyStrength
opforInfCountOptimal = 6
opforTankCountOptimal = 0
opforInfCount = opforInfCountOptimal*opforStrength
opforTankCount = opforTankCountOptimal*opforStrength

#experience modifier used in attackRatio
friendlyExperience = 9000
opforExperience = 0

unitHp = infStats[0]*infBatCount+medTankStats[0]*medTankBatCount #sum of all battalions
unitOrg = (infStats[1]*infBatCount+medTankStats[1]*medTankBatCount)/(infBatCount+medTankBatCount) #average of all battalions
unitSoftAttack = infStats[2]*infBatCount+medTankStats[2]*medTankBatCount #sum of all battalions
unitHardAttack = infStats[3]*infBatCount+medTankStats[3]*medTankBatCount #sum of all battalions
unitDefense = infStats[4]*infBatCount+medTankStats[4]*medTankBatCount #sum of all battalions
unitBreakthrough = infStats[5]*infBatCount+medTankStats[5]*medTankBatCount #sum of all battalions
unitPiercing = medTankStats[6]*0.4+0.6*((medTankStats[6]*medTankBatCount+infStats[6]*infBatCount)/(infBatCount+medTankBatCount)) #40% of highest value + 60% of average value of all battalions
unitHardness = (infStats[7]*infBatCount+medTankStats[7]*medTankBatCount)/(infBatCount+medTankBatCount) #average of all battalions
unitManpower = infStats[8]*infBatCount+medTankStats[8]*medTankBatCount #sum of all battalions
if medTankBatCount>0:
    unitArmor = 0.3*(medTankStats[9])+0.7*((medTankStats[9]*medTankBatCount+infStats[9]*infBatCount)/(infBatCount+medTankBatCount)) #30% of highest value + 70% of average value of all battalions
else:
    unitArmor = 0.0 * (medTankStats[9]) + 0.7 * ((medTankStats[9] * medTankBatCount + infStats[9] * infBatCount) / (
                infBatCount + medTankBatCount))  # 30% of highest value + 70% of average value of all battalions

opforHp = infStats[0]*opforInfCount+medTankStats[0]*opforTankCount  #sum of all battalions
opforOrg = (infStats[1]*opforInfCount+medTankStats[1]*opforTankCount)/(opforInfCount+opforTankCount)  #average of all battalions
opforSoftAttack = infStats[2]*opforInfCount+medTankStats[2]*opforTankCount  #sum of all battalions
opforHardAttack = infStats[3]*opforInfCount+medTankStats[3]*opforTankCount  #sum of all battalions
opforDefense = infStats[4]*opforInfCount+medTankStats[4]*opforTankCount  #sum of all battalions
opforBreakthrough = infStats[5]*opforInfCount+medTankStats[5]*opforTankCount  #sum of all battalions
opforPiercing = medTankStats[6]*0.4+0.6*((medTankStats[6]*opforTankCount+infStats[6]*opforInfCount)/(opforInfCount+opforTankCount)) #40% of highest value + 60% of average value of all battalions
opforHardness = (infStats[7]*opforInfCount+medTankStats[7]*opforTankCount)/(opforInfCount+opforTankCount)  #average of all battalions
opforManpower = infStats[8]*opforInfCount+medTankStats[8]*opforTankCount  #sum of all battalions
if opforTankCount>0:
    opforArmor = 0.3*(medTankStats[9])+0.7*((medTankStats[9]*opforTankCount+infStats[9]*opforInfCount)/(opforInfCount+opforTankCount)) #30% of highest value + 70% of average value of all battalions
else:
    opforArmor = 0.0*(medTankStats[9])+0.7*((medTankStats[9]*opforTankCount+infStats[9]*opforInfCount)/(opforInfCount+opforTankCount)) #30% of highest value + 70% of average value of all battalions


  #check who is attacking and who is defending
weAreAttacking = True
if weAreAttacking is True:
    attackerHp = unitHp
    attackerOrg = unitOrg
    attackerSoftAttack = unitSoftAttack
    attackerHardAttack = unitHardAttack
    attackerDefense = unitDefense
    attackerBreakthrough = unitBreakthrough
    attackerPiercing = unitPiercing
    attackerHardness = unitHardness
    attackerManpower = unitManpower
    attackerArmor = unitArmor
    attackerExperience = friendlyExperience
    defenderHp = opforHp
    defenderOrg = opforOrg
    defenderSoftAttack = opforSoftAttack
    defenderHardAttack = opforHardAttack
    defenderDefense = opforDefense
    defenderBreakthrough = opforBreakthrough
    defenderPiercing = opforPiercing
    defenderHardness = opforHardness
    defenderManpower = opforManpower
    defenderArmor = opforArmor
    defenderExperience = opforExperience
else:
    attackerHp = opforHp
    attackerOrg = opforOrg
    attackerSoftAttack = opforSoftAttack
    attackerHardAttack = opforHardAttack
    attackerDefense = opforDefense
    attackerBreakthrough = opforBreakthrough
    attackerPiercing = opforPiercing
    attackerHardness = opforHardness
    attackerManpower = opforManpower
    attackerArmor = opforArmor
    attackerExperience = opforExperience
    defenderHp = unitHp
    defenderOrg = unitOrg
    defenderSoftAttack = unitSoftAttack
    defenderHardAttack = unitHardAttack
    defenderDefense = unitDefense
    defenderBreakthrough = unitBreakthrough
    defenderPiercing = unitPiercing
    defenderHardness = unitHardness
    defenderManpower = unitManpower
    defenderArmor = unitArmor
    defenderExperience = friendlyExperience

  # modifies attack for unit hardness
attackerHardnessModifiedAttack = (1 - defenderHardness) * attackerSoftAttack + defenderHardness * attackerHardAttack
defenderHardnessModifiedAttack = (1 - attackerHardness) * defenderSoftAttack + attackerHardness * defenderHardAttack

  #check if attacker piercing > armor
if attackerPiercing>defenderArmor:
    attackerCanPierce = True
    attackerDamageRatio = 1
else:
    attackerCanPierce = False
    attackerDamageRatio = 0.5

if defenderPiercing>attackerArmor:
    defenderCanPierce = True
    defenderDamageRatio = 1
else:
    defenderCanPierce = False
    defenderDamageRatio = 0.5
  #attacks and defenses dealt, based on a normal distribution with mu 1 and sigma 0.2, then with an bonuses added
attackRatio = ((random.gauss(1, 0.4))+(attackerExperience*0.01))
defenderAttackRatio = (random.gauss(1, 0.4))+(defenderExperience*0.01)

attackerAttacksRaw = (attackerHardnessModifiedAttack*0.1)*attackRatio #attacks and defense stats for side that initiated combat
breakthroughRaw = (attackerBreakthrough * 0.1)

defenderAttacksRaw = (defenderHardnessModifiedAttack*0.1)*defenderAttackRatio #attacks and defense stats for side that did not initiate combat
defensesRaw = (defenderDefense*0.1)

#rounds num of attacks and defenses , since you cant have non-integer number of attacks/defenses
aAttacks = round(attackerAttacksRaw)
aDefenses = round(breakthroughRaw)

dAttacks = round(defenderAttacksRaw)
dDefenses = round(defensesRaw)

battleStatus = True

while battleStatus is True:

    while dDefenses > 0 and aDefenses > 0 and battleStatus is True:
        attackerDamageDealtHp = random.randint(1,2) * 0.05 * aAttacks * 0.1 * attackerDamageRatio
        if attackerCanPierce is True:
            attackerDamageDealtOrg = random.randint(1,6) * 0.05 * aAttacks*0.1 * attackerDamageRatio
        else:
            attackerDamageDealtOrg = random.randint(1,4) * 0.05 * aAttacks * 0.1 * attackerDamageRatio
        defenderHp -= attackerDamageDealtHp
        defenderOrg -= attackerDamageDealtOrg
        dDefenses -= aAttacks
        defenderDamageDealtHp = random.randint(1, 2) * 0.05 * dAttacks * 0.1 * defenderDamageRatio
        if defenderCanPierce is True:
            defenderDamageDealtOrg = random.randint(1, 6) * 0.05 * dAttacks * 0.1 * defenderDamageRatio
        else:
            defenderDamageDealtOrg = random.randint(1, 4) * 0.05 * dAttacks * 0.1 * defenderDamageRatio
        attackerHp -= defenderDamageDealtHp
        attackerOrg -= defenderDamageDealtOrg
        aDefenses -= dAttacks
        if attackerOrg > 0 and defenderOrg > 0:
            battleStatus = True
        else:
            battleStatus = False

    while dDefenses > 0 and aDefenses <= 0 and battleStatus is True:
        attackerDamageDealtHp = random.randint(1,2)* 0.05 * aAttacks * 0.1 * attackerDamageRatio
        if attackerCanPierce is True:
            attackerDamageDealtOrg = random.randint(1, 6) * 0.05 * aAttacks * 0.1 * attackerDamageRatio
        else:
            attackerDamageDealtOrg = random.randint(1, 4) * 0.05 * aAttacks * 0.1 * attackerDamageRatio
        defenderHp -= attackerDamageDealtHp
        defenderOrg -= attackerDamageDealtOrg
        dDefenses -= aAttacks
        defenderDamageDealtHp = random.randint(1, 2) * 0.05 * dAttacks * 0.4 * defenderDamageRatio
        if defenderCanPierce is True:
            defenderDamageDealtOrg = random.randint(1, 6) * 0.05 * dAttacks * 0.4 * defenderDamageRatio
        else:
            defenderDamageDealtOrg = random.randint(1, 4) * 0.05 * dAttacks * 0.4 * defenderDamageRatio
        attackerHp -= defenderDamageDealtHp
        attackerOrg -= defenderDamageDealtOrg
        aDefenses -= dAttacks
        if attackerOrg > 0 and defenderOrg > 0:
            battleStatus = True
        else:
            battleStatus = False

    while dDefenses <= 0 and aDefenses > 0 and battleStatus is True:
        attackerDamageDealtHp = random.randint(1,2)* 0.05 * aAttacks * 0.4 * attackerDamageRatio
        if attackerCanPierce is True:
            attackerDamageDealtOrg = random.randint(1, 6) * 0.05 * aAttacks * 0.4 * attackerDamageRatio
        else:
            attackerDamageDealtOrg = random.randint(1, 4) * 0.05 * aAttacks * 0.4 * attackerDamageRatio
        defenderHp -= attackerDamageDealtHp
        defenderOrg -= attackerDamageDealtOrg
        dDefenses -= aAttacks
        defenderDamageDealtHp = random.randint(1, 2) * 0.05 * dAttacks * 0.1 * defenderDamageRatio
        if defenderCanPierce is True:
            defenderDamageDealtOrg = random.randint(1, 6) * 0.05 * dAttacks * 0.1 * defenderDamageRatio
        else:
            defenderDamageDealtOrg = random.randint(1, 4) * 0.05 * dAttacks * 0.1 * defenderDamageRatio
        attackerHp -= defenderDamageDealtHp
        attackerOrg -= defenderDamageDealtOrg
        aDefenses -= dAttacks
        if attackerOrg > 0 and defenderOrg > 0:
            battleStatus = True
        else:
            battleStatus = False

    while dDefenses <= 0 and aDefenses <= 0 and battleStatus is True:
        attackerDamageDealtHp = random.randint(1, 2) * 0.05 * aAttacks * 0.4 * attackerDamageRatio
        if attackerCanPierce is True:
            attackerDamageDealtOrg = random.randint(1, 6) * 0.05 * aAttacks * 0.4 * attackerDamageRatio
        else:
            attackerDamageDealtOrg = random.randint(1, 4) * 0.05 * aAttacks * 0.4 * attackerDamageRatio
        defenderHp -= attackerDamageDealtHp
        defenderOrg -= attackerDamageDealtOrg
        dDefenses -= aAttacks
        defenderDamageDealtHp = random.randint(1, 2) * 0.05 * dAttacks * 0.4 * defenderDamageRatio
        if defenderCanPierce is True:
            defenderDamageDealtOrg = random.randint(1, 6) * 0.05 * dAttacks * 0.4 * defenderDamageRatio
        else:
            defenderDamageDealtOrg = random.randint(1, 4) * 0.05 * dAttacks * 0.4 * defenderDamageRatio
        attackerHp -= defenderDamageDealtHp
        attackerOrg -= defenderDamageDealtOrg
        aDefenses -= dAttacks
        if attackerOrg > 0 and defenderOrg > 0:
            battleStatus = True
        else:
            battleStatus = False

if weAreAttacking is True:
    if attackerOrg>0:
        print("we won the battle")
    else:
        print("we lost the battle")
else:
    if defenderOrg>0:
        print("we won the battle")
    else:
        print("we lost the battle")

if weAreAttacking is True:
    attackerCasualtiesRaw = ((unitHp-attackerHp)/unitHp)*unitManpower
    defenderCasualtiesRaw = ((opforHp-defenderHp)/opforHp)*opforManpower
    attackerCasualties = round(attackerCasualtiesRaw)
    defenderCasualties = round(defenderCasualtiesRaw)
    print("We took ",attackerCasualties, " casualties while causing ",defenderCasualties, " casualties" )
else:
    attackerCasualtiesRaw = ((opforHp - attackerHp) / opforHp) * opforManpower
    defenderCasualtiesRaw = ((unitHp - defenderHp) / unitHp) * unitManpower
    attackerCasualties = round(attackerCasualtiesRaw)
    defenderCasualties = round(defenderCasualtiesRaw)
    print("We took ", defenderCasualties, " casualties while causing ", attackerCasualties, " casualties")



