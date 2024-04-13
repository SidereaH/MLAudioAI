#import files
#import learning
import os

#print("Экспорт модели")
#exec(open('files.py').read())
#print("Обучение модели")
#exec(open(learning.py))
#exec(open('audioProccessing.py').read())

# Путь к папке, содержащей файлы
folder_path = 'audioVal'
# Получение списка файлов в папке
#добавить listbox с выбором файла
files = os.listdir(folder_path)
print(files)


