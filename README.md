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

**210** channels, **5,606,738** programs, **3,876,692** hours playtime between **2023-01-17** and **2026-10-29**


### playtime per genre (top 30)

    1,066,138.5h 27.50% Serie
    535,169.9h   13.80% Magazin
    508,444.7h   13.12% Dokumentation
    360,661.3h   9.30%  Spielfilm
    317,928.7h   8.20%  Show
    311,149.0h   8.03%  Sport
    279,706.5h   7.22%  Werbung
    206,404.2h   5.32%  Nachrichten
    83,389.9h    2.15%  Musik
    74,124.9h    1.91%  Reportage
    43,787.4h    1.13%  Verschiedenes
    23,250.9h    0.60%  Wetter
    11,167.4h    0.29%  Programmende
    10,423.8h    0.27%  Bericht
    9,515.0h     0.25%  E-Sport
    9,490.0h     0.24%  Event
    8,527.0h     0.22%  Videoclip
    7,345.0h     0.19%  Kurzfilm
    3,541.9h     0.09%  *unknown*
    2,045.6h     0.05%  Verkaufsshow
    353.9h       0.01%  Eishockey
    299.8h       0.01%  Judo
    257.0h       0.01%  Darts
    232.8h       0.01%  Handball
    219.5h       0.01%  Dokureihe
    212.4h       0.01%  Leichtathletik
    190.7h       0.00%  Gespräch
    169.7h       0.00%  Erotikfilm
    157.3h       0.00%  Fußball
    147.0h       0.00%  Wirtschaftsmagazin
