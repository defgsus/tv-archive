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

**203** channels, **5,419,786** programs, **3,740,605** hours playtime between **2023-01-17** and **2026-09-26**


### playtime per genre (top 30)

    1,026,523.2h 27.44% Serie
    518,475.2h   13.86% Magazin
    488,964.9h   13.07% Dokumentation
    346,461.8h   9.26%  Spielfilm
    307,161.0h   8.21%  Show
    296,746.5h   7.93%  Sport
    272,410.1h   7.28%  Werbung
    200,446.2h   5.36%  Nachrichten
    80,919.2h    2.16%  Musik
    71,726.6h    1.92%  Reportage
    42,537.7h    1.14%  Verschiedenes
    22,655.0h    0.61%  Wetter
    11,167.4h    0.30%  Programmende
    10,138.2h    0.27%  Bericht
    9,515.0h     0.25%  E-Sport
    9,234.4h     0.25%  Event
    8,172.6h     0.22%  Videoclip
    7,282.5h     0.19%  Kurzfilm
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
