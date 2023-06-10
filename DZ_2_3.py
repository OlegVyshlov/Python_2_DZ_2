import os


def merge_files(input_files, output_file):
    file_info = []

    # Считываем содержимое каждого файла и сохраняем информацию о нем
    for input_file in input_files:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            file_info.append((input_file, len(lines), lines))

    # Сортируем информацию о файлах по количеству строк в них
    file_info.sort(key=lambda x: x[1])

    # Записываем содержимое файлов в результирующий файл с указанием имени файла и количества строк
    with open(output_file, 'w') as file:
        for info in file_info:
            file.write(info[0] + '\n')
            file.write(str(info[1]) + '\n')
            file.writelines(info[2])
            file.write('\n')


def main():
    input_files = ['1.txt', '2.txt', '3.txt']
    output_file = 'result.txt'

    merge_files(input_files, output_file)
    print('Файлы успешно объединены.')


if __name__ == '__main__':
    main()
