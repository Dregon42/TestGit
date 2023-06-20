def do_something(a_list):
    my_string= " "
    for element in a_list:
        my_string += element[0]
    return my_string

characters = ["jasimine", "Alladin", "Genie," "Monkey"]
print(do_something(characters))