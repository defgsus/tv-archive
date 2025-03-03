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

**195** channels, **2,069,715*** programs, **1,332,443.4** hours playtime between **2023-01-17** and **2025-03-03**


### playtime per genre (top 30)

    338,451.0h 25.40% Serie
    237,279.4h 17.81% Magazin
    157,341.8h 11.81% Dokumentation
    131,921.5h 9.90%  Werbung
    126,168.3h 9.47%  Show
    102,359.4h 7.68%  Nachrichten
    79,615.3h  5.98%  Spielfilm
    51,723.2h  3.88%  Sport
    28,637.1h  2.15%  Reportage
    16,536.1h  1.24%  Musik
    11,722.0h  0.88%  Wetter
    11,167.4h  0.84%  Programmende
    9,515.0h   0.71%  E-Sport
    7,094.4h   0.53%  Verschiedenes
    5,596.1h   0.42%  Bericht
    4,768.9h   0.36%  Event
    3,541.9h   0.27%  *unknown*
    2,045.6h   0.15%  Verkaufsshow
    1,996.8h   0.15%  Videoclip
    504.5h     0.04%  Kurzfilm
    353.9h     0.03%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.02%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
