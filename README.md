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

**197** channels, **3,494,975*** programs, **2,358,994.1** hours playtime between **2023-01-17** and **2025-10-27**


### playtime per genre (top 30)

    627,816.6h 26.61% Serie
    357,345.8h 15.15% Magazin
    293,895.8h 12.46% Dokumentation
    203,936.7h 8.65%  Show
    194,044.8h 8.23%  Werbung
    193,086.3h 8.19%  Spielfilm
    153,819.5h 6.52%  Sport
    141,260.5h 5.99%  Nachrichten
    50,787.6h  2.15%  Musik
    46,678.1h  1.98%  Reportage
    25,677.2h  1.09%  Verschiedenes
    16,276.0h  0.69%  Wetter
    11,167.4h  0.47%  Programmende
    9,515.0h   0.40%  E-Sport
    7,528.2h   0.32%  Bericht
    6,555.3h   0.28%  Event
    4,943.2h   0.21%  Kurzfilm
    4,607.0h   0.20%  Videoclip
    3,541.9h   0.15%  *unknown*
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
