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

**195** channels, **2,303,775*** programs, **1,499,601.7** hours playtime between **2023-01-17** and **2025-04-11**


### playtime per genre (top 30)

    385,411.6h 25.70% Serie
    257,189.0h 17.15% Magazin
    179,136.8h 11.95% Dokumentation
    142,535.1h 9.50%  Werbung
    139,350.7h 9.29%  Show
    109,000.5h 7.27%  Nachrichten
    97,052.7h  6.47%  Spielfilm
    68,384.0h  4.56%  Sport
    31,478.3h  2.10%  Reportage
    22,287.8h  1.49%  Musik
    12,430.1h  0.83%  Wetter
    11,167.4h  0.74%  Programmende
    10,048.4h  0.67%  Verschiedenes
    9,515.0h   0.63%  E-Sport
    5,891.1h   0.39%  Bericht
    5,047.7h   0.34%  Event
    3,541.9h   0.24%  *unknown*
    2,372.7h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    1,255.4h   0.08%  Kurzfilm
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
