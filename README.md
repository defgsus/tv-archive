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

**198** channels, **4,092,890*** programs, **2,792,040.6** hours playtime between **2023-01-17** and **2026-02-05**


### playtime per genre (top 30)

    747,730.7h 26.78% Serie
    407,721.8h 14.60% Magazin
    352,758.4h 12.63% Dokumentation
    246,667.9h 8.83%  Spielfilm
    235,733.2h 8.44%  Show
    219,210.5h 7.85%  Werbung
    196,843.7h 7.05%  Sport
    158,005.9h 5.66%  Nachrichten
    63,084.7h  2.26%  Musik
    54,200.3h  1.94%  Reportage
    32,839.7h  1.18%  Verschiedenes
    18,308.8h  0.66%  Wetter
    11,167.4h  0.40%  Programmende
    9,515.0h   0.34%  E-Sport
    8,216.6h   0.29%  Bericht
    7,356.1h   0.26%  Event
    6,827.5h   0.24%  Kurzfilm
    5,784.3h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
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
