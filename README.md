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

**195** channels, **2,100,135*** programs, **1,353,853.1** hours playtime between **2023-01-17** and **2025-03-08**


### playtime per genre (top 30)

    344,606.7h 25.45% Serie
    239,866.5h 17.72% Magazin
    160,067.4h 11.82% Dokumentation
    133,281.8h 9.84%  Werbung
    127,911.3h 9.45%  Show
    103,307.6h 7.63%  Nachrichten
    81,702.4h  6.03%  Spielfilm
    53,794.9h  3.97%  Sport
    28,948.8h  2.14%  Reportage
    17,255.1h  1.27%  Musik
    11,816.8h  0.87%  Wetter
    11,167.4h  0.82%  Programmende
    9,515.0h   0.70%  E-Sport
    7,467.8h   0.55%  Verschiedenes
    5,644.4h   0.42%  Bericht
    4,815.6h   0.36%  Event
    3,541.9h   0.26%  *unknown*
    2,046.3h   0.15%  Videoclip
    2,045.6h   0.15%  Verkaufsshow
    592.1h     0.04%  Kurzfilm
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
