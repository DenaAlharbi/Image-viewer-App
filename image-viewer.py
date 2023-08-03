from tkinter import *
from PIL import ImageTk, Image  # It is used to import images easily

root = Tk()
root.title("Images - Exit - Icons")
# The icon
photo = PhotoImage(file="icon-image_viewer.png")
root.iconphoto(False, photo)

# Using images
my_img = ImageTk.PhotoImage(Image.open("image_1.png"))  # The PhotoImage is the same as before
my_img2 = ImageTk.PhotoImage(Image.open("image2.png"))  # The PhotoImage is the same as before
my_img3 = ImageTk.PhotoImage(Image.open("image3.png"))  # The PhotoImage is the same as before

images = [my_img, my_img3, my_img2]

my_label = Label(image=my_img)
# my_label.pack() Since we have more than one image and buttons it is better to use grid
my_label.grid(row=0, column=0, columnspan=3)
my_label2 = Label(image=my_img2)
# my_label2.pack()
my_label3 = Label(image=my_img3)
#my_label3.pack()


# we need to create three buttons
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=1, column=1)

button_back = Button(root, text="<<", command=)
button_back.grid(row=1, column=0)

button_forward = Button(root, text=">>", command=)
button_forward.grid(row=1, column=2)

# we need to create the functions that make them work
# we have the images list to go through
def button_back():
    


def button_forward():




# my_img4 = ImageTk.PhotoImage(Image.open("imagg_1.png"))  # The PhotoImage is the same as before
# my_label4 = Label(image=my_img)
# my_label4.pack()
# An exit button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
