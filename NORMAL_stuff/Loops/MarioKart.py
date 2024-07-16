results=["Mario","Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

# add them as a list to the end
results.append(["Bowser","Donkey Kong"])
#erase the chosen members
results.remove(["Bowser","Donkey Kong"])
#add them as an member to the list
results.extend(["Bowser","Donkey Kong"])
#the name should be with the list
results.remove("Bowser")
#Insert a certain variable to the given index 
results.insert(0,"Bowser")
#reverse the list
results.reverse()
print(results)

