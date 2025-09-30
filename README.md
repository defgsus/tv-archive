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

**197** channels, **3,333,949*** programs, **2,241,751.6** hours playtime between **2023-01-17** and **2025-09-30**


### playtime per genre (top 30)

    594,819.8h 26.53% Serie
    343,192.2h 15.31% Magazin
    278,257.2h 12.41% Dokumentation
    195,081.1h 8.70%  Show
    187,077.7h 8.35%  Werbung
    180,167.1h 8.04%  Spielfilm
    142,501.5h 6.36%  Sport
    136,696.4h 6.10%  Nachrichten
    46,776.4h  2.09%  Musik
    44,693.5h  1.99%  Reportage
    23,719.7h  1.06%  Verschiedenes
    15,752.4h  0.70%  Wetter
    11,167.4h  0.50%  Programmende
    9,515.0h   0.42%  E-Sport
    7,174.5h   0.32%  Bericht
    6,370.7h   0.28%  Event
    4,450.9h   0.20%  Kurzfilm
    4,289.6h   0.19%  Videoclip
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
