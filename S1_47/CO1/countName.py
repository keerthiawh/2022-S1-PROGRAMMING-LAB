list_name = ['adil','jseem','sreerag','saam','ram']
list_name_count = [(i,list_name.count(x)) for x in list_name for i in x if i in "a"]
print("All list ",list_name)
print("Count list ",list_name_count)