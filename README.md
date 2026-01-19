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

**197** channels, **3,990,979*** programs, **2,720,072.5** hours playtime between **2023-01-17** and **2026-01-19**


### playtime per genre (top 30)

    726,814.9h 26.72% Serie
    399,317.8h 14.68% Magazin
    342,859.3h 12.60% Dokumentation
    238,599.1h 8.77%  Spielfilm
    230,393.2h 8.47%  Show
    215,018.6h 7.90%  Werbung
    189,389.8h 6.96%  Sport
    155,088.6h 5.70%  Nachrichten
    61,799.4h  2.27%  Musik
    52,897.7h  1.94%  Reportage
    31,682.7h  1.16%  Verschiedenes
    17,959.4h  0.66%  Wetter
    11,167.4h  0.41%  Programmende
    9,515.0h   0.35%  E-Sport
    8,113.4h   0.30%  Bericht
    7,254.2h   0.27%  Event
    6,537.9h   0.24%  Kurzfilm
    5,595.6h   0.21%  Videoclip
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
