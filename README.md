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

**197** channels, **3,310,653*** programs, **2,224,580.5** hours playtime between **2023-01-17** and **2025-09-26**


### playtime per genre (top 30)

    590,150.1h 26.53% Serie
    341,255.4h 15.34% Magazin
    275,802.3h 12.40% Dokumentation
    193,724.8h 8.71%  Show
    186,159.5h 8.37%  Werbung
    178,137.8h 8.01%  Spielfilm
    140,747.4h 6.33%  Sport
    136,101.3h 6.12%  Nachrichten
    46,229.8h  2.08%  Musik
    44,418.7h  2.00%  Reportage
    23,393.3h  1.05%  Verschiedenes
    15,679.3h  0.70%  Wetter
    11,167.4h  0.50%  Programmende
    9,515.0h   0.43%  E-Sport
    7,083.8h   0.32%  Bericht
    6,329.6h   0.28%  Event
    4,388.6h   0.20%  Kurzfilm
    4,248.0h   0.19%  Videoclip
    3,541.9h   0.16%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
