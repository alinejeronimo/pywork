import string
a = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you".lower()
b = []
for i in string.punctuation:
    a = a.replace(i,' ')
a = a.split() 
for palavra in a:
    if (palavra[0] in 'python' or palavra[-1] in 'python'):
        b.append(palavra)
print(a)
print('\nlista de palavras: ', b)
