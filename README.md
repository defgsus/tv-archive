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

**197** channels, **3,166,914*** programs, **2,120,988.9** hours playtime between **2023-01-17** and **2025-09-02**


### playtime per genre (top 30)

    560,936.1h 26.45% Serie
    328,799.2h 15.50% Magazin
    261,719.2h 12.34% Dokumentation
    185,801.9h 8.76%  Show
    180,123.2h 8.49%  Werbung
    167,091.6h 7.88%  Spielfilm
    132,051.3h 6.23%  Nachrichten
    130,587.8h 6.16%  Sport
    43,097.4h  2.03%  Musik
    42,651.8h  2.01%  Reportage
    21,309.1h  1.00%  Verschiedenes
    15,200.8h  0.72%  Wetter
    11,167.4h  0.53%  Programmende
    9,515.0h   0.45%  E-Sport
    6,806.6h   0.32%  Bericht
    6,148.2h   0.29%  Event
    3,967.8h   0.19%  Kurzfilm
    3,966.2h   0.19%  Videoclip
    3,541.9h   0.17%  *unknown*
    2,045.6h   0.10%  Verkaufsshow
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
