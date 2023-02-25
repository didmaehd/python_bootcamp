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

# import prettytable
# x = prettytable.PrettyTable()
# x.field_names = ["NO","NAME","POINT"]
# for i in range(10):
#     x.add_row([1, "tykim", 34])
# print(x)

 
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pekemon Name",["Pikachu","Squirtle","Chanabder"])
table.add_column("Type",["Electric","Water","Fire"])
table.add_column("Level",[45,34,43])
table.add_row(["Raichu","Electric",39])
table.align = "l"
table.align["Level"] = "r"
print(table)