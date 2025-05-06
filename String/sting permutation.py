str="GFG"

import itertools

for i in itertools.permutations(str):
    # print(''.join(i))
    print('-'.join(i))

