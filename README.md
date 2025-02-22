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

**195** channels, **2,016,467*** programs, **1,293,725.4** hours playtime between **2023-01-17** and **2025-02-22**


### playtime per genre (top 30)

    327,928.1h 25.35% Serie
    232,675.9h 17.98% Magazin
    152,217.0h 11.77% Dokumentation
    129,540.7h 10.01% Werbung
    122,902.8h 9.50%  Show
    100,866.4h 7.80%  Nachrichten
    75,349.6h  5.82%  Spielfilm
    47,889.9h  3.70%  Sport
    28,039.4h  2.17%  Reportage
    15,190.6h  1.17%  Musik
    11,568.4h  0.89%  Wetter
    11,167.4h  0.86%  Programmende
    9,515.0h   0.74%  E-Sport
    6,438.1h   0.50%  Verschiedenes
    5,468.9h   0.42%  Bericht
    4,653.7h   0.36%  Event
    3,541.9h   0.27%  *unknown*
    2,045.6h   0.16%  Verkaufsshow
    1,919.7h   0.15%  Videoclip
    353.9h     0.03%  Eishockey
    348.6h     0.03%  Kurzfilm
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.02%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
