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

**203** channels, **5,397,184** programs, **3,724,499** hours playtime between **2023-01-17** and **2026-09-22**


### playtime per genre (top 30)

    1,021,543.8h 27.43% Serie
    516,405.5h   13.87% Magazin
    486,763.4h   13.07% Dokumentation
    344,966.0h   9.26%  Spielfilm
    305,937.5h   8.21%  Show
    295,140.2h   7.92%  Sport
    271,579.2h   7.29%  Werbung
    199,648.7h   5.36%  Nachrichten
    80,617.2h    2.16%  Musik
    71,473.3h    1.92%  Reportage
    42,378.8h    1.14%  Verschiedenes
    22,575.7h    0.61%  Wetter
    11,167.4h    0.30%  Programmende
    10,096.8h    0.27%  Bericht
    9,515.0h     0.26%  E-Sport
    9,214.4h     0.25%  Event
    8,131.6h     0.22%  Videoclip
    7,276.2h     0.20%  Kurzfilm
    3,541.9h     0.10%  *unknown*
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
