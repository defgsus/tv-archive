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

**195** channels, **2,166,256*** programs, **1,401,072.6** hours playtime between **2023-01-17** and **2025-03-19**


### playtime per genre (top 30)

    357,823.5h 25.54% Serie
    245,463.0h 17.52% Magazin
    166,174.0h 11.86% Dokumentation
    136,268.2h 9.73%  Werbung
    131,581.8h 9.39%  Show
    105,095.1h 7.50%  Nachrichten
    86,803.3h  6.20%  Spielfilm
    58,562.4h  4.18%  Sport
    29,762.3h  2.12%  Reportage
    18,935.5h  1.35%  Musik
    12,011.5h  0.86%  Wetter
    11,167.4h  0.80%  Programmende
    9,515.0h   0.68%  E-Sport
    8,305.4h   0.59%  Verschiedenes
    5,707.3h   0.41%  Bericht
    4,895.2h   0.35%  Event
    3,541.9h   0.25%  *unknown*
    2,153.2h   0.15%  Videoclip
    2,045.6h   0.15%  Verkaufsshow
    803.2h     0.06%  Kurzfilm
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
