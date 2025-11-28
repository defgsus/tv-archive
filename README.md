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

**197** channels, **3,685,841*** programs, **2,497,052.7** hours playtime between **2023-01-17** and **2025-11-28**


### playtime per genre (top 30)

    666,039.0h 26.67% Serie
    374,082.6h 14.98% Magazin
    312,386.1h 12.51% Dokumentation
    214,182.3h 8.58%  Show
    208,809.3h 8.36%  Spielfilm
    202,415.8h 8.11%  Werbung
    167,226.4h 6.70%  Sport
    146,787.0h 5.88%  Nachrichten
    55,454.1h  2.22%  Musik
    49,038.6h  1.96%  Reportage
    27,897.7h  1.12%  Verschiedenes
    16,902.3h  0.68%  Wetter
    11,167.4h  0.45%  Programmende
    9,515.0h   0.38%  E-Sport
    7,778.2h   0.31%  Bericht
    6,776.4h   0.27%  Event
    5,545.2h   0.22%  Kurzfilm
    4,987.9h   0.20%  Videoclip
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
