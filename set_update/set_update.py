def set_update(s, ns):
    s.update(s, ns)
    return s


students = {'Luke', 'Peter', 'Homer'}
new_students = {'Bart', 'Neo'}
print('Example 1')
print(set_update(students, new_students))
