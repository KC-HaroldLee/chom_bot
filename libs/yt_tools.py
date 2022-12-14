import pytube
import os
import pandas as pd
import uuid


DOWNLOAD_PATH = "./music/"

def to_time(s_length) -> str:
    min_v = int(s_length/60)
    sec_v = str(s_length - min_v*60).zfill(2)
    return f"{min_v}:{sec_v}"


def down_load_source(source, new_hash_v) :
    print(f"{source.title} 다운로드 시작...", end="")
    source.streams.filter(only_audio=True).first().download(os.path.join(DOWNLOAD_PATH), filename=f"{new_hash_v}.mp4")
    print("성공")


class YTTools():
    def __init__(self) :
        pass

    def get_file_by_url(self, yt_url:str) -> str : 
        song_csv_path = "./music/music_list.csv"
        song_df = pd.read_csv(song_csv_path)
        hash_v_list = list(song_df["yt_url"])

        '''
        hash_v,yt_url,yt_title,play_cnt,song_len,
        '''
        if not yt_url in hash_v_list :
            new_hash_v = str(uuid.uuid4())[-12:]

            source = pytube.YouTube(yt_url)
            yt_title = source.title
            play_cnt = 1
            song_len = to_time(source.length)

            
            next_idx = len(hash_v_list)+1

            down_load_source(source, new_hash_v)
            song_df.loc[next_idx] = [next_idx, new_hash_v, yt_url, yt_title, play_cnt, song_len]
            hash_v = new_hash_v

        else :
            condition = song_df['yt_url'] == yt_url
            target_row = song_df[condition]
            hash_v = target_row['hash_v'].values.item()
            yt_title = target_row['yt_title'].values.item()

            song_df.loc[song_df[condition].index, 'play_cnt'] += 1

        try :
            song_df.to_csv(song_csv_path, columns = ['hash_v', 'yt_url','yt_title','play_cnt','song_len'])
        except Exception as e:
            print(e)
        return hash_v, yt_title


