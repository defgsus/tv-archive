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

**203** channels, **5,279,745** programs, **3,640,113** hours playtime between **2023-01-17** and **2026-09-01**


### playtime per genre (top 30)

    996,647.1h 27.38% Serie
    506,249.2h 13.91% Magazin
    474,616.5h 13.04% Dokumentation
    336,371.3h 9.24%  Spielfilm
    299,315.9h 8.22%  Show
    286,230.3h 7.86%  Sport
    267,249.1h 7.34%  Werbung
    195,808.7h 5.38%  Nachrichten
    79,143.3h  2.17%  Musik
    69,895.9h  1.92%  Reportage
    41,582.2h  1.14%  Verschiedenes
    22,187.8h  0.61%  Wetter
    11,167.4h  0.31%  Programmende
    9,856.8h   0.27%  Bericht
    9,515.0h   0.26%  E-Sport
    9,047.6h   0.25%  Event
    7,919.2h   0.22%  Videoclip
    7,241.9h   0.20%  Kurzfilm
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
