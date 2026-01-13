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

**197** channels, **3,955,579*** programs, **2,694,904.6** hours playtime between **2023-01-17** and **2026-01-13**


### playtime per genre (top 30)

    719,503.9h 26.70% Serie
    396,387.4h 14.71% Magazin
    339,443.7h 12.60% Dokumentation
    235,642.1h 8.74%  Spielfilm
    228,560.7h 8.48%  Show
    213,543.4h 7.92%  Werbung
    186,803.7h 6.93%  Sport
    154,089.5h 5.72%  Nachrichten
    61,342.8h  2.28%  Musik
    52,448.2h  1.95%  Reportage
    31,266.7h  1.16%  Verschiedenes
    17,841.7h  0.66%  Wetter
    11,167.4h  0.41%  Programmende
    9,515.0h   0.35%  E-Sport
    8,083.2h   0.30%  Bericht
    7,221.4h   0.27%  Event
    6,441.7h   0.24%  Kurzfilm
    5,533.9h   0.21%  Videoclip
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
