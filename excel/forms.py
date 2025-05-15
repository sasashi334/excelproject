from django import forms
from .models import History


class FileUploadForm(forms.ModelForm):

    RowOrCol = forms.ChoiceField(
        label="行/列",
        choices=(
            ("row", "行"),
            ("col", "列"),
        ),
        initial="",
        widget=forms.Select(),
    )

    num = forms.CharField(label="何行/列目から")

    removestr = forms.CharField(
        label="検索する文字",
        required=False,
    )

    class Meta:
        model = History
        fields = ("file",)
