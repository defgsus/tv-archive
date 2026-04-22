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

**198** channels, **4,529,965*** programs, **3,104,120.0** hours playtime between **2023-01-17** and **2026-04-22**


### playtime per genre (top 30)

    838,887.2h 27.02% Serie
    444,957.0h 14.33% Magazin
    396,737.0h 12.78% Dokumentation
    280,253.9h 9.03%  Spielfilm
    259,405.7h 8.36%  Show
    237,551.4h 7.65%  Werbung
    229,465.2h 7.39%  Sport
    170,880.7h 5.50%  Nachrichten
    68,944.0h  2.22%  Musik
    60,214.8h  1.94%  Reportage
    35,981.8h  1.16%  Verschiedenes
    19,713.5h  0.64%  Wetter
    11,167.4h  0.36%  Programmende
    9,515.0h   0.31%  E-Sport
    8,814.3h   0.28%  Bericht
    7,979.1h   0.26%  Event
    7,022.8h   0.23%  Kurzfilm
    6,560.5h   0.21%  Videoclip
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
