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

**195** channels, **2,279,408*** programs, **1,482,465.5** hours playtime between **2023-01-17** and **2025-04-07**


### playtime per genre (top 30)

    380,352.4h 25.66% Serie
    255,082.5h 17.21% Magazin
    176,915.2h 11.93% Dokumentation
    141,451.7h 9.54%  Werbung
    138,055.4h 9.31%  Show
    108,253.5h 7.30%  Nachrichten
    95,504.8h  6.44%  Spielfilm
    66,749.6h  4.50%  Sport
    31,160.4h  2.10%  Reportage
    21,714.3h  1.46%  Musik
    12,353.6h  0.83%  Wetter
    11,167.4h  0.75%  Programmende
    9,747.4h   0.66%  Verschiedenes
    9,515.0h   0.64%  E-Sport
    5,844.9h   0.39%  Bericht
    5,032.7h   0.34%  Event
    3,541.9h   0.24%  *unknown*
    2,334.1h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    1,183.1h   0.08%  Kurzfilm
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
