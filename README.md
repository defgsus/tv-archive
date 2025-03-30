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

**195** channels, **2,231,863*** programs, **1,448,216.6** hours playtime between **2023-01-17** and **2025-03-30**


### playtime per genre (top 30)

    370,947.1h 25.61% Serie
    251,049.2h 17.34% Magazin
    172,246.8h 11.89% Dokumentation
    139,293.1h 9.62%  Werbung
    135,339.5h 9.35%  Show
    106,952.3h 7.39%  Nachrichten
    91,759.6h  6.34%  Spielfilm
    63,327.6h  4.37%  Sport
    30,571.8h  2.11%  Reportage
    20,590.1h  1.42%  Musik
    12,208.7h  0.84%  Wetter
    11,167.4h  0.77%  Programmende
    9,515.0h   0.66%  E-Sport
    9,164.4h   0.63%  Verschiedenes
    5,778.9h   0.40%  Bericht
    4,967.4h   0.34%  Event
    3,541.9h   0.24%  *unknown*
    2,260.2h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    1,030.0h   0.07%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
