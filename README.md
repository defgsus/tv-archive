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

**198** channels, **4,151,522*** programs, **2,834,052.9** hours playtime between **2023-01-17** and **2026-02-15**


### playtime per genre (top 30)

    759,568.3h 26.80% Serie
    412,639.1h 14.56% Magazin
    358,610.5h 12.65% Dokumentation
    251,342.4h 8.87%  Spielfilm
    239,019.2h 8.43%  Show
    221,700.0h 7.82%  Werbung
    201,472.4h 7.11%  Sport
    159,670.2h 5.63%  Nachrichten
    63,870.7h  2.25%  Musik
    54,986.2h  1.94%  Reportage
    33,376.8h  1.18%  Verschiedenes
    18,490.5h  0.65%  Wetter
    11,167.4h  0.39%  Programmende
    9,515.0h   0.34%  E-Sport
    8,286.2h   0.29%  Bericht
    7,427.9h   0.26%  Event
    6,950.9h   0.25%  Kurzfilm
    5,890.9h   0.21%  Videoclip
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
    147.0h     0.01%  Wirtschaftsmagazin
