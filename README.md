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

**197** channels, **3,997,025*** programs, **2,724,261.0** hours playtime between **2023-01-17** and **2026-01-20**


### playtime per genre (top 30)

    728,158.4h 26.73% Serie
    399,789.1h 14.68% Magazin
    343,426.5h 12.61% Dokumentation
    238,995.7h 8.77%  Spielfilm
    230,669.6h 8.47%  Show
    215,263.3h 7.90%  Werbung
    189,805.3h 6.97%  Sport
    155,265.5h 5.70%  Nachrichten
    61,870.9h  2.27%  Musik
    52,977.4h  1.94%  Reportage
    31,769.6h  1.17%  Verschiedenes
    17,981.1h  0.66%  Wetter
    11,167.4h  0.41%  Programmende
    9,515.0h   0.35%  E-Sport
    8,118.0h   0.30%  Bericht
    7,258.6h   0.27%  Event
    6,553.5h   0.24%  Kurzfilm
    5,607.7h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
    2,045.6h   0.08%  Verkaufsshow
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
