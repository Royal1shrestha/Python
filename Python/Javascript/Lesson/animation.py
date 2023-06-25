from tkinter import *
import time

WIDTH = 800
HEIGHT = 600
xspeed = 2.5
yspeed = 3

# BACKGROUND_IMAGE_PATH = "C:\\Users\\Admin\\Pictures\\th.jpg"
IMAGE_PATH = "C:\\Users\\Admin\\Pictures\\Saved Pictures\\pic.png"

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# background_photo = PhotoImage(file=BACKGROUND_IMAGE_PATH)
# background_image = canvas.create_image(0, 0, image=background_photo, anchor=NW)
photo = PhotoImage(file=IMAGE_PATH)
image = canvas.create_image(0, 0, image=photo, anchor=NW)
image_width = photo.width()
image_height = photo.height()

def update_animation():
    global xspeed, yspeed
    coordinates = canvas.coords(image)
    if coordinates[0] > (WIDTH - image_width) or coordinates[0] < 0:
        xspeed = -xspeed
    if coordinates[1] > (HEIGHT - image_height) or coordinates[1] < 0:
        yspeed = -yspeed
    canvas.move(image, xspeed, yspeed)
    window.after(15, update_animation)

update_animation()
window.mainloop()