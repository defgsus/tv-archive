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

**195** channels, **2,022,070*** programs, **1,298,017.3** hours playtime between **2023-01-17** and **2025-02-23**


### playtime per genre (top 30)

    329,030.1h 25.35% Serie
    233,112.1h 17.96% Magazin
    152,807.7h 11.77% Dokumentation
    129,813.3h 10.00% Werbung
    123,306.9h 9.50%  Show
    100,995.8h 7.78%  Nachrichten
    75,887.5h  5.85%  Spielfilm
    48,350.9h  3.72%  Sport
    28,121.8h  2.17%  Reportage
    15,336.0h  1.18%  Musik
    11,584.8h  0.89%  Wetter
    11,167.4h  0.86%  Programmende
    9,515.0h   0.73%  E-Sport
    6,503.4h   0.50%  Verschiedenes
    5,480.0h   0.42%  Bericht
    4,664.7h   0.36%  Event
    3,541.9h   0.27%  *unknown*
    2,045.6h   0.16%  Verkaufsshow
    1,928.6h   0.15%  Videoclip
    366.1h     0.03%  Kurzfilm
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
