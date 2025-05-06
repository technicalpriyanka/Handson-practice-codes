#checking url in string

s = 'My Profile: https://auth.geeksforgeeks.org/user/Rayyyy%20/articles in the portal of https://www.geeksforgeeks.org/'

import re

pattern = r'(https?://[^\s]+)'

urls = re.findall(pattern, s)


# print(urls)
for url in urls:
    print(url)
    # print(url, end="\n")
    # print(url, end=" ")