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

**198** channels, **4,180,101*** programs, **2,854,644.4** hours playtime between **2023-01-17** and **2026-02-20**


### playtime per genre (top 30)

    765,595.3h 26.82% Serie
    415,205.4h 14.54% Magazin
    361,501.3h 12.66% Dokumentation
    253,365.8h 8.88%  Spielfilm
    240,669.5h 8.43%  Show
    222,903.4h 7.81%  Werbung
    203,734.7h 7.14%  Sport
    160,511.0h 5.62%  Nachrichten
    64,224.1h  2.25%  Musik
    55,346.1h  1.94%  Reportage
    33,535.1h  1.17%  Verschiedenes
    18,577.1h  0.65%  Wetter
    11,167.4h  0.39%  Programmende
    9,515.0h   0.33%  E-Sport
    8,325.3h   0.29%  Bericht
    7,498.0h   0.26%  Event
    6,956.7h   0.24%  Kurzfilm
    5,944.8h   0.21%  Videoclip
    3,541.9h   0.12%  *unknown*
    2,045.6h   0.07%  Verkaufsshow
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
