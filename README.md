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

**197** channels, **3,410,935*** programs, **2,297,886.4** hours playtime between **2023-01-17** and **2025-10-13**


### playtime per genre (top 30)

    610,324.6h 26.56% Serie
    349,882.3h 15.23% Magazin
    285,983.5h 12.45% Dokumentation
    199,375.9h 8.68%  Show
    190,366.0h 8.28%  Werbung
    186,538.3h 8.12%  Spielfilm
    147,790.6h 6.43%  Sport
    138,865.5h 6.04%  Nachrichten
    48,712.9h  2.12%  Musik
    45,616.1h  1.99%  Reportage
    24,736.8h  1.08%  Verschiedenes
    16,006.3h  0.70%  Wetter
    11,167.4h  0.49%  Programmende
    9,515.0h   0.41%  E-Sport
    7,381.2h   0.32%  Bericht
    6,454.6h   0.28%  Event
    4,680.6h   0.20%  Kurzfilm
    4,440.4h   0.19%  Videoclip
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
