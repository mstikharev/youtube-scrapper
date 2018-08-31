from stikpro_yt_api import YoutubeAPI


class YoutubeSAPI:

    channel_list: list = None
    yt_api = None

    def __init__(self, dev_token: str, channel_list: list):
        self.yt_api = YoutubeAPI(dev_token)
        self.channel_list = [YoutubeAPI.parse_channel_id(self.yt_api, ch) for ch in channel_list]

    def __get_channel_stat(self, ch_id: str) -> dict:

        last_ten_videos: list = []

        def create_video_stat():
            curr_page_token: str = ''
            while curr_page_token is not None:
                curr_video_list = self.yt_api.get_videos_from_playlist(pl_id='UU' + ch_id[2:], max_results=50, next_page_token=curr_page_token)
                curr_page_token = curr_video_list[1]
                for video in curr_video_list[0]:
                    stat: dict = video.get('statistics')
                    like_c: int = int(stat.get('likeCount')) if stat.get('likeCount') is not None else 0
                    dl_c: int = int(stat.get('dislikeCount')) if stat.get('dislikeCount') is not None else 0
                    c_c = int(stat.get('commentCount')) if stat.get('commentCount') is not None else 0
                    try:
                        video['er'] = round((like_c + dl_c + c_c) / int(stat.get('viewCount')) * 100, 3)
                    except:
                        video['er'] = None
                    if len(last_ten_videos) < 10: last_ten_videos.append(video)
                    yield video

        def get_last_ten_videos_stat(videos: list) -> int:
            v: int = 0
            l: int = 0
            dl: int = 0
            c: int = 0
            for video in videos:
                video_stat: dict = video.get('statistics')
                v += int(video_stat.get('viewCount'))
                l += int(video_stat.get('likeCount'))
                dl += int(video_stat.get('dislikeCount'))
                c += int(video_stat.get('commentCount'))
            return round((l + dl + c) / v * 100, 3)

        data: dict = {
            "channel_info": self.yt_api.get_channel_info(ch_id),
            "videos_stat": list(create_video_stat())
        }
        data['channel_info']['last_tenv_stat'] = get_last_ten_videos_stat(last_ten_videos)
        return data

    def get_channels_info(self) -> list:
        return [self.__get_channel_stat(e) for e in self.channel_list]
