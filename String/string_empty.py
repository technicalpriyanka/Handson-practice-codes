#Check if a string can become empty by recursive deletion using Slicing

def can_become_empty(string, substring):
    ## If the string is empty, it can be considered successfully reduced to empty
    if not string:
        return True
    
    #substring exists in string
    index = string.find(substring)

    if index != -1:

        return can_become_empty(string[:index] + string[index + len(substring):], substring)
    
    return False


string = "geekforsgeeks"
substring = "geeks"

ans= can_become_empty(string, substring)
print(ans)