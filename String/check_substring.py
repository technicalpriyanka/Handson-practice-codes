def check_substring(string, substring):
    if substring in string:
        return True
    return False

string="priyanka"
substring="ank"

ans=check_substring(string, substring)
print(ans)