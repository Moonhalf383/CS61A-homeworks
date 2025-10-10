from wave import open
from struct import Struct
from math import floor

frame_rate = 11025

def encode(x):
    """Encode float x between -1 and 1 as two bytes.
    """
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name='song.wav', second=2):
    #通过采样器函数生成wav文件
    out = open(name,'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < second * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t += 1
    out.close()

def tri(frequency,amlitude = 0.3):
    #生成一个持续的具有指定频率和振幅的三角波采样器
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t/period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amlitude * tri_wave
    return sampler
 
c_freq,e_freq,g_freq = 261.63,329.63,392.00

def both(f,g):
    #返回一个函数，效果是输入的两个函数的效果之和
    return lambda t:f(t) + g(t)

def note(f, start, end, fade = 0.01):
    #f为一个采样器函数
    #本函数输出一个始于start秒终于end秒并播放f的新采样器函数。
    def sampler(t):
        second = t / frame_rate
        if second < start:
            return 0
        elif second > end:
            return 0
        elif second <start + fade:
            return (second - start) / fade * f(t)
        elif second > end - fade:
            return (end - second) / fade * f(t)
        else:
            return f(t)
    return sampler

c,e = tri(c_freq),tri(e_freq)
g, low_g = tri(g_freq),tri(g_freq / 2)
play(both(note(c,0,1/4),note(e,1/2,1)))

def mario_at(octave):
    c,e = c,e = tri(octave * c_freq),tri(octave * e_freq)
    g, low_g = tri(octave * g_freq),tri(octave * g_freq / 2)
    return mario(c,e,g,low_g)

def mario(c,e,g,low_g):
    z = 0
    song = note(e,z,z+1/8)
    z += 1/8
    song = both(song,note(e,z,z+1/8))
    z += 1/4
    song = both(song,note(e,z,z+1/8))
    z += 1/4
    song = both(song,note(c,z,z+1/8))
    z += 1/8
    song = both(song,note(e,z,z+1/8))
    z += 1/4
    song = both(song,note(g,z,z+1/4))
    z += 1/2
    song = both(song,note(low_g,z,z+1/4))
    return song

play(both(mario_at(1),mario_at(0.5)))