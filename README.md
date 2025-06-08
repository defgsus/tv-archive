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

**197** channels, **2,651,068*** programs, **1,750,427.6** hours playtime between **2023-01-17** and **2025-06-08**


### playtime per genre (top 30)

    455,960.6h 26.05% Serie
    285,951.8h 16.34% Magazin
    212,044.8h 12.11% Dokumentation
    158,396.4h 9.05%  Show
    157,925.0h 9.02%  Werbung
    125,582.4h 7.17%  Spielfilm
    118,317.2h 6.76%  Nachrichten
    93,743.6h  5.36%  Sport
    35,940.9h  2.05%  Reportage
    30,873.4h  1.76%  Musik
    14,364.6h  0.82%  Verschiedenes
    13,485.4h  0.77%  Wetter
    11,167.4h  0.64%  Programmende
    9,515.0h   0.54%  E-Sport
    6,291.4h   0.36%  Bericht
    5,524.4h   0.32%  Event
    3,541.9h   0.20%  *unknown*
    2,945.3h   0.17%  Videoclip
    2,349.7h   0.13%  Kurzfilm
    2,045.6h   0.12%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
