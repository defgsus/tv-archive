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

**195** channels, **2,237,611*** programs, **1,452,555.8** hours playtime between **2023-01-17** and **2025-03-31**


### playtime per genre (top 30)

    371,988.1h 25.61% Serie
    251,535.2h 17.32% Magazin
    172,896.5h 11.90% Dokumentation
    139,555.8h 9.61%  Werbung
    135,703.7h 9.34%  Show
    107,074.6h 7.37%  Nachrichten
    92,320.0h  6.36%  Spielfilm
    63,822.3h  4.39%  Sport
    30,645.5h  2.11%  Reportage
    20,731.0h  1.43%  Musik
    12,225.6h  0.84%  Wetter
    11,167.4h  0.77%  Programmende
    9,515.0h   0.66%  E-Sport
    9,239.1h   0.64%  Verschiedenes
    5,784.9h   0.40%  Bericht
    4,982.4h   0.34%  Event
    3,541.9h   0.24%  *unknown*
    2,270.7h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    1,050.5h   0.07%  Kurzfilm
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
