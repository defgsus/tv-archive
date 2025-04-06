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

**195** channels, **2,273,702*** programs, **1,478,173.6** hours playtime between **2023-01-17** and **2025-04-06**


### playtime per genre (top 30)

    379,318.3h 25.66% Serie
    254,578.1h 17.22% Magazin
    176,273.4h 11.93% Dokumentation
    141,182.1h 9.55%  Werbung
    137,712.9h 9.32%  Show
    108,133.4h 7.32%  Nachrichten
    94,935.8h  6.42%  Spielfilm
    66,299.2h  4.49%  Sport
    31,073.7h  2.10%  Reportage
    21,583.5h  1.46%  Musik
    12,339.8h  0.83%  Wetter
    11,167.4h  0.76%  Programmende
    9,676.4h   0.65%  Verschiedenes
    9,515.0h   0.64%  E-Sport
    5,838.1h   0.39%  Bericht
    5,010.2h   0.34%  Event
    3,541.9h   0.24%  *unknown*
    2,324.5h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    1,164.4h   0.08%  Kurzfilm
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
