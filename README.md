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

**197** channels, **3,227,455*** programs, **2,164,273.0** hours playtime between **2023-01-17** and **2025-09-12**


### playtime per genre (top 30)

    573,168.2h 26.48% Serie
    334,060.7h 15.44% Magazin
    267,616.9h 12.37% Dokumentation
    189,092.7h 8.74%  Show
    182,763.7h 8.44%  Werbung
    171,630.1h 7.93%  Spielfilm
    134,705.9h 6.22%  Sport
    133,785.3h 6.18%  Nachrichten
    44,378.0h  2.05%  Musik
    43,363.0h  2.00%  Reportage
    22,254.0h  1.03%  Verschiedenes
    15,405.5h  0.71%  Wetter
    11,167.4h  0.52%  Programmende
    9,515.0h   0.44%  E-Sport
    6,863.9h   0.32%  Bericht
    6,224.7h   0.29%  Event
    4,144.0h   0.19%  Kurzfilm
    4,085.5h   0.19%  Videoclip
    3,541.9h   0.16%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
