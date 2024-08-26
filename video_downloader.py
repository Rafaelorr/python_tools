from pytube import YouTube
link = input('link: ')

yt = YouTube(link)

opitie = input('hoe wil de video donwloaden ? lowest_resolution,highest_resolution,audio_only')
if opitie == 'highest_resolution':
  video = yt.streams.get_highest_resolution()
elif opitie == 'audio_only':
  video = yt.streams.get_audio_only()
elif opitie == 'lowest_resolution':
  video = yt.streams.get_lowest_resolution()
else:
  video = yt.streams.get_highest_resolution()

video.download()

print('klaar !')
