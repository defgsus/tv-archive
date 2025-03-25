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

**195** channels, **2,201,944*** programs, **1,426,806.5** hours playtime between **2023-01-17** and **2025-03-25**


### playtime per genre (top 30)

    364,926.0h 25.58% Serie
    248,558.0h 17.42% Magazin
    169,486.1h 11.88% Dokumentation
    137,921.0h 9.67%  Werbung
    133,641.8h 9.37%  Show
    106,099.9h 7.44%  Nachrichten
    89,577.8h  6.28%  Spielfilm
    61,147.9h  4.29%  Sport
    30,209.0h  2.12%  Reportage
    19,816.2h  1.39%  Musik
    12,117.8h  0.85%  Wetter
    11,167.4h  0.78%  Programmende
    9,515.0h   0.67%  E-Sport
    8,771.9h   0.61%  Verschiedenes
    5,731.4h   0.40%  Bericht
    4,934.8h   0.35%  Event
    3,541.9h   0.25%  *unknown*
    2,212.3h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    926.9h     0.06%  Kurzfilm
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
