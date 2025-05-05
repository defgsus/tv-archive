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

**197** channels, **2,445,663*** programs, **1,603,084.7** hours playtime between **2023-01-17** and **2025-05-05**


### playtime per genre (top 30)

    413,911.4h 25.82% Serie
    268,935.9h 16.78% Magazin
    192,992.9h 12.04% Dokumentation
    148,882.9h 9.29%  Werbung
    147,097.8h 9.18%  Show
    112,780.8h 7.04%  Nachrichten
    109,731.0h 6.84%  Spielfilm
    78,650.1h  4.91%  Sport
    33,321.2h  2.08%  Reportage
    25,781.4h  1.61%  Musik
    12,859.8h  0.80%  Wetter
    11,812.1h  0.74%  Verschiedenes
    11,167.4h  0.70%  Programmende
    9,515.0h   0.59%  E-Sport
    5,996.1h   0.37%  Bericht
    5,277.5h   0.33%  Event
    3,541.9h   0.22%  *unknown*
    2,608.9h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,714.2h   0.11%  Kurzfilm
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
