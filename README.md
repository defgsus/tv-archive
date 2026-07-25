# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

[webapp on github.io](https://defgsus.github.io/tv-archive/)

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
  "description": null,
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**203** channels, **5,064,403** programs, **3,486,572** hours playtime between **2023-01-17** and **2026-07-25**


### playtime per genre (top 30)

    951,378.5h 27.29% Serie
    488,435.2h 14.01% Magazin
    451,841.6h 12.96% Dokumentation
    320,466.3h 9.19%  Spielfilm
    287,657.8h 8.25%  Show
    270,691.8h 7.76%  Sport
    258,855.1h 7.42%  Werbung
    188,751.0h 5.41%  Nachrichten
    76,192.8h  2.19%  Musik
    66,918.6h  1.92%  Reportage
    40,167.7h  1.15%  Verschiedenes
    21,418.7h  0.61%  Wetter
    11,167.4h  0.32%  Programmende
    9,643.4h   0.28%  Bericht
    9,515.0h   0.27%  E-Sport
    8,710.0h   0.25%  Event
    7,519.6h   0.22%  Videoclip
    7,174.1h   0.21%  Kurzfilm
    3,541.9h   0.10%  *unknown*
    2,045.6h   0.06%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.00%  Erotikfilm
    157.3h     0.00%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
