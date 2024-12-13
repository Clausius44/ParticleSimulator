



import random


class particle():

    def __init__(self, posx, posy, velx, vely, color):
        self.posx = posx
        self.posy = posy
        self.velx = velx
        self.vely = vely
        self.color = color

def randParticle(color):
    posx = random.random() * 400 + 50
    posy = random.random() * 400 + 50
    velx, vely = 0, 0

    part = particle(posx, posy, velx, vely, color)

    return part

def createGroup(num, color):
    group = []
    for h in range(num):
        part = randParticle(color)
        group.append(part)

    return group

class workGroup():

    def __init__(self, create):
        self.group = createGroup(create[0], create[1])

class workRule():

    def __init__(self, rule):
        self.first = rule[0]
        self.second = rule[1]
        self.value = rule[2]

def readParameters(fileName):
    create = []
    rules = []
    for thing in open(fileName):
        lin = thing.split()
        if lin[0] == "particles": create.append([int(lin[1]), lin[2]])
        if lin[0] == "rule": rules.append([lin[1], lin[2], float(lin[3])])

    return create, rules

def buildSystem(create, rules):

    allGroups, allRules = [], []
    for thing in create:
        allGroups.append(workGroup(thing))

