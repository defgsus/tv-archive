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

**197** channels, **3,387,375*** programs, **2,280,625.5** hours playtime between **2023-01-17** and **2025-10-09**


### playtime per genre (top 30)

    605,563.8h 26.55% Serie
    347,860.8h 15.25% Magazin
    283,656.5h 12.44% Dokumentation
    198,007.0h 8.68%  Show
    189,312.5h 8.30%  Werbung
    184,544.0h 8.09%  Spielfilm
    146,097.9h 6.41%  Sport
    138,231.5h 6.06%  Nachrichten
    48,104.0h  2.11%  Musik
    45,359.5h  1.99%  Reportage
    24,456.2h  1.07%  Verschiedenes
    15,931.3h  0.70%  Wetter
    11,167.4h  0.49%  Programmende
    9,515.0h   0.42%  E-Sport
    7,346.8h   0.32%  Bericht
    6,417.7h   0.28%  Event
    4,612.7h   0.20%  Kurzfilm
    4,392.6h   0.19%  Videoclip
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
