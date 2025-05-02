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

**197** channels, **2,427,978*** programs, **1,590,037.3** hours playtime between **2023-01-17** and **2025-05-02**


### playtime per genre (top 30)

    410,350.0h 25.81% Serie
    267,500.2h 16.82% Magazin
    191,285.4h 12.03% Dokumentation
    148,088.8h 9.31%  Werbung
    146,087.1h 9.19%  Show
    112,355.2h 7.07%  Nachrichten
    108,076.1h 6.80%  Spielfilm
    77,293.4h  4.86%  Sport
    33,073.9h  2.08%  Reportage
    25,321.1h  1.59%  Musik
    12,812.0h  0.81%  Wetter
    11,592.4h  0.73%  Verschiedenes
    11,167.4h  0.70%  Programmende
    9,515.0h   0.60%  E-Sport
    5,983.9h   0.38%  Bericht
    5,252.1h   0.33%  Event
    3,541.9h   0.22%  *unknown*
    2,580.6h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,654.3h   0.10%  Kurzfilm
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
