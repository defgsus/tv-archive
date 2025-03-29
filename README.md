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

**195** channels, **2,226,274*** programs, **1,443,879.1** hours playtime between **2023-01-17** and **2025-03-29**


### playtime per genre (top 30)

    369,791.0h 25.61% Serie
    250,634.4h 17.36% Magazin
    171,684.8h 11.89% Dokumentation
    139,014.1h 9.63%  Werbung
    134,957.5h 9.35%  Show
    106,827.0h 7.40%  Nachrichten
    91,190.5h  6.32%  Spielfilm
    62,837.8h  4.35%  Sport
    30,506.8h  2.11%  Reportage
    20,429.4h  1.41%  Musik
    12,192.1h  0.84%  Wetter
    11,167.4h  0.77%  Programmende
    9,515.0h   0.66%  E-Sport
    9,088.8h   0.63%  Verschiedenes
    5,777.3h   0.40%  Bericht
    4,958.0h   0.34%  Event
    3,541.9h   0.25%  *unknown*
    2,252.4h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    1,009.3h   0.07%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
