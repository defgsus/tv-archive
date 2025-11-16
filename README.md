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

**197** channels, **3,614,344*** programs, **2,445,399.7** hours playtime between **2023-01-17** and **2025-11-16**


### playtime per genre (top 30)

    651,807.0h 26.65% Serie
    367,683.3h 15.04% Magazin
    305,428.1h 12.49% Dokumentation
    210,376.8h 8.60%  Show
    203,009.1h 8.30%  Spielfilm
    199,292.2h 8.15%  Werbung
    162,240.6h 6.63%  Sport
    144,706.7h 5.92%  Nachrichten
    53,670.7h  2.19%  Musik
    48,140.7h  1.97%  Reportage
    27,104.1h  1.11%  Verschiedenes
    16,664.2h  0.68%  Wetter
    11,167.4h  0.46%  Programmende
    9,515.0h   0.39%  E-Sport
    7,677.9h   0.31%  Bericht
    6,688.6h   0.27%  Event
    5,324.4h   0.22%  Kurzfilm
    4,843.6h   0.20%  Videoclip
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
