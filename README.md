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

**195** channels, **2,136,282*** programs, **1,379,643.7** hours playtime between **2023-01-17** and **2025-03-14**


### playtime per genre (top 30)

    351,837.7h 25.50% Serie
    242,932.2h 17.61% Magazin
    163,408.8h 11.84% Dokumentation
    134,907.5h 9.78%  Werbung
    129,933.4h 9.42%  Show
    104,305.4h 7.56%  Nachrichten
    84,439.4h  6.12%  Spielfilm
    56,388.6h  4.09%  Sport
    29,398.2h  2.13%  Reportage
    18,166.5h  1.32%  Musik
    11,921.2h  0.86%  Wetter
    11,167.4h  0.81%  Programmende
    9,515.0h   0.69%  E-Sport
    7,926.1h   0.57%  Verschiedenes
    5,687.2h   0.41%  Bericht
    4,856.3h   0.35%  Event
    3,541.9h   0.26%  *unknown*
    2,104.1h   0.15%  Videoclip
    2,045.6h   0.15%  Verkaufsshow
    703.3h     0.05%  Kurzfilm
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
