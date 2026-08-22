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

**203** channels, **5,223,205** programs, **3,599,610** hours playtime between **2023-01-17** and **2026-08-22**


### playtime per genre (top 30)

    984,984.0h 27.36% Serie
    501,493.0h 13.93% Magazin
    468,565.5h 13.02% Dokumentation
    332,039.9h 9.22%  Spielfilm
    296,050.4h 8.22%  Show
    282,142.1h 7.84%  Sport
    265,072.7h 7.36%  Werbung
    193,985.6h 5.39%  Nachrichten
    78,371.5h  2.18%  Musik
    69,150.3h  1.92%  Reportage
    41,208.0h  1.14%  Verschiedenes
    21,989.8h  0.61%  Wetter
    11,167.4h  0.31%  Programmende
    9,814.9h   0.27%  Bericht
    9,515.0h   0.26%  E-Sport
    8,963.0h   0.25%  Event
    7,816.9h   0.22%  Videoclip
    7,211.8h   0.20%  Kurzfilm
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
