import tensorflow as tf
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

def load_and_extract_features(audio_file):
    audio, sr = librosa.load(audio_file, sr=None)
    spectrogram = np.abs(librosa.stft(audio))
    resized_spectrogram = np.resize(spectrogram, (desired_rows, desired_columns))
    return resized_spectrogram

model_path = 'audio_model.h5'
model = tf.keras.models.load_model(model_path)
desired_rows = 128
desired_columns = 128
contBool = True

def audioProc(audio_file_to_check):
# while contBool ==True:
#     print("Введите название аудио, предварительно вставив его в каталог audioVal проекта")
#     findFile = True
#     while findFile == True:
#         filename = input()
#         projPath = "audioVal/" + filename
#         audio_file_to_check = projPath
#         if(os.path.exists(projPath) == False):
#             print("Не найден файл. Введите другое название")
#             findFile = True
#         else:
#             findFile = False
    spectrogram_to_check = load_and_extract_features(audio_file_to_check)
    prediction = model.predict(np.expand_dims(spectrogram_to_check, axis=0))

    if prediction[0][0] > 0.5:
        try:
            y, sr = librosa.load(audio_file_to_check, sr=None)
        # Создание спектрограммы
            plt.figure(figsize=(10, 4))
            librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max), sr=sr, x_axis='time',
                                    y_axis='log')
            plt.colorbar(format='%+2.0f dB')
            plt.title('Спектрограмма. Аудиофайл не является дипфейком')
            plt.show()
        except Exception as e:
            print(f"Ошибка при обработке файла {audio_file_to_check}: {e}")
    else:
        try:
            y, sr = librosa.load(audio_file_to_check, sr=None)
            # Создание спектрограммы
            plt.figure(figsize=(10, 4))
            librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max), sr=sr, x_axis='time',
                                     y_axis='log')
            plt.colorbar(format='%+2.0f dB')
            plt.title('Спектрограмма. Аудиофайл является дипфейком')
            plt.show()
        except Exception as e:
            print(f"Ошибка при обработке файла {audio_file_to_check}: {e}")


