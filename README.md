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

**197** channels, **4,027,072*** programs, **2,745,447.6** hours playtime between **2023-01-17** and **2026-01-25**


### playtime per genre (top 30)

    734,382.0h 26.75% Serie
    402,258.4h 14.65% Magazin
    346,277.8h 12.61% Dokumentation
    241,375.1h 8.79%  Spielfilm
    232,201.6h 8.46%  Show
    216,509.8h 7.89%  Werbung
    192,069.1h 7.00%  Sport
    156,122.8h 5.69%  Nachrichten
    62,251.2h  2.27%  Musik
    53,353.6h  1.94%  Reportage
    32,085.0h  1.17%  Verschiedenes
    18,084.5h  0.66%  Wetter
    11,167.4h  0.41%  Programmende
    9,515.0h   0.35%  E-Sport
    8,151.6h   0.30%  Bericht
    7,285.6h   0.27%  Event
    6,627.5h   0.24%  Kurzfilm
    5,661.4h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
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
