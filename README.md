# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

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
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**198** channels, **4,162,643*** programs, **2,842,295.6** hours playtime between **2023-01-17** and **2026-02-17**


### playtime per genre (top 30)

    761,853.4h 26.80% Serie
    413,602.9h 14.55% Magazin
    359,825.7h 12.66% Dokumentation
    252,239.3h 8.87%  Spielfilm
    239,745.8h 8.43%  Show
    222,174.6h 7.82%  Werbung
    202,393.3h 7.12%  Sport
    159,972.2h 5.63%  Nachrichten
    64,013.0h  2.25%  Musik
    55,118.6h  1.94%  Reportage
    33,441.5h  1.18%  Verschiedenes
    18,522.9h  0.65%  Wetter
    11,167.4h  0.39%  Programmende
    9,515.0h   0.33%  E-Sport
    8,304.0h   0.29%  Bericht
    7,474.9h   0.26%  Event
    6,951.1h   0.24%  Kurzfilm
    5,911.8h   0.21%  Videoclip
    3,541.9h   0.12%  *unknown*
    2,045.6h   0.07%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
