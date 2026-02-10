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

**198** channels, **4,122,396*** programs, **2,813,212.1** hours playtime between **2023-01-17** and **2026-02-10**


### playtime per genre (top 30)

    753,597.0h 26.79% Serie
    410,175.9h 14.58% Magazin
    355,752.2h 12.65% Dokumentation
    249,158.2h 8.86%  Spielfilm
    237,353.1h 8.44%  Show
    220,446.4h 7.84%  Werbung
    199,132.3h 7.08%  Sport
    158,821.8h 5.65%  Nachrichten
    63,474.1h  2.26%  Musik
    54,597.6h  1.94%  Reportage
    33,153.7h  1.18%  Verschiedenes
    18,401.5h  0.65%  Wetter
    11,167.4h  0.40%  Programmende
    9,515.0h   0.34%  E-Sport
    8,242.8h   0.29%  Bericht
    7,399.4h   0.26%  Event
    6,917.3h   0.25%  Kurzfilm
    5,838.0h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
    2,045.6h   0.07%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
