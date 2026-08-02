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

**203** channels, **5,109,791** programs, **3,518,917** hours playtime between **2023-01-17** and **2026-08-02**


### playtime per genre (top 30)

    960,932.2h 27.31% Serie
    491,987.0h 13.98% Magazin
    456,664.8h 12.98% Dokumentation
    323,878.8h 9.20%  Spielfilm
    290,030.7h 8.24%  Show
    274,077.8h 7.79%  Sport
    260,645.6h 7.41%  Werbung
    190,228.9h 5.41%  Nachrichten
    76,813.6h  2.18%  Musik
    67,579.1h  1.92%  Reportage
    40,464.4h  1.15%  Verschiedenes
    21,577.8h  0.61%  Wetter
    11,167.4h  0.32%  Programmende
    9,701.7h   0.28%  Bericht
    9,515.0h   0.27%  E-Sport
    8,795.7h   0.25%  Event
    7,604.5h   0.22%  Videoclip
    7,183.5h   0.20%  Kurzfilm
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
