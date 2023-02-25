# from turtle import Turtle, Screen

# tinny = Turtle()
# tinny.shape("turtle")

# for i in range(200):
#     tinny.color("red")
#     tinny.forward(50)
#     tinny.color("blue")
#     tinny.right(50)
#     tinny.forward(50)
#     # tinny.color("green")
#     # tinny.left(50)
#     # tinny.forward(50)
# my_screen = Screen()
# print (my_screen.canvheight)
# my_screen.exitonclick()

import prettytable
x = prettytable.PrettyTable()
x.field_names = ["NO","NAME","POINT"]
for i in range(10):
    x.add_row([1, "tykim", 34])
print(x)
