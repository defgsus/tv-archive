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

**196** channels, **2,374,109*** programs, **1,551,175.8** hours playtime between **2023-01-17** and **2025-04-23**


### playtime per genre (top 30)

    399,421.3h 25.75% Serie
    262,938.8h 16.95% Magazin
    186,111.7h 12.00% Dokumentation
    145,682.5h 9.39%  Werbung
    143,168.2h 9.23%  Show
    110,841.5h 7.15%  Nachrichten
    103,789.6h 6.69%  Spielfilm
    73,440.0h  4.73%  Sport
    32,392.8h  2.09%  Reportage
    24,023.0h  1.55%  Musik
    12,642.8h  0.82%  Wetter
    11,167.4h  0.72%  Programmende
    10,923.0h  0.70%  Verschiedenes
    9,515.0h   0.61%  E-Sport
    5,918.5h   0.38%  Bericht
    5,156.8h   0.33%  Event
    3,541.9h   0.23%  *unknown*
    2,491.4h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,504.0h   0.10%  Kurzfilm
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
