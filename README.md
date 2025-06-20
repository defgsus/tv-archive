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

**197** channels, **2,723,031*** programs, **1,802,486.6** hours playtime between **2023-01-17** and **2025-06-20**


### playtime per genre (top 30)

    470,302.0h 26.09% Serie
    291,936.7h 16.20% Magazin
    218,911.6h 12.14% Dokumentation
    162,398.4h 9.01%  Show
    161,104.6h 8.94%  Werbung
    131,789.4h 7.31%  Spielfilm
    120,131.7h 6.66%  Nachrichten
    98,968.1h  5.49%  Sport
    36,922.3h  2.05%  Reportage
    32,664.3h  1.81%  Musik
    15,238.6h  0.85%  Verschiedenes
    13,718.5h  0.76%  Wetter
    11,167.4h  0.62%  Programmende
    9,515.0h   0.53%  E-Sport
    6,404.1h   0.36%  Bericht
    5,619.0h   0.31%  Event
    3,541.9h   0.20%  *unknown*
    3,066.8h   0.17%  Videoclip
    2,579.8h   0.14%  Kurzfilm
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
