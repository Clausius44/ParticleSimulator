



import matplotlib.pyplot as plt
import matplotlib.animation as animation

def represent(allGroups):
    plt.figure(figsize=(10,10))

    for thing in allGroups:
        showGroup(thing)

    plt.xlim(0,500)
    plt.ylim(0,500)
    plt.show()

def showGroup(group):

    for thing in group:
        plt.scatter(thing.posx, thing.posy, color=thing.color)
