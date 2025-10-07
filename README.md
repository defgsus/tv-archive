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

**197** channels, **3,375,131*** programs, **2,271,929.3** hours playtime between **2023-01-17** and **2025-10-07**


### playtime per genre (top 30)

    603,067.6h 26.54% Serie
    346,753.5h 15.26% Magazin
    282,510.3h 12.43% Dokumentation
    197,366.0h 8.69%  Show
    188,780.0h 8.31%  Werbung
    183,679.9h 8.08%  Spielfilm
    145,323.2h 6.40%  Sport
    137,843.8h 6.07%  Nachrichten
    47,807.4h  2.10%  Musik
    45,207.5h  1.99%  Reportage
    24,303.6h  1.07%  Verschiedenes
    15,886.5h  0.70%  Wetter
    11,167.4h  0.49%  Programmende
    9,515.0h   0.42%  E-Sport
    7,315.3h   0.32%  Bericht
    6,410.3h   0.28%  Event
    4,575.1h   0.20%  Kurzfilm
    4,368.4h   0.19%  Videoclip
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
