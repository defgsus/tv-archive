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

**195** channels, **2,172,352*** programs, **1,405,376.5** hours playtime between **2023-01-17** and **2025-03-20**


### playtime per genre (top 30)

    359,085.3h 25.55% Serie
    245,996.9h 17.50% Magazin
    166,687.5h 11.86% Dokumentation
    136,543.1h 9.72%  Werbung
    131,938.3h 9.39%  Show
    105,288.6h 7.49%  Nachrichten
    87,206.8h  6.21%  Spielfilm
    58,976.3h  4.20%  Sport
    29,835.4h  2.12%  Reportage
    19,079.0h  1.36%  Musik
    12,031.9h  0.86%  Wetter
    11,167.4h  0.79%  Programmende
    9,515.0h   0.68%  E-Sport
    8,382.3h   0.60%  Verschiedenes
    5,713.4h   0.41%  Bericht
    4,897.8h   0.35%  Event
    3,541.9h   0.25%  *unknown*
    2,162.9h   0.15%  Videoclip
    2,045.6h   0.15%  Verkaufsshow
    823.3h     0.06%  Kurzfilm
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
