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

**210** channels, **5,555,214** programs, **3,838,780** hours playtime between **2023-01-17** and **2026-10-20**


### playtime per genre (top 30)

    1,054,828.7h 27.48% Serie
    530,576.7h   13.82% Magazin
    503,085.0h   13.11% Dokumentation
    356,838.2h   9.30%  Spielfilm
    315,012.5h   8.21%  Show
    307,054.2h   8.00%  Sport
    277,627.1h   7.23%  Werbung
    204,784.5h   5.33%  Nachrichten
    82,705.8h    2.15%  Musik
    73,437.5h    1.91%  Reportage
    43,447.7h    1.13%  Verschiedenes
    23,086.1h    0.60%  Wetter
    11,167.4h    0.29%  Programmende
    10,358.0h    0.27%  Bericht
    9,515.0h     0.25%  E-Sport
    9,432.2h     0.25%  Event
    8,428.2h     0.22%  Videoclip
    7,327.4h     0.19%  Kurzfilm
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
