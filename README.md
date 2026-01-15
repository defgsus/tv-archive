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

**197** channels, **3,967,616*** programs, **2,703,300.8** hours playtime between **2023-01-17** and **2026-01-15**


### playtime per genre (top 30)

    722,110.9h 26.71% Serie
    397,439.6h 14.70% Magazin
    340,541.7h 12.60% Dokumentation
    236,533.6h 8.75%  Spielfilm
    229,096.5h 8.47%  Show
    214,037.0h 7.92%  Werbung
    187,601.6h 6.94%  Sport
    154,462.0h 5.71%  Nachrichten
    61,487.9h  2.27%  Musik
    52,600.9h  1.95%  Reportage
    31,403.4h  1.16%  Verschiedenes
    17,884.4h  0.66%  Wetter
    11,167.4h  0.41%  Programmende
    9,515.0h   0.35%  E-Sport
    8,095.9h   0.30%  Bericht
    7,225.4h   0.27%  Event
    6,473.6h   0.24%  Kurzfilm
    5,555.9h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
    2,045.6h   0.08%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
