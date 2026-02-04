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

**198** channels, **4,086,782*** programs, **2,787,784.3** hours playtime between **2023-01-17** and **2026-02-04**


### playtime per genre (top 30)

    746,468.2h 26.78% Serie
    407,160.7h 14.61% Magazin
    352,221.3h 12.63% Dokumentation
    246,200.8h 8.83%  Spielfilm
    235,413.1h 8.44%  Show
    218,960.8h 7.85%  Werbung
    196,440.1h 7.05%  Sport
    157,816.8h 5.66%  Nachrichten
    63,015.6h  2.26%  Musik
    54,131.5h  1.94%  Reportage
    32,775.8h  1.18%  Verschiedenes
    18,285.1h  0.66%  Wetter
    11,167.4h  0.40%  Programmende
    9,515.0h   0.34%  E-Sport
    8,212.1h   0.29%  Bericht
    7,350.9h   0.26%  Event
    6,807.7h   0.24%  Kurzfilm
    5,773.4h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
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
    147.0h     0.01%  Wirtschaftsmagazin
