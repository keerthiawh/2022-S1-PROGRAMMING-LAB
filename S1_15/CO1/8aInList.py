#Store a list of first names. Count the occurrences of ‘a’ within the list.

list_name = ["apple","banana","Mengo","cherry","apple"]
list_a_count = [ x.count("a") for x in list_name]
print("All list ",list_name)
print("Count list ",list_a_count)