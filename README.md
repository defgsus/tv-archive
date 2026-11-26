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

**210** channels, **5,749,638** programs, **3,980,433** hours playtime between **2023-01-17** and **2026-11-26**


### playtime per genre (top 30)

    1,095,382.7h 27.52% Serie
    547,652.5h   13.76% Magazin
    523,240.2h   13.15% Dokumentation
    372,339.5h   9.35%  Spielfilm
    326,226.2h   8.20%  Show
    322,140.5h   8.09%  Sport
    285,465.6h   7.17%  Werbung
    211,175.2h   5.31%  Nachrichten
    85,192.8h    2.14%  Musik
    75,953.9h    1.91%  Reportage
    44,716.9h    1.12%  Verschiedenes
    23,683.3h    0.59%  Wetter
    11,167.4h    0.28%  Programmende
    10,622.0h    0.27%  Bericht
    9,680.3h     0.24%  Event
    9,515.0h     0.24%  E-Sport
    8,792.3h     0.22%  Videoclip
    7,419.1h     0.19%  Kurzfilm
    3,541.9h     0.09%  *unknown*
    2,045.6h     0.05%  Verkaufsshow
    353.9h       0.01%  Eishockey
    299.8h       0.01%  Judo
    257.0h       0.01%  Darts
    232.8h       0.01%  Handball
    219.5h       0.01%  Dokureihe
    212.4h       0.01%  Leichtathletik
    190.7h       0.00%  Gespräch
    169.7h       0.00%  Erotikfilm
    157.3h       0.00%  Fußball
    147.0h       0.00%  Wirtschaftsmagazin
