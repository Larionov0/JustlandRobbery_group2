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
                'дата': line_list[4],
                'пойман': line_list[5] == 'T',
                'речь': line_list[6]
            }

            robberies.append(line_dict)
    return robberies


def get_konfetolub_name():
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


get_konfetolub_name()
