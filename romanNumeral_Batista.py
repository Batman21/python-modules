"""
Roman Numeral Algorithm
"""
#  Value Mapper.

ROMAN_NUMERALS = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1

}


def precision_test(negative_list):
    # Error prone R.N. end with a list that is not greatest to lowest naturally
    precision_test = negative_list[:]
    precision_test.sort()
    precision_test.reverse()
    if precision_test == negative_list:
        return True
    else:
        return False


def analyze_list(helper_list):
    # Looping func for the list result R.N.
    x = 0
    helper_len = len(helper_list) - 1
    negative_list = []
    while helper_len > x:
        if helper_list[x] < helper_list[x+1]:
            if helper_list[x] == helper_list[x-1]:
                negative_list.append(helper_list.pop(x))
                helper_list.append(0)
                x -= 1
            else:
                negative_list.append(helper_list.pop(x))
                helper_list.append(0)
        else:
            x += 1
    if precision_test(negative_list) is True:
        positive = sum(helper_list)
        negative = sum(negative_list)
        print("Your answer is %i." % (positive-negative))
    else:
        print("Log your roman numerals from highest to lowest for accuracy.")


def conversion(roman):
    # Main function
    helper_list = []
    roman = roman.upper()
    roman = roman.replace(" ", "")
    for x in roman:  # Pending KeyError handling
        helper_list.append(ROMAN_NUMERALS[x])

    analyze_list(helper_list)


def testing_conversion():
    # Script loop
    while 1:
        print("Enter roman numerals.")
        conversion(input(""))

testing_conversion()
