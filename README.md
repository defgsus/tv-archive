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

**197** channels, **2,729,147*** programs, **1,806,807.2** hours playtime between **2023-01-17** and **2025-06-21**


### playtime per genre (top 30)

    471,507.0h 26.10% Serie
    292,449.2h 16.19% Magazin
    219,497.8h 12.15% Dokumentation
    162,744.3h 9.01%  Show
    161,373.8h 8.93%  Werbung
    132,242.8h 7.32%  Spielfilm
    120,297.8h 6.66%  Nachrichten
    99,389.7h  5.50%  Sport
    37,004.7h  2.05%  Reportage
    32,817.8h  1.82%  Musik
    15,311.1h  0.85%  Verschiedenes
    13,737.5h  0.76%  Wetter
    11,167.4h  0.62%  Programmende
    9,515.0h   0.53%  E-Sport
    6,407.0h   0.35%  Bericht
    5,623.5h   0.31%  Event
    3,541.9h   0.20%  *unknown*
    3,076.1h   0.17%  Videoclip
    2,596.5h   0.14%  Kurzfilm
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
