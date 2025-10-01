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

**197** channels, **3,339,879*** programs, **2,246,024.7** hours playtime between **2023-01-17** and **2025-10-01**


### playtime per genre (top 30)

    596,055.8h 26.54% Serie
    343,733.0h 15.30% Magazin
    278,887.9h 12.42% Dokumentation
    195,376.7h 8.70%  Show
    187,306.3h 8.34%  Werbung
    180,601.3h 8.04%  Spielfilm
    142,889.1h 6.36%  Sport
    136,872.0h 6.09%  Nachrichten
    46,907.1h  2.09%  Musik
    44,746.8h  1.99%  Reportage
    23,805.4h  1.06%  Verschiedenes
    15,773.6h  0.70%  Wetter
    11,167.4h  0.50%  Programmende
    9,515.0h   0.42%  E-Sport
    7,199.6h   0.32%  Bericht
    6,374.4h   0.28%  Event
    4,467.7h   0.20%  Kurzfilm
    4,297.2h   0.19%  Videoclip
    3,541.9h   0.16%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
