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

**197** channels, **2,578,061*** programs, **1,698,374.0** hours playtime between **2023-01-17** and **2025-05-27**


### playtime per genre (top 30)

    441,140.4h 25.97% Serie
    279,980.6h 16.49% Magazin
    205,238.2h 12.08% Dokumentation
    154,750.6h 9.11%  Werbung
    154,423.4h 9.09%  Show
    119,780.9h 7.05%  Spielfilm
    116,399.4h 6.85%  Nachrichten
    88,510.1h  5.21%  Sport
    35,011.2h  2.06%  Reportage
    29,088.4h  1.71%  Musik
    13,453.9h  0.79%  Verschiedenes
    13,246.3h  0.78%  Wetter
    11,167.4h  0.66%  Programmende
    9,515.0h   0.56%  E-Sport
    6,234.8h   0.37%  Bericht
    5,443.7h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,824.5h   0.17%  Videoclip
    2,116.7h   0.12%  Kurzfilm
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
