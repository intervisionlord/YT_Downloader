from pytube import YouTube
from threading import *
import subprocess
import re
import sys
import os

class TThread(Thread):
      def __init__(self):
            Thread.__init__(self)
            self.thread = None
      
      def start(self, job, *args):
            self.thread = Thread(target = job, args = (args) )
            self.thread.run()

def multithread(videos, audios, video_id, audio_id, filename):
      def download_video(videos, video_id, filename):
            videos.get_by_itag(video_id).download(output_path= '', filename = f'Downloads\{filename}.video')

      def download_audio(audios, audio_id, filename):
            audios.get_by_itag(audio_id).download(output_path = '', filename = f'Downloads\{filename}.audio')
      
      threads_v = Thread(target = download_video, args = (videos, video_id, filename))
      threads_a = Thread(target = download_audio, args = (audios, audio_id, filename))
            
      threads_v.start()
      threads_a.start()
      
      threads_v.join()
      threads_a.join()
      video_merge(filename)

def dumper(pack_urls):
      if not os.path.isdir('Downloads'):
            os.mkdir('Downloads')
      for url in pack_urls:
            loader = YouTube(url)
            filename = re.sub('[\W\s]', '_', f'{loader.author}_{loader.title}')
            print(loader.streams)
            try:
                  videos = loader.streams.filter(resolution = '360p', type = 'video')
            except:
                  videos = loader.streams.filter(resolution = '360p', type = 'video')
            print(videos)
            video_id = int(list(videos.itag_index.copy().keys())[0])
            audios = loader.streams.filter(mime_type = 'audio/mp4', type = 'audio', bitrate = '48kbps')
            audio_id = int(list(audios.itag_index.copy().keys())[0])
            threads = Thread(target = multithread, args = (videos, audios, video_id, audio_id, filename))
            threads.start()
            
def video_merge(filename):
      # Вызов комманды с несколькими параметрами
      subprocess.call(
            [
                  'bin/ffmpeg.exe',
                  '-i',
                  f'Downloads\{filename}.video',
                  '-i',
                  f'Downloads\{filename}.audio',
                  '-c:v',
                  'copy',
                  '-c:a',
                  'aac',
                  fr'Downloads\{filename}.mp4'
                  ]
            )
      parts_delete(filename)

def parts_delete(filename):
      os.remove(f'Downloads\{filename}.audio')
      os.remove(f'Downloads\{filename}.video')

if 1 < len(sys.argv) <= 2:
      pack_urls = list(sys.argv[1])
else:
      getdata = input('Enter full URL: ').split(', ')
      print(getdata)
      dumper(getdata)