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

**197** channels, **3,191,251*** programs, **2,138,242.4** hours playtime between **2023-01-17** and **2025-09-06**


### playtime per genre (top 30)

    565,853.2h 26.46% Serie
    330,946.2h 15.48% Magazin
    264,067.0h 12.35% Dokumentation
    187,067.8h 8.75%  Show
    181,173.4h 8.47%  Werbung
    168,821.9h 7.90%  Spielfilm
    132,790.2h 6.21%  Nachrichten
    132,164.7h 6.18%  Sport
    43,596.5h  2.04%  Musik
    42,921.8h  2.01%  Reportage
    21,774.8h  1.02%  Verschiedenes
    15,282.8h  0.71%  Wetter
    11,167.4h  0.52%  Programmende
    9,515.0h   0.44%  E-Sport
    6,823.7h   0.32%  Bericht
    6,171.5h   0.29%  Event
    4,039.6h   0.19%  Kurzfilm
    4,016.6h   0.19%  Videoclip
    3,541.9h   0.17%  *unknown*
    2,045.6h   0.10%  Verkaufsshow
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
