# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

[webapp on github.io](https://defgsus.github.io/tv-archive/)

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
  "description": null,
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**210** channels, **5,651,850** programs, **3,909,857** hours playtime between **2023-01-17** and **2026-11-09**


### playtime per genre (top 30)

    1,075,135.4h 27.50% Serie
    539,107.3h   13.79% Magazin
    513,180.7h   13.13% Dokumentation
    364,778.6h   9.33%  Spielfilm
    320,601.7h   8.20%  Show
    314,856.0h   8.05%  Sport
    281,539.5h   7.20%  Werbung
    207,773.5h   5.31%  Nachrichten
    83,955.5h    2.15%  Musik
    74,712.9h    1.91%  Reportage
    44,078.0h    1.13%  Verschiedenes
    23,379.5h    0.60%  Wetter
    11,167.4h    0.29%  Programmende
    10,465.3h    0.27%  Bericht
    9,562.1h     0.24%  Event
    9,515.0h     0.24%  E-Sport
    8,608.1h     0.22%  Videoclip
    7,372.5h     0.19%  Kurzfilm
    3,541.9h     0.09%  *unknown*
    2,045.6h     0.05%  Verkaufsshow
    353.9h       0.01%  Eishockey
    299.8h       0.01%  Judo
    257.0h       0.01%  Darts
    232.8h       0.01%  Handball
    219.5h       0.01%  Dokureihe
    212.4h       0.01%  Leichtathletik
    190.7h       0.00%  Gespräch
    169.7h       0.00%  Erotikfilm
    157.3h       0.00%  Fußball
    147.0h       0.00%  Wirtschaftsmagazin
