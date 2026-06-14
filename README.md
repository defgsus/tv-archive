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

**203** channels, **4,832,290*** programs, **3,320,297.4** hours playtime between **2023-01-17** and **2026-06-14**


### playtime per genre (top 30)

    902,156.2h 27.17% Serie
    469,662.1h 14.15% Magazin
    427,975.9h 12.89% Dokumentation
    303,685.0h 9.15%  Spielfilm
    275,482.8h 8.30%  Show
    252,049.4h 7.59%  Sport
    249,839.3h 7.52%  Werbung
    181,012.8h 5.45%  Nachrichten
    73,011.5h  2.20%  Musik
    63,913.3h  1.92%  Reportage
    38,191.9h  1.15%  Verschiedenes
    20,731.8h  0.62%  Wetter
    11,167.4h  0.34%  Programmende
    9,515.0h   0.29%  E-Sport
    9,203.3h   0.28%  Bericht
    8,399.4h   0.25%  Event
    7,135.6h   0.21%  Kurzfilm
    7,096.3h   0.21%  Videoclip
    3,541.9h   0.11%  *unknown*
    2,045.6h   0.06%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.00%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
