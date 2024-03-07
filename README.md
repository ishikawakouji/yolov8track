# yolov8track
YOLO v8 tracking

## YOLO v8 を使った追跡

自分の手で動かしたのは初めてだったけど、うまく作られており、労せず使うことができたのでメモがわりに


- track_video_write.py
  - ビデオファイルを読み込んで、検出、追跡した結果をビデオファイルに保存するところまで。YouTubeをビデオファイル代わりに使う方法も載せた。
  コメントアウトしている部分を参照のこと


```python
# Open youtube
#video_url = "youtubeのURL"
#video = pafy.new(video_url)
#best = video.getbest(preftype="mp4")
```

## 参考

[マルチオブジェクト・トラッキングUltralytics YOLO](https://docs.ultralytics.com/ja/modes/track/)

[YouTube動画をOpenCVでキャプチャするスクリプト](https://qiita.com/suo-takefumi/items/4c63399e39edecdcf323)
