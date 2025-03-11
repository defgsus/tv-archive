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

**195** channels, **2,117,763*** programs, **1,366,763.1** hours playtime between **2023-01-17** and **2025-03-11**


### playtime per genre (top 30)

    348,049.8h 25.47% Serie
    241,349.4h 17.66% Magazin
    161,806.9h 11.84% Dokumentation
    134,088.0h 9.81%  Werbung
    128,905.2h 9.43%  Show
    103,743.7h 7.59%  Nachrichten
    83,240.7h  6.09%  Spielfilm
    55,144.9h  4.03%  Sport
    29,200.7h  2.14%  Reportage
    17,721.2h  1.30%  Musik
    11,866.2h  0.87%  Wetter
    11,167.4h  0.82%  Programmende
    9,515.0h   0.70%  E-Sport
    7,701.6h   0.56%  Verschiedenes
    5,652.9h   0.41%  Bericht
    4,842.6h   0.35%  Event
    3,541.9h   0.26%  *unknown*
    2,074.8h   0.15%  Videoclip
    2,045.6h   0.15%  Verkaufsshow
    647.0h     0.05%  Kurzfilm
    353.9h     0.03%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.02%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
