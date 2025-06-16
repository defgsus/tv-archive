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

**197** channels, **2,698,665*** programs, **1,785,199.0** hours playtime between **2023-01-17** and **2025-06-16**


### playtime per genre (top 30)

    465,357.5h 26.07% Serie
    289,847.5h 16.24% Magazin
    216,677.3h 12.14% Dokumentation
    161,059.7h 9.02%  Show
    160,036.4h 8.96%  Werbung
    129,991.7h 7.28%  Spielfilm
    119,476.6h 6.69%  Nachrichten
    97,308.5h  5.45%  Sport
    36,578.4h  2.05%  Reportage
    32,076.9h  1.80%  Musik
    14,953.9h  0.84%  Verschiedenes
    13,635.8h  0.76%  Wetter
    11,167.4h  0.63%  Programmende
    9,515.0h   0.53%  E-Sport
    6,341.5h   0.36%  Bericht
    5,596.1h   0.31%  Event
    3,541.9h   0.20%  *unknown*
    3,027.6h   0.17%  Videoclip
    2,502.9h   0.14%  Kurzfilm
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
