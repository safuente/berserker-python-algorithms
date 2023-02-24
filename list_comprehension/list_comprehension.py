def get_name_by_char(c, input_list):
    return([x for x in input_list if c in x])


print('Example 1')
names = ['Peter', 'Mark', 'Martin', 'Luke']
c = 'u'
print(get_name_by_char(c, names))
