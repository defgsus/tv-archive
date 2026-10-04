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

**203** channels, **5,464,524** programs, **3,773,030** hours playtime between **2023-01-17** and **2026-10-04**


### playtime per genre (top 30)

    1,035,957.8h 27.46% Serie
    522,487.7h   13.85% Magazin
    493,703.5h   13.09% Dokumentation
    349,912.0h   9.27%  Spielfilm
    309,697.0h   8.21%  Show
    300,057.2h   7.95%  Sport
    274,037.5h   7.26%  Werbung
    201,905.9h   5.35%  Nachrichten
    81,507.6h    2.16%  Musik
    72,297.2h    1.92%  Reportage
    42,846.9h    1.14%  Verschiedenes
    22,797.9h    0.60%  Wetter
    11,167.4h    0.30%  Programmende
    10,198.0h    0.27%  Bericht
    9,515.0h     0.25%  E-Sport
    9,311.4h     0.25%  Event
    8,257.6h     0.22%  Videoclip
    7,304.5h     0.19%  Kurzfilm
    3,541.9h     0.09%  *unknown*
    2,045.6h     0.05%  Verkaufsshow
    353.9h       0.01%  Eishockey
    299.8h       0.01%  Judo
    257.0h       0.01%  Darts
    232.8h       0.01%  Handball
    219.5h       0.01%  Dokureihe
    212.4h       0.01%  Leichtathletik
    190.7h       0.01%  Gespräch
    169.7h       0.00%  Erotikfilm
    157.3h       0.00%  Fußball
    147.0h       0.00%  Wirtschaftsmagazin
