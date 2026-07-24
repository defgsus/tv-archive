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

**203** channels, **5,058,624** programs, **3,482,544** hours playtime between **2023-01-17** and **2026-07-24**


### playtime per genre (top 30)

    950,166.3h 27.28% Serie
    487,968.8h 14.01% Magazin
    451,275.9h 12.96% Dokumentation
    320,056.0h 9.19%  Spielfilm
    287,360.1h 8.25%  Show
    270,283.6h 7.76%  Sport
    258,624.9h 7.43%  Werbung
    188,550.5h 5.41%  Nachrichten
    76,110.7h  2.19%  Musik
    66,837.8h  1.92%  Reportage
    40,131.6h  1.15%  Verschiedenes
    21,398.8h  0.61%  Wetter
    11,167.4h  0.32%  Programmende
    9,638.5h   0.28%  Bericht
    9,515.0h   0.27%  E-Sport
    8,704.3h   0.25%  Event
    7,512.2h   0.22%  Videoclip
    7,173.4h   0.21%  Kurzfilm
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
