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

**197** channels, **3,149,543*** programs, **2,108,160.5** hours playtime between **2023-01-17** and **2025-08-30**


### playtime per genre (top 30)

    557,495.6h 26.44% Serie
    327,437.5h 15.53% Magazin
    259,949.3h 12.33% Dokumentation
    184,767.2h 8.76%  Show
    179,342.1h 8.51%  Werbung
    165,525.1h 7.85%  Spielfilm
    131,626.8h 6.24%  Nachrichten
    129,277.9h 6.13%  Sport
    42,728.8h  2.03%  Musik
    42,408.6h  2.01%  Reportage
    20,967.0h  0.99%  Verschiedenes
    15,145.0h  0.72%  Wetter
    11,167.4h  0.53%  Programmende
    9,515.0h   0.45%  E-Sport
    6,799.3h   0.32%  Bericht
    6,117.7h   0.29%  Event
    3,926.1h   0.19%  Videoclip
    3,915.8h   0.19%  Kurzfilm
    3,541.9h   0.17%  *unknown*
    2,045.6h   0.10%  Verkaufsshow
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
