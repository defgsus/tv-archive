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

**197** channels, **3,697,641*** programs, **2,505,736.0** hours playtime between **2023-01-17** and **2025-11-30**


### playtime per genre (top 30)

    668,378.6h 26.67% Serie
    375,062.2h 14.97% Magazin
    313,513.3h 12.51% Dokumentation
    214,833.9h 8.57%  Show
    209,915.3h 8.38%  Spielfilm
    202,949.4h 8.10%  Werbung
    168,128.0h 6.71%  Sport
    147,099.9h 5.87%  Nachrichten
    55,779.3h  2.23%  Musik
    49,159.8h  1.96%  Reportage
    28,047.5h  1.12%  Verschiedenes
    16,939.7h  0.68%  Wetter
    11,167.4h  0.45%  Programmende
    9,515.0h   0.38%  E-Sport
    7,799.6h   0.31%  Bericht
    6,792.1h   0.27%  Event
    5,583.1h   0.22%  Kurzfilm
    5,010.5h   0.20%  Videoclip
    3,541.9h   0.14%  *unknown*
    2,045.6h   0.08%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
