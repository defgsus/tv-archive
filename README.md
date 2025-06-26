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

**197** channels, **2,759,131*** programs, **1,828,459.6** hours playtime between **2023-01-17** and **2025-06-26**


### playtime per genre (top 30)

    477,612.3h 26.12% Serie
    294,944.2h 16.13% Magazin
    222,365.1h 12.16% Dokumentation
    164,416.7h 8.99%  Show
    162,716.8h 8.90%  Werbung
    134,661.1h 7.36%  Spielfilm
    121,061.2h 6.62%  Nachrichten
    101,569.1h 5.55%  Sport
    37,377.2h  2.04%  Reportage
    33,584.7h  1.84%  Musik
    15,668.4h  0.86%  Verschiedenes
    13,833.0h  0.76%  Wetter
    11,167.4h  0.61%  Programmende
    9,515.0h   0.52%  E-Sport
    6,443.7h   0.35%  Bericht
    5,654.8h   0.31%  Event
    3,541.9h   0.19%  *unknown*
    3,125.7h   0.17%  Videoclip
    2,694.8h   0.15%  Kurzfilm
    2,045.6h   0.11%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
