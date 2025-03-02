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

**195** channels, **2,064,018*** programs, **1,328,124.9** hours playtime between **2023-01-17** and **2025-03-02**


### playtime per genre (top 30)

    337,409.9h 25.40% Serie
    236,767.8h 17.83% Magazin
    156,771.7h 11.80% Dokumentation
    131,656.5h 9.91%  Werbung
    125,783.8h 9.47%  Show
    102,231.9h 7.70%  Nachrichten
    79,047.1h  5.95%  Spielfilm
    51,263.7h  3.86%  Sport
    28,572.1h  2.15%  Reportage
    16,387.7h  1.23%  Musik
    11,709.7h  0.88%  Wetter
    11,167.4h  0.84%  Programmende
    9,515.0h   0.72%  E-Sport
    7,021.1h   0.53%  Verschiedenes
    5,574.0h   0.42%  Bericht
    4,720.4h   0.36%  Event
    3,541.9h   0.27%  *unknown*
    2,045.6h   0.15%  Verkaufsshow
    1,992.2h   0.15%  Videoclip
    487.5h     0.04%  Kurzfilm
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
