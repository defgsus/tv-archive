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

**197** channels, **2,926,969*** programs, **1,949,197.2** hours playtime between **2023-01-17** and **2025-07-24**


### playtime per genre (top 30)

    511,915.1h 26.26% Serie
    309,174.2h 15.86% Magazin
    238,335.7h 12.23% Dokumentation
    173,385.7h 8.90%  Show
    169,915.2h 8.72%  Werbung
    147,882.9h 7.59%  Spielfilm
    125,551.4h 6.44%  Nachrichten
    113,795.3h 5.84%  Sport
    39,453.6h  2.02%  Reportage
    37,742.5h  1.94%  Musik
    17,743.2h  0.91%  Verschiedenes
    14,376.5h  0.74%  Wetter
    11,167.4h  0.57%  Programmende
    9,515.0h   0.49%  E-Sport
    6,689.9h   0.34%  Bericht
    5,841.8h   0.30%  Event
    3,541.9h   0.18%  *unknown*
    3,438.0h   0.18%  Videoclip
    3,225.6h   0.17%  Kurzfilm
    2,045.6h   0.10%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
