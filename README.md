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

**197** channels, **2,819,199*** programs, **1,871,583.9** hours playtime between **2023-01-17** and **2025-07-06**


### playtime per genre (top 30)

    489,864.5h 26.17% Serie
    300,072.8h 16.03% Magazin
    228,002.9h 12.18% Dokumentation
    167,751.8h 8.96%  Show
    165,291.2h 8.83%  Werbung
    139,410.9h 7.45%  Spielfilm
    122,655.9h 6.55%  Nachrichten
    105,841.8h 5.66%  Sport
    38,100.8h  2.04%  Reportage
    35,079.0h  1.87%  Musik
    16,398.3h  0.88%  Verschiedenes
    14,034.5h  0.75%  Wetter
    11,167.4h  0.60%  Programmende
    9,515.0h   0.51%  E-Sport
    6,524.1h   0.35%  Bericht
    5,718.9h   0.31%  Event
    3,541.9h   0.19%  *unknown*
    3,221.9h   0.17%  Videoclip
    2,884.1h   0.15%  Kurzfilm
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
