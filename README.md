# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

[webapp on github.io](https://defgsus.github.io/tv-archive/)

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
  "description": null,
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**203** channels, **4,990,062** programs, **3,433,897** hours playtime between **2023-01-17** and **2026-07-12**


### playtime per genre (top 30)

    935,594.9h 27.25% Serie
    482,540.4h 14.05% Magazin
    444,093.2h 12.93% Dokumentation
    315,220.6h 9.18%  Spielfilm
    283,785.0h 8.26%  Show
    265,096.7h 7.72%  Sport
    255,936.7h 7.45%  Werbung
    186,230.0h 5.42%  Nachrichten
    75,163.9h  2.19%  Musik
    65,954.9h  1.92%  Reportage
    39,673.0h  1.16%  Verschiedenes
    21,175.3h  0.62%  Wetter
    11,167.4h  0.33%  Programmende
    9,523.4h   0.28%  Bericht
    9,515.0h   0.28%  E-Sport
    8,616.9h   0.25%  Event
    7,380.8h   0.21%  Videoclip
    7,161.6h   0.21%  Kurzfilm
    3,541.9h   0.10%  *unknown*
    2,045.6h   0.06%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.00%  Erotikfilm
    157.3h     0.00%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
