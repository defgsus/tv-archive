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

**197** channels, **3,602,582*** programs, **2,436,752.6** hours playtime between **2023-01-17** and **2025-11-14**


### playtime per genre (top 30)

    649,525.2h 26.66% Serie
    366,736.2h 15.05% Magazin
    304,247.0h 12.49% Dokumentation
    209,696.2h 8.61%  Show
    201,889.9h 8.29%  Spielfilm
    198,761.2h 8.16%  Werbung
    161,334.1h 6.62%  Sport
    144,388.4h 5.93%  Nachrichten
    53,354.7h  2.19%  Musik
    48,027.4h  1.97%  Reportage
    26,971.0h  1.11%  Verschiedenes
    16,628.4h  0.68%  Wetter
    11,167.4h  0.46%  Programmende
    9,515.0h   0.39%  E-Sport
    7,668.6h   0.31%  Bericht
    6,677.0h   0.27%  Event
    5,284.1h   0.22%  Kurzfilm
    4,822.6h   0.20%  Videoclip
    3,541.9h   0.15%  *unknown*
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
