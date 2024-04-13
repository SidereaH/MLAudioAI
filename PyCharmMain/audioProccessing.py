import tensorflow as tf
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np



def load_and_extract_features(audio_file):
    audio, sr = librosa.load(audio_file, sr=None)
    # Преобразуем аудио в спектрограмму
    spectrogram = np.abs(librosa.stft(audio))
    # Изменяем размер спектрограммы для получения фиксированного размера входных данных
    resized_spectrogram = np.resize(spectrogram, (desired_rows, desired_columns))
    return resized_spectrogram

model_path = 'audio_model.h5'

model = tf.keras.models.load_model(model_path)


desired_rows = 128
desired_columns = 128
contBool = True
while contBool ==True:
    # Загрузка аудиофайла
    print("Введите название аудио, предварительно вставив его в каталог audioVal проекта")
    try:
        filename = input()
        projPath = "audioVal/" + filename
    except FileNotFoundError:
        print("Не найден файл")


    audio_file_to_check = projPath

    # Преобразование аудиофайла в спектрограмму
    spectrogram_to_check = load_and_extract_features(audio_file_to_check)
    # Загрузка сохранённой модели
    # loaded_model = models.load_model("audio_model.h5")

    prediction = model.predict(np.expand_dims(spectrogram_to_check, axis=0))

    # Анализ предсказания
    if prediction[0][0] > 0.5:
        print("Аудиофайл не является дипфейком.")
    else:
        print("Аудиофайл является дипфейком. ")

    try:
        y, sr = librosa.load(audio_file_to_check, sr=None)
        # Создание спектрограммы
        plt.figure(figsize=(10, 4))
        librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max), sr=sr, x_axis='time',
                             y_axis='log')
        plt.colorbar(format='%+2.0f dB')
        plt.title('Спектрограмма ' + filename)
        plt.show()
    except Exception as e:
         print(f"Ошибка при обработке файла {audio_file_to_check}: {e}")
