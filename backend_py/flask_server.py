from flask import Flask, request, jsonify
from nlp import query_hugging_face
from spotify_call import search_tracks_by_valence, create_playlist_with_tracks

app = Flask(__name__)

@app.route('/receive_text', methods=['POST'])
def receive_text():
    data = request.json
    input_text = data.get('text')

    # 초기 playlist_url 설정
    playlist_url = None

    if input_text:
        print(f"받은 텍스트: {input_text}")
        try:
            valence_score = query_hugging_face(input_text)
            track_ids = search_tracks_by_valence(valence_score)
            playlist_url = create_playlist_with_tracks(track_ids)
        except Exception as e:
            print(f"오류 발생: {str(e)}")
            return jsonify({'error': '처리 중 오류가 발생했습니다.'}), 500

    if playlist_url:
        return jsonify({'playlist_url': playlist_url})
    else:
        return jsonify({'error': '플레이리스트를 생성하지 못했습니다.'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


