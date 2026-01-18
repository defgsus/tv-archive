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

**197** channels, **3,985,410*** programs, **2,715,875.9** hours playtime between **2023-01-17** and **2026-01-18**


### playtime per genre (top 30)

    725,755.3h 26.72% Serie
    398,875.3h 14.69% Magazin
    342,218.0h 12.60% Dokumentation
    238,004.7h 8.76%  Spielfilm
    230,075.0h 8.47%  Show
    214,779.8h 7.91%  Werbung
    188,908.2h 6.96%  Sport
    154,955.6h 5.71%  Nachrichten
    61,722.3h  2.27%  Musik
    52,834.3h  1.95%  Reportage
    31,598.2h  1.16%  Verschiedenes
    17,942.8h  0.66%  Wetter
    11,167.4h  0.41%  Programmende
    9,515.0h   0.35%  E-Sport
    8,112.4h   0.30%  Bericht
    7,238.9h   0.27%  Event
    6,519.4h   0.24%  Kurzfilm
    5,584.9h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
    2,045.6h   0.08%  Verkaufsshow
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
