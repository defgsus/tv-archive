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

**197** channels, **3,452,837*** programs, **2,328,163.1** hours playtime between **2023-01-17** and **2025-10-20**


### playtime per genre (top 30)

    618,949.5h 26.59% Serie
    353,560.6h 15.19% Magazin
    289,882.9h 12.45% Dokumentation
    201,686.8h 8.66%  Show
    192,206.8h 8.26%  Werbung
    189,770.8h 8.15%  Spielfilm
    150,783.0h 6.48%  Sport
    140,061.9h 6.02%  Nachrichten
    49,750.8h  2.14%  Musik
    46,120.8h  1.98%  Reportage
    25,203.3h  1.08%  Verschiedenes
    16,148.1h  0.69%  Wetter
    11,167.4h  0.48%  Programmende
    9,515.0h   0.41%  E-Sport
    7,469.9h   0.32%  Bericht
    6,507.2h   0.28%  Event
    4,805.7h   0.21%  Kurzfilm
    4,522.2h   0.19%  Videoclip
    3,541.9h   0.15%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
