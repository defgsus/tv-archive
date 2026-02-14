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

**198** channels, **4,146,023*** programs, **2,829,913.0** hours playtime between **2023-01-17** and **2026-02-14**


### playtime per genre (top 30)

    758,476.6h 26.80% Serie
    412,235.1h 14.57% Magazin
    358,040.6h 12.65% Dokumentation
    250,811.8h 8.86%  Spielfilm
    238,632.0h 8.43%  Show
    221,443.2h 7.83%  Werbung
    200,961.3h 7.10%  Sport
    159,533.4h 5.64%  Nachrichten
    63,785.2h  2.25%  Musik
    54,894.2h  1.94%  Reportage
    33,346.0h  1.18%  Verschiedenes
    18,474.1h  0.65%  Wetter
    11,167.4h  0.39%  Programmende
    9,515.0h   0.34%  E-Sport
    8,275.6h   0.29%  Bericht
    7,423.0h   0.26%  Event
    6,950.2h   0.25%  Kurzfilm
    5,880.0h   0.21%  Videoclip
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
