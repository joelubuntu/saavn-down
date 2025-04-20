import requests,sys,json
from mutagen.mp4 import MP4, MP4Cover
file = requests.get("https://saavn.dev/api/songs",params={"link":sys.argv[1]})
x = json.loads(file.content)
artist = x["data"][0]['artists']['primary'][0]['name']
song_name = x["data"][0]['name'] + ' - ' + artist + '.m4a'
song_year = x["data"][0]['year']
language = x["data"][0]['language']
album_name = x["data"][0]['album']['name']
image_link = x["data"][0]['image'][2]['url']
if sys.argv[2].lower() == "low":
    link = audio_96 = x["data"][0]['downloadUrl'][2]['url']
if sys.argv[2].lower() == "medium":
    link = audio_160 = x["data"][0]['downloadUrl'][3]['url']
if sys.argv[2].lower() == "high":
    link = audio_320 = x["data"][0]['downloadUrl'][4]['url']
with open(song_name,'wb') as f:
    f.write(requests.get(link).content)

audio = MP4(song_name)
image = requests.get(image_link).content
audio["covr"] = [MP4Cover(image, imageformat=MP4Cover.FORMAT_JPEG)]
audio["\xa9nam"] = [x["data"][0]['name']]
audio["\xa9ART"] = [artist]   
audio["\xa9alb"] = [album_name]   
audio["\xa9day"] = [song_year]
audio["\xa9gen"] = [language]    
audio.save()
