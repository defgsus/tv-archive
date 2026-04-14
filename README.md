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

**198** channels, **4,483,810*** programs, **3,071,438.5** hours playtime between **2023-01-17** and **2026-04-14**


### playtime per genre (top 30)

    829,106.5h 26.99% Serie
    441,096.5h 14.36% Magazin
    392,155.0h 12.77% Dokumentation
    276,996.2h 9.02%  Spielfilm
    257,010.1h 8.37%  Show
    235,624.9h 7.67%  Werbung
    226,051.7h 7.36%  Sport
    169,390.6h 5.52%  Nachrichten
    68,314.8h  2.22%  Musik
    59,586.6h  1.94%  Reportage
    35,618.1h  1.16%  Verschiedenes
    19,561.2h  0.64%  Wetter
    11,167.4h  0.36%  Programmende
    9,515.0h   0.31%  E-Sport
    8,763.3h   0.29%  Bericht
    7,915.9h   0.26%  Event
    7,014.6h   0.23%  Kurzfilm
    6,481.6h   0.21%  Videoclip
    3,541.9h   0.12%  *unknown*
    2,045.6h   0.07%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
