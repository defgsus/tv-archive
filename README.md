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

**197** channels, **3,465,052*** programs, **2,336,810.5** hours playtime between **2023-01-17** and **2025-10-22**


### playtime per genre (top 30)

    621,486.3h 26.60% Serie
    354,625.5h 15.18% Magazin
    291,020.2h 12.45% Dokumentation
    202,280.3h 8.66%  Show
    192,734.0h 8.25%  Werbung
    190,626.9h 8.16%  Spielfilm
    151,611.5h 6.49%  Sport
    140,425.2h 6.01%  Nachrichten
    50,038.5h  2.14%  Musik
    46,304.5h  1.98%  Reportage
    25,336.7h  1.08%  Verschiedenes
    16,190.7h  0.69%  Wetter
    11,167.4h  0.48%  Programmende
    9,515.0h   0.41%  E-Sport
    7,489.4h   0.32%  Bericht
    6,515.8h   0.28%  Event
    4,842.5h   0.21%  Kurzfilm
    4,547.6h   0.19%  Videoclip
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
