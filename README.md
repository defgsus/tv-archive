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

**197** channels, **2,692,932*** programs, **1,780,878.7** hours playtime between **2023-01-17** and **2025-06-15**


### playtime per genre (top 30)

    464,286.6h 26.07% Serie
    289,358.8h 16.25% Magazin
    216,066.6h 12.13% Dokumentation
    160,719.3h 9.02%  Show
    159,765.4h 8.97%  Werbung
    129,403.1h 7.27%  Spielfilm
    119,375.0h 6.70%  Nachrichten
    96,829.9h  5.44%  Sport
    36,501.2h  2.05%  Reportage
    31,920.8h  1.79%  Musik
    14,881.1h  0.84%  Verschiedenes
    13,618.8h  0.76%  Wetter
    11,167.4h  0.63%  Programmende
    9,515.0h   0.53%  E-Sport
    6,339.2h   0.36%  Bericht
    5,581.9h   0.31%  Event
    3,541.9h   0.20%  *unknown*
    3,018.1h   0.17%  Videoclip
    2,482.3h   0.14%  Kurzfilm
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
