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

**197** channels, **3,661,480*** programs, **2,479,725.5** hours playtime between **2023-01-17** and **2025-11-24**


### playtime per genre (top 30)

    661,065.6h 26.66% Serie
    371,837.9h 15.00% Magazin
    310,040.0h 12.50% Dokumentation
    212,943.3h 8.59%  Show
    207,087.2h 8.35%  Spielfilm
    201,365.2h 8.12%  Werbung
    165,648.1h 6.68%  Sport
    146,043.5h 5.89%  Nachrichten
    54,870.5h  2.21%  Musik
    48,719.1h  1.96%  Reportage
    27,630.5h  1.11%  Verschiedenes
    16,816.5h  0.68%  Wetter
    11,167.4h  0.45%  Programmende
    9,515.0h   0.38%  E-Sport
    7,742.6h   0.31%  Bericht
    6,762.1h   0.27%  Event
    5,471.8h   0.22%  Kurzfilm
    4,937.8h   0.20%  Videoclip
    3,541.9h   0.14%  *unknown*
    2,045.6h   0.08%  Verkaufsshow
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
