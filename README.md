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

**96** channels, **140,970.9** hours playtime between **2023-01-17** and **2023-04-05**


### playtime per genre (top 30)

    9823.6h 6.97% Nachrichten
    7015.8h 4.98% Verkaufsshow
    5879.9h 4.17% Krimiserie
    4753.9h 3.37% Werbesendung
    4468.2h 3.17% Dokureihe
    4316.3h 3.06% Dokusoap
    4143.7h 2.94% Regionalmagazin
    3499.7h 2.48% Dokumentation
    3262.3h 2.31% *unknown*
    2658.1h 1.89% Animationsserie
    2600.9h 1.84% Infomercial
    2585.6h 1.83% Zeichentrickserie
    2316.1h 1.64% Comedyserie
    2008.2h 1.42% Morgenmagazin
    1944.0h 1.38% Programmende
    1867.0h 1.32% Talkshow
    1841.2h 1.31% Religionsmagazin
    1501.3h 1.06% Magazin
    1449.9h 1.03% E-Sport
    1346.3h 0.96% Sitcom
    1332.0h 0.94% Börsenmagazin
    1262.1h 0.90% Wetterbericht
    1151.3h 0.82% Wirtschaftsmagazin
    1106.7h 0.79% Wissensmagazin
    1073.7h 0.76% Quiz
    1068.6h 0.76% Musikmagazin
    997.5h  0.71% Dramaserie
    992.9h  0.70% Telenovela
    974.3h  0.69% Sportmagazin
    972.2h  0.69% Gesundheitsmagazin
