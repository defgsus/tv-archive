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

**197** channels, **2,512,147*** programs, **1,650,640.0** hours playtime between **2023-01-17** and **2025-05-16**


### playtime per genre (top 30)

    427,656.4h 25.91% Serie
    274,574.3h 16.63% Magazin
    199,080.0h 12.06% Dokumentation
    151,806.3h 9.20%  Werbung
    150,749.8h 9.13%  Show
    114,661.4h 6.95%  Nachrichten
    114,551.0h 6.94%  Spielfilm
    83,429.0h  5.05%  Sport
    34,165.9h  2.07%  Reportage
    27,417.4h  1.66%  Musik
    13,061.8h  0.79%  Wetter
    12,639.3h  0.77%  Verschiedenes
    11,167.4h  0.68%  Programmende
    9,515.0h   0.58%  E-Sport
    6,129.5h   0.37%  Bericht
    5,359.4h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,716.8h   0.16%  Videoclip
    2,045.6h   0.12%  Verkaufsshow
    1,910.9h   0.12%  Kurzfilm
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
