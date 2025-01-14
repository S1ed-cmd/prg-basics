names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest_names = names[0]


for name in names:
    if len(name) > len(longest_names):
        longest_names = name

        
print("Names:", " ".join(names))
print("Longest name:", longest_names)