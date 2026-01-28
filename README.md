# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

TV is not as important anymore but still, archiving the decisions of which programs to run at what time
becomes another puzzle piece in the revelation of mind-control.. 

Data is stored in [docs/data/YEAR/MONTH/YEAR-MONTH-DAY.ndjson](docs/data/) files. 
Each entry looks like this:

```python
{
  "id": "181043890", 
  "url": "https://www.hoerzu.de/tv-programm/south-park-kohle-an-den-chefkoch/bid_181043890/", 
  "channel": "Comedy Central", 
  "title": "South Park", 
  "date": "2023-01-17T05:15:00",    # probably Europe/Berlin timezone 
  "length": 25,                     # minutes 
  "sub_title": "Serie", 
  "genre": "Erwachsenen-Animationsserie", 
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**198** channels, **4,044,892*** programs, **2,758,125.6** hours playtime between **2023-01-17** and **2026-01-28**


### playtime per genre (top 30)

    737,991.5h 26.76% Serie
    403,709.3h 14.64% Magazin
    348,118.3h 12.62% Dokumentation
    242,792.7h 8.80%  Spielfilm
    233,131.9h 8.45%  Show
    217,249.3h 7.88%  Werbung
    193,406.1h 7.01%  Sport
    156,621.3h 5.68%  Nachrichten
    62,477.9h  2.27%  Musik
    53,593.0h  1.94%  Reportage
    32,288.0h  1.17%  Verschiedenes
    18,146.9h  0.66%  Wetter
    11,167.4h  0.40%  Programmende
    9,515.0h   0.34%  E-Sport
    8,167.4h   0.30%  Bericht
    7,304.7h   0.26%  Event
    6,680.9h   0.24%  Kurzfilm
    5,695.5h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
    2,045.6h   0.07%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
