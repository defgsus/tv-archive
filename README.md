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

**201** channels, **4,809,163*** programs, **3,303,821.2** hours playtime between **2023-01-17** and **2026-06-10**


### playtime per genre (top 30)

    897,376.1h 27.16% Serie
    467,743.1h 14.16% Magazin
    425,665.7h 12.88% Dokumentation
    302,037.0h 9.14%  Spielfilm
    274,186.9h 8.30%  Show
    250,230.7h 7.57%  Sport
    248,934.8h 7.53%  Werbung
    180,231.5h 5.46%  Nachrichten
    72,694.7h  2.20%  Musik
    63,645.4h  1.93%  Reportage
    37,968.7h  1.15%  Verschiedenes
    20,654.5h  0.63%  Wetter
    11,167.4h  0.34%  Programmende
    9,515.0h   0.29%  E-Sport
    9,142.3h   0.28%  Bericht
    8,370.2h   0.25%  Event
    7,132.6h   0.22%  Kurzfilm
    7,056.2h   0.21%  Videoclip
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
