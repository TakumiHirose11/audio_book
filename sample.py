from ttslearn.dnntts import DNNTTS
from Ipython.display import Audio

engine = DNNTTS()
wav, sr = engine.tts("日本語音声合成のデモです。")
Audio(wav, rate=sr)