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

**198** channels, **4,277,772*** programs, **2,924,354.6** hours playtime between **2023-01-17** and **2026-03-09**


### playtime per genre (top 30)

    786,039.0h 26.88% Serie
    423,648.9h 14.49% Magazin
    371,321.8h 12.70% Dokumentation
    260,781.2h 8.92%  Spielfilm
    245,994.5h 8.41%  Show
    227,001.3h 7.76%  Werbung
    210,979.5h 7.21%  Sport
    163,261.7h 5.58%  Nachrichten
    65,543.4h  2.24%  Musik
    56,722.5h  1.94%  Reportage
    34,220.4h  1.17%  Verschiedenes
    18,872.7h  0.65%  Wetter
    11,167.4h  0.38%  Programmende
    9,515.0h   0.33%  E-Sport
    8,491.9h   0.29%  Bericht
    7,637.2h   0.26%  Event
    6,972.0h   0.24%  Kurzfilm
    6,115.9h   0.21%  Videoclip
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
