#enumerate with list
fruits= ["orange", "Cherry","kiwi"]
for index , fruit in enumerate(fruits):
    print(index, fruit)
#enumerate with list starting from 1
fruits= ["orange", "Cherry","kiwi"]
for index , fruit in enumerate(fruits, start=1):
    print(index, fruit)
#enumerate with string
word=("python")
for i, ch in enumerate(word):
    print(i,ch)
#enumerate with tuples
fruits= ("orange", "Cherry","kiwi")
for index , fruit in enumerate(fruits):
    print(index, fruit)


char=["angel", "anima","angel", "anima","angel", "anima"]
character_map={character:[] for character in set(char)}
for index, character in enumerate(char):
    character_map[character].append(index)
print(character_map)
