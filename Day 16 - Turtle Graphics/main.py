# from turtle import Turtle, Screen
# timmy = Turtle()
# #print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkSeaGreen4")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()



from prettytable import PrettyTable
table = PrettyTable()

pokemon = ['Pikachu', 'Squirtle', 'Charmader']
pokemon_type = ['Electric', 'Water', 'Fire']

table.add_column("Pokemon Name", pokemon)
table.add_column("Type", pokemon_type)
table.align = 'l'

print(table)