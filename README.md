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

**198** channels, **4,507,314*** programs, **3,087,782.3** hours playtime between **2023-01-17** and **2026-04-18**


### playtime per genre (top 30)

    834,167.3h 27.02% Serie
    443,138.8h 14.35% Magazin
    394,359.3h 12.77% Dokumentation
    278,472.4h 9.02%  Spielfilm
    258,179.8h 8.36%  Show
    236,590.0h 7.66%  Werbung
    227,744.4h 7.38%  Sport
    170,164.9h 5.51%  Nachrichten
    68,627.2h  2.22%  Musik
    59,903.4h  1.94%  Reportage
    35,772.0h  1.16%  Verschiedenes
    19,641.2h  0.64%  Wetter
    11,167.4h  0.36%  Programmende
    9,515.0h   0.31%  E-Sport
    8,796.8h   0.28%  Bericht
    7,936.9h   0.26%  Event
    7,018.3h   0.23%  Kurzfilm
    6,518.9h   0.21%  Videoclip
    3,541.9h   0.11%  *unknown*
    2,045.6h   0.07%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
