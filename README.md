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

**197** channels, **3,584,451*** programs, **2,423,865.9** hours playtime between **2023-01-17** and **2025-11-11**


### playtime per genre (top 30)

    645,814.8h 26.64% Serie
    365,118.7h 15.06% Magazin
    302,555.1h 12.48% Dokumentation
    208,743.5h 8.61%  Show
    200,575.2h 8.28%  Spielfilm
    197,973.2h 8.17%  Werbung
    160,136.0h 6.61%  Sport
    143,826.0h 5.93%  Nachrichten
    52,924.0h  2.18%  Musik
    47,823.8h  1.97%  Reportage
    26,771.8h  1.10%  Verschiedenes
    16,565.1h  0.68%  Wetter
    11,167.4h  0.46%  Programmende
    9,515.0h   0.39%  E-Sport
    7,624.4h   0.31%  Bericht
    6,659.9h   0.27%  Event
    5,227.4h   0.22%  Kurzfilm
    4,786.3h   0.20%  Videoclip
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
