# by Antoni Gual Via 4/2015
import numpy as np
from tkinter import Tk, Canvas, PhotoImage,NW,mainloop 


def mandel_pixel(c):
  """ calculates the color index of the mandelbrot plane point passed in the arguments """
  maxIt = 100
  z = c   
  for i in range(maxIt):
      a=z**2
      z=a+c
      if z.real**2+z.imag**2 >= 4.:
         return i
  return 100

def mandelbrot(xa,xb,ya,yb,x,y):
    """ returns a mandelbrot in a string for Tk PhotoImage"""
    #color string table in Photoimage format #RRGGBB 
    
    clr=[ ' #%02x%02x%02x' % (int(100*((i/100)**.25)),int(100*((i/100)**.25)),0) for i in range(100)]
    clr.append(' #000000')  #append the color of the centre as index 256
    #calculate mandelbrot x,y coordinates for each screen pixel
    xm=[xa + (xb - xa) * kx /x  for kx in range(x)]
    ym=[ya + (yb - ya) * ky /y  for ky in range(y)]
    #build the Photoimage string by calling mandel_pixel to index in the color table
    return" ".join((("{"+" ".join(clr[mandel_pixel(complex(i,j))] for i in xm))+"}" for j in ym))



#window size
x=1000
y=1000
#corners of  the mandelbrot plan to display  
xa = -2.0; xb = 2.0
ya = -2.; yb = 2.

#Tkinter window
window = Tk()
canvas = Canvas(window, width = x, height = y, bg = "#000000");canvas.pack()
img = PhotoImage(width = x, height = y)
canvas.create_image((0, 0), image = img, state = "normal", anchor = NW)

#do the mandelbrot 

img.put(mandelbrot(xa,xb,ya,yb,x,y))


mainloop()
'''


color_1=np.array([130,125,191],dtype=int)
color_2=np.array([21,4,31],dtype=int)
color_a=[' #%02x%02x%02x' % tuple((i*color_2)//100+(100-i)*color_1//100) for i in range(100)]
print(color_a)
'''
