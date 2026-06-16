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

**203** channels, **4,843,421*** programs, **3,328,547.3** hours playtime between **2023-01-17** and **2026-06-16**


### playtime per genre (top 30)

    904,496.8h 27.17% Serie
    470,550.0h 14.14% Magazin
    429,149.0h 12.89% Dokumentation
    304,570.8h 9.15%  Spielfilm
    276,080.0h 8.29%  Show
    253,068.2h 7.60%  Sport
    250,291.9h 7.52%  Werbung
    181,368.8h 5.45%  Nachrichten
    73,172.9h  2.20%  Musik
    64,076.4h  1.93%  Reportage
    38,322.9h  1.15%  Verschiedenes
    20,760.8h  0.62%  Wetter
    11,167.4h  0.34%  Programmende
    9,515.0h   0.29%  E-Sport
    9,216.3h   0.28%  Bericht
    8,417.8h   0.25%  Event
    7,137.0h   0.21%  Kurzfilm
    7,117.0h   0.21%  Videoclip
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
