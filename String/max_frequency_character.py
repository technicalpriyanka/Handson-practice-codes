from collections import Counter
def max_frequency_character(s):
    frequency=Counter(s)
    max_frequncy_counter = max(frequency, key=frequency.get)
    return max_frequncy_counter, frequency[max_frequncy_counter]

def main():


    s = "GeeksforGeeks"

    ans = max_frequency_character(s)
    print("The maximum frequency character in the string is:", ans)