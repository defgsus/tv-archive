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

**195** channels, **2,058,302*** programs, **1,323,830.1** hours playtime between **2023-01-17** and **2025-03-01**


### playtime per genre (top 30)

    336,327.6h 25.41% Serie
    236,317.0h 17.85% Magazin
    156,185.8h 11.80% Dokumentation
    131,384.9h 9.92%  Werbung
    125,405.6h 9.47%  Show
    102,105.0h 7.71%  Nachrichten
    78,501.1h  5.93%  Spielfilm
    50,787.9h  3.84%  Sport
    28,499.7h  2.15%  Reportage
    16,216.2h  1.22%  Musik
    11,695.3h  0.88%  Wetter
    11,167.4h  0.84%  Programmende
    9,515.0h   0.72%  E-Sport
    6,947.9h   0.52%  Verschiedenes
    5,567.0h   0.42%  Bericht
    4,706.1h   0.36%  Event
    3,541.9h   0.27%  *unknown*
    2,045.6h   0.15%  Verkaufsshow
    1,987.1h   0.15%  Videoclip
    468.2h     0.04%  Kurzfilm
    353.9h     0.03%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.02%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
