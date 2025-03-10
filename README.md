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

**195** channels, **2,111,605*** programs, **1,362,451.7** hours playtime between **2023-01-17** and **2025-03-10**


### playtime per genre (top 30)

    346,781.3h 25.45% Serie
    240,815.4h 17.68% Magazin
    161,257.9h 11.84% Dokumentation
    133,819.5h 9.82%  Werbung
    128,595.8h 9.44%  Show
    103,556.9h 7.60%  Nachrichten
    82,815.1h  6.08%  Spielfilm
    54,748.8h  4.02%  Sport
    29,109.1h  2.14%  Reportage
    17,573.4h  1.29%  Musik
    11,847.0h  0.87%  Wetter
    11,167.4h  0.82%  Programmende
    9,515.0h   0.70%  E-Sport
    7,624.1h   0.56%  Verschiedenes
    5,648.9h   0.41%  Bericht
    4,835.9h   0.35%  Event
    3,541.9h   0.26%  *unknown*
    2,064.4h   0.15%  Videoclip
    2,045.6h   0.15%  Verkaufsshow
    630.5h     0.05%  Kurzfilm
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
