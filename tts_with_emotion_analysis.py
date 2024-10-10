import pyttsx3
from transformers import pipeline

def emotion_analyzer(text: str):
    # 감정 분석 파이프라인 생성
    analyzer = pipeline("sentiment-analysis")

    # 텍스트의 감정 분석
    emotion = analyzer(text)[0]  # 결과는 리스트로 반환되므로 첫 번째 결과를 사용
    print(f"감정 분석 결과: {emotion}")
    return emotion

# TTS 음성 설정 함수
def set_tts_properties(engine, emotion_label):
    if emotion_label == "POSITIVE":
        # 긍정적인 감정일 때
        engine.setProperty('rate', 200)  # 빠른 속도
        engine.setProperty('volume', 1.0)  # 큰 소리
        # engine.setProperty('pitch', 150)  # 높은 톤 (pyttsx3는 pitch 직접 설정을 지원하지 않음)
    elif emotion_label == "NEGATIVE":
        # 부정적인 감정일 때
        engine.setProperty('rate', 100)  # 느린 속도
        engine.setProperty('volume', 0.5)  # 작은 소리
        # 낮은 톤은 기본 TTS에서 직접 설정할 수 없음
    else:
        # 중립적인 감정일 때
        engine.setProperty('rate', 150)  # 중간 속도
        engine.setProperty('volume', 0.8)  # 중간 소리

# 메인 코드
if __name__ == "__main__":
    # 변환할 텍스트
    # text = "오늘은 정말 좋은 하루야!"
    text = "최악이네."

    # 감정 분석
    emotion = emotion_analyzer(text)
    emotion_label = emotion["label"]

    # TTS 엔진 초기화
    engine = pyttsx3.init()

    # TTS 설정을 감정 분석 결과에 따라 조정
    set_tts_properties(engine, emotion_label)

    # 텍스트를 음성으로 변환하여 재생
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"음성 변환 중 오류가 발생했습니다: {e}")
