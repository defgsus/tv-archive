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

**203** channels, **4,978,818** programs, **3,425,820** hours playtime between **2023-01-17** and **2026-07-10**


### playtime per genre (top 30)

    933,277.2h 27.24% Serie
    481,722.5h 14.06% Magazin
    442,914.0h 12.93% Dokumentation
    314,353.7h 9.18%  Spielfilm
    283,136.5h 8.26%  Show
    264,144.2h 7.71%  Sport
    255,497.6h 7.46%  Werbung
    185,859.5h 5.43%  Nachrichten
    75,003.5h  2.19%  Musik
    65,798.1h  1.92%  Reportage
    39,595.1h  1.16%  Verschiedenes
    21,143.2h  0.62%  Wetter
    11,167.4h  0.33%  Programmende
    9,515.0h   0.28%  E-Sport
    9,500.1h   0.28%  Bericht
    8,600.9h   0.25%  Event
    7,363.9h   0.21%  Videoclip
    7,159.2h   0.21%  Kurzfilm
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
