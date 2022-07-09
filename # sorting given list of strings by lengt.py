# sorting given list of strings by length of string

def sort_by_length(lst):
    lst.sort(key=len)
    return lst

a=['a','bb','ccc','dddd','eeeee']
print(sort_by_length(a))
# ['a', 'bb', 'ccc', 'dddd', 'eeeeee']
