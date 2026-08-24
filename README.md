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

**203** channels, **5,234,153** programs, **3,607,738** hours playtime between **2023-01-17** and **2026-08-24**


### playtime per genre (top 30)

    987,123.8h 27.36% Serie
    502,325.3h 13.92% Magazin
    469,833.5h 13.02% Dokumentation
    333,090.1h 9.23%  Spielfilm
    296,765.8h 8.23%  Show
    283,023.5h 7.84%  Sport
    265,521.3h 7.36%  Werbung
    194,298.3h 5.39%  Nachrichten
    78,531.9h  2.18%  Musik
    69,305.6h  1.92%  Reportage
    41,283.6h  1.14%  Verschiedenes
    22,025.4h  0.61%  Wetter
    11,167.4h  0.31%  Programmende
    9,816.9h   0.27%  Bericht
    9,515.0h   0.26%  E-Sport
    8,984.4h   0.25%  Event
    7,836.9h   0.22%  Videoclip
    7,220.9h   0.20%  Kurzfilm
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
