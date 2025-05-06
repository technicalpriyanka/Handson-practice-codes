#replace all duplicate occurrences of a word in a string with a single occurrence

def replace_duplicate_occurrences(test_str, replace_dict):
    test_list = test_str.split(' ')
    res = set()
    # print(res)


    for idx, ele in enumerate(test_list):
        # print(idx, ele)
        if ele in replace_dict:
            # print(ele)
            if ele in res:
                print(ele)
                test_list[idx] = replace_dict[ele]
            else:
                res.add(ele)

    res= ' '.join(test_list)
    return res

test_str = 'Gfg is best . Gfg also has Classes now Classes help understand better . ' 
replace_dict = {'Gfg': 'GFG', 'Classes': 'CLASSES'} 

ans  = replace_duplicate_occurrences(test_str, replace_dict)
print(str(ans))

