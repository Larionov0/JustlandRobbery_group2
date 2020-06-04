file = open('Странное письмо.txt', 'rt')

text = file.read()
numbers = text.split(' ')

text2 = ""
for number_str in numbers:
    if number_str != '':
        number = int(number_str)   # 1045
        symbol = chr(number)
        text2 += symbol
file.close()

file = open('письмо.txt', 'wt')

file.write(text2)

file.close()
