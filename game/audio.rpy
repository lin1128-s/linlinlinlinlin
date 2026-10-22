################################################################################
## 音频
################################################################################

define audio.rain = "audio/rain_loop.wav"
define audio.rain_heavy = "audio/rain_heavy.wav"
define audio.thunder = "audio/thunder.wav"
define audio.knock = "audio/knock.wav"
define audio.door = "audio/door_creak.wav"
define audio.suitcase = "audio/suitcase.wav"
define audio.tv = "audio/tv.wav"
define audio.heart = "audio/heartbeat.wav"
define audio.flash = "audio/flash.wav"
define audio.bgm = "audio/bgm.wav"

init python:

    ## 雨声与电视各占一个循环声道，互不打断
    renpy.music.register_channel("rain", mixer="sfx", loop=True)
    renpy.music.register_channel("amb", mixer="sfx", loop=True)
