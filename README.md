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

**197** channels, **2,920,882*** programs, **1,944,899.4** hours playtime between **2023-01-17** and **2025-07-23**


### playtime per genre (top 30)

    510,628.2h 26.25% Serie
    308,664.7h 15.87% Magazin
    237,764.8h 12.23% Dokumentation
    173,077.2h 8.90%  Show
    169,664.5h 8.72%  Werbung
    147,484.1h 7.58%  Spielfilm
    125,368.2h 6.45%  Nachrichten
    113,372.3h 5.83%  Sport
    39,388.0h  2.03%  Reportage
    37,602.6h  1.93%  Musik
    17,647.2h  0.91%  Verschiedenes
    14,357.6h  0.74%  Wetter
    11,167.4h  0.57%  Programmende
    9,515.0h   0.49%  E-Sport
    6,680.1h   0.34%  Bericht
    5,839.2h   0.30%  Event
    3,541.9h   0.18%  *unknown*
    3,424.6h   0.18%  Videoclip
    3,205.2h   0.16%  Kurzfilm
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
