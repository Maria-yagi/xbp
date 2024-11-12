import lyricsgenius
from googletrans import Translator

# Genius APIの設定
genius= lyricsgenius.Genius("あなたのGeniusAPIトークン")

# 曲名を入力
song_title =input("曲名を入力してください")
artist_name=input("アーティスト名を入力してください")
    

 # 歌詞を取得
song = genius.search_song(song_title,artist_name)

if song:
        lyrics = song.lyrics
        print("\n歌詞を取得しました")

        #翻訳の準備
        Translator =Translator()
        translated_lyrics= Translator.translate(lyrics, src="en",dest="ja")

        print("\n日本語に翻訳された歌詞:\n", translated_lyrics.text)
else:
        print("歌詞が見つかりませんでした")


 