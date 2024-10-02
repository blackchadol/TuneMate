import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
#from nlp import genre

cid = 'bad5081179454c7aac97e6f6eabbb794'
secret = '0aa836ce7d22486c8e2b5b51dec47687'
redirect_uri = 'http://localhost:8080/callback'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri=redirect_uri,  scope="playlist-modify-public"))


# valence에 따라 트랙 검색 함수 (장르 제외)
def search_tracks_by_valence(valence_threshold):
    results = sp.search(q='track', type='track', limit=50)  # 기본 검색, 장르 제한 없음
    tracks = []

    for track in results['tracks']['items']:
        # 각 트랙의 오디오 피처 가져오기
        track_features = sp.audio_features(track['id'])[0]

        # 지정된 valence 범위와 일치하는 트랙만 추가
        if track_features and 0.0 <= track_features['valence'] <= valence_threshold:
            tracks.append(track['id'])

    return tracks

# 플레이리스트 생성 함수
def create_playlist(user_id, playlist_name):
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
    return playlist

# 유저 이름과 생성할 플레이리스트 이름
user_id = sp.current_user()['id']  # OAuth 인증된 사용자 ID 가져오기
playlist_name = 'Generated Playlist'

# 플레이리스트 생성 함수
def create_playlist(user_id, playlist_name, tracks):
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
    sp.playlist_add_items(playlist['id'], tracks)
    return playlist

# 긍정도에 따른 플레이리스트 생성 예시
positivity_score = 0.5  # Hugging Face API로부터 받은 긍정도 (0.0 ~ 1.0)
valence_threshold = positivity_score  # valence 기준을 긍정도로 설정

# 사용자 정보 가져오기
user_id = sp.current_user()['id']

# valence 기준으로 트랙 검색 및 플레이리스트 생성
tracks = search_tracks_by_valence(valence_threshold)
if tracks:
    playlist = create_playlist(user_id, 'Valence-based Playlist', tracks)
    print(f"플레이리스트 생성 성공: {playlist['external_urls']['spotify']}")
else:
    print("해당 valence 기준에 맞는 트랙을 찾을 수 없습니다.")