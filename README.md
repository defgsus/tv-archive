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

**203** channels, **4,973,202** programs, **3,421,809** hours playtime between **2023-01-17** and **2026-07-09**


### playtime per genre (top 30)

    932,056.1h 27.24% Serie
    481,261.6h 14.06% Magazin
    442,367.2h 12.93% Dokumentation
    313,984.4h 9.18%  Spielfilm
    282,851.7h 8.27%  Show
    263,695.5h 7.71%  Sport
    255,281.5h 7.46%  Werbung
    185,663.2h 5.43%  Nachrichten
    74,927.4h  2.19%  Musik
    65,712.2h  1.92%  Reportage
    39,554.2h  1.16%  Verschiedenes
    21,125.2h  0.62%  Wetter
    11,167.4h  0.33%  Programmende
    9,515.0h   0.28%  E-Sport
    9,475.8h   0.28%  Bericht
    8,591.3h   0.25%  Event
    7,352.6h   0.21%  Videoclip
    7,158.7h   0.21%  Kurzfilm
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
