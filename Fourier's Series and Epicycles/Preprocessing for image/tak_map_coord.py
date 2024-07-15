from tkinter import * 
from PIL import ImageTk, Image



NAME="Gojo.png"
W=801
H=783
razmer=str(W)+"x"+str(H)
root = Tk()
root.geometry(razmer)


image = Image.open(NAME)
photo = ImageTk.PhotoImage(image)


# Label widget to display the image
label = Label(root, image=photo)
label.pack()


coords=[]
def motion(event):
    coords.append((event.x, event.y))



root.bind('<Motion>', motion)
root.mainloop()

def some_tr(x,y):
    # x~ 854 ,14.222, 60.0478132471
    # y~ 480 ,8, 60
    #c_x=60.0478132471
    #c_y=60
    c_x=W/14.222
    c_y=H/8
    x_,y_=(x/c_x-7.111),((H-y)/c_y-4)
    return x_,y_

f=open("new_coord.txt","w")
for i in coords:
    s=some_tr(*i)
    f.write("({}, {}),".format(s[0], s[1]))
f.close() 