
def is_reversible(number):
    string_repr = str(number)
    if (string_repr[-1] =='0') or (int(string_repr[-1]) % 2 == 1 and int(string_repr[0]) % 2 == 1) or ((int(string_repr[-1]) % 2 == 0 and int(string_repr[0]) % 2 == 1)):
        return False



print(is_reversible(123450))