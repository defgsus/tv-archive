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

**197** channels, **2,734,983*** programs, **1,811,129.2** hours playtime between **2023-01-17** and **2025-06-22**


### playtime per genre (top 30)

    472,669.9h 26.10% Serie
    292,866.4h 16.17% Magazin
    220,065.9h 12.15% Dokumentation
    163,093.5h 9.01%  Show
    161,643.0h 8.92%  Werbung
    132,834.1h 7.33%  Spielfilm
    120,416.7h 6.65%  Nachrichten
    99,871.3h  5.51%  Sport
    37,068.2h  2.05%  Reportage
    33,000.5h  1.82%  Musik
    15,381.6h  0.85%  Verschiedenes
    13,752.7h  0.76%  Wetter
    11,167.4h  0.62%  Programmende
    9,515.0h   0.53%  E-Sport
    6,408.0h   0.35%  Bericht
    5,626.5h   0.31%  Event
    3,541.9h   0.20%  *unknown*
    3,085.7h   0.17%  Videoclip
    2,614.6h   0.14%  Kurzfilm
    2,045.6h   0.11%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
