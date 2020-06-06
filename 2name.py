def get_robberies():
    robberies = []
    with open('грабители.csv', 'rt', encoding='utf-8') as file:
        headers = file.readline()
        for line in file:  # 'Бибка, Джастленд, ультрамаркет Ультруся, ручка; помидор#10; булка, 02-11-2131, F, -\n'
            line_list = line.rstrip().split(', ')

            line_dict = {
                "имя": line_list[0],
                'город': line_list[1],
                'жертва': line_list[2],
                'вещи': line_list[3],
                'дата': line_list[4],
                'пойман': line_list[5] == 'T',
                'речь': line_list[6]
            }

            robberies.append(line_dict)
    return robberies


def get_cities_dict(robberies):
    cities_dict = {}

    for robbery in robberies:
        name = robbery['город']
        if name != 'Джастленд':
            if name not in cities_dict:
                cities_dict[name] = 0
            cities_dict[name] += 1
    return cities_dict


def find_our_city(cities_dict):
    name_max = ""
    max = 0
    for name in cities_dict:
        if cities_dict[name] > max:
            max = cities_dict[name]
            name_max = name
    return name_max


def find_city():
    robberies = get_robberies()
    cities = get_cities_dict(robberies)
    print(cities)
    name = find_our_city(cities)

    if len(name) == 0:
        print("НЕТ ТАКОГО ГОРОДА!!! :(")
    else:
        print(name)


def count_of_nu_in_string(string):  # string = 'Ну не! Так не подеть ну'
    count = 0
    words = string.split(' ')  # ['Ну', 'не!', "Так", "не"]
    for word in words:
        clear_word = word_filter(word)
        if clear_word == 'ну':
            count += 1
    return count


def word_filter(word):  # 'Lol?!' -> 'lol'
    clear_word = ""
    for symbol in word:
        if symbol.isalpha():
            clear_letter = symbol.lower()
            clear_word += clear_letter

    return clear_word




