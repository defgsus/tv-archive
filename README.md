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

**197** channels, **2,548,088*** programs, **1,676,604.6** hours playtime between **2023-01-17** and **2025-05-22**


### playtime per genre (top 30)

    435,040.7h 25.95% Serie
    277,517.3h 16.55% Magazin
    202,339.1h 12.07% Dokumentation
    153,435.8h 9.15%  Werbung
    152,745.9h 9.11%  Show
    117,375.0h 7.00%  Spielfilm
    115,627.0h 6.90%  Nachrichten
    86,150.0h  5.14%  Sport
    34,664.8h  2.07%  Reportage
    28,342.0h  1.69%  Musik
    13,156.6h  0.78%  Wetter
    13,087.6h  0.78%  Verschiedenes
    11,167.4h  0.67%  Programmende
    9,515.0h   0.57%  E-Sport
    6,181.2h   0.37%  Bericht
    5,403.1h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,776.5h   0.17%  Videoclip
    2,045.6h   0.12%  Verkaufsshow
    2,031.2h   0.12%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
