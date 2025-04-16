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

**195** channels, **2,333,546*** programs, **1,521,060.4** hours playtime between **2023-01-17** and **2025-04-16**


### playtime per genre (top 30)

    391,459.0h 25.74% Serie
    259,703.8h 17.07% Magazin
    181,978.3h 11.96% Dokumentation
    143,888.4h 9.46%  Werbung
    141,008.7h 9.27%  Show
    109,779.3h 7.22%  Nachrichten
    99,422.1h  6.54%  Spielfilm
    70,526.1h  4.64%  Sport
    31,838.9h  2.09%  Reportage
    23,011.4h  1.51%  Musik
    12,518.2h  0.82%  Wetter
    11,167.4h  0.73%  Programmende
    10,414.2h  0.68%  Verschiedenes
    9,515.0h   0.63%  E-Sport
    5,906.5h   0.39%  Bericht
    5,087.4h   0.33%  Event
    3,541.9h   0.23%  *unknown*
    2,420.9h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,367.4h   0.09%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
