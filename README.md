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

**198** channels, **4,363,739*** programs, **2,985,623.4** hours playtime between **2023-01-17** and **2026-03-24**


### playtime per genre (top 30)

    804,245.8h 26.94% Serie
    431,153.0h 14.44% Magazin
    379,837.7h 12.72% Dokumentation
    266,995.1h 8.94%  Spielfilm
    250,693.0h 8.40%  Show
    230,687.3h 7.73%  Werbung
    217,238.6h 7.28%  Sport
    165,842.1h 5.55%  Nachrichten
    66,697.9h  2.23%  Musik
    57,875.5h  1.94%  Reportage
    34,802.8h  1.17%  Verschiedenes
    19,155.7h  0.64%  Wetter
    11,167.4h  0.37%  Programmende
    9,515.0h   0.32%  E-Sport
    8,635.6h   0.29%  Bericht
    7,756.4h   0.26%  Event
    6,987.5h   0.23%  Kurzfilm
    6,268.7h   0.21%  Videoclip
    3,541.9h   0.12%  *unknown*
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
    147.0h     0.00%  Wirtschaftsmagazin
