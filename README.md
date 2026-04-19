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

**198** channels, **4,512,831*** programs, **3,091,910.6** hours playtime between **2023-01-17** and **2026-04-19**


### playtime per genre (top 30)

    835,284.0h 27.02% Serie
    443,538.6h 14.35% Magazin
    394,960.5h 12.77% Dokumentation
    278,996.4h 9.02%  Spielfilm
    258,529.9h 8.36%  Show
    236,827.1h 7.66%  Werbung
    228,215.2h 7.38%  Sport
    170,327.1h 5.51%  Nachrichten
    68,710.9h  2.22%  Musik
    59,974.3h  1.94%  Reportage
    35,849.4h  1.16%  Verschiedenes
    19,659.5h  0.64%  Wetter
    11,167.4h  0.36%  Programmende
    9,515.0h   0.31%  E-Sport
    8,797.8h   0.28%  Bericht
    7,941.8h   0.26%  Event
    7,018.7h   0.23%  Kurzfilm
    6,528.6h   0.21%  Videoclip
    3,541.9h   0.11%  *unknown*
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
    147.0h     0.00%  Wirtschaftsmagazin
