
def is_reversible(number):
    string_repr = str(number)
    if (string_repr[-1] =='0') or (int(string_repr[-1]) % 2 == 1 and int(string_repr[0]) % 2 == 1) or ((int(string_repr[-1]) % 2 == 0 and int(string_repr[0]) % 2 == 0)):
        return False
    sum = number + int(string_repr[:-1])
    print(sum)
    for i in str(sum):
        print()
    return True



print(is_reversible(36))