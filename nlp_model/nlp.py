import requests

API_URL = "https://api-inference.huggingface.co/models/matthewburke/korean_sentiment"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

# 입력 문장에 대한 감정 분석
input_text = "I like you. I love you."
output = query({"inputs": input_text})

# 레이블과 스코어 확인
label = output[0][0]['label']  # LABEL_1 또는 LABEL_0
score = output[0][0]['score']   # 스코어 값

# 장르 결정
if label == "LABEL_1":
    genre = "happy"  # 긍정적
else:
    genre = "sad"  # 부정적
	
print(label)
print(score)