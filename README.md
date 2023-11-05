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

**97** channels, **527,306.1** hours playtime between **2023-01-17** and **2023-11-06**


### playtime per genre (top 30)

    34684.1h 6.58% Nachrichten
    25174.2h 4.77% Verkaufsshow
    21187.0h 4.02% Krimiserie
    17872.2h 3.39% Werbesendung
    17320.0h 3.28% Dokureihe
    16024.5h 3.04% Dokusoap
    15189.5h 2.88% Regionalmagazin
    13453.8h 2.55% Dokumentation
    12739.8h 2.42% *unknown*
    9819.4h  1.86% Zeichentrickserie
    9600.4h  1.82% Infomercial
    9424.3h  1.79% Animationsserie
    8309.6h  1.58% Comedyserie
    7474.8h  1.42% Morgenmagazin
    7119.6h  1.35% Religionsmagazin
    7035.7h  1.33% Talkshow
    6666.4h  1.26% Magazin
    5373.7h  1.02% Programmende
    5175.3h  0.98% E-Sport
    5030.2h  0.95% Sitcom
    4876.5h  0.92% Wetterbericht
    4768.0h  0.90% Börsenmagazin
    4395.8h  0.83% Quiz
    4141.4h  0.79% Komödie
    3984.9h  0.76% Wissensmagazin
    3964.4h  0.75% Wirtschaftsmagazin
    3932.3h  0.75% Musikmagazin
    3779.4h  0.72% Telenovela
    3626.9h  0.69% Politikmagazin
    3558.3h  0.67% Realityshow
