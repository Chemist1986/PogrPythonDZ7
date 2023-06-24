import os
import shutil

def sort_files(source_folder):
    # Создание папок для групп файлов
    groups = {
        'Videos': ['.mp4', '.mov', '.avi'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Text': ['.txt', '.doc', '.docx', '.pdf'],
        # Добавьте другие группы и их расширения, если необходимо
    }

    # Создание папок для каждой группы
    for group in groups:
        folder_path = os.path.join(source_folder, group)
        os.makedirs(folder_path, exist_ok=True)

    # Перебор файлов в исходной папке
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Игнорирование папок
        if os.path.isdir(file_path):
            continue

        # Получение расширения файла
        _, file_extension = os.path.splitext(filename)

        # Перемещение файла в соответствующую группу, если расширение известно
        moved = False
        for group, extensions in groups.items():
            if file_extension.lower() in extensions:
                destination_folder = os.path.join(source_folder, group)
                shutil.move(file_path, destination_folder)
                moved = True
                break

        # Если файл не подошел для сортировки, оставляем его в исходной папке
        if not moved:
            print(f"Не удалось сортировать файл: {filename}")

if __name__ == "__main__":
    source_folder = input("Введите путь к исходной папке: ")
    sort_files(source_folder)
