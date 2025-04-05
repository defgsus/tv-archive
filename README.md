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

**195** channels, **2,267,947*** programs, **1,473,893.2** hours playtime between **2023-01-17** and **2025-04-05**


### playtime per genre (top 30)

    378,168.1h 25.66% Serie
    254,133.9h 17.24% Magazin
    175,715.3h 11.92% Dokumentation
    140,906.6h 9.56%  Werbung
    137,345.1h 9.32%  Show
    108,010.6h 7.33%  Nachrichten
    94,362.1h  6.40%  Spielfilm
    65,850.6h  4.47%  Sport
    31,009.0h  2.10%  Reportage
    21,432.3h  1.45%  Musik
    12,322.3h  0.84%  Wetter
    11,167.4h  0.76%  Programmende
    9,605.2h   0.65%  Verschiedenes
    9,515.0h   0.65%  E-Sport
    5,836.6h   0.40%  Bericht
    5,006.9h   0.34%  Event
    3,541.9h   0.24%  *unknown*
    2,315.5h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    1,143.4h   0.08%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
