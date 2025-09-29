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

**197** channels, **3,327,967*** programs, **2,237,490.4** hours playtime between **2023-01-17** and **2025-09-29**


### playtime per genre (top 30)

    593,573.3h 26.53% Serie
    342,665.7h 15.31% Magazin
    277,629.8h 12.41% Dokumentation
    194,785.4h 8.71%  Show
    186,846.2h 8.35%  Werbung
    179,755.0h 8.03%  Spielfilm
    142,114.0h 6.35%  Sport
    136,520.8h 6.10%  Nachrichten
    46,648.8h  2.08%  Musik
    44,616.4h  1.99%  Reportage
    23,637.6h  1.06%  Verschiedenes
    15,731.1h  0.70%  Wetter
    11,167.4h  0.50%  Programmende
    9,515.0h   0.43%  E-Sport
    7,153.6h   0.32%  Bericht
    6,363.5h   0.28%  Event
    4,436.8h   0.20%  Kurzfilm
    4,281.4h   0.19%  Videoclip
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
