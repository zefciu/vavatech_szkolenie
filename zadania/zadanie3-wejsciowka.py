def m(c):
    """Jeśli po 20 iteracji abs(z) < 2: zwróć None
    Jeśli po którejkolwiek iteracji abs(z) > 2: zwróć numer iteracji"""
    pass

from tkinter import *
import colorsys

master = Tk()

canvas = Canvas(master, width=500, height=500)
canvas.pack()
img = PhotoImage(width=500, height=500)
canvas.create_image((250, 250), image=img, state="normal")

for i in range(500):
    for j in range(500):
        point = complex(((i - 250) / 100), ((j - 250) / 100))
        result = m(point)
        if result == None:
            color = '#000000'
        else:
            hue = result / 20
            rgb = [int(255 * x) for x in colorsys.hsv_to_rgb(hue, 1, 1)]
            color = '#{:02x}{:02x}{:02x}'.format(*rgb)
        img.put(color, (i, j))
mainloop()

