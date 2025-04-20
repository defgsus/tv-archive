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

**196** channels, **2,357,123*** programs, **1,538,349.8** hours playtime between **2023-01-17** and **2025-04-20**


### playtime per genre (top 30)

    396,120.5h 25.75% Serie
    261,597.2h 17.01% Magazin
    184,319.0h 11.98% Dokumentation
    144,948.5h 9.42%  Werbung
    142,268.8h 9.25%  Show
    110,402.3h 7.18%  Nachrichten
    101,795.3h 6.62%  Spielfilm
    72,203.2h  4.69%  Sport
    32,127.0h  2.09%  Reportage
    23,604.5h  1.53%  Musik
    12,590.6h  0.82%  Wetter
    11,167.4h  0.73%  Programmende
    10,707.3h  0.70%  Verschiedenes
    9,515.0h   0.62%  E-Sport
    5,911.6h   0.38%  Bericht
    5,124.9h   0.33%  Event
    3,541.9h   0.23%  *unknown*
    2,459.6h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,439.9h   0.09%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
