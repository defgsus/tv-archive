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

**203** channels, **5,018,614** programs, **3,454,201** hours playtime between **2023-01-17** and **2026-07-17**


### playtime per genre (top 30)

    941,746.9h 27.26% Serie
    484,807.2h 14.04% Magazin
    447,084.8h 12.94% Dokumentation
    317,195.0h 9.18%  Spielfilm
    285,232.2h 8.26%  Show
    267,305.5h 7.74%  Sport
    257,052.4h 7.44%  Werbung
    187,188.4h 5.42%  Nachrichten
    75,561.2h  2.19%  Musik
    66,308.0h  1.92%  Reportage
    39,863.5h  1.15%  Verschiedenes
    21,265.3h  0.62%  Wetter
    11,167.4h  0.32%  Programmende
    9,583.2h   0.28%  Bericht
    9,515.0h   0.28%  E-Sport
    8,652.8h   0.25%  Event
    7,437.0h   0.22%  Videoclip
    7,167.6h   0.21%  Kurzfilm
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
