from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Bulbasaur", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Grass/Poison", "Fire", "Water"])

print(table)