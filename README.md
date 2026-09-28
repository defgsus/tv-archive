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

**203** channels, **5,430,585** programs, **3,748,719** hours playtime between **2023-01-17** and **2026-09-28**


### playtime per genre (top 30)

    1,028,673.8h 27.44% Serie
    519,398.8h   13.86% Magazin
    490,221.2h   13.08% Dokumentation
    347,487.7h   9.27%  Spielfilm
    307,853.1h   8.21%  Show
    297,668.3h   7.94%  Sport
    272,808.5h   7.28%  Werbung
    200,736.9h   5.35%  Nachrichten
    81,062.2h    2.16%  Musik
    71,858.0h    1.92%  Reportage
    42,612.3h    1.14%  Verschiedenes
    22,688.5h    0.61%  Wetter
    11,167.4h    0.30%  Programmende
    10,154.0h    0.27%  Bericht
    9,515.0h     0.25%  E-Sport
    9,266.3h     0.25%  Event
    8,193.2h     0.22%  Videoclip
    7,286.0h     0.19%  Kurzfilm
    3,541.9h     0.09%  *unknown*
    2,045.6h     0.05%  Verkaufsshow
    353.9h       0.01%  Eishockey
    299.8h       0.01%  Judo
    257.0h       0.01%  Darts
    232.8h       0.01%  Handball
    219.5h       0.01%  Dokureihe
    212.4h       0.01%  Leichtathletik
    190.7h       0.01%  Gespräch
    169.7h       0.00%  Erotikfilm
    157.3h       0.00%  Fußball
    147.0h       0.00%  Wirtschaftsmagazin
