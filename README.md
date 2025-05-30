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

**197** channels, **2,596,293*** programs, **1,711,397.5** hours playtime between **2023-01-17** and **2025-05-30**


### playtime per genre (top 30)

    444,814.9h 25.99% Serie
    281,461.5h 16.45% Magazin
    207,075.1h 12.10% Dokumentation
    155,509.6h 9.09%  Werbung
    155,363.0h 9.08%  Show
    121,219.6h 7.08%  Spielfilm
    116,915.3h 6.83%  Nachrichten
    89,808.6h  5.25%  Sport
    35,241.8h  2.06%  Reportage
    29,524.3h  1.73%  Musik
    13,676.5h  0.80%  Verschiedenes
    13,308.2h  0.78%  Wetter
    11,167.4h  0.65%  Programmende
    9,515.0h   0.56%  E-Sport
    6,248.0h   0.37%  Bericht
    5,466.3h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,855.1h   0.17%  Videoclip
    2,178.8h   0.13%  Kurzfilm
    2,045.6h   0.12%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
