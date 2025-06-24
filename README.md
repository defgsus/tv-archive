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

**197** channels, **2,746,801*** programs, **1,819,764.5** hours playtime between **2023-01-17** and **2025-06-24**


### playtime per genre (top 30)

    475,033.7h 26.10% Serie
    293,864.7h 16.15% Magazin
    221,222.9h 12.16% Dokumentation
    163,772.9h 9.00%  Show
    162,180.6h 8.91%  Werbung
    133,834.4h 7.35%  Spielfilm
    120,697.9h 6.63%  Nachrichten
    100,756.4h 5.54%  Sport
    37,232.3h  2.05%  Reportage
    33,292.9h  1.83%  Musik
    15,525.5h  0.85%  Verschiedenes
    13,790.3h  0.76%  Wetter
    11,167.4h  0.61%  Programmende
    9,515.0h   0.52%  E-Sport
    6,420.4h   0.35%  Bericht
    5,649.1h   0.31%  Event
    3,541.9h   0.19%  *unknown*
    3,106.2h   0.17%  Videoclip
    2,653.7h   0.15%  Kurzfilm
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
