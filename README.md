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

**197** channels, **2,801,236*** programs, **1,858,669.3** hours playtime between **2023-01-17** and **2025-07-03**


### playtime per genre (top 30)

    486,240.6h 26.16% Serie
    298,561.8h 16.06% Magazin
    226,282.1h 12.17% Dokumentation
    166,744.6h 8.97%  Show
    164,500.9h 8.85%  Werbung
    137,976.0h 7.42%  Spielfilm
    122,193.8h 6.57%  Nachrichten
    104,541.7h 5.62%  Sport
    37,873.0h  2.04%  Reportage
    34,612.4h  1.86%  Musik
    16,191.9h  0.87%  Verschiedenes
    13,972.2h  0.75%  Wetter
    11,167.4h  0.60%  Programmende
    9,515.0h   0.51%  E-Sport
    6,517.9h   0.35%  Bericht
    5,703.8h   0.31%  Event
    3,541.9h   0.19%  *unknown*
    3,193.8h   0.17%  Videoclip
    2,831.9h   0.15%  Kurzfilm
    2,045.6h   0.11%  Verkaufsshow
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
