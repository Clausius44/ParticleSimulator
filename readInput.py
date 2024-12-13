

class ruleClass():

    def __init__(self, first, second, val):
        self.both = [first, second]
        self.val = float(val)

def readGeneral(filename):

    particles = [thing for thing in open(filename) if "particles" in thing.split()[0]]
    particlesReturn = []
    for thing in particles:
        particlesReturn.append([thing.split()[1], thing.split()[2]])

    rules = [thing for thing in open(filename) if "rule" in thing.split()[0]]
    rulesReturn = []
    for thing in rules:
        rulesReturn.append(ruleClass(thing.split()[1], thing.split()[2], thing.split()[3]))

    return particlesReturn, rulesReturn

def vecInteractionsBuild(particles, rules):

    vecRules = []

    for thing in rules:
        for group1 in particles:
            for group2 in particles:

                if thing.both[0] == group1[0].color and thing.both[1] == group2[0].color:
                    vecRules.append([group1, group2, thing.val])

    return vecRules