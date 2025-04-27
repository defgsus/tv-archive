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

**197** channels, **2,398,176*** programs, **1,568,416.6** hours playtime between **2023-01-17** and **2025-04-27**


### playtime per genre (top 30)

    404,340.0h 25.78% Serie
    264,985.5h 16.90% Magazin
    188,407.5h 12.01% Dokumentation
    146,767.7h 9.36%  Werbung
    144,485.3h 9.21%  Show
    111,529.0h 7.11%  Nachrichten
    105,572.3h 6.73%  Spielfilm
    75,134.3h  4.79%  Sport
    32,655.8h  2.08%  Reportage
    24,614.7h  1.57%  Musik
    12,716.0h  0.81%  Wetter
    11,223.6h  0.72%  Verschiedenes
    11,167.4h  0.71%  Programmende
    9,515.0h   0.61%  E-Sport
    5,959.1h   0.38%  Bericht
    5,197.5h   0.33%  Event
    3,541.9h   0.23%  *unknown*
    2,529.4h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,568.9h   0.10%  Kurzfilm
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
