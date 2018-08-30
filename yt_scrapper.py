from stikpro_yt_api import YoutubeAPI


class YoutubeSAPI:

    channel_list: list = None
    yt_api = None

    def __init__(self, dev_token: str, channel_list: list):
        self.channel_list = list(map(YoutubeAPI.parse_channel_id, channel_list))
        self.yt_api = YoutubeAPI(dev_token)

    def __get_channel_stat(self, ch_id: str) -> dict:

        def create_video_stat():
            curr_page_token: str = ''
            while curr_page_token is not None:
                curr_video_list = self.yt_api.get_videos_from_playlist(pl_id='UU' + ch_id[2:], max_results=50, next_page_token=curr_page_token)
                curr_page_token = curr_video_list[1]
                for video in curr_video_list[0]:
                    stat: dict = video.get('statistics')
                    try:
                        video['er'] = round((int(stat.get('dislikeCount')) + int(stat.get('likeCount')) + int(stat.get('commentCount'))) / int(stat.get('viewCount')) * 100, 3)
                    except:
                        video['er'] = None
                    yield video

        return {
            "channel_info": self.yt_api.get_channel_info(ch_id),
            "videos_stat": list(create_video_stat()),
        }

    def get_channels_info(self) -> list:
        return [self.__get_channel_stat(e) for e in self.channel_list]
