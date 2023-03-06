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

**96** channels, **90,215.2** hours playtime between **2023-01-17** and **2023-03-07**


### playtime per genre (top 30)

    6352.5h 7.04% Nachrichten
    4536.2h 5.03% Verkaufsshow
    3792.8h 4.20% Krimiserie
    3062.0h 3.39% Werbesendung
    2952.7h 3.27% Dokusoap
    2717.4h 3.01% Dokureihe
    2636.8h 2.92% Regionalmagazin
    2209.3h 2.45% Dokumentation
    2199.7h 2.44% *unknown*
    1719.7h 1.91% Animationsserie
    1650.8h 1.83% Infomercial
    1637.4h 1.81% Zeichentrickserie
    1454.0h 1.61% Comedyserie
    1266.0h 1.40% Morgenmagazin
    1227.4h 1.36% Programmende
    1188.8h 1.32% Religionsmagazin
    1178.2h 1.31% Talkshow
    942.8h  1.05% Magazin
    934.8h  1.04% E-Sport
    850.1h  0.94% Sitcom
    817.5h  0.91% Börsenmagazin
    792.1h  0.88% Wetterbericht
    731.6h  0.81% Wirtschaftsmagazin
    710.1h  0.79% Wissensmagazin
    675.5h  0.75% Quiz
    662.2h  0.73% Musikmagazin
    647.8h  0.72% Dramaserie
    635.5h  0.70% Gesundheitsmagazin
    611.2h  0.68% Telenovela
    585.9h  0.65% Sportmagazin
