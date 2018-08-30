## Youtube scrapper
Youtube scrapper for stikpro

**Установка:**
* `pip install git+https://github.com/fn12gl34/youtube-api` (временно)
* `pip install git+https://github.com/fn12gl34/youtube-scrapper`

**Использование:**
```python
# Инициализация скрапера
yc = YoutubeSAPI('dev_token', [
    'channel_link1',
    'channel_link2'
])
# На данный момент можно передавать только линки вида https://www.youtube.com/channel/UCWmg4yE--6K8Kvr7BEGQFIw

# Заполнение структуры
data = {"items": yc.get_channels_info()}

# При дампе в json следует делать encoding='utf8'
```

**Возвращаемое значение:**
```json
[
  {
    "channel_info": {
      "title": "Имя канала",
      "description": "Описание канала",
      "customUrl": "Уникальная приставка к юрл",
      "published": "Дата открытия канала",
      "imgUrl": "Юрл изображения канала",
      "country": "Страна канала",
      "statistics": {
        "followers": "Кол-во подписчиков",
        "views": "Общее кол-во просмотров",
        "videoCount": "Кол-во видео на канале"
      }
    },
    "videos_stat": [
      {
        "title": "Имя видео",
        "description": "Описание видео",
        "imgUrl": "Юрл на обложку видео",
        "tags": ["Список тегов"],
        "defaultAudioLanguage": "Язык аудиодорожки по умолчанию",
        "video_id": "Айди видео",
        "statistics": {
          "viewCount": "Кол-во просмотров",
          "likeCount": "Кол-во лайков",
          "dislikeCount": "Кол-во дизлайков",
          "commentCount": "Кол-во комментариев"
        },
        "er": "Рейтинг вовлеченности (в процентах)"
      }
    ]
   }
]
```
