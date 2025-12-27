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

**197** channels, **3,856,996*** programs, **2,622,320.9** hours playtime between **2023-01-17** and **2025-12-27**


### playtime per genre (top 30)

    700,028.4h 26.69% Serie
    388,560.5h 14.82% Magazin
    329,051.1h 12.55% Dokumentation
    225,130.4h 8.59%  Spielfilm
    223,151.7h 8.51%  Show
    209,498.6h 7.99%  Werbung
    179,598.0h 6.85%  Sport
    151,490.5h 5.78%  Nachrichten
    59,749.6h  2.28%  Musik
    51,249.6h  1.95%  Reportage
    30,044.7h  1.15%  Verschiedenes
    17,492.1h  0.67%  Wetter
    11,167.4h  0.43%  Programmende
    9,515.0h   0.36%  E-Sport
    8,029.5h   0.31%  Bericht
    7,035.3h   0.27%  Event
    6,122.8h   0.23%  Kurzfilm
    5,339.3h   0.20%  Videoclip
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
