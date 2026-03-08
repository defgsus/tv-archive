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

**198** channels, **4,272,364*** programs, **2,920,218.7** hours playtime between **2023-01-17** and **2026-03-08**


### playtime per genre (top 30)

    784,938.8h 26.88% Serie
    423,205.6h 14.49% Magazin
    370,706.7h 12.69% Dokumentation
    260,208.4h 8.91%  Spielfilm
    245,685.7h 8.41%  Show
    226,766.9h 7.77%  Werbung
    210,509.4h 7.21%  Sport
    163,125.4h 5.59%  Nachrichten
    65,468.2h  2.24%  Musik
    56,649.8h  1.94%  Reportage
    34,182.8h  1.17%  Verschiedenes
    18,862.8h  0.65%  Wetter
    11,167.4h  0.38%  Programmende
    9,515.0h   0.33%  E-Sport
    8,458.9h   0.29%  Bericht
    7,621.1h   0.26%  Event
    6,972.0h   0.24%  Kurzfilm
    6,105.5h   0.21%  Videoclip
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
