# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

[webapp on github.io](https://defgsus.github.io/tv-archive/)

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
  "description": null,
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**203** channels, **5,251,475** programs, **3,619,833** hours playtime between **2023-01-17** and **2026-08-27**


### playtime per genre (top 30)

    990,858.8h 27.37% Serie
    503,866.4h 13.92% Magazin
    471,591.8h 13.03% Dokumentation
    334,178.5h 9.23%  Spielfilm
    297,668.6h 8.22%  Show
    284,154.4h 7.85%  Sport
    266,176.0h 7.35%  Werbung
    194,892.0h 5.38%  Nachrichten
    78,766.5h  2.18%  Musik
    69,515.1h  1.92%  Reportage
    41,394.2h  1.14%  Verschiedenes
    22,089.5h  0.61%  Wetter
    11,167.4h  0.31%  Programmende
    9,831.2h   0.27%  Bericht
    9,515.0h   0.26%  E-Sport
    8,999.3h   0.25%  Event
    7,869.9h   0.22%  Videoclip
    7,230.3h   0.20%  Kurzfilm
    3,541.9h   0.10%  *unknown*
    2,045.6h   0.06%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.00%  Erotikfilm
    157.3h     0.00%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
