# Generating random strings until a given string is generated
import string
import random

#possible characters
possible_characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase + string.printable + string.hexdigits + string.octdigits + string.punctuation + string.whitespace + ' ., !?;:'

#target string
target = "Priyanka"

#generate initial random string
def generate_random_string(length, possible_characters):
    result = ""
    for _ in range(length):
        result+=random.choice(possible_characters) #choose random from empty string
    return result


def fitness(current):
    # Calculate the fitness of the current string compared to the target string
    count = 0
    for i in range(len(current)):
        for j in range(len(target)):
            if current[i] == target[i]:
                count+=1
    return count

#mutation function
def mutate(parent):
    index = random.randint(0, len(parent) - 1) #choose random index to mutate
    child = list(parent) #convert string to list    
    child[index] = generate_random_string(1, possible_characters)

    return ''.join(child) #convert list back to string

#main function
attempt = generate_random_string(len(target), possible_characters)
 #generate random string of same length as target
print("Initial random string:", attempt)
print("Target string:", target)
print("Possible characters:", possible_characters)

iteration = 0

while attempt != target:
    print("Current string:", attempt)

    new_attempt = mutate(attempt) #mutate the string

    if fitness(new_attempt) >= fitness(attempt):
        attempt=new_attempt

    iteration+=1

print(f"Target string '{target}' generated after {iteration} iterations.")

print("Final string:", attempt)