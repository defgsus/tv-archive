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

**210** channels, **5,657,646** programs, **3,913,995** hours playtime between **2023-01-17** and **2026-11-10**


### playtime per genre (top 30)

    1,076,411.1h 27.50% Serie
    539,599.1h   13.79% Magazin
    513,798.3h   13.13% Dokumentation
    365,153.1h   9.33%  Spielfilm
    320,903.6h   8.20%  Show
    315,273.5h   8.06%  Sport
    281,771.4h   7.20%  Werbung
    207,975.4h   5.31%  Nachrichten
    84,025.8h    2.15%  Musik
    74,783.5h    1.91%  Reportage
    44,116.2h    1.13%  Verschiedenes
    23,398.3h    0.60%  Wetter
    11,167.4h    0.29%  Programmende
    10,472.4h    0.27%  Bericht
    9,570.8h     0.24%  Event
    9,515.0h     0.24%  E-Sport
    8,620.1h     0.22%  Videoclip
    7,372.5h     0.19%  Kurzfilm
    3,541.9h     0.09%  *unknown*
    2,045.6h     0.05%  Verkaufsshow
    353.9h       0.01%  Eishockey
    299.8h       0.01%  Judo
    257.0h       0.01%  Darts
    232.8h       0.01%  Handball
    219.5h       0.01%  Dokureihe
    212.4h       0.01%  Leichtathletik
    190.7h       0.00%  Gespräch
    169.7h       0.00%  Erotikfilm
    157.3h       0.00%  Fußball
    147.0h       0.00%  Wirtschaftsmagazin
