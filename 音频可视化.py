# coding=gbk
import warnings
warnings.simplefilter("ignore", DeprecationWarning)  # ��ֹ������
import pyaudio
import pydub
import wave
import numpy as np
import pygame
from pygame.locals import *

CHUNK = 1024  # �Ұ������Ϊ������

# song = pydub.AudioSegment.from_mp3(r"G:\CloudMusic\���� - ����д��ɢ��ʫ��Cover����ɣ�.mp3")
# song.export(r"G:\CloudMusic\newsong.wav", format='wav')
# print('ת��wav���')
wf = wave.open(r"G:\CloudMusic\newsong.wav", mode='rb')  # ��ֻ���ķ�ʽ��".wav"�ļ�

# ����������
p = pyaudio.PyAudio()
# ��������  output=True��ʾ��Ƶ���
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),  # ����������
                rate=wf.getframerate(),  # ��������Ƶ��
                output=True)

data = wf.readframes(CHUNK)  # ��Ƶ���ݳ�ʼ��
pygame.init()  # pygame��ʼ��

pygame.display.set_caption('ʵʱƵ��')  # ���ô��ڱ���
screen = pygame.display.set_mode((850, 400), 0, 32)  # ���ڴ�СΪ(850,400)
print('��ʼ������Ƶ')
while data != '':  # ֱ����Ƶ����

    stream.write(data)  # ���Ż���������Ƶ
    data = wf.readframes(CHUNK)  # ����data
    numpydata = np.fromstring(data, dtype=np.int16)  # ��data���ַ�����ʮ�����Ƶķ�ʽת��Ϊ����
    transforamed = np.real(np.fft.fft(numpydata))  # ����Ҷ�任��ȡʵ������

    screen.fill((0, 0, 0))  # �����Ļ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # ��δ����ֹ����Ӧ
    count = 50  # ���ü����
    for n in range(0, transforamed.size, count):  # ��Ƶ���е�2048��������û��count��������ѡȡһ��
        hight = abs(int(transforamed[n] / 10000))  # ����ô������ȡ���;���ֵ

        pygame.draw.rect(screen, (255, 255, 255), Rect((20 * n / count, 400), (20, -hight)))  # ������

    pygame.display.update()  # ������Ļ

stream.stop_stream()
stream.close()
# �ر���
p.terminate()
