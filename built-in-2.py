def counter_of_cases(your_string):
    upper_count = sum(map(str.isupper,your_string))
    lower_count = sum(map(str.islower,your_string))
    print(f"Number of upper case letters: {upper_count}")
    print(f"Number of lower case letters: {lower_count}")

your_string_baee = input()
counter_of_cases(your_string_baee)