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

**197** channels, **2,626,395*** programs, **1,732,996.5** hours playtime between **2023-01-17** and **2025-06-04**


### playtime per genre (top 30)

    450,901.5h 26.02% Serie
    283,941.5h 16.38% Magazin
    209,881.4h 12.11% Dokumentation
    157,009.0h 9.06%  Show
    156,839.9h 9.05%  Werbung
    123,701.7h 7.14%  Spielfilm
    117,660.0h 6.79%  Nachrichten
    92,031.9h  5.31%  Sport
    35,612.6h  2.05%  Reportage
    30,263.9h  1.75%  Musik
    14,060.2h  0.81%  Verschiedenes
    13,405.2h  0.77%  Wetter
    11,167.4h  0.64%  Programmende
    9,515.0h   0.55%  E-Sport
    6,266.9h   0.36%  Bericht
    5,506.7h   0.32%  Event
    3,541.9h   0.20%  *unknown*
    2,905.6h   0.17%  Videoclip
    2,277.6h   0.13%  Kurzfilm
    2,045.6h   0.12%  Verkaufsshow
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
