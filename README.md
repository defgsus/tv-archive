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

**203** channels, **5,363,821** programs, **3,700,358** hours playtime between **2023-01-17** and **2026-09-16**


### playtime per genre (top 30)

    1,014,388.9h 27.41% Serie
    513,508.6h   13.88% Magazin
    483,390.4h   13.06% Dokumentation
    342,501.1h   9.26%  Spielfilm
    303,989.5h   8.22%  Show
    292,567.8h   7.91%  Sport
    270,346.2h   7.31%  Werbung
    198,563.5h   5.37%  Nachrichten
    80,192.4h    2.17%  Musik
    71,015.2h    1.92%  Reportage
    42,154.7h    1.14%  Verschiedenes
    22,465.3h    0.61%  Wetter
    11,167.4h    0.30%  Programmende
    10,028.6h    0.27%  Bericht
    9,515.0h     0.26%  E-Sport
    9,162.8h     0.25%  Event
    8,070.5h     0.22%  Videoclip
    7,262.2h     0.20%  Kurzfilm
    3,541.9h     0.10%  *unknown*
    2,045.6h     0.06%  Verkaufsshow
    353.9h       0.01%  Eishockey
    299.8h       0.01%  Judo
    257.0h       0.01%  Darts
    232.8h       0.01%  Handball
    219.5h       0.01%  Dokureihe
    212.4h       0.01%  Leichtathletik
    190.7h       0.01%  Gespräch
    169.7h       0.00%  Erotikfilm
    157.3h       0.00%  Fußball
    147.0h       0.00%  Wirtschaftsmagazin
