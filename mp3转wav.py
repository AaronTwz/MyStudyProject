from pydub import AudioSegment

fileName = 'i_1'
filePath = 'G:/CloudMusic/'
file = filePath + fileName + '.mp3'
song = AudioSegment.from_mp3(file)
song.export(filePath + fileName + '.wav', format="wav")

print("转换完成！")
