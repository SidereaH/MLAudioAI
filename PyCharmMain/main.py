#import files
#import learning
import os
import audioProccessing
#print("Экспорт модели")
#exec(open('files.py').read())
#print("Обучение модели")
#exec(open(learning.py))

print("Добро пожаловать на арену смерти")
#exec(open('audioProccessing.py').read())

# Путь к папке, содержащей файлы
folder_path = 'audioVal'

# Получение списка файлов в папке
files = os.listdir(folder_path)
print(files)
# # Теперь переменная files содержит список файлов в указанной папке
#
# # Дополнительно, чтобы получить только файлы, а не папки:
# files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
#
# # Для получения полного пути к файлам:
# file_paths = [os.path.join(folder_path, f) for f in files]

# Теперь переменная file_paths содержит список полных путей к файлам в указанной папке



