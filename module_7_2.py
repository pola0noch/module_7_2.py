# Домашнее задание по теме "Позиционирование в файле".

def custom_write(file_name, strings):
    file = open(file_name, "a", encoding="utf-8")
    strings_positions = {}

    for number, string in enumerate(strings, start=1):
        current_position = file.tell()
        strings_positions[(number, current_position)] = string
        file.write(f"{string}\n")

    file.close()

    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



