#conversion of snake case to pascal case

def snake_to_pascal_case(s):

    s=s.replace("_", " ")
    s=s.title()
    s=s.replace(" ", "")
    return s

s = 'geeksforgeeks_is_best'

ans= snake_to_pascal_case(s)
print(ans)
#conversion of snake case to pascal case    

