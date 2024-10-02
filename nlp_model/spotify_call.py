import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
#from nlp import genre

cid = 'bad5081179454c7aac97e6f6eabbb794'
secret = '0aa836ce7d22486c8e2b5b51dec47687'
redirect_uri = 'http://localhost:8080/callback'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri=redirect_uri,  scope="playlist-modify-public"))

# 플레이리스트 생성 함수
def create_playlist(user_id, playlist_name):
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
    return playlist

# 유저 이름과 생성할 플레이리스트 이름
user_id = sp.current_user()['id']  # OAuth 인증된 사용자 ID 가져오기
playlist_name = 'Generated Playlist'

# 플레이리스트 생성 시도
try:
    playlist = create_playlist(user_id, playlist_name)
    print(f"플레이리스트 생성 성공: {playlist['id']}")
except spotipy.exceptions.SpotifyException as e:
    print(f"플레이리스트 생성 실패: {e}")