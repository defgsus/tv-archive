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

**195** channels, **2,123,925*** programs, **1,371,055.0** hours playtime between **2023-01-17** and **2025-03-12**


### playtime per genre (top 30)

    349,329.9h 25.48% Serie
    241,871.0h 17.64% Magazin
    162,369.0h 11.84% Dokumentation
    134,358.7h 9.80%  Werbung
    129,232.4h 9.43%  Show
    103,927.4h 7.58%  Nachrichten
    83,636.7h  6.10%  Spielfilm
    55,549.3h  4.05%  Sport
    29,262.3h  2.13%  Reportage
    17,871.8h  1.30%  Musik
    11,884.8h  0.87%  Wetter
    11,167.4h  0.81%  Programmende
    9,515.0h   0.69%  E-Sport
    7,776.2h   0.57%  Verschiedenes
    5,659.2h   0.41%  Bericht
    4,848.4h   0.35%  Event
    3,541.9h   0.26%  *unknown*
    2,084.3h   0.15%  Videoclip
    2,045.6h   0.15%  Verkaufsshow
    665.9h     0.05%  Kurzfilm
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
