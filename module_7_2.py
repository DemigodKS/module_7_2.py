from pprint import pprint

strings = ['Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']

def custom_write(file_name, strings):

    name = 'test.txt'
    file_name = open(name, 'a', encoding='utf-8')
    for i in strings:
        file_name.write(i + '\n')
    file_name.close()

    #1
    file_name = open(name, 'r', encoding='utf-8')
    n = 0
    for i in strings:
        n += 1
        tell_start = file_name.tell()
        read_ = file_name.readline()
        numbers_ = (n, tell_start)
        strings_positions = dict(zip([numbers_], [i]))
        print(strings_positions)
    file_name.close()
    print()
    #2
    file_name = open(name, 'r', encoding='utf-8')
    n = 0
    for i in strings:
        n += 1
        tell_start = file_name.tell()
        read_ = file_name.readline()
        print(f'(({n}, {tell_start}), {repr(i)})')
    file_name.close()

cc = custom_write('test.txt', strings)

