import librosa.display
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    file_name = "C:\\Users\\linpa\\github\\pl728.github.io\\media\\audio\\testing-4-23-2020\\song04-22-2020--18-54-09.wav"
    y, sr = librosa.load(file_name, sr=None, mono=True, offset=0.0)

    # print(len(samples), sampling_rate)
    #
    # duration = len(samples) / sampling_rate
    # print(duration)

    # plt.figure()
    # librosa.display.waveplot(y=samples, sr=sampling_rate)
    # plt.xlabel("time (seconds) -->")
    # plt.ylabel("amplitude")
    # plt.show()

    D = librosa.stft(y)
    D_harmonic, D_percussive = librosa.decompose.hpss(D)

    # Pre-compute a global reference power from the input spectrum
    rp = np.max(np.abs(D))

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    librosa.display.specshow(librosa.amplitude_to_db(np.abs(D), ref=rp), y_axis='log')
    plt.colorbar()
    plt.title('Full spectrogram')

    plt.subplot(3, 1, 2)
    librosa.display.specshow(librosa.amplitude_to_db(np.abs(D_harmonic), ref=rp), y_axis='log')
    plt.colorbar()
    plt.title('Harmonic spectrogram')

    plt.subplot(3, 1, 3)
    librosa.display.specshow(librosa.amplitude_to_db(np.abs(D_percussive), ref=rp), y_axis='log',
                             x_axis='time')
    plt.colorbar()
    plt.title('Percussive spectrogram')
    plt.tight_layout()
    plt.show()
