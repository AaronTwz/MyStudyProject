import wave
import struct
import math


def write_frame(time, freq, framerate, file, wave=0.4, sampwidth=2):
    # time 持续时间 freq 音频频率 framerate采样频率 file 音频文件 wave 音量 sampwidth 采样深度
    t = 0  # 时刻
    step = 1.0 / framerate  # 每帧间隔时长
    fw = 2.0 * math.pi * freq  # 频率控制参数
    wave = wave * (math.pow(2, sampwidth * 8 - 1) - 1)  # 音量控制
    while t <= time:
        v = int(math.sin(t * fw) * wave)  # 对波采样 math.sin(t*fw)产生freq频率的正弦波
        t += step  # 更新时刻
    # 最后这里是与sampwidth的值有关的，下面语句当前仅当sampwidth=2时成立，详细信息参考struct.pack()
    file.writeframesraw(struct.pack("h", v))  # 写入文件 struct.pack("h",v)将有符号整数v转化成16比特2进制


tw = wave.open("./two_tigers.wav", "wb")  # 打开或创建./two_tigers.wav
tw.setnchannels(1)  # 设置声道数 1
tw.setframerate(8000)  # 设置帧率 8000
tw.setsampwidth(2)  # 设置采样宽度2B 16bit

# 写入声音
# 1 2 3 1 1 2 3 1
write_frame(time=0.5, freq=256, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=288, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=320, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=256, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=256, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=288, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=320, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=256, framerate=8000, file=tw, wave=0.4, sampwidth=2)

# 3 4 5 - 3 4 5 -
write_frame(time=0.5, freq=320, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=341.33, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=384, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.25, freq=0, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=320, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=341.33, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=384, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.25, freq=0, framerate=8000, file=tw, wave=0.4, sampwidth=2)

# 56 54 3 1 - 56 54 3 1 -
write_frame(time=0.25, freq=384, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.25, freq=426.67, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.25, freq=384, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.25, freq=341.33, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=320, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=256, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.25, freq=384, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.25, freq=426.67, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.25, freq=384, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.25, freq=341.33, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=320, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=256, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.25, freq=0, framerate=8000, file=tw, wave=0.4, sampwidth=2)

# 2 6（低音） 1 - 2 6（低音） 1 -
write_frame(time=0.5, freq=288, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=144, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=256, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.25, freq=0, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=288, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=144, framerate=8000, file=tw, wave=0.4, sampwidth=2)
write_frame(time=0.5, freq=256, framerate=8000, file=tw, wave=0.4, sampwidth=2)

tw.close()

# C 1 do 256
# D 2 re 288
# E 3 mi 320
# F 4 fa 341又1/3
# G 5 so 384
# A 6 la 426又2/3
# B 7 si 480
# C 1 (上面一个点)do 512
# C:D=8:9
# D:E=9:10
# E:F=15:16
# F:G=8;9
# G:A=9:10
# A:B=15:16
