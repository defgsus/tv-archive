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

**198** channels, **4,168,398*** programs, **2,846,379.6** hours playtime between **2023-01-17** and **2026-02-18**


### playtime per genre (top 30)

    763,090.6h 26.81% Serie
    414,102.9h 14.55% Magazin
    360,383.9h 12.66% Dokumentation
    252,613.0h 8.87%  Spielfilm
    240,088.2h 8.43%  Show
    222,414.1h 7.81%  Werbung
    202,843.1h 7.13%  Sport
    160,143.1h 5.63%  Nachrichten
    64,077.0h  2.25%  Musik
    55,190.8h  1.94%  Reportage
    33,473.5h  1.18%  Verschiedenes
    18,540.4h  0.65%  Wetter
    11,167.4h  0.39%  Programmende
    9,515.0h   0.33%  E-Sport
    8,311.2h   0.29%  Bericht
    7,482.3h   0.26%  Event
    6,952.2h   0.24%  Kurzfilm
    5,922.5h   0.21%  Videoclip
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
