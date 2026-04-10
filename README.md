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

**198** channels, **4,460,958*** programs, **3,055,059.4** hours playtime between **2023-01-17** and **2026-04-10**


### playtime per genre (top 30)

    824,402.6h 26.98% Serie
    439,247.0h 14.38% Magazin
    389,868.4h 12.76% Dokumentation
    275,090.4h 9.00%  Spielfilm
    255,772.9h 8.37%  Show
    234,663.4h 7.68%  Werbung
    224,270.6h 7.34%  Sport
    168,722.9h 5.52%  Nachrichten
    67,986.7h  2.23%  Musik
    59,277.0h  1.94%  Reportage
    35,457.3h  1.16%  Verschiedenes
    19,484.8h  0.64%  Wetter
    11,167.4h  0.37%  Programmende
    9,515.0h   0.31%  E-Sport
    8,729.1h   0.29%  Bericht
    7,886.2h   0.26%  Event
    7,008.4h   0.23%  Kurzfilm
    6,440.9h   0.21%  Videoclip
    3,541.9h   0.12%  *unknown*
    2,045.6h   0.07%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
