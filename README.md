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

**108** channels, **863,436.4** hours playtime between **2023-01-17** and **2024-05-21**


### playtime per genre (top 30)

    56336.2h 6.52% Nachrichten
    41085.0h 4.76% Verkaufsshow
    35107.2h 4.07% Krimiserie
    30243.1h 3.50% Werbesendung
    27214.4h 3.15% Dokureihe
    26114.8h 3.02% Dokusoap
    25072.8h 2.90% Regionalmagazin
    22417.7h 2.60% Dokumentation
    21934.3h 2.54% *unknown*
    15874.0h 1.84% Zeichentrickserie
    15695.6h 1.82% Infomercial
    15372.7h 1.78% Animationsserie
    12991.8h 1.50% Comedyserie
    12251.3h 1.42% Magazin
    12138.3h 1.41% Morgenmagazin
    11681.0h 1.35% Religionsmagazin
    11489.2h 1.33% Talkshow
    8562.9h  0.99% E-Sport
    7979.0h  0.92% Programmende
    7964.2h  0.92% Sitcom
    7674.9h  0.89% Wetterbericht
    7571.1h  0.88% Börsenmagazin
    7470.7h  0.87% Komödie
    7462.1h  0.86% Quiz
    6380.1h  0.74% Wissensmagazin
    6366.1h  0.74% Realityshow
    6336.1h  0.73% Politikmagazin
    6139.3h  0.71% Wirtschaftsmagazin
    6110.6h  0.71% Telenovela
    5716.4h  0.66% Musikmagazin
