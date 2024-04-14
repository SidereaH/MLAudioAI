import pandas as pd
import pyarrow.parquet as pq
import os
import stat

def filesFun():
     try:
          if(os.path.isdir('audio') == True):
               os.chmod('audio', stat.S_IWRITE)
               os.remove('audio')
     except (PermissionError):
          error = "Отказано в доступе при создании каталогов"
          print("error")
          return error


# Чтение данных из файла Parquet
     table = pq.read_table('data/validation-00000-of-00001-9b512eeb26464fba.parquet')
# Преобразование в DataFrame
     df = table.to_pandas()

# Установка параметров отображения pandas
     pd.set_option('display.max_rows', None)  # Показывать все строки
     pd.set_option('display.max_columns', None)  # Показывать все столбцы
     pd.set_option('display.width', None)  # Не обрезать вывод по ширине экрана


# Вывод всей информации о DataFrame
     print(df)

     #создание папок для хранения аудио базы обучения
     if os.path.isdir('audio') == False:
          os.mkdir("audio")

     os.chdir("audio")
     if os.path.isdir('spoofed') == False:
          os.mkdir("spoofed")
     if os.path.isdir('authentic') == False:
          os.mkdir("authentic")

     for i in range(len(df)):
          label = df.loc[i,'label']
          if label == "spoofed":
               os.chdir("spoofed")
               audio_file_path = df.loc[i, 'audio']
               byte = audio_file_path['bytes']
               with open(f'myfile{i}.wav', mode='bx') as f:
                    f.write(byte)
               os.chdir("..")
          else:
               os.chdir("authentic")
               audio_file_path = df.loc[i, 'audio']
               byte = audio_file_path['bytes']
               with open(f'myfile{i}.wav', mode='bx') as f:
                    f.write(byte)
               os.chdir("..")
     print("Done")
