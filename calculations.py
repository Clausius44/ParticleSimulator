



import numpy as np

def rule(group1, group2, g = 0, cutoff = 50):
    for h in group1:
        fx = 0
        fy = 0
        for j in group2:
            dx = h.posx - j.posx
            dy = h.posy - j.posy
            dist = np.sqrt(dx**2 + dy**2)

            if dist > 0 and dist < cutoff:
                Ftot = g / dist
                fx += (Ftot * dx)
                fy += (Ftot * dy)
            j.velx = (j.velx + fx) * 0.02
            j.vely = (j.vely + fy) * 0.02
            if j.posx <= 0 or j.posx >= 500: j.velx = j.velx * -1
            if j.posy <= 0 or j.posy >= 500: j.vely = j.vely * -1
            j.posx += j.velx
            j.posy += j.vely
