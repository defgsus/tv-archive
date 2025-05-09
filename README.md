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

**197** channels, **2,470,259*** programs, **1,620,326.0** hours playtime between **2023-01-17** and **2025-05-09**


### playtime per genre (top 30)

    419,106.6h 25.87% Serie
    271,032.6h 16.73% Magazin
    195,158.5h 12.04% Dokumentation
    149,915.9h 9.25%  Werbung
    148,373.5h 9.16%  Show
    113,531.5h 7.01%  Nachrichten
    111,304.4h 6.87%  Spielfilm
    80,331.3h  4.96%  Sport
    33,637.5h  2.08%  Reportage
    26,376.3h  1.63%  Musik
    12,937.9h  0.80%  Wetter
    12,109.5h  0.75%  Verschiedenes
    11,167.4h  0.69%  Programmende
    9,515.0h   0.59%  E-Sport
    6,047.8h   0.37%  Bericht
    5,298.0h   0.33%  Event
    3,541.9h   0.22%  *unknown*
    2,648.7h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,785.2h   0.11%  Kurzfilm
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
