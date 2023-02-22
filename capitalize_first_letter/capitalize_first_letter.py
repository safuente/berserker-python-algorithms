def capitalize(s):
    return(' '.join([ word.replace(word[0], word[0].upper(), 1) if word != ''  else '' for word in s.split(' ')]))

print("Example 1")
print(capitalize('berserker is teaching me python'))
print("\nExample 2")
print(capitalize('1 2 3 4 5'))
print("\nExample 3")
print(capitalize('1 2 3 4  5'))