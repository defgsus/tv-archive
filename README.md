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

**197** channels, **2,782,920*** programs, **1,845,809.6** hours playtime between **2023-01-17** and **2025-06-30**


### playtime per genre (top 30)

    482,384.3h 26.13% Serie
    296,959.8h 16.09% Magazin
    224,633.7h 12.17% Dokumentation
    165,815.3h 8.98%  Show
    163,750.1h 8.87%  Werbung
    136,690.9h 7.41%  Spielfilm
    121,656.3h 6.59%  Nachrichten
    103,342.4h 5.60%  Sport
    37,648.1h  2.04%  Reportage
    34,193.4h  1.85%  Musik
    15,971.0h  0.87%  Verschiedenes
    13,908.1h  0.75%  Wetter
    11,167.4h  0.61%  Programmende
    9,515.0h   0.52%  E-Sport
    6,502.5h   0.35%  Bericht
    5,688.8h   0.31%  Event
    3,541.9h   0.19%  *unknown*
    3,163.9h   0.17%  Videoclip
    2,770.2h   0.15%  Kurzfilm
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
