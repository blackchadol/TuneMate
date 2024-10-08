# Tune Mate - AI 기반 Spotify 플레이리스트 생성기

이 프로젝트는 사용자의 음성입력을 텍스트로 변환 후 감정 분석을 수행하고, 그에 따라 Spotify에서 적절한 플레이리스트를 생성하는 Flask 기반 웹 애플리케이션입니다. 
사용자는 안드로이드에서 음성 인식을 통해 텍스트를 입력할 수 있으며, Flask 서버가 텍스트를 처리해 Spotify에서 감정에 맞는 트랙들을 추천합니다.

## 백엔드 프로젝트 구조

- `flask_server.py`: Flask 서버 파일로, 안드로이드로부터 텍스트 입력을 받아 Hugging Face 감정 분석을 수행한 후, Spotify에서 플레이리스트를 생성후 서버로 반환
- `spotify_call.py`: 입력받은 텍스트의 긍정도를 바탕으로 Spotify API를 이용해 트랙을 검색하고 플레이리스트를 생성 후 URL 반환
- `nlp.py`: Hugging Face API를 호출해 텍스트 감정 분석을 수행하고, 긍정적인 감정의 점수를 반환
- `requirements.txt`: 프로젝트 실행에 필요한 모든 Python 라이브러리 목록
- `AWS E2C` : AWS EC2 인스턴스를 이용해 FLASK서버 호스팅, http://3.26.61.213:5000/receive_text에 POST 방식으로 JSON 형식의 텍스트 데이터를 전송하여 서버 사용 가능

## 필요한 설정

1. **Spotify API 설정**
   - Spotify 개발자 계정에서 클라이언트 ID, 시크릿을 생성하고, 리다이렉트 URI를 설정해야 함
   - 이를 위해 [Spotify 개발자 콘솔](https://developer.spotify.com/dashboard/)에서 애플리케이션을 등록하고, `spotify_call.py`에 해당 정보를 입력

2. **Hugging Face API 설정**
   - Hugging Face에서 제공하는 한국어 감정 분석 모델을 사용
   - [Hugging Face API 토큰](https://huggingface.co/settings/tokens)을 생성한 후, `nlp.py` 파일에 이를 추가

## 설치 방법

1. GitHub에서 프로젝트를 클론합니다.

```
git clone https://github.com/blackchadol/TuneMate.git
cd TuneMate
```


##  필요한 설정
```
pip install -r requirements.txt
```
터미널에 위 명령어를 입력해 프로그램 실행에 필요한 패키지 설치필수

