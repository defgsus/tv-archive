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

**96** channels, **219,237.3** hours playtime between **2023-01-17** and **2023-05-18**


### playtime per genre (top 30)

    14797.9h 6.75% Nachrichten
    10635.8h 4.85% Verkaufsshow
    8908.5h  4.06% Krimiserie
    7283.6h  3.32% Werbesendung
    7127.9h  3.25% Dokureihe
    6481.8h  2.96% Dokusoap
    6331.2h  2.89% Regionalmagazin
    5557.9h  2.54% Dokumentation
    5412.1h  2.47% *unknown*
    4081.5h  1.86% Zeichentrickserie
    4022.3h  1.83% Infomercial
    3952.8h  1.80% Animationsserie
    3669.4h  1.67% Comedyserie
    3051.9h  1.39% Morgenmagazin
    3003.8h  1.37% Programmende
    2898.9h  1.32% Talkshow
    2864.3h  1.31% Religionsmagazin
    2519.1h  1.15% Magazin
    2200.2h  1.00% E-Sport
    2076.2h  0.95% Sitcom
    2001.0h  0.91% Börsenmagazin
    1986.6h  0.91% Wetterbericht
    1736.9h  0.79% Wirtschaftsmagazin
    1719.2h  0.78% Wissensmagazin
    1691.8h  0.77% Musikmagazin
    1688.8h  0.77% Quiz
    1559.8h  0.71% Telenovela
    1525.8h  0.70% Sportmagazin
    1494.8h  0.68% Komödie
    1489.9h  0.68% Gesundheitsmagazin
