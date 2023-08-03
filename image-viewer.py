from _ast import Lambda
from tkinter import *
from PIL import ImageTk, Image  # It is used to import images easily

root = Tk()
root.title("Image-Viewer")
# The icon
photo = PhotoImage(file="pics/icon-image_viewer.png")
root.iconphoto(False, photo)

# Using images
my_img = ImageTk.PhotoImage(Image.open("pics/image1.png"))  # The PhotoImage is the same as before
my_img2 = ImageTk.PhotoImage(Image.open("pics/image2.png"))  # The PhotoImage is the same as before
my_img3 = ImageTk.PhotoImage(Image.open("pics/image3.png"))  # The PhotoImage is the same as before
my_img4 = ImageTk.PhotoImage(Image.open("pics/image4.png"))  # The PhotoImage is the same as before
my_img5 = ImageTk.PhotoImage(Image.open("pics/image5.png"))  # The PhotoImage is the same as before

images = [my_img, my_img2, my_img4, my_img3, my_img5]

my_label = Label(image=my_img)
# my_label.pack() Since we have more than one image and buttons it is better to use grid
my_label.grid(row=0, column=0, columnspan=3)
my_label2 = Label(image=my_img2)
# my_label2.pack()
my_label3 = Label(image=my_img3)
# my_label3.pack()


# we need to create three buttons
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=1, column=1)


# we need to create the functions that make them work
# we have the images list to go through
def button_back():
    global my_label
    global button_backk
    global button_forwardd


def button_forward(image_num):
    global my_label
    global button_backk
    global button_forwardd

    my_label.grid_forget()
    my_label = Label(images[image_num - 1])
    button_forwardd = Button(root, text=">>", command=lambda: button_forward(2))
    button_backk = Button(root, text="<<", command=button_back)

    button_forwardd.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)


# The buttons
button_backk = Button(root, text="<<", command=button_back)
button_backk.grid(row=1, column=0)

button_forwardd = Button(root, text=">>", command=lambda: button_forward(2))
button_forwardd.grid(row=1, column=2)

# An exit button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=1, column=1)

root.mainloop()
