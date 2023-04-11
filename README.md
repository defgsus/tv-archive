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

**96** channels, **153,791.4** hours playtime between **2023-01-17** and **2023-04-12**


### playtime per genre (top 30)

    10557.8h 6.86% Nachrichten
    7618.8h  4.95% Verkaufsshow
    6318.3h  4.11% Krimiserie
    5150.2h  3.35% Werbesendung
    4934.6h  3.21% Dokureihe
    4662.4h  3.03% Dokusoap
    4451.1h  2.89% Regionalmagazin
    3907.9h  2.54% Dokumentation
    3622.8h  2.36% *unknown*
    2865.8h  1.86% Animationsserie
    2818.8h  1.83% Zeichentrickserie
    2791.9h  1.82% Infomercial
    2511.0h  1.63% Comedyserie
    2134.3h  1.39% Morgenmagazin
    2118.9h  1.38% Programmende
    2008.4h  1.31% Religionsmagazin
    1982.1h  1.29% Talkshow
    1640.2h  1.07% Magazin
    1584.8h  1.03% E-Sport
    1446.5h  0.94% Sitcom
    1416.8h  0.92% Börsenmagazin
    1383.3h  0.90% Wetterbericht
    1240.0h  0.81% Wirtschaftsmagazin
    1197.1h  0.78% Wissensmagazin
    1165.9h  0.76% Musikmagazin
    1155.4h  0.75% Quiz
    1070.5h  0.70% Dramaserie
    1057.9h  0.69% Gesundheitsmagazin
    1055.1h  0.69% Telenovela
    1053.4h  0.68% Sportmagazin
