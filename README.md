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

**195** channels, **2,033,777*** programs, **1,306,597.8** hours playtime between **2023-01-17** and **2025-02-25**


### playtime per genre (top 30)

    331,334.8h 25.36% Serie
    234,135.2h 17.92% Magazin
    153,989.8h 11.79% Dokumentation
    130,320.9h 9.97%  Werbung
    123,984.4h 9.49%  Show
    101,342.4h 7.76%  Nachrichten
    76,863.7h  5.88%  Spielfilm
    49,202.9h  3.77%  Sport
    28,245.2h  2.16%  Reportage
    15,624.2h  1.20%  Musik
    11,616.1h  0.89%  Wetter
    11,167.4h  0.85%  Programmende
    9,515.0h   0.73%  E-Sport
    6,645.7h   0.51%  Verschiedenes
    5,524.5h   0.42%  Bericht
    4,687.9h   0.36%  Event
    3,541.9h   0.27%  *unknown*
    2,045.6h   0.16%  Verkaufsshow
    1,950.5h   0.15%  Videoclip
    401.8h     0.03%  Kurzfilm
    353.9h     0.03%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.02%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
