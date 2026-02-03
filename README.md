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

**198** channels, **4,080,757*** programs, **2,783,596.9** hours playtime between **2023-01-17** and **2026-02-03**


### playtime per genre (top 30)

    745,222.8h 26.77% Serie
    406,656.1h 14.61% Magazin
    351,629.9h 12.63% Dokumentation
    245,782.2h 8.83%  Spielfilm
    235,088.6h 8.45%  Show
    218,714.2h 7.86%  Werbung
    196,036.1h 7.04%  Sport
    157,639.9h 5.66%  Nachrichten
    62,942.0h  2.26%  Musik
    54,054.1h  1.94%  Reportage
    32,716.1h  1.18%  Verschiedenes
    18,262.9h  0.66%  Wetter
    11,167.4h  0.40%  Programmende
    9,515.0h   0.34%  E-Sport
    8,207.9h   0.29%  Bericht
    7,343.4h   0.26%  Event
    6,788.2h   0.24%  Kurzfilm
    5,761.7h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
    2,045.6h   0.07%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
