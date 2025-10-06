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

**197** channels, **3,369,015*** programs, **2,267,590.0** hours playtime between **2023-01-17** and **2025-10-06**


### playtime per genre (top 30)

    601,807.7h 26.54% Serie
    346,202.2h 15.27% Magazin
    281,925.1h 12.43% Dokumentation
    197,049.5h 8.69%  Show
    188,522.1h 8.31%  Werbung
    183,249.0h 8.08%  Spielfilm
    144,941.6h 6.39%  Sport
    137,655.1h 6.07%  Nachrichten
    47,663.6h  2.10%  Musik
    45,131.4h  1.99%  Reportage
    24,222.1h  1.07%  Verschiedenes
    15,864.4h  0.70%  Wetter
    11,167.4h  0.49%  Programmende
    9,515.0h   0.42%  E-Sport
    7,304.3h   0.32%  Bericht
    6,406.1h   0.28%  Event
    4,558.9h   0.20%  Kurzfilm
    4,356.2h   0.19%  Videoclip
    3,541.9h   0.16%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
