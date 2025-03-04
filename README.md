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

**195** channels, **2,075,802*** programs, **1,336,743.0** hours playtime between **2023-01-17** and **2025-03-04**


### playtime per genre (top 30)

    339,709.4h 25.41% Serie
    237,768.2h 17.79% Magazin
    157,897.2h 11.81% Dokumentation
    132,186.5h 9.89%  Werbung
    126,559.3h 9.47%  Show
    102,547.5h 7.67%  Nachrichten
    80,024.9h  5.99%  Spielfilm
    52,115.1h  3.90%  Sport
    28,705.2h  2.15%  Reportage
    16,668.9h  1.25%  Musik
    11,741.0h  0.88%  Wetter
    11,167.4h  0.84%  Programmende
    9,515.0h   0.71%  E-Sport
    7,172.9h   0.54%  Verschiedenes
    5,603.9h   0.42%  Bericht
    4,784.9h   0.36%  Event
    3,541.9h   0.26%  *unknown*
    2,045.6h   0.15%  Verkaufsshow
    2,007.8h   0.15%  Videoclip
    522.7h     0.04%  Kurzfilm
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
