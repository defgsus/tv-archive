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

**195** channels, **2,081,911*** programs, **1,341,011.6** hours playtime between **2023-01-17** and **2025-03-05**


### playtime per genre (top 30)

    340,950.9h 25.42% Serie
    238,273.9h 17.77% Magazin
    158,432.2h 11.81% Dokumentation
    132,452.5h 9.88%  Werbung
    126,929.9h 9.47%  Show
    102,734.4h 7.66%  Nachrichten
    80,437.9h  6.00%  Spielfilm
    52,526.4h  3.92%  Sport
    28,761.9h  2.14%  Reportage
    16,805.1h  1.25%  Musik
    11,759.2h  0.88%  Wetter
    11,167.4h  0.83%  Programmende
    9,515.0h   0.71%  E-Sport
    7,244.7h   0.54%  Verschiedenes
    5,618.8h   0.42%  Bericht
    4,797.1h   0.36%  Event
    3,541.9h   0.26%  *unknown*
    2,045.6h   0.15%  Verkaufsshow
    2,017.6h   0.15%  Videoclip
    541.4h     0.04%  Kurzfilm
    353.9h     0.03%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.02%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
