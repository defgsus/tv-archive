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

**197** channels, **3,578,370*** programs, **2,419,525.1** hours playtime between **2023-01-17** and **2025-11-10**


### playtime per genre (top 30)

    644,562.7h 26.64% Serie
    364,584.7h 15.07% Magazin
    301,963.9h 12.48% Dokumentation
    208,469.7h 8.62%  Show
    200,113.0h 8.27%  Spielfilm
    197,709.8h 8.17%  Werbung
    159,719.0h 6.60%  Sport
    143,641.6h 5.94%  Nachrichten
    52,776.7h  2.18%  Musik
    47,739.5h  1.97%  Reportage
    26,705.7h  1.10%  Verschiedenes
    16,543.2h  0.68%  Wetter
    11,167.4h  0.46%  Programmende
    9,515.0h   0.39%  E-Sport
    7,614.6h   0.31%  Bericht
    6,655.5h   0.28%  Event
    5,211.4h   0.22%  Kurzfilm
    4,774.3h   0.20%  Videoclip
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
