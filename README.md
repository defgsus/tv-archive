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

**99** channels, **730,608.2** hours playtime between **2023-01-17** and **2024-02-29**


### playtime per genre (top 30)

    47568.8h 6.51% Nachrichten
    35077.3h 4.80% Verkaufsshow
    29685.0h 4.06% Krimiserie
    25248.7h 3.46% Werbesendung
    23396.0h 3.20% Dokureihe
    22048.8h 3.02% Dokusoap
    21192.0h 2.90% Regionalmagazin
    18824.5h 2.58% Dokumentation
    18655.6h 2.55% *unknown*
    13536.5h 1.85% Zeichentrickserie
    13281.6h 1.82% Infomercial
    12861.2h 1.76% Animationsserie
    11070.2h 1.52% Comedyserie
    10363.6h 1.42% Morgenmagazin
    9875.1h  1.35% Religionsmagazin
    9820.0h  1.34% Magazin
    9703.4h  1.33% Talkshow
    7220.9h  0.99% E-Sport
    6945.1h  0.95% Programmende
    6909.4h  0.95% Sitcom
    6522.7h  0.89% Börsenmagazin
    6497.4h  0.89% Wetterbericht
    6180.9h  0.85% Komödie
    6149.3h  0.84% Quiz
    5472.6h  0.75% Wissensmagazin
    5333.0h  0.73% Realityshow
    5298.4h  0.73% Wirtschaftsmagazin
    5262.8h  0.72% Politikmagazin
    5215.4h  0.71% Telenovela
    5025.6h  0.69% Musikmagazin
