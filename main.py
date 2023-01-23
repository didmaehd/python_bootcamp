
# x = ("abc")
# y = ["a","b","c"]
# print(x[1]) 
# print(y[1])

# print(x[1] == y[1])
# print (x.index("b") + 1)


shift = 4
text = ("abc")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cipher = ""
for i in range(len(text)):
    replace_position = alphabet.index(text[i]) + shift
    replace_text = alphabet[replace_position]
    cipher = cipher + replace_text
print(cipher)
    
