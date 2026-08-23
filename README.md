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

**203** channels, **5,228,720** programs, **3,603,669** hours playtime between **2023-01-17** and **2026-08-23**


### playtime per genre (top 30)

    986,093.1h 27.36% Serie
    501,898.5h 13.93% Magazin
    469,166.4h 13.02% Dokumentation
    332,553.5h 9.23%  Spielfilm
    296,423.4h 8.23%  Show
    282,577.7h 7.84%  Sport
    265,302.3h 7.36%  Werbung
    194,148.2h 5.39%  Nachrichten
    78,453.1h  2.18%  Musik
    69,220.0h  1.92%  Reportage
    41,245.4h  1.14%  Verschiedenes
    22,007.2h  0.61%  Wetter
    11,167.4h  0.31%  Programmende
    9,816.2h   0.27%  Bericht
    9,515.0h   0.26%  E-Sport
    8,968.9h   0.25%  Event
    7,827.2h   0.22%  Videoclip
    7,217.7h   0.20%  Kurzfilm
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
