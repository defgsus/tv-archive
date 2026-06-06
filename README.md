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

**200** channels, **4,786,425*** programs, **3,287,525.4** hours playtime between **2023-01-17** and **2026-06-06**


### playtime per genre (top 30)

    892,708.1h 27.15% Serie
    465,867.8h 14.17% Magazin
    423,243.0h 12.87% Dokumentation
    300,227.2h 9.13%  Spielfilm
    272,958.9h 8.30%  Show
    248,535.6h 7.56%  Sport
    248,076.3h 7.55%  Werbung
    179,474.2h 5.46%  Nachrichten
    72,380.9h  2.20%  Musik
    63,343.7h  1.93%  Reportage
    37,787.0h  1.15%  Verschiedenes
    20,576.0h  0.63%  Wetter
    11,167.4h  0.34%  Programmende
    9,515.0h   0.29%  E-Sport
    9,117.5h   0.28%  Bericht
    8,338.0h   0.25%  Event
    7,124.7h   0.22%  Kurzfilm
    7,015.7h   0.21%  Videoclip
    3,541.9h   0.11%  *unknown*
    2,045.6h   0.06%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.00%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
