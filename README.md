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

**197** channels, **2,464,158*** programs, **1,615,998.1** hours playtime between **2023-01-17** and **2025-05-08**


### playtime per genre (top 30)

    417,865.3h 25.86% Serie
    270,519.0h 16.74% Magazin
    194,588.0h 12.04% Dokumentation
    149,641.1h 9.26%  Werbung
    148,038.6h 9.16%  Show
    113,339.1h 7.01%  Nachrichten
    110,897.1h 6.86%  Spielfilm
    79,901.0h  4.94%  Sport
    33,562.9h  2.08%  Reportage
    26,229.7h  1.62%  Musik
    12,918.5h  0.80%  Wetter
    12,030.9h  0.74%  Verschiedenes
    11,167.4h  0.69%  Programmende
    9,515.0h   0.59%  E-Sport
    6,036.7h   0.37%  Bericht
    5,291.9h   0.33%  Event
    3,541.9h   0.22%  *unknown*
    2,639.1h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,768.7h   0.11%  Kurzfilm
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
