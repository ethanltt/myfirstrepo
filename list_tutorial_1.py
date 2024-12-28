def get_superheroes():
    superhero = ["Batman","Superman","Ironman","Spider-man","X-man"]
    return superhero

#print(superhero[4])
#print(superhero[3])

superhero = get_superheroes()

for hero in superhero:
    print(hero)
superhero.append("Black Panther")
print(superhero)
superhero.remove("Batman")
print(superhero)
superhero.pop()
superhero.pop(1)
print(superhero)