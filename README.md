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

**96** channels, **204,832.9** hours playtime between **2023-01-17** and **2023-05-10**


### playtime per genre (top 30)

    13831.3h 6.75% Nachrichten
    10001.6h 4.88% Verkaufsshow
    8343.2h  4.07% Krimiserie
    6812.3h  3.33% Werbesendung
    6628.8h  3.24% Dokureihe
    6084.5h  2.97% Dokusoap
    5890.3h  2.88% Regionalmagazin
    5207.6h  2.54% Dokumentation
    5029.1h  2.46% *unknown*
    3803.6h  1.86% Zeichentrickserie
    3751.8h  1.83% Infomercial
    3716.2h  1.81% Animationsserie
    3408.1h  1.66% Comedyserie
    2831.2h  1.38% Morgenmagazin
    2815.0h  1.37% Programmende
    2694.7h  1.32% Talkshow
    2684.9h  1.31% Religionsmagazin
    2287.0h  1.12% Magazin
    2070.8h  1.01% E-Sport
    1931.9h  0.94% Sitcom
    1868.0h  0.91% Börsenmagazin
    1851.7h  0.90% Wetterbericht
    1619.7h  0.79% Wirtschaftsmagazin
    1598.9h  0.78% Wissensmagazin
    1584.8h  0.77% Musikmagazin
    1566.0h  0.76% Quiz
    1445.4h  0.71% Telenovela
    1432.7h  0.70% Sportmagazin
    1408.2h  0.69% Gesundheitsmagazin
    1398.4h  0.68% Dramaserie
