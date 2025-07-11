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

**197** channels, **2,855,182*** programs, **1,897,367.2** hours playtime between **2023-01-17** and **2025-07-12**


### playtime per genre (top 30)

    497,257.7h 26.21% Serie
    303,211.2h 15.98% Magazin
    231,380.9h 12.19% Dokumentation
    169,595.9h 8.94%  Show
    166,855.8h 8.79%  Werbung
    142,092.7h 7.49%  Spielfilm
    123,606.9h 6.51%  Nachrichten
    108,464.5h 5.72%  Sport
    38,551.3h  2.03%  Reportage
    35,967.9h  1.90%  Musik
    16,829.6h  0.89%  Verschiedenes
    14,148.6h  0.75%  Wetter
    11,167.4h  0.59%  Programmende
    9,515.0h   0.50%  E-Sport
    6,637.5h   0.35%  Bericht
    5,755.0h   0.30%  Event
    3,541.9h   0.19%  *unknown*
    3,281.2h   0.17%  Videoclip
    2,999.7h   0.16%  Kurzfilm
    2,045.6h   0.11%  Verkaufsshow
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
