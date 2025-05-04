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

**197** channels, **2,439,893*** programs, **1,598,755.8** hours playtime between **2023-01-17** and **2025-05-04**


### playtime per genre (top 30)

    412,856.3h 25.82% Serie
    268,446.2h 16.79% Magazin
    192,349.6h 12.03% Dokumentation
    148,625.1h 9.30%  Werbung
    146,764.8h 9.18%  Show
    112,665.8h 7.05%  Nachrichten
    109,149.4h 6.83%  Spielfilm
    78,181.1h  4.89%  Sport
    33,225.0h  2.08%  Reportage
    25,633.9h  1.60%  Musik
    12,846.5h  0.80%  Wetter
    11,739.0h  0.73%  Verschiedenes
    11,167.4h  0.70%  Programmende
    9,515.0h   0.60%  E-Sport
    5,988.4h   0.37%  Bericht
    5,266.1h   0.33%  Event
    3,541.9h   0.22%  *unknown*
    2,599.0h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,689.1h   0.11%  Kurzfilm
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
