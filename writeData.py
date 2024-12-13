



import os as os

def fileWrite(allGroups, time, nameFile):

    if nameFile not in os.listdir(): open(nameFile, "w")

    out = open(nameFile, "a")
    out.write("Timestep {}\n".format(time))
    for groups in allGroups:
        for thing in groups:
            out.write("{:<12}  {:9.6f}  {:9.6f}\n".format(thing.color, thing.posx, thing.posy))


    out.close()

def getAllTimes(filename):

    times = 0
    for h in open(filename):
        if "Timestep" in h: times += 1

    return times
