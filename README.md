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

**203** channels, **5,132,467** programs, **3,535,033** hours playtime between **2023-01-17** and **2026-08-06**


### playtime per genre (top 30)

    965,807.6h 27.32% Serie
    493,924.1h 13.97% Magazin
    459,026.5h 12.99% Dokumentation
    325,497.7h 9.21%  Spielfilm
    291,202.9h 8.24%  Show
    275,623.9h 7.80%  Sport
    261,512.2h 7.40%  Werbung
    190,971.8h 5.40%  Nachrichten
    77,129.8h  2.18%  Musik
    67,920.7h  1.92%  Reportage
    40,598.7h  1.15%  Verschiedenes
    21,658.5h  0.61%  Wetter
    11,167.4h  0.32%  Programmende
    9,743.5h   0.28%  Bericht
    9,515.0h   0.27%  E-Sport
    8,826.8h   0.25%  Event
    7,650.5h   0.22%  Videoclip
    7,187.4h   0.20%  Kurzfilm
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
