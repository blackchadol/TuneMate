from flask import Flask, request, jsonify
from nlp import query_hugging_face
from spotify_call import search_tracks_by_valence, create_playlist_with_tracks
app = Flask(__name__)

@app.route('/receive_text', methods=['POST'])
def receive_text():
    # JSON 요청에서 'text' 데이터 가져오기
    data = request.json  # JSON 데이터 가져오기
    input_text = data.get('text')  # 'text' 키에서 데이터 추출

    if input_text:
        print(f"받은 텍스트: {input_text}")  # 입력된 텍스트 출력 (디버깅 용도)
        valence_score = query_hugging_face(input_text)
        track_ids = search_tracks_by_valence(valence_score)
        playlist_url = create_playlist_with_tracks(track_ids)


        # 추가적으로 여기서 Hugging Face API를 호출하거나 다른 작업을 수행할 수 있습니다.
    return jsonify({'playlist_url': playlist_url})



    
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)  # 모든 IP에서 접근 가능

