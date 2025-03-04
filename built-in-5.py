def checker_of_tuples(your_tuple):
    return all(your_tuple)



where_is_my_tuple = ("something", "letter", 2.71, 3.14, True, 1-7j)
print(f"HERE IS YOUR TUPLE AND IT IS {checker_of_tuples(where_is_my_tuple)}!")

your_variables = input("white with comma as (smth,anothsmth,next......)----> ")
tuple_of_variables = eval(f"({your_variables})")
print(f"Your tuple is {checker_of_tuples(tuple_of_variables)}")