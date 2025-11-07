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

**197** channels, **3,560,900*** programs, **2,406,528.3** hours playtime between **2023-01-17** and **2025-11-07**


### playtime per genre (top 30)

    641,252.2h 26.65% Serie
    363,171.9h 15.09% Magazin
    300,158.8h 12.47% Dokumentation
    207,445.9h 8.62%  Show
    198,367.1h 8.24%  Spielfilm
    196,918.2h 8.18%  Werbung
    158,324.9h 6.58%  Sport
    143,186.1h 5.95%  Nachrichten
    52,320.4h  2.17%  Musik
    47,544.2h  1.98%  Reportage
    26,488.6h  1.10%  Verschiedenes
    16,496.2h  0.69%  Wetter
    11,167.4h  0.46%  Programmende
    9,515.0h   0.40%  E-Sport
    7,600.1h   0.32%  Bericht
    6,622.4h   0.28%  Event
    5,151.4h   0.21%  Kurzfilm
    4,739.9h   0.20%  Videoclip
    3,541.9h   0.15%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
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
