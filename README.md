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

**96** channels, **219,236.6** hours playtime between **2023-01-17** and **2023-05-18**


### playtime per genre (top 30)

    14798.2h 6.75% Nachrichten
    10639.0h 4.85% Verkaufsshow
    8908.3h  4.06% Krimiserie
    7280.6h  3.32% Werbesendung
    7128.2h  3.25% Dokureihe
    6481.7h  2.96% Dokusoap
    6331.1h  2.89% Regionalmagazin
    5557.6h  2.53% Dokumentation
    5412.5h  2.47% *unknown*
    4081.4h  1.86% Zeichentrickserie
    4022.3h  1.83% Infomercial
    3953.1h  1.80% Animationsserie
    3669.8h  1.67% Comedyserie
    3051.9h  1.39% Morgenmagazin
    3003.8h  1.37% Programmende
    2898.9h  1.32% Talkshow
    2864.3h  1.31% Religionsmagazin
    2519.4h  1.15% Magazin
    2200.2h  1.00% E-Sport
    2076.2h  0.95% Sitcom
    2001.4h  0.91% Börsenmagazin
    1986.8h  0.91% Wetterbericht
    1736.9h  0.79% Wirtschaftsmagazin
    1719.1h  0.78% Wissensmagazin
    1691.8h  0.77% Musikmagazin
    1688.8h  0.77% Quiz
    1559.8h  0.71% Telenovela
    1524.0h  0.70% Sportmagazin
    1494.8h  0.68% Komödie
    1489.9h  0.68% Gesundheitsmagazin
