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

**197** channels, **3,590,482*** programs, **2,428,163.8** hours playtime between **2023-01-17** and **2025-11-12**


### playtime per genre (top 30)

    647,027.2h 26.65% Serie
    365,652.3h 15.06% Magazin
    303,137.1h 12.48% Dokumentation
    209,062.6h 8.61%  Show
    201,027.1h 8.28%  Spielfilm
    198,231.2h 8.16%  Werbung
    160,534.1h 6.61%  Sport
    144,010.9h 5.93%  Nachrichten
    53,066.7h  2.19%  Musik
    47,905.5h  1.97%  Reportage
    26,837.5h  1.11%  Verschiedenes
    16,585.8h  0.68%  Wetter
    11,167.4h  0.46%  Programmende
    9,515.0h   0.39%  E-Sport
    7,630.1h   0.31%  Bericht
    6,668.7h   0.27%  Event
    5,248.5h   0.22%  Kurzfilm
    4,798.0h   0.20%  Videoclip
    3,541.9h   0.15%  *unknown*
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
