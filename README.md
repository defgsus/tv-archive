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

**210** channels, **5,703,593** programs, **3,947,217** hours playtime between **2023-01-17** and **2026-11-18**


### playtime per genre (top 30)

    1,085,930.8h 27.51% Serie
    543,599.7h   13.77% Magazin
    518,555.1h   13.14% Dokumentation
    368,704.9h   9.34%  Spielfilm
    323,563.4h   8.20%  Show
    318,698.9h   8.07%  Sport
    283,625.4h   7.19%  Werbung
    209,598.6h   5.31%  Nachrichten
    84,617.2h    2.14%  Musik
    75,356.1h    1.91%  Reportage
    44,416.5h    1.13%  Verschiedenes
    23,537.8h    0.60%  Wetter
    11,167.4h    0.28%  Programmende
    10,538.1h    0.27%  Bericht
    9,623.0h     0.24%  Event
    9,515.0h     0.24%  E-Sport
    8,706.4h     0.22%  Videoclip
    7,394.6h     0.19%  Kurzfilm
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
