def check_of_drome(now_my_string):
    if now_my_string == now_my_string[::-1]:
        return True
    else: 
        return False

# def checker_number_2(now_my_string_2):
#     return now_my_string_2 == now_my_string_2[::-1]
# print(checker_number_2(candidate))

candidate = input("Enter your string and we will check is it palindrome, or not. ")
boolean_boy = check_of_drome(candidate)
print(boolean_boy)

