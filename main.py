



import particlesData as pd
import animation as an
import calculations as cal
import writeData as wd
import visualizer as vz
import readInput as ri

parametersname = "parameters.txt"
namefile = "outFile.txt"

allParts = []

groupsCreate, rules = ri.readGeneral(parametersname)

for thing in groupsCreate:
    allParts.append(pd.createGroup(int(thing[0]), thing[1]))

vecInter = ri.vecInteractionsBuild(allParts, rules)

out = open(namefile, "w")
for h in range(20):

    for thing in vecInter:
        cal.rule(thing[0], thing[1], thing[2])

    wd.fileWrite(allParts, h, namefile)

vz.visualize(namefile)
