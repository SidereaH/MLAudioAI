import keras.saving
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
import librosa
import os


# Функция для загрузки аудиофайлов и создания спектрограмм
def load_and_extract_features(audio_file):
    audio, sr = librosa.load(audio_file, sr=None)
    # Преобразуем аудио в спектрограмму
    spectrogram = np.abs(librosa.stft(audio))
    # Изменяем размер спектрограммы для получения фиксированного размера входных данных
    resized_spectrogram = np.resize(spectrogram, (desired_rows, desired_columns))
    return resized_spectrogram

# Путь к папкам с аудиофайлами
fake_folder = "audio/spoofed"
real_folder = "audio/authentic"

# Загрузка и обработка аудиофайлов
fake_files = [os.path.join(fake_folder, f) for f in os.listdir(fake_folder) if f.endswith('.wav')]
real_files = [os.path.join(real_folder, f) for f in os.listdir(real_folder) if f.endswith('.wav')]

# Создание списка меток: 1 для дипфейков, 0 для нормальных аудиофайлов
labels = [1] * len(fake_files) + [0] * len(real_files)

# Слияние файлов и меток в один список
all_files = fake_files + real_files

# Параметры спектрограммы
desired_rows = 128
desired_columns = 128

# Создание массива признаков и меток
features = [load_and_extract_features(f) for f in all_files]

# Преобразование в numpy массивы
features = np.array(features)
labels = np.array(labels)

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Создание модели нейронной сети
model = models.Sequential([
    layers.Reshape((desired_rows, desired_columns, 1), input_shape=(desired_rows, desired_columns)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Компиляция модели
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Обучение модели
model.fit(X_train, y_train, epochs=5, batch_size=1, validation_data=(X_test, y_test))

# Сохранение модели
keras.saving.save_model(model,'audio_model.h5')

#while continue == True:
   # continue == False


# while contBool ==True:
#     # Загрузка аудиофайла
#     print("Введите название аудио, предварительно вставив его в каталог audioVal проекта")
#     try:
#         filename = input()
#         projPath = "audioVal/" + filename
#     except FileNotFoundError:
#         print("Не найден файл")
#
#     print(projPath)
#     audio_file_to_check = projPath
#
#     # Преобразование аудиофайла в спектрограмму
#     spectrogram_to_check = load_and_extract_features(audio_file_to_check)
#
#     # Загрузка сохранённой модели
#     loaded_model = models.load_model("audio_model.h5")
#
#     prediction = loaded_model.predict(np.expand_dims(spectrogram_to_check, axis=0))
#
#     # Анализ предсказания
#     if prediction[0][0] > 0.5:
#         print("Аудиофайл не является дипфейком.")
#     else:
#         print("Аудиофайл является дипфейком. ")
