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

**197** channels, **3,251,035*** programs, **2,181,522.1** hours playtime between **2023-01-17** and **2025-09-16**


### playtime per genre (top 30)

    577,866.9h 26.49% Serie
    336,005.2h 15.40% Magazin
    269,988.9h 12.38% Dokumentation
    190,446.5h 8.73%  Show
    183,751.2h 8.42%  Werbung
    173,645.0h 7.96%  Spielfilm
    136,580.4h 6.26%  Sport
    134,402.5h 6.16%  Nachrichten
    44,902.4h  2.06%  Musik
    43,673.2h  2.00%  Reportage
    22,566.8h  1.03%  Verschiedenes
    15,476.1h  0.71%  Wetter
    11,167.4h  0.51%  Programmende
    9,515.0h   0.44%  E-Sport
    6,883.6h   0.32%  Bericht
    6,255.9h   0.29%  Event
    4,215.2h   0.19%  Kurzfilm
    4,131.4h   0.19%  Videoclip
    3,541.9h   0.16%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
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
