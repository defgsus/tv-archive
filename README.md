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

**96** channels, **77,471.1** hours playtime between **2023-01-17** and **2023-02-28**


### playtime per genre (top 30)

    5476.5h 7.07% Nachrichten
    3901.3h 5.04% Verkaufsshow
    3265.2h 4.21% Krimiserie
    2635.7h 3.40% Werbesendung
    2554.6h 3.30% Dokusoap
    2314.5h 2.99% Dokureihe
    2263.6h 2.92% Regionalmagazin
    1908.7h 2.46% Dokumentation
    1860.1h 2.40% *unknown*
    1463.0h 1.89% Animationsserie
    1427.6h 1.84% Zeichentrickserie
    1417.2h 1.83% Infomercial
    1258.7h 1.62% Comedyserie
    1093.8h 1.41% Morgenmagazin
    1045.6h 1.35% Programmende
    1021.0h 1.32% Religionsmagazin
    1013.6h 1.31% Talkshow
    831.4h  1.07% Magazin
    810.8h  1.05% E-Sport
    724.1h  0.93% Sitcom
    688.5h  0.89% Börsenmagazin
    681.4h  0.88% Wetterbericht
    626.8h  0.81% Wirtschaftsmagazin
    608.9h  0.79% Wissensmagazin
    587.1h  0.76% Quiz
    564.9h  0.73% Musikmagazin
    559.9h  0.72% Dramaserie
    545.8h  0.70% Gesundheitsmagazin
    525.9h  0.68% Telenovela
    499.4h  0.64% Sportmagazin
