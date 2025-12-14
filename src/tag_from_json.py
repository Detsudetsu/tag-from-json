import json
from pathlib import Path
import typer
from mutagen.flac import FLAC
import re

def confirm(prompt: str) -> bool:
    """ユーザーに確認を求める"""
    return typer.confirm(prompt)

def write_tags(music_folder: Path, json_file: Path):
    # JSONファイルを読み込む
    with open(json_file, 'r', encoding='utf-8') as f:
        tracks_info = json.load(f)

    # 楽曲フォルダ内のすべてのFLACファイルを取得し、昇順にソートする
    files = sorted(music_folder.glob('*.flac'))

    # ファイルの数とトラック数が一致するか確認
    if len(files) != len(tracks_info):
        typer.echo("フォルダ内のファイル数とJSONデータのトラック数が一致しません。")
        if not confirm("それでも処理を続行しますか？"):
            typer.echo("処理を中止しました。")
            raise typer.Abort()

    # ソートされたファイルリストとJSONデータを使ってタグを更新する
    for file_path, track in zip(files, tracks_info):
        try:
            # ファイルのタグを読み込む
            audio = FLAC(file_path)
        except FileNotFoundError:
            typer.echo(f'ファイルが見つかりません: {file_path}')
            continue

        # タグ情報を更新する
        audio['discnumber'] = track['DISCNUMBER']
        audio['tracknumber'] = track['TRACKNUMBER']
        audio['title'] = track['TITLE']
        audio['artist'] = track['ARTIST']
        audio['album'] = track['ALBUM']
        audio['albumartist'] = track['ALBUMARTIST']
        
        # 変更を保存する
        audio.save()

        # now rename the file, but track name may contain some characters that won't be allowed to use in filename
        # so make sure to turn it into a valid filename
        track_name = re.sub(r'[\\/:*?"<>|]+', "_", track["TITLE"])
        file_name = (
            str(track["DISCNUMBER"]) + "." + str(track["TRACKNUMBER"]).zfill(2) + ". "
            + track_name
            + file_path.suffix
        )
        print(f'ファイル名: {file_name}')
        file_path.rename(music_folder / file_name)

        typer.echo(f'タグが更新されました: {file_path}')    #TODO: プログレスバーにする

    # フォルダ名リネーム時、ALBUM名のスラッシュやドット等もアンダーバーに変換
    safe_album = re.sub(r'[\\/:*?"<>|.]+', "-", track['ALBUM'])
    music_folder.rename(music_folder.parent / safe_album)


def main(music_folder: str, json_file: str):
    write_tags(Path(music_folder), Path(json_file))

if __name__ == "__main__":
    typer.run(main)
