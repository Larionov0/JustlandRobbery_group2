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


def get_thieves_dict(robberies):
    thieves_dict = {}

    for robbery in robberies:
        name = robbery['имя']
        is_caught = robbery['пойман']

        if name not in thieves_dict:
            thieves_dict[name] = {
                'удачи': 0,
                'неудачи': 0
            }

        if is_caught is True:
            thieves_dict[name]['неудачи'] += 1
        else:
            thieves_dict[name]['удачи'] += 1
    return thieves_dict


def find_our_thief(thieves_dict, lucks=5, failures=1):
    names = []
    for name in thieves_dict:
        if thieves_dict[name]['удачи'] == lucks and thieves_dict[name]['неудачи'] == failures:
            names.append(name)
    return names


def find_failures_and_words():
    robberies = get_robberies()
    thieves = get_thieves_dict(robberies)
    print(thieves)
    names = find_our_thief(thieves)

    if len(names) != 1:
        print("НЕ ОДИН ВОР!!! :(")
        print(names)
    else:
        name = names[0]
        print(name)
        for robbery in robberies:
            if robbery['имя']  == name:
                if robbery['пойман'] is True:
                    print(robbery['речь'])


find_failures_and_words()
