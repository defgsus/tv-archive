# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

[webapp on github.io](https://defgsus.github.io/tv-archive/)

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
  "description": null,
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**203** channels, **4,894,083** programs, **3,365,083** hours playtime between **2023-01-17** and **2026-06-25**


### playtime per genre (top 30)

    915,255.8h 27.20% Serie
    474,828.8h 14.11% Magazin
    434,235.5h 12.90% Dokumentation
    308,230.8h 9.16%  Spielfilm
    278,722.5h 8.28%  Show
    257,237.1h 7.64%  Sport
    252,238.0h 7.50%  Werbung
    183,028.0h 5.44%  Nachrichten
    73,850.9h  2.19%  Musik
    64,737.2h  1.92%  Reportage
    38,923.6h  1.16%  Verschiedenes
    20,913.7h  0.62%  Wetter
    11,167.4h  0.33%  Programmende
    9,515.0h   0.28%  E-Sport
    9,292.1h   0.28%  Bericht
    8,480.8h   0.25%  Event
    7,209.3h   0.21%  Videoclip
    7,148.2h   0.21%  Kurzfilm
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
