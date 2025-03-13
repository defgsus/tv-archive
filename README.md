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

**195** channels, **2,130,105*** programs, **1,375,350.1** hours playtime between **2023-01-17** and **2025-03-13**


### playtime per genre (top 30)

    350,580.5h 25.49% Serie
    242,402.5h 17.62% Magazin
    162,877.1h 11.84% Dokumentation
    134,635.0h 9.79%  Werbung
    129,594.9h 9.42%  Show
    104,117.6h 7.57%  Nachrichten
    84,063.4h  6.11%  Spielfilm
    55,950.1h  4.07%  Sport
    29,320.3h  2.13%  Reportage
    18,019.7h  1.31%  Musik
    11,902.1h  0.87%  Wetter
    11,167.4h  0.81%  Programmende
    9,515.0h   0.69%  E-Sport
    7,851.7h   0.57%  Verschiedenes
    5,676.8h   0.41%  Bericht
    4,853.0h   0.35%  Event
    3,541.9h   0.26%  *unknown*
    2,094.4h   0.15%  Videoclip
    2,045.6h   0.15%  Verkaufsshow
    683.5h     0.05%  Kurzfilm
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
