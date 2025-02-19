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

**195** channels, **2,642,883*** programs, **1,735,667.1** hours playtime between **2023-01-17** and **2025-02-20**


### playtime per genre (top 30)

    418,356.6h 24.10% Serie
    305,892.1h 17.62% Magazin
    213,796.6h 12.32% Dokumentation
    177,626.9h 10.23% Werbung
    169,665.2h 9.78%  Show
    129,712.8h 7.47%  Nachrichten
    114,524.1h 6.60%  Spielfilm
    58,474.0h  3.37%  Sport
    39,363.6h  2.27%  Reportage
    18,520.5h  1.07%  Musik
    17,127.9h  0.99%  Programmende
    14,199.0h  0.82%  E-Sport
    12,957.0h  0.75%  Wetter
    8,410.6h   0.48%  Verschiedenes
    7,688.1h   0.44%  Videoclip
    6,492.1h   0.37%  Bericht
    5,425.1h   0.31%  Event
    5,237.8h   0.30%  *unknown*
    2,418.7h   0.14%  Verkaufsshow
    1,600.2h   0.09%  Porno Clips
    1,395.5h   0.08%  Nachtprogramm
    599.1h     0.03%  Kurzfilm
    526.1h     0.03%  Erotikfilm
    517.3h     0.03%  Dokureihe
    487.2h     0.03%  Eishockey
    356.7h     0.02%  Judo
    354.5h     0.02%  Handball
    293.9h     0.02%  Darts
    272.0h     0.02%  Leichtathletik
    236.6h     0.01%  Gespräch
