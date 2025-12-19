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

**197** channels, **3,811,310*** programs, **2,587,660.1** hours playtime between **2023-01-17** and **2025-12-19**


### playtime per genre (top 30)

    691,555.7h 26.73% Serie
    385,091.5h 14.88% Magazin
    324,230.3h 12.53% Dokumentation
    220,732.5h 8.53%  Show
    219,120.5h 8.47%  Spielfilm
    207,555.6h 8.02%  Werbung
    176,185.2h 6.81%  Sport
    150,330.5h 5.81%  Nachrichten
    58,591.0h  2.26%  Musik
    50,660.5h  1.96%  Reportage
    29,398.5h  1.14%  Verschiedenes
    17,334.2h  0.67%  Wetter
    11,167.4h  0.43%  Programmende
    9,515.0h   0.37%  E-Sport
    8,011.6h   0.31%  Bericht
    6,938.0h   0.27%  Event
    5,947.5h   0.23%  Kurzfilm
    5,228.2h   0.20%  Videoclip
    3,541.9h   0.14%  *unknown*
    2,045.6h   0.08%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
