
#enter word
my_str = input("Enter a string: ")

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("True")
else:
   print("False")