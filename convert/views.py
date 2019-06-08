from django.shortcuts import render, redirect
from .forms import DownloadForm
from .models import Video
from youtube_dl import YoutubeDL

def index(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('link')
            Video.objects.create(link=link)
            options = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }
            ydl = YoutubeDL(options)
            extracted_info_about_video = ydl.extract_info(link, download=False)
            download_link = extracted_info_about_video['url']
            return redirect(download_link)
    else:
        form = DownloadForm()
    return render(request, 'convert/index.html', {'form': form})
