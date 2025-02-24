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

**195** channels, **2,027,685*** programs, **1,302,323.8** hours playtime between **2023-01-17** and **2025-02-24**


### playtime per genre (top 30)

    330,064.9h 25.34% Serie
    233,608.0h 17.94% Magazin
    153,428.1h 11.78% Dokumentation
    130,076.9h 9.99%  Werbung
    123,664.7h 9.50%  Show
    101,148.2h 7.77%  Nachrichten
    76,477.7h  5.87%  Spielfilm
    48,795.0h  3.75%  Sport
    28,171.6h  2.16%  Reportage
    15,476.0h  1.19%  Musik
    11,596.4h  0.89%  Wetter
    11,167.4h  0.86%  Programmende
    9,515.0h   0.73%  E-Sport
    6,572.3h   0.50%  Verschiedenes
    5,509.1h   0.42%  Bericht
    4,683.1h   0.36%  Event
    3,541.9h   0.27%  *unknown*
    2,045.6h   0.16%  Verkaufsshow
    1,939.8h   0.15%  Videoclip
    384.2h     0.03%  Kurzfilm
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
