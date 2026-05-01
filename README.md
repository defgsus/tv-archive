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

**198** channels, **4,581,954*** programs, **3,140,897.5** hours playtime between **2023-01-17** and **2026-05-01**


### playtime per genre (top 30)

    849,979.0h 27.06% Serie
    449,263.0h 14.30% Magazin
    401,961.0h 12.80% Dokumentation
    283,896.5h 9.04%  Spielfilm
    262,179.8h 8.35%  Show
    239,700.0h 7.63%  Werbung
    233,249.1h 7.43%  Sport
    172,640.0h 5.50%  Nachrichten
    69,634.8h  2.22%  Musik
    60,787.1h  1.94%  Reportage
    36,348.8h  1.16%  Verschiedenes
    19,890.2h  0.63%  Wetter
    11,167.4h  0.36%  Programmende
    9,515.0h   0.30%  E-Sport
    8,883.0h   0.28%  Bericht
    8,045.9h   0.26%  Event
    7,034.2h   0.22%  Kurzfilm
    6,654.2h   0.21%  Videoclip
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
