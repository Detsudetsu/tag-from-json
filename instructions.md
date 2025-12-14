# 楽曲ファイルへのタグ付与手順

## 目的
指定したフォルダ内の楽曲ファイル（例：mp3, flacなど）に、インターネットから取得した正確な曲情報をタグとして付与します。

## 手順
1. 対象となる楽曲の情報（タイトル、アーティスト、アルバム名など）をインターネットで調査し、下記のJSON形式で保存します。
   - 曲数や曲順、アーティスト名などは公式情報や信頼できるデータベースを参考にしてください。
   - 「Off Vocal」曲も含め、トラック順に記載してください。
2. タグ付けしたい楽曲ファイルを、任意のフォルダ（例：dist/split）に配置します。
   - ファイル名が「1.01. 不明なタイトル.flac」などでも、TRACKNUMBER順にタグが付与されます。
3. 以下のコマンドでタグ付けを実行します：

   ```bash
   python src/tag_from_json.py <楽曲フォルダのパス> <曲情報jsonファイルのパス>
   ```
   例：
   ```bash
   python src/tag_from_json.py dist/split dist/split.json
   ```
4. 実行後、指定フォルダ内の楽曲ファイルにタグが正しく付与されているか確認してください。

## JSONファイルの例

```json
[
  {
    "DISCNUMBER": "1",
    "TRACKNUMBER": "1",
    "TITLE": "37.5℃のファンタジー",
    "ARTIST": ["スリーズブーケ"],
    "ALBUM": "37.5℃のファンタジー / アイマイメーデー / BLAST!! / 十六夜セレーネ",
    "ALBUMARTIST": ["蓮ノ空女学院スクールアイドルクラブ"]
  },
  {
    "DISCNUMBER": "1",
    "TRACKNUMBER": "2",
    "TITLE": "アイマイメーデー",
    "ARTIST": ["DOLLCHESTRA"],
    "ALBUM": "37.5℃のファンタジー / アイマイメーデー / BLAST!! / 十六夜セレーネ",
    "ALBUMARTIST": ["蓮ノ空女学院スクールアイドルクラブ"]
  },
  {
    "DISCNUMBER": "1",
    "TRACKNUMBER": "3",
    "TITLE": "BLAST!!",
    "ARTIST": ["みらくらぱーく！"],
    "ALBUM": "37.5℃のファンタジー / アイマイメーデー / BLAST!! / 十六夜セレーネ",
    "ALBUMARTIST": ["蓮ノ空女学院スクールアイドルクラブ"]
  },
  {
    "DISCNUMBER": "1",
    "TRACKNUMBER": "4",
    "TITLE": "十六夜セレーネ",
    "ARTIST": ["Edel Note"],
    "ALBUM": "37.5℃のファンタジー / アイマイメーデー / BLAST!! / 十六夜セレーネ",
    "ALBUMARTIST": ["蓮ノ空女学院スクールアイドルクラブ"]
  },
  {
    "DISCNUMBER": "1",
    "TRACKNUMBER": "5",
    "TITLE": "37.5℃のファンタジー（Off Vocal）",
    "ARTIST": ["スリーズブーケ"],
    "ALBUM": "37.5℃のファンタジー / アイマイメーデー / BLAST!! / 十六夜セレーネ",
    "ALBUMARTIST": ["蓮ノ空女学院スクールアイドルクラブ"]
  },
  {
    "DISCNUMBER": "1",
    "TRACKNUMBER": "6",
    "TITLE": "アイマイメーデー（Off Vocal）",
    "ARTIST": ["DOLLCHESTRA"],
    "ALBUM": "37.5℃のファンタジー / アイマイメーデー / BLAST!! / 十六夜セレーネ",
    "ALBUMARTIST": ["蓮ノ空女学院スクールアイドルクラブ"]
  },
  {
    "DISCNUMBER": "1",
    "TRACKNUMBER": "7",
    "TITLE": "BLAST!!（Off Vocal）",
    "ARTIST": ["みらくらぱーく！"],
    "ALBUM": "37.5℃のファンタジー / アイマイメーデー / BLAST!! / 十六夜セレーネ",
    "ALBUMARTIST": ["蓮ノ空女学院スクールアイドルクラブ"]
  },
  {
    "DISCNUMBER": "1",
    "TRACKNUMBER": "8",
    "TITLE": "十六夜セレーネ（Off Vocal）",
    "ARTIST": ["Edel Note"],
    "ALBUM": "37.5℃のファンタジー / アイマイメーデー / BLAST!! / 十六夜セレーネ",
    "ALBUMARTIST": ["蓮ノ空女学院スクールアイドルクラブ"]
  }
]
```

## 注意事項
- JSONファイルの形式が正しくない場合、タグ付けに失敗することがあります。
- 曲情報は公式サイトや信頼できる音楽データベースから取得してください。
- 作詞・作曲・編曲などの情報はJSONに含めず、上記のシンプルな形式（DISCNUMBER, TRACKNUMBER, TITLE, ARTIST, ALBUM, ALBUMARTIST）を守ってください。
- TRACKNUMBER順にファイルへタグが付与されるため、楽曲ファイルの並び順とjsonの順番が一致していることを確認してください。
- 不明なタイトルや仮のファイル名でも、タグ付与後は正しい曲名・アーティスト名が反映されます。
- 既存のjsonファイルやサンプルファイルは消える可能性があるため、必ずこのファイル内の例を参照してください。
