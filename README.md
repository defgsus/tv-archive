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

**197** channels, **3,275,310*** programs, **2,198,783.3** hours playtime between **2023-01-17** and **2025-09-20**


### playtime per genre (top 30)

    582,914.2h 26.51% Serie
    338,227.2h 15.38% Magazin
    272,243.2h 12.38% Dokumentation
    191,724.8h 8.72%  Show
    184,727.7h 8.40%  Werbung
    175,344.0h 7.97%  Spielfilm
    138,221.5h 6.29%  Sport
    135,130.6h 6.15%  Nachrichten
    45,424.9h  2.07%  Musik
    43,948.5h  2.00%  Reportage
    22,921.4h  1.04%  Verschiedenes
    15,557.8h  0.71%  Wetter
    11,167.4h  0.51%  Programmende
    9,515.0h   0.43%  E-Sport
    6,924.8h   0.31%  Bericht
    6,281.3h   0.29%  Event
    4,283.1h   0.19%  Kurzfilm
    4,177.4h   0.19%  Videoclip
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
