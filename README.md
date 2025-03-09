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

**195** channels, **2,105,928*** programs, **1,358,160.6** hours playtime between **2023-01-17** and **2025-03-09**


### playtime per genre (top 30)

    345,727.2h 25.46% Serie
    240,307.9h 17.69% Magazin
    160,669.2h 11.83% Dokumentation
    133,554.0h 9.83%  Werbung
    128,254.6h 9.44%  Show
    103,432.5h 7.62%  Nachrichten
    82,227.9h  6.05%  Spielfilm
    54,279.5h  4.00%  Sport
    29,043.4h  2.14%  Reportage
    17,427.8h  1.28%  Musik
    11,833.7h  0.87%  Wetter
    11,167.4h  0.82%  Programmende
    9,515.0h   0.70%  E-Sport
    7,547.5h   0.56%  Verschiedenes
    5,645.4h   0.42%  Bericht
    4,819.0h   0.35%  Event
    3,541.9h   0.26%  *unknown*
    2,054.5h   0.15%  Videoclip
    2,045.6h   0.15%  Verkaufsshow
    608.5h     0.04%  Kurzfilm
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
