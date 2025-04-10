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

**195** channels, **2,297,698*** programs, **1,495,329.3** hours playtime between **2023-01-17** and **2025-04-10**


### playtime per genre (top 30)

    384,156.0h 25.69% Serie
    256,662.4h 17.16% Magazin
    178,591.1h 11.94% Dokumentation
    142,265.3h 9.51%  Werbung
    139,023.1h 9.30%  Show
    108,810.9h 7.28%  Nachrichten
    96,681.3h  6.47%  Spielfilm
    67,960.0h  4.54%  Sport
    31,401.1h  2.10%  Reportage
    22,146.4h  1.48%  Musik
    12,411.0h  0.83%  Wetter
    11,167.4h  0.75%  Programmende
    9,974.7h   0.67%  Verschiedenes
    9,515.0h   0.64%  E-Sport
    5,877.9h   0.39%  Bericht
    5,039.3h   0.34%  Event
    3,541.9h   0.24%  *unknown*
    2,362.2h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    1,237.0h   0.08%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
