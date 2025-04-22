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

**196** channels, **2,367,939*** programs, **1,546,861.1** hours playtime between **2023-01-17** and **2025-04-22**


### playtime per genre (top 30)

    398,153.3h 25.74% Serie
    262,417.3h 16.96% Magazin
    185,497.9h 11.99% Dokumentation
    145,420.6h 9.40%  Werbung
    142,850.4h 9.23%  Show
    110,656.9h 7.15%  Nachrichten
    103,387.8h 6.68%  Spielfilm
    73,047.7h  4.72%  Sport
    32,315.2h  2.09%  Reportage
    23,873.3h  1.54%  Musik
    12,623.0h  0.82%  Wetter
    11,167.4h  0.72%  Programmende
    10,850.7h  0.70%  Verschiedenes
    9,515.0h   0.62%  E-Sport
    5,916.0h   0.38%  Bericht
    5,154.5h   0.33%  Event
    3,541.9h   0.23%  *unknown*
    2,481.5h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,485.3h   0.10%  Kurzfilm
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
