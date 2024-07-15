import tkinter as tk
from tkinter import *
import numpy as np
import random as rand
import numba

'''
def scale_aff(x,y):
   x=250*x+500
   y=250*y-500
   return np.array([x,y])
def inv_scale_aff(x,y):
   x=x/250-2
   y=-y/250+2
   return np.array([x,y],dtype=np.float64)

def mandelbrot_3():
    max_iter=100
    z1=np.linspace(0,1000,1000)
    z2=np.linspace(0,1000,1000)
    c=z1/250-2,-z2/250+2
    x,y=c[0],c[1]
    z=x+1j*y[:,None]
    z0=x+1j*y[:,None]
    clr=np.full((1000,1000),0)
    for i in range(max_iter):
        mask =(clr==0)
        z[mask]=z[mask]**2+z0[mask]
        clr[mask &(abs(z)>4)]=i+1  
    return clr



def computing(c0,c1,clr):
    c=inv_scale_aff(c0,c1)
    x,y=c[0],c[1]
    for i in range(100):
        x0=x**2-y**2+c[0]
        y0=2*x*y+c[1]
        x=x0
        y=y0
        if x**2+y**2 >= 4:
            return clr[i]
    return "#000000"


def homotopi(c,O_coord,frac):
   dx=dy=250
   dh=(c[0]-250)/frac
   H=[]
   for i in range(frac+1):
      H.append(((i*dh,c[1]-1000/c[0]*i*dh),1000/c[1]*(c[1]-i*dh),1000/c[0]*(c[0]-i*dh)))
   return H   
      
def mandelbrot_2(img,clr,O,x,y):
   dx=x//1000
   dy=y//1000
   img.put( " ".join((("{"+" ".join(clr[computing(O[0]+i*dx,O[1]+i*dy)] for i in range(1000)))+"}" for j in range(1000))))

def on_click(event):
   c=(int(event.x),int(event.y))
   H=homotopi(c,(0,0),10)
   for i in H:
      mandelbrot_2(img,clr,i[0],i[1],i[2])


def mandelbrot(img,clr):
 s=" "
 img.put( s.join((("{"+" ".join(computing(i,j,clr) for i in range(1000)))+"}" for j in range(1000))))      
 clr=[ ' #%02x%02x%02x' % (int(100*((i/100)**.25)),0,0) for i in range(100)]
 clr.append(' #000000')  #append the color of the centre as index 100  
'''      
def np_inv_scale(x,y):
   x=x/250-2
   y=-y/250+2
   return x,y



OOO=(0,0)
X_O=1000
Y_O=1000
clr=[ ' #%02x%02x%02x' % (int(100*((i/100)**.25)),0,0) for i in range(100)]
clr.append(' #000000') 

@numba.njit(fastmath=True)
def homotopi(c,frac):
   dx=dy=10
   dh=(c[0]-5-OOO[0])/frac
   dh_y=(c[1]-((5)/(c[0]-OOO[0])*Y_O/2 )-OOO[1])/frac
   H=[]
   for i in range(frac+1):
      H.append(((OOO[0]+i*dh,OOO[1]+max(c[1]-(Y_O/(c[0]-OOO[0])*(c[0]-i*dh-OOO[0]))/2,0)),X_O/(c[1]-OOO[1])*(c[1]-i*dh_y-OOO[1]),Y_O/(c[0]-OOO[0])*(c[0]-i*dh-OOO[0])))
   return H   

@numba.njit(fastmath=True)
def computing(c0,c1):
    c_0=c0/250-2
    c_1=-c1/250+2
    c= np.array([c_0,c_1])
    x,y=c[0],c[1]
    for i in range(100):
        x0=x**2-y**2+c[0]
        y0=2*x*y+c[1]
        x=x0
        y=y0
        if x**2+y**2 >= 4:
            return i
    return 0
def mandelbrot(img,clr):
 s=" "
 
 img.put( s.join((("{"+" ".join(clr[computing(i,j)] for i in range(1000)))+"}" for j in range(1000))))      
 #append the color of the centre as index 100  
def mandelbrot_2(img,clr,O,x,y):
   dx=x/1000
   dy=y/1000
   img.put( " ".join((("{"+" ".join(clr[computing(O[0]+i*dx,O[1]+j*dy)] for i in range(1000)))+"}" for j in range(1000)))) 


def updating(H,i):
   global OOO
   global X_O,Y_O
   print(OOO,"dAAAAA")
   if i<len(H):
    print(H[i][0])
    mandelbrot_2(img,clr,H[i][0],H[i][1],H[i][2])
    root.after(1,updating,H,i+1)
   elif i==len(H):
      
      OOO=H[-1][0]
      X_O=H[-1][1]
      Y_O=H[-1][2]
def on_click(event):
   c=(OOO[0]+int(event.x*X_O/1000),OOO[1]+int(event.y*Y_O/1000))
   
   
   H=homotopi(c,30) 
   #print(H)
   updating(H,0)
   
     




root = Tk()
root.bind("<Button-1>",on_click)
canvas = Canvas(root, width = 1000, height =1000, bg = "#000000")

canvas = Canvas(bg="white", width=1000, height=1000)





canvas.pack()
img = PhotoImage(width = 1000, height = 1000)
canvas.create_image((0, 0), image = img, state = "normal", anchor = NW)

mandelbrot(img,clr)


root.mainloop() 



