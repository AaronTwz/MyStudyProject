from pydub import AudioSegment
import os


def trans_wav_to_mp3(filepath):
    song = AudioSegment.from_wav(filepath)
    songName = os.path.basename(file)
    song.export("%s.mp3" % songName, format="mp3")

file = r"C:\Users\Administrator\Desktop\bgm.wav"

trans_wav_to_mp3(file)
print("转换完成")
