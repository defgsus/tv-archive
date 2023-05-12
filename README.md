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

**96** channels, **210,261.1** hours playtime between **2023-01-17** and **2023-05-13**


### playtime per genre (top 30)

    14224.8h 6.77% Nachrichten
    10249.6h 4.87% Verkaufsshow
    8565.8h  4.07% Krimiserie
    6977.9h  3.32% Werbesendung
    6788.6h  3.23% Dokureihe
    6247.5h  2.97% Dokusoap
    6087.0h  2.89% Regionalmagazin
    5336.1h  2.54% Dokumentation
    5189.6h  2.47% *unknown*
    3902.9h  1.86% Zeichentrickserie
    3853.9h  1.83% Infomercial
    3801.5h  1.81% Animationsserie
    3517.5h  1.67% Comedyserie
    2934.4h  1.40% Morgenmagazin
    2895.3h  1.38% Programmende
    2769.3h  1.32% Talkshow
    2742.1h  1.30% Religionsmagazin
    2382.9h  1.13% Magazin
    2124.3h  1.01% E-Sport
    1991.9h  0.95% Sitcom
    1919.7h  0.91% Börsenmagazin
    1905.1h  0.91% Wetterbericht
    1670.9h  0.79% Wirtschaftsmagazin
    1645.0h  0.78% Wissensmagazin
    1624.7h  0.77% Musikmagazin
    1620.9h  0.77% Quiz
    1496.8h  0.71% Telenovela
    1459.7h  0.69% Sportmagazin
    1437.2h  0.68% Gesundheitsmagazin
    1426.8h  0.68% Dramaserie
