from tkinter import * 
from PIL import ImageTk, Image
root = Tk()
root.geometry("854x480")


NAME="Lesh_1.png"
image = Image.open(NAME)
photo = ImageTk.PhotoImage(image)

# Label widget to display the image
label = Label(root, image=photo)
label.pack()


file=open("coord.txt",'w')
def motion(event):
    x, y = event.x, event.y
    stroka="({}, {}),".format(x, y)
    print(stroka)
    file.write(stroka)

root.bind('<Motion>', motion)
root.mainloop()
file.close()