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

**198** channels, **4,656,561*** programs, **3,194,039.0** hours playtime between **2023-01-17** and **2026-05-14**


### playtime per genre (top 30)

    865,612.4h 27.10% Serie
    455,467.0h 14.26% Magazin
    409,585.8h 12.82% Dokumentation
    289,571.8h 9.07%  Spielfilm
    266,140.9h 8.33%  Show
    242,827.2h 7.60%  Werbung
    238,703.5h 7.47%  Sport
    175,070.9h 5.48%  Nachrichten
    70,612.0h  2.21%  Musik
    61,734.7h  1.93%  Reportage
    36,853.8h  1.15%  Verschiedenes
    20,140.1h  0.63%  Wetter
    11,167.4h  0.35%  Programmende
    9,515.0h   0.30%  E-Sport
    8,960.5h   0.28%  Bericht
    8,156.0h   0.26%  Event
    7,068.3h   0.22%  Kurzfilm
    6,783.2h   0.21%  Videoclip
    3,541.9h   0.11%  *unknown*
    2,045.6h   0.06%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.00%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
