from random import randint, choice


def gen_age():
    age = randint(13, 159)
    return age


def gen_count():
    count = randint(3, 1000)
    return count


def gen_name():
    glas = "аоиеёэыуюя"
    sogl = "бвгджзйклмнпрстфхцчшщ"
    count_glas = 0
    count_sogl = 0
    count = randint(2, 15)

    name = ""
    i = 0
    while i < count:
        if count_glas == 2:
            vibor = 1
        elif count_sogl == 2:
            vibor = 0
        else:
            vibor = randint(0, 1)
        if vibor == 0:
            letter = choice(glas)
            count_glas += 1
            count_sogl = 0
        elif vibor == 1:
            letter = choice(sogl)
            count_sogl += 1
            count_glas = 0
        name += letter
        i += 1

    return name


def gen_policai():
    name = gen_name()
    age = gen_age()
    count = gen_count()

    string = f"{name}, {age}, {count}\n"
    return string


def fill_file():
    file = open('совершенно_секретно.csv', 'wt', encoding='utf-8')
    i = 0
    while i < 1100:
        file.write(gen_policai())
        i += 1
    file.close()


fill_file()
