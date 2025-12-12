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

**197** channels, **3,769,645*** programs, **2,557,497.3** hours playtime between **2023-01-17** and **2025-12-12**


### playtime per genre (top 30)

    683,072.2h 26.71% Serie
    381,490.2h 14.92% Magazin
    320,284.0h 12.52% Dokumentation
    218,513.6h 8.54%  Show
    215,641.6h 8.43%  Spielfilm
    205,878.7h 8.05%  Werbung
    173,185.1h 6.77%  Sport
    149,153.2h 5.83%  Nachrichten
    57,544.7h  2.25%  Musik
    50,126.2h  1.96%  Reportage
    28,881.5h  1.13%  Verschiedenes
    17,192.2h  0.67%  Wetter
    11,167.4h  0.44%  Programmende
    9,515.0h   0.37%  E-Sport
    7,932.3h   0.31%  Bericht
    6,893.4h   0.27%  Event
    5,814.1h   0.23%  Kurzfilm
    5,146.6h   0.20%  Videoclip
    3,541.9h   0.14%  *unknown*
    2,045.6h   0.08%  Verkaufsshow
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
