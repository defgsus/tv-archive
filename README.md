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

**197** channels, **2,499,929*** programs, **1,641,974.0** hours playtime between **2023-01-17** and **2025-05-14**


### playtime per genre (top 30)

    425,136.2h 25.89% Serie
    273,511.5h 16.66% Magazin
    197,975.6h 12.06% Dokumentation
    151,269.6h 9.21%  Werbung
    150,063.2h 9.14%  Show
    114,299.1h 6.96%  Nachrichten
    113,763.3h 6.93%  Spielfilm
    82,565.9h  5.03%  Sport
    34,007.8h  2.07%  Reportage
    27,132.2h  1.65%  Musik
    13,024.0h  0.79%  Wetter
    12,485.8h  0.76%  Verschiedenes
    11,167.4h  0.68%  Programmende
    9,515.0h   0.58%  E-Sport
    6,081.4h   0.37%  Bericht
    5,351.6h   0.33%  Event
    3,541.9h   0.22%  *unknown*
    2,697.6h   0.16%  Videoclip
    2,045.6h   0.12%  Verkaufsshow
    1,878.3h   0.11%  Kurzfilm
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
