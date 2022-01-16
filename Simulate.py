from contextlib import nullcontext
import math
import random
import csv

day = 0
regions = {}

with open('regional.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        key = row[0]
        NCA = float(row[1].strip("%"))
        FCP = float(row[2].strip("%"))
        NLP = float(row[3].strip("%"))
        ULP = float(row[4].strip("%"))
        GRN = float(row[5].strip("%"))
        regions[key]=[NCA,FCP,NLP,ULP,GRN]
print(regions)

## Normal News Day
# 50% of the time, no result
# 24% of the time, +5%
# 24% of the time, -5%
# 1% of the time, +15%
# 1% of the time, -15%

## Debate Day
#7.5% of the time, triumph, +10% in all regions
#7.5% of the time, collapse, -10% in all regions
#25% of the time, rally, +5% in all regions
#25% of the time, stumble, -5% in all regions
#35% of the time, stagnation, nothing happens

for day in range(28):
    if day == 6 or day == 13 or day == 20 or day == 27:
        print("\033[1mDebate on day "+ str(day) + " of the Campaign\033[0m")
        debateDice = random.randint(1,1000)
        debateSelector = random.randint(0,4)
        if dice <= 75:
            if debateSelector == 0:
                print('NCA triumph in Debate') 
            if debateSelector == 1:
                print('FCP triumph in Debate')
            if debateSelector == 2:
                print("NLP triumph in Debate")
            if debateSelector == 3:
                print("ULP triumph in Debate")
            if debateSelector == 4:
                print("Greens triumph in Debate")
            for region in regions:
                regions[region][debateSelector] *= 1.10
        if dice > 75 and dice <= 150:
            if debateSelector == 0:
                print('NCA breaks down in Debate') 
            if debateSelector == 1:
                print('FCP breaks down in Debate')
            if debateSelector == 2:
                print("NLP breaks down in Debate")
            if debateSelector == 3:
                print("ULP breaks down in Debate")
            if debateSelector == 4:
                print("Greens breaks down in Debate")
            for region in regions:
                regions[region][debateSelector] *= 0.90
        if dice > 150 and dice <= 400:
            if debateSelector == 0:
                print('NCA rallies at Debate') 
            if debateSelector == 1:
                print('FCP rallies at Debate')
            if debateSelector == 2:
                print("NLP rallies at Debate")
            if debateSelector == 3:
                print("ULP rallies at Debate")
            if debateSelector == 4:
                print("Greens rally at Debate")
            for region in regions:
                regions[region][debateSelector] *= 1.05
        if dice > 400 and dice <= 650:
            if debateSelector == 0:
                print('NCA stumble at Debate') 
            if debateSelector == 1:
                print('FCP stumble at Debate')
            if debateSelector == 2:
                print("NLP stumble at Debate")
            if debateSelector == 3:
                print("ULP stumble at Debate")
            if debateSelector == 4:
                print("Greens stumble at Debate")
            for region in regions:
                regions[region][debateSelector] *= 0.95
        continue

    print("\033[1mDay "+ str(day) + " of the Campaign\033[0m")
    for region in regions:
        partySelector = random.randint(1,5)
        dice = random.randint(1,100)
        if dice <= 24:
            if partySelector == 1:
                regions[region][0] *= 1.05
                print('NCA bump in '+ region)
            if partySelector == 2:
                regions[region][1] *=1.05
                print('FCP bump in '+ region)
            if partySelector == 3:
                regions[region][2] *=1.05
                print('NLP bump in '+ region)
            if partySelector == 4:
                regions[region][3] *=1.05
                print('ULP bump in '+ region)
            if partySelector == 5:
                regions[region][4] *=1.05
                print('Green bump in '+ region) 
        if dice > 24 and dice <= 47:
            partySelector = random.randint(1,5)
            if partySelector == 1:
                regions[region][0] *= 0.95
                print('NCA slump in '+ region)
            if partySelector == 2:
                regions[region][1] *= 0.95
                print('FCP slump in '+ region)
            if partySelector == 3:
                regions[region][2] *= 0.95
                print('NLP slump in '+ region)
            if partySelector == 4:
                regions[region][3] *= 0.95
                print('ULP slump in '+ region)
            if partySelector == 5:
                regions[region][4] *= 0.95
                print('Green slump in '+ region)
        if dice == 48:
            partySelector = random.randint(1,5)
            if partySelector == 1:
                regions[region][0] *= 1.15
                print('NCA surge in '+ region)
            if partySelector == 2:
                regions[region][1] *=1.15
                print('FCP surge in '+ region)
            if partySelector == 3:
                regions[region][2] *=1.15
                print('NLP surge in '+ region)
            if partySelector == 4:
                regions[region][3] *=1.15
                print('ULP surge in '+ region)
            if partySelector == 5:
                regions[region][4] *=1.15
                print('Green surge in '+ region)
        if dice == 49:
            partySelector = random.randint(1,5)
            if partySelector == 1:
                regions[region][0] *= 0.85
                print('NCA collapse in '+ region)
            if partySelector == 2:
                regions[region][1] *= 0.85
                print('FCP collapse in '+ region)
            if partySelector == 3:
                regions[region][2] *= 0.85
                print('NLP collapse in '+ region)
            if partySelector == 4:
                regions[region][3] *= 0.85
                print('ULP collapse in '+ region)
            if partySelector == 5:
                regions[region][4] *= 0.85
                print('Green collapse in '+ region)
        if dice >= 50:
            print('All quiet in '+ region)

percents = {}

for region in regions:
    regionSum = sum(regions[region])
    percents[region] = []
    for n in regions[region]:
        percents[region].append(n/(regionSum))

with open('polling.csv', 'w', newline='') as csv2:
    writer = csv.writer(csv2)
    for region in percents:
        writer.writerow([region]+percents[region])