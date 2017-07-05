import string
texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you".lower()
palavra_texto = []
for i in string.punctuation:
    texto = texto.replace(i,' ')
texto = texto.split() 
for palavra in texto:
    for letra in palavra:
        if (len(palavra)>= 4) and letra in 'python':
            palavra_texto.append(palavra)
            break
print (palavra_texto)
