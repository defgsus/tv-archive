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

**195** channels, **2,153,995*** programs, **1,392,539.0** hours playtime between **2023-01-17** and **2025-03-17**


### playtime per genre (top 30)

    355,248.5h 25.51% Serie
    244,434.3h 17.55% Magazin
    165,096.5h 11.86% Dokumentation
    135,729.1h 9.75%  Werbung
    130,956.0h 9.40%  Show
    104,728.9h 7.52%  Nachrichten
    86,016.3h  6.18%  Spielfilm
    57,763.2h  4.15%  Sport
    29,605.6h  2.13%  Reportage
    18,636.3h  1.34%  Musik
    11,973.6h  0.86%  Wetter
    11,167.4h  0.80%  Programmende
    9,515.0h   0.68%  E-Sport
    8,150.9h   0.59%  Verschiedenes
    5,691.2h   0.41%  Bericht
    4,887.8h   0.35%  Event
    3,541.9h   0.25%  *unknown*
    2,133.3h   0.15%  Videoclip
    2,045.6h   0.15%  Verkaufsshow
    759.7h     0.05%  Kurzfilm
    353.9h     0.03%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.02%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
