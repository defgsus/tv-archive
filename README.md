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

**197** channels, **2,506,149*** programs, **1,646,339.2** hours playtime between **2023-01-17** and **2025-05-15**


### playtime per genre (top 30)

    426,432.4h 25.90% Serie
    274,056.9h 16.65% Magazin
    198,524.2h 12.06% Dokumentation
    151,540.3h 9.20%  Werbung
    150,379.2h 9.13%  Show
    114,479.4h 6.95%  Nachrichten
    114,175.7h 6.94%  Spielfilm
    82,986.2h  5.04%  Sport
    34,087.4h  2.07%  Reportage
    27,274.7h  1.66%  Musik
    13,043.7h  0.79%  Wetter
    12,562.6h  0.76%  Verschiedenes
    11,167.4h  0.68%  Programmende
    9,515.0h   0.58%  E-Sport
    6,108.3h   0.37%  Bericht
    5,356.1h   0.33%  Event
    3,541.9h   0.22%  *unknown*
    2,707.1h   0.16%  Videoclip
    2,045.6h   0.12%  Verkaufsshow
    1,894.2h   0.12%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
