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

**197** channels, **3,721,659*** programs, **2,523,059.1** hours playtime between **2023-01-17** and **2025-12-04**


### playtime per genre (top 30)

    673,238.0h 26.68% Serie
    377,193.6h 14.95% Magazin
    315,837.0h 12.52% Dokumentation
    216,040.1h 8.56%  Show
    211,824.4h 8.40%  Spielfilm
    203,973.6h 8.08%  Werbung
    169,826.6h 6.73%  Sport
    147,800.2h 5.86%  Nachrichten
    56,362.1h  2.23%  Musik
    49,494.5h  1.96%  Reportage
    28,315.5h  1.12%  Verschiedenes
    17,022.1h  0.67%  Wetter
    11,167.4h  0.44%  Programmende
    9,515.0h   0.38%  E-Sport
    7,827.9h   0.31%  Bericht
    6,835.2h   0.27%  Event
    5,666.4h   0.22%  Kurzfilm
    5,056.2h   0.20%  Videoclip
    3,541.9h   0.14%  *unknown*
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
