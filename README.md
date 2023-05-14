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

**96** channels, **213,893.2** hours playtime between **2023-01-17** and **2023-05-15**


### playtime per genre (top 30)

    14397.9h 6.73% Nachrichten
    10403.7h 4.86% Verkaufsshow
    8699.0h  4.07% Krimiserie
    7109.8h  3.32% Werbesendung
    6943.2h  3.25% Dokureihe
    6319.9h  2.95% Dokusoap
    6142.4h  2.87% Regionalmagazin
    5449.1h  2.55% Dokumentation
    5290.5h  2.47% *unknown*
    3976.6h  1.86% Zeichentrickserie
    3922.8h  1.83% Infomercial
    3865.9h  1.81% Animationsserie
    3552.8h  1.66% Comedyserie
    2961.6h  1.38% Programmende
    2948.7h  1.38% Morgenmagazin
    2830.1h  1.32% Talkshow
    2809.2h  1.31% Religionsmagazin
    2428.4h  1.14% Magazin
    2155.8h  1.01% E-Sport
    2020.0h  0.94% Sitcom
    1938.6h  0.91% Börsenmagazin
    1933.6h  0.90% Wetterbericht
    1687.0h  0.79% Wirtschaftsmagazin
    1673.3h  0.78% Wissensmagazin
    1653.6h  0.77% Musikmagazin
    1629.4h  0.76% Quiz
    1498.8h  0.70% Telenovela
    1493.2h  0.70% Sportmagazin
    1481.2h  0.69% Komödie
    1453.4h  0.68% Gesundheitsmagazin
