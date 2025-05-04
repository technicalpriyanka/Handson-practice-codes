# Least Frequent Character in String
from collections import Counter
def least_frequent_character(s):
    frequency = Counter(s)
    least_frequency_character = min(frequency, key=frequency.get)   #This finds the character with the lowest frequency.
    return least_frequency_character
    
    
s = "GeeksforGeeks"
ans=least_frequent_character(s)
print("The least frequent character in the string is:", ans) 

