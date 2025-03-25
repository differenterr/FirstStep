import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

# (2) 钢琴音符的生成
def generate_sine_wave(frequency, duration, sampling_rate=44100):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * frequency * t)
piano_notes_freqs=[261,293,251,541,622,415,168,965,325,821]
# 钢琴音符频率（例如：C4, D4, E4, F4, G4）
duration = 1  # 每个音符时长 1秒
sampling_rate = 44100  # 抽样频率 44.1kHz
sampling_orate = 44100
# 生成多个音符并将它们拼接成一段乐曲
song_signal = np.array([])  # 空数组用于拼接音符
for freq in piano_notes_freqs:
    note_signal = generate_sine_wave(freq, duration, sampling_rate)
    song_signal = np.concatenate((song_signal, note_signal))  # 拼接音符
# 保存音频文件
# sf.write('piano_song.wav', song_signal, sampling_orate)

# 播放音频
sd.play(song_signal, sampling_orate)
sd.wait()
