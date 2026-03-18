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

**198** channels, **4,329,331*** programs, **2,961,010.3** hours playtime between **2023-01-17** and **2026-03-18**


### playtime per genre (top 30)

    797,066.4h 26.92% Serie
    428,211.1h 14.46% Magazin
    376,378.6h 12.71% Dokumentation
    264,404.4h 8.93%  Spielfilm
    248,795.1h 8.40%  Show
    229,224.9h 7.74%  Werbung
    214,651.7h 7.25%  Sport
    164,805.4h 5.57%  Nachrichten
    66,225.0h  2.24%  Musik
    57,436.4h  1.94%  Reportage
    34,562.4h  1.17%  Verschiedenes
    19,042.9h  0.64%  Wetter
    11,167.4h  0.38%  Programmende
    9,515.0h   0.32%  E-Sport
    8,565.4h   0.29%  Bericht
    7,702.3h   0.26%  Event
    6,981.8h   0.24%  Kurzfilm
    6,205.7h   0.21%  Videoclip
    3,541.9h   0.12%  *unknown*
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
