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

**197** channels, **3,572,697*** programs, **2,415,182.1** hours playtime between **2023-01-17** and **2025-11-09**


### playtime per genre (top 30)

    643,535.5h 26.65% Serie
    364,116.4h 15.08% Magazin
    301,315.7h 12.48% Dokumentation
    208,135.5h 8.62%  Show
    199,475.0h 8.26%  Spielfilm
    197,451.4h 8.18%  Werbung
    159,232.7h 6.59%  Sport
    143,506.8h 5.94%  Nachrichten
    52,622.0h  2.18%  Musik
    47,684.6h  1.97%  Reportage
    26,633.3h  1.10%  Verschiedenes
    16,533.2h  0.68%  Wetter
    11,167.4h  0.46%  Programmende
    9,515.0h   0.39%  E-Sport
    7,611.6h   0.32%  Bericht
    6,638.6h   0.27%  Event
    5,188.9h   0.21%  Kurzfilm
    4,761.2h   0.20%  Videoclip
    3,541.9h   0.15%  *unknown*
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
