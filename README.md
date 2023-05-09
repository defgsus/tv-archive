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

**96** channels, **204,785.2** hours playtime between **2023-01-17** and **2023-05-10**


### playtime per genre (top 30)

    13829.6h 6.75% Nachrichten
    10000.1h 4.88% Verkaufsshow
    8346.1h  4.08% Krimiserie
    6811.4h  3.33% Werbesendung
    6626.1h  3.24% Dokureihe
    6084.5h  2.97% Dokusoap
    5886.1h  2.87% Regionalmagazin
    5204.6h  2.54% Dokumentation
    5025.9h  2.45% *unknown*
    3803.5h  1.86% Zeichentrickserie
    3751.3h  1.83% Infomercial
    3717.1h  1.82% Animationsserie
    3405.7h  1.66% Comedyserie
    2829.2h  1.38% Morgenmagazin
    2815.1h  1.37% Programmende
    2694.7h  1.32% Talkshow
    2683.0h  1.31% Religionsmagazin
    2285.2h  1.12% Magazin
    2070.8h  1.01% E-Sport
    1931.9h  0.94% Sitcom
    1869.2h  0.91% Börsenmagazin
    1851.9h  0.90% Wetterbericht
    1619.7h  0.79% Wirtschaftsmagazin
    1597.9h  0.78% Wissensmagazin
    1584.8h  0.77% Musikmagazin
    1564.7h  0.76% Quiz
    1445.4h  0.71% Telenovela
    1432.0h  0.70% Sportmagazin
    1404.7h  0.69% Gesundheitsmagazin
    1398.4h  0.68% Dramaserie
