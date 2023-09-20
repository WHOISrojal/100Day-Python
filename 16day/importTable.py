## Constructing table using prettytable class

import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charizard"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)