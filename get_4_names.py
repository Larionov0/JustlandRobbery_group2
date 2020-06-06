def parse_product(string):
    """
    :param string: "помидор#15; чипсы#3; шоколадка#20; телефон"
    :return: {
        'помидоры': 15,
        'чипсы': 3,
        'шоколадка': 20,
        'телефон': 1
    }
    """
    prods_list = string.split('; ')  # ['помидор#15', 'чипсы#3', 'шоколадка#20', 'телефон']
    prods_dict = {}
    for prod in prods_list:  # 'помидор#15'  'телефон'
        if "#" in prod:
            name_count = prod.split('#')  # ['cat', '10']
            prods_dict[name_count[0]] = int(name_count[1])
        else:
            prods_dict[prod] = 1
    return prods_dict


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
                'вещи': parse_product(line_list[3]),
                'дата': str_date_to_list(line_list[4]),
                'пойман': line_list[5] == 'T',
                'речь': line_list[6]
            }

            robberies.append(line_dict)
    return robberies


def str_date_to_list(string):  # "02-11-2131"  ->  [2, 11, 2131]
    lst = string.split('-')
    new_list = []
    for el in lst:
        new_list.append(int(el))
    return new_list


def get_konfetolub_name():  # Лопаточка
    robberies = get_robberies()
    thieves_counts = {}

    for robbery in robberies:
        if 'конфета' in robbery['вещи']:
            if robbery['имя'] not in thieves_counts:
                thieves_counts[robbery['имя']] = 0

            thieves_counts[robbery['имя']] += robbery['вещи']['конфета']

    print(thieves_counts)

    max_name = ""
    max_count = 0
    for name in thieves_counts:
        if thieves_counts[name] > max_count:
            max_count = thieves_counts[name]
            max_name = name

    print(max_name)


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


def get_city_name():  # Здесьтаун
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


def get_nuker_name():  # Воробоб
    thieves_counts = {}
    robberies = get_robberies()
    for robbery in robberies:
        name = robbery['имя']
        speak = robbery['речь']
        count = count_of_nu_in_string(speak)

        if name not in thieves_counts:
            thieves_counts[name] = 0

        thieves_counts[name] += count

    for name in thieves_counts:
        if thieves_counts[name] > 5:
            print(name)


def find_max_seria(months):
    months.sort()
    max_ = 0
    m = 1
    i = 1
    while i < len(months):
        if months[i] - months[i-1] == 1:
            m += 1
        else:
            if m > max_:
                max_ = m
            m = 1
        i += 1

    if m > max_:
        max_ = m

    return max_


def group_thefts_by_thieves(robberies):
    thieves_dates = {}
    for robbery in robberies:
        date = robbery['дата']
        name = robbery['имя']

        if name not in thieves_dates:
            thieves_dates[name] = {}

        year = date[2]
        month = date[1]

        if year not in thieves_dates[name]:
            thieves_dates[name][year] = []

        thieves_dates[name][year].append(month)

    return thieves_dates


def find_seriynik():  # Копырсанка
    robberies = get_robberies()
    thieves_dates = group_thefts_by_thieves(robberies)
    for thief in thieves_dates:
        max_ = 0
        for year in thieves_dates[thief]:
            seria = find_max_seria(thieves_dates[thief][year])
            if seria > max_:
                max_ = seria

        if max_ >= 4:
            print(thief)


find_seriynik()
