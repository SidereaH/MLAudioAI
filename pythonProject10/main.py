import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Папка, содержащая аудиофайлы
audio_dir = "audio"

# Перебор всех файлов в указанной директории
for filename in os.listdir(audio_dir):
    if filename.endswith(".wav") or filename.endswith(".mp3"):  # Можно добавить другие форматы аудиофайлов
        audio_file = os.path.join(audio_dir, filename)
        try:
            # Загрузка аудиофайла с помощью librosa
            y, sr = librosa.load(audio_file, sr=None)

            # Создание спектрограммы
            plt.figure(figsize=(10, 4))
            librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max), sr=sr, x_axis='time',
                                     y_axis='log')
            plt.colorbar(format='%+2.0f dB')
            plt.title('Спектрограмма ' + filename)
            #plt.show()
        except Exception as e:
            print(f"Ошибка при обработке файла {audio_file}: {e}")
