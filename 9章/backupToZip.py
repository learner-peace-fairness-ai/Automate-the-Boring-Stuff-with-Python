#! python3
# backupToZip.py - フォルダ全体を連番付きZIPファイルにコピーする

import os
from os import path
import zipfile
from zipfile import ZipFile


def backup_to_zip(folder):
    # フォルダ全体をZIPファイルにバックアップする

    # 既存のファイル名からファイル名の連番を決める
    number = 1
    while True:
        zip_filename = f'{path.basename(folder)}_{number}.zip'
        if not path.exists(zip_filename):
            break

        number += 1

    # ZIPファイルを作成する
    print(f'Creating {zip_filename}...')
    backup_zip = ZipFile(zip_filename, 'w')

    # フォルダのツリーを渡り歩いてその中のファイルを圧縮する
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # 現在のフォルダをZIPファイルに追加する
        backup_zip.write(foldername)
        # 現在のフォルダの中の全ファイルをZIPファイルに追加する
        new_base = f'{path.basename(folder)}_'
        for filename in filenames:
            if filename.startswith(new_base) and zipfile.is_zipfile(filename):
                continue  # バックアップ用ZIPファイルはバックアップしない
            backup_zip.write(os.path.join(foldername, filename))

    backup_zip.close()
    print('Done.')


backup_to_zip('delicious')
