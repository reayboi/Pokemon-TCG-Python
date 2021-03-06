import tkinter as tk
import time
import random
from tkinter.constants import NUMERIC

from PIL import Image, ImageTk

master = tk.Tk()
width = int(master.winfo_screenwidth() * 0.75)
height = int(master.winfo_screenheight() * 0.75)
master.geometry(f"{width}x{height}")
master.title("TCG REMAKE")

canvas = tk.Canvas(master, width=width, height=height)
canvas.place(x=0,y=0)


##WORDS THAT APPEAR AS IF THEY ARE BEING TYPED CODE --
# canvas_text = canvas.create_text(10, 10, text='', anchor=tk.NW)

# test_string = "Pikachu used lightning bolt! It did 30 damage!"
# # #Time delay between chars, in milliseconds
# #change the first value (milliseconds for how long you want it to take the text to appear)
# delta = int(1000/len(test_string))
# delay = 0
# for i in range(0, len(test_string)+1):
#     s = test_string[:i]
#     update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
#     canvas.after(delay, update_text)
#     delay += delta


###END

# canvas = tk.Canvas(master, width=width, height=height)
# canvas.place(x=0,y=0)

# points = {
#     0: [(0, 0), (100, 0), (100, 150), (0, 150), (30, 120), (70, 120), (70, 30), (30, 30), (30, 120), (0, 150)],
#     1: [(10,30), (40, 30), (40, 0), (70, 0), (70, 120), (100, 120), (100, 150), (10, 150), (10, 120), (40, 120), (40, 60), (10, 60)],
#     2: [(0, 0), (100, 0), (100, 90), (30, 90), (30, 120), (100, 120), (100, 150), (0, 150), (0, 60), (70, 60), (70, 30), (0, 30), (0, 0)],
#     3: [(0, 0), (100, 0), (100, 150), (0, 150), (0, 120), (70, 120), (70, 90), (0, 90), (0, 60), (70, 60), (70, 30), (0, 30)],
#     4: [(0, 0), (30, 0), (30, 60), (70, 60), (70, 0), (100, 0), (100, 150), (70, 150), (70, 90), (0, 90)], 
#     "4 original": [(0, 60), (50, 0), (80, 0), (80, 60), (100, 60), (100, 90), (80, 90), (80, 150), (50, 150), (50, 90), (0, 90), (30, 60), (50, 60), (50, 30), (30, 60), (0, 90)],
#     5: [(0, 0), (100, 0), (100, 30), (30, 30), (30, 60), (100, 60), (100, 150), (0, 150), (0, 120), (70, 120), (70, 90), (0, 90)],
#     6: [(0, 0), (100, 0), (100, 30), (30, 30), (30, 60), (100, 60), (100, 150), (0, 150), (30, 120), (70, 120), (70, 90), (30, 90), (30, 120), (0, 150)],
#     7: [(0, 0), (100, 0), (100, 90), (70, 90), (70, 150), (40, 150), (40, 90), (70, 90), (70, 30), (0, 30)],
#     "7 original": [(0, 0), (100, 0), (70, 150), (45, 150), (65, 30), (0, 30)],
#     8: [(0, 0), (30, 30), (30, 60), (70, 60), (70, 30), (30, 30), (0, 0), (100, 0), (100, 150), (0, 150), (30, 120), (70, 120), (70, 90), (30, 90), (30, 120), (0, 150)],
#     "8bit": [(0, 30), (20, 30), (40, 30), (40, 60), (60, 60), (60, 30), (40, 30), (20, 30), (20, 0), (80, 0), (80, 30), (100, 30), (100, 60), (80, 60), (80, 90), (100, 90), (100, 120), (80, 120), (80, 150), (20, 150), (20, 120), (40, 120), (60, 120), (60, 90), (40, 90), (40, 120), (20, 120), (0, 120), (0, 90), (20, 90), (20, 60), (0, 60), (0, 30)],
#     9: [(0, 0), (100, 0), (100, 150), (70, 150), (70, 80), (0, 80), (30, 50), (70, 50), (70, 30), (30, 30), (30, 50), (0, 80)]
# }

# attack = random.randint(0, 999999999)
# digits = [int(digit) for digit in str(attack)]
# print(digits)
# for digit in range (0, len(digits)):
#     if digit == 0:
#         canvas.create_polygon(points[digits[digit]], fill="red")
#     else: 
#         coords_list = []
#         for tup in points[digits[digit]]:
#             for index in range(0, len(tup)):
#                 if index == 0:
#                     x = tup[index] + (110*digit)
#                     coords_list.append(x)
#                 else:
#                     coords_list.append(tup[index])
#         canvas.create_polygon(coords_list, fill="red")

# max_health = random.randint(0, 100)
# current_health = random.randint(0, max_health)
# ratio = current_health/max_health
# max_x = int(100 * ratio)
# green = [(0, 0), (max_x, 0), (max_x, 30), (0, 30)]
# red = [(max_x, 0), (100, 0), (100, 30), (max_x, 30)]
# canvas.create_polygon(green, fill="green")
# canvas.create_polygon(red, fill="red")

# burn_marker = Image.open("images/burn_marker.png").resize((50, 50))
# burn_marker = ImageTk.PhotoImage(burn_marker)
# # label = tk.Label(canvas, image=burn_marker, width=50, height=50, bg="black")
# # label.place(x=0, y=200)
# marker = canvas.create_image(50, 200, image=burn_marker)
# #canvas.move(marker, 200, 200)

# print(canvas.type(marker))

# label = tk.Label(canvas, width=200, height=200, bg="#FFDFF1")
# label.place(x=0, y=300)

# turn = {
#     "Place": "Unlimited",
#     "Evolve": "Unlimited",
#     "Attach": False, #once per turn
#     "Trainer": "Unlimited",
#     "Supporter": False, #once per turn
#     "Stadium": False,  #once per turn
#     "Retreat": False,  #once per turn
#     "Abilities": "Unlimited",
#     "Attack": False, #last action before ending turn

# }

#CANVAS CAN CREATE ELEMENTS
# # Load the .gif image file.
# gif1 = tk.PhotoImage(file='small_globe.gif')

# # Put gif image on canvas.
# # Pic's upper-left corner (NW) on the canvas is at x=50 y=10.
# canvas.create_image(50, 10, image=gif1, anchor=NW)



# for index in range (0, len(points[digits[digit]])):
#     if (index == 0) or (index %2 == 0):
        
#         points[digits[digit]][index] += (110*digit)
# rec = canvas.create_rectangle(0, 0, 100, 100, fill="red")

# def test(event=None, canvas_item=None):
#     x = 12
#     canvas.move(canvas_item, x, 0)
#     try:
#         x1, y1, x2, x2 = canvas.coords(canvas_item)
#     except:
#         x1, y1  = canvas.coords(canvas_item)
#     if x1 >= 400:
#         print("done")
#         master.unbind("<Return>")
#     else:
#         canvas.after(16, test)

# x = 0
# master.bind("<Return>", lambda event: test(event, marker))
# canvas.after(1000, lambda: canvas.move(rec, 0, 400))
# #canvas.move(rec, 400, 400)
#master.mainloop()


