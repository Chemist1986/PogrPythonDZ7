import os

def rename_files(directory, desired_name=None, digits_count=2, source_extension=None, target_extension=None, name_range=(0, -1)):
    # Получение списка файлов в указанной директории
    files = os.listdir(directory)

    # Перебор файлов
    for i, filename in enumerate(files, start=1):
        # Получение полного пути к файлу
        file_path = os.path.join(directory, filename)

        # Проверка расширения исходного файла
        if source_extension and not filename.endswith(source_extension):
            continue

        # Получение диапазона символов из исходного имени файла
        name_range_start, name_range_end = name_range
        original_name = filename[name_range_start:name_range_end]

        # Формирование нового имени файла
        new_name = f"{desired_name or ''}{original_name}{i:0{digits_count}}.{target_extension or ''}"

        # Получение полного пути к новому файлу
        new_file_path = os.path.join(directory, new_name)

        # Переименование файла
        os.rename(file_path, new_file_path)

if __name__ == "__main__":
    # Параметры функции
    directory = input("Введите путь к каталогу: ")
    desired_name = input("Введите желаемое конечное имя файлов (если не требуется, нажмите Enter): ")
    digits_count = int(input("Введите количество цифр в порядковом номере (по умолчанию 2): "))
    source_extension = input("Введите расширение исходного файла (если не требуется, нажмите Enter): ")
    target_extension = input("Введите расширение конечного файла (если не требуется, нажмите Enter): ")
    name_range_start = int(input("Введите начало диапазона сохраняемого оригинального имени: "))
    name_range_end = int(input("Введите конец диапазона сохраняемого оригинального имени: "))
    name_range = (name_range_start, name_range_end + 1)

    # Вызов функции переименования файлов
    rename_files(directory, desired_name, digits_count, source_extension, target_extension, name_range)
