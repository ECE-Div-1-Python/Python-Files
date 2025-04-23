from operator import truediv


def emp(dictionary):
    if not dictionary:
        return True
    else:
        return False

empty_dict={}
empty_dict1={'key':'value'}
print("empty set:",emp(empty_dict))
print("non empty set:" ,emp(empty_dict1))
