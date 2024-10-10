import pyttsx3

# TTS 엔진 초기화
engine = pyttsx3.init()

# 변환할 텍스트
text = "안녕하세요! 파이티티에스엑스쓰리입니다."

# 텍스트를 음성으로 변환하여 재생
engine.say(text)
engine.runAndWait()
