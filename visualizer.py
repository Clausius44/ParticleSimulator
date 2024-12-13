



import matplotlib.pyplot as plt
from matplotlib import cm
from celluloid import Camera

def visualize(nameFile):

    camera = Camera(plt.figure())

    plt.xlim(-5,505)
    plt.ylim(-5,505)
    time = -1
    read = False
    colors, positions = [], []
    for line in open(nameFile):
        if "Timestep" in line and time < 0:
            time += 1
            continue

        if "Timestep" in line and read == True:
            posx = [h[0] for h in positions]
            posy = [h[1] for h in positions]
            plt.vlines([-5,505], [-5,-5], [505,505], colors="k", linewidth=10 )
            plt.hlines([-5,505], [-5,-5], [505,505], colors="k", linewidth=10 )
            plt.scatter(posx, posy, color=colors)
            camera.snap()
            colors, positions = [], []
            continue

        if "Timestep" in line:
            read = True
            time += 1
            continue

        if read:
            linSp = line.split()
            colors.append(linSp[0])
            positions.append([float(linSp[1]), float(linSp[2])])
    anim = camera.animate(interval=45, blit=True)
    plt.show()
    #anim.save("PROVA.mp4")
