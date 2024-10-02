from nlp import query_hugging_face
from spotify_call import search_tracks_by_valence, create_playlist_with_tracks

def main(): 
    input_text = input("감정 분석할 문장을 입력하세요: ")
    valence_score = query_hugging_face(input_text)  # Hugging Face API로부터 점수 받기
    print(f"긍정적인 점수: {valence_score}")

    # valence_score를 이용해 트랙 검색
    track_ids = search_tracks_by_valence(valence_score)
    if track_ids:
        # 플레이리스트 생성 및 트랙 추가
        create_playlist_with_tracks(track_ids)
    else:
        print("트랙을 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
   