def slice_less(my_list, lesser):
    return sorted([num for num in my_list if num > lesser], reverse=True)

my_list = [234,999,51,5,1,5124,52,15,9,24,1,42]
foo = slice_less(my_list, 55)
print(foo)
