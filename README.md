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

**197** channels, **3,124,997*** programs, **2,091,030.0** hours playtime between **2023-01-17** and **2025-08-26**


### playtime per genre (top 30)

    552,475.4h 26.42% Serie
    325,327.3h 15.56% Magazin
    257,659.1h 12.32% Dokumentation
    183,508.5h 8.78%  Show
    178,297.5h 8.53%  Werbung
    163,812.1h 7.83%  Spielfilm
    130,903.8h 6.26%  Nachrichten
    127,727.2h 6.11%  Sport
    42,209.1h  2.02%  Musik
    42,126.6h  2.01%  Reportage
    20,609.4h  0.99%  Verschiedenes
    15,055.3h  0.72%  Wetter
    11,167.4h  0.53%  Programmende
    9,515.0h   0.46%  E-Sport
    6,782.0h   0.32%  Bericht
    6,093.4h   0.29%  Event
    3,874.8h   0.19%  Videoclip
    3,837.7h   0.18%  Kurzfilm
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
