# YT Downloader
![GitHub](https://img.shields.io/github/license/intervisionlord/YT_Downloader)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/intervisionlord/YT_Downloader/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/intervisionlord/YT_Downloader/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/intervisionlord/YT_Downloader/?branch=master)
![GitHub last commit](https://img.shields.io/github/last-commit/intervisionlord/YT_Downloader)

- [YT Downloader](#yt-downloader)
  - [Способ запуска](#способ-запуска)
  - [Потоки и нагрузка](#потоки-и-нагрузка)

Многопоточный массовый загрузчик видео с youtube

## Способ запуска
Принимает на вход одиночный URL на видео при запуске без аргументов в интерактивном режиме, либо список URL через запятую в качестве аргументов.

## Потоки и нагрузка
Пока ограничений по нагрузке не реализовано.
После запуска каждый URL обрабатывается в отдельном потоке. При обработке URL создается еще 2 потока. По одному на скачивание видео и аудио, соответственно. Следовательно, каждая дополнительная ссылка увеличивает нагрузку на сеть, CPU и диски суммарно на 3 потока.

После завершения 2х потоков на скачивание создается поток с вызовом ffmpeg для склеивания в единый файл аудио дорожки и видеоряда.

Удаление исходных файлов происходит в первом дочернем потоке обработки URL.