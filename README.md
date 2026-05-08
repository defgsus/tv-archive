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

**198** channels, **4,622,134*** programs, **3,169,498.1** hours playtime between **2023-01-17** and **2026-05-08**


### playtime per genre (top 30)

    858,389.9h 27.08% Serie
    452,539.4h 14.28% Magazin
    406,120.2h 12.81% Dokumentation
    286,963.0h 9.05%  Spielfilm
    264,308.4h 8.34%  Show
    241,349.6h 7.61%  Werbung
    236,231.7h 7.45%  Sport
    173,948.1h 5.49%  Nachrichten
    70,146.0h  2.21%  Musik
    61,297.3h  1.93%  Reportage
    36,621.3h  1.16%  Verschiedenes
    20,025.5h  0.63%  Wetter
    11,167.4h  0.35%  Programmende
    9,515.0h   0.30%  E-Sport
    8,922.9h   0.28%  Bericht
    8,100.4h   0.26%  Event
    7,059.6h   0.22%  Kurzfilm
    6,724.0h   0.21%  Videoclip
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
