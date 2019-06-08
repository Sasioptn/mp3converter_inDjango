from django import forms

class DownloadForm(forms.Form):
    link = forms.RegexField(
        regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$', max_length=264)
