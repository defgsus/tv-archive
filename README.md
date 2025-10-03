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

**197** channels, **3,351,816*** programs, **2,254,580.6** hours playtime between **2023-01-17** and **2025-10-03**


### playtime per genre (top 30)

    598,541.6h 26.55% Serie
    344,823.2h 15.29% Magazin
    280,043.7h 12.42% Dokumentation
    195,995.5h 8.69%  Show
    187,756.9h 8.33%  Werbung
    181,434.9h 8.05%  Spielfilm
    143,672.1h 6.37%  Sport
    137,232.1h 6.09%  Nachrichten
    47,207.6h  2.09%  Musik
    44,893.8h  1.99%  Reportage
    23,979.2h  1.06%  Verschiedenes
    15,816.8h  0.70%  Wetter
    11,167.4h  0.50%  Programmende
    9,515.0h   0.42%  E-Sport
    7,243.7h   0.32%  Bericht
    6,380.4h   0.28%  Event
    4,507.1h   0.20%  Kurzfilm
    4,321.3h   0.19%  Videoclip
    3,541.9h   0.16%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
