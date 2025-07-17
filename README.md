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

**197** channels, **2,885,085*** programs, **1,918,990.0** hours playtime between **2023-01-17** and **2025-07-17**


### playtime per genre (top 30)

    503,355.4h 26.23% Serie
    305,657.1h 15.93% Magazin
    234,281.5h 12.21% Dokumentation
    171,184.5h 8.92%  Show
    168,147.4h 8.76%  Werbung
    144,547.0h 7.53%  Spielfilm
    124,403.4h 6.48%  Nachrichten
    110,719.3h 5.77%  Sport
    38,937.7h  2.03%  Reportage
    36,713.8h  1.91%  Musik
    17,182.3h  0.90%  Verschiedenes
    14,244.3h  0.74%  Wetter
    11,167.4h  0.58%  Programmende
    9,515.0h   0.50%  E-Sport
    6,658.4h   0.35%  Bericht
    5,796.0h   0.30%  Event
    3,541.9h   0.18%  *unknown*
    3,343.0h   0.17%  Videoclip
    3,088.2h   0.16%  Kurzfilm
    2,045.6h   0.11%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
