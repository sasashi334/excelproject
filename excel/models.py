from django.db import models
from django.core.validators import FileExtensionValidator
import os
import datetime
from django.utils import timezone
from pathlib import Path


def dir_path_name(instance, filename):
    tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
    date_time = datetime.datetime.now(tokyo_tz)  # 現在の時刻を取得
    date_dir = date_time.strftime("%Y/%m/%d")  # 年/月/日のフォーマットの作成
    time_stamp = date_time.strftime("%H-%M-%S")  # 時-分-秒のフォーマットを作成
    new_filename = time_stamp + filename  # 実際のファイル名と結合
    dir_path = os.path.join("files", date_dir, new_filename)  # 階層構造にする
    return dir_path


class History(models.Model):

    file = models.FileField(
        validators=[FileExtensionValidator(["xlsx", "xlsm"])], upload_to=dir_path_name
    )

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file.name

    def file_name(self):
        path = os.path.basename(self.file.name)  # ファイル名のみ抽出
        return path
