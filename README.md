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

**196** channels, **2,386,332*** programs, **1,559,798.0** hours playtime between **2023-01-17** and **2025-04-25**


### playtime per genre (top 30)

    401,938.8h 25.77% Serie
    263,997.1h 16.93% Magazin
    187,262.0h 12.01% Dokumentation
    146,220.1h 9.37%  Werbung
    143,807.1h 9.22%  Show
    111,214.4h 7.13%  Nachrichten
    104,579.9h 6.70%  Spielfilm
    74,281.8h  4.76%  Sport
    32,545.1h  2.09%  Reportage
    24,318.0h  1.56%  Musik
    12,681.7h  0.81%  Wetter
    11,167.4h  0.72%  Programmende
    11,074.1h  0.71%  Verschiedenes
    9,515.0h   0.61%  E-Sport
    5,938.5h   0.38%  Bericht
    5,162.6h   0.33%  Event
    3,541.9h   0.23%  *unknown*
    2,510.7h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,536.5h   0.10%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
