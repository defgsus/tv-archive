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

**197** channels, **2,765,259*** programs, **1,832,803.2** hours playtime between **2023-01-17** and **2025-06-27**


### playtime per genre (top 30)

    478,898.1h 26.13% Serie
    295,495.7h 16.12% Magazin
    222,920.1h 12.16% Dokumentation
    164,769.7h 8.99%  Show
    162,982.3h 8.89%  Werbung
    135,041.2h 7.37%  Spielfilm
    121,245.9h 6.62%  Nachrichten
    101,970.8h 5.56%  Sport
    37,450.3h  2.04%  Reportage
    33,736.8h  1.84%  Musik
    15,739.0h  0.86%  Verschiedenes
    13,854.3h  0.76%  Wetter
    11,167.4h  0.61%  Programmende
    9,515.0h   0.52%  E-Sport
    6,462.2h   0.35%  Bericht
    5,658.2h   0.31%  Event
    3,541.9h   0.19%  *unknown*
    3,135.3h   0.17%  Videoclip
    2,712.7h   0.15%  Kurzfilm
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
