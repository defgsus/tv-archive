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

**197** channels, **2,608,236*** programs, **1,720,041.5** hours playtime between **2023-01-17** and **2025-06-01**


### playtime per genre (top 30)

    447,231.2h 26.00% Serie
    282,425.8h 16.42% Magazin
    208,195.5h 12.10% Dokumentation
    156,049.2h 9.07%  Werbung
    156,038.5h 9.07%  Show
    122,258.7h 7.11%  Spielfilm
    117,212.3h 6.81%  Nachrichten
    90,702.7h  5.27%  Sport
    35,376.3h  2.06%  Reportage
    29,824.5h  1.73%  Musik
    13,823.6h  0.80%  Verschiedenes
    13,346.2h  0.78%  Wetter
    11,167.4h  0.65%  Programmende
    9,515.0h   0.55%  E-Sport
    6,253.1h   0.36%  Bericht
    5,480.5h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,874.4h   0.17%  Videoclip
    2,218.2h   0.13%  Kurzfilm
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
