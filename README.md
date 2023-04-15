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

**96** channels, **161,120.6** hours playtime between **2023-01-17** and **2023-04-16**


### playtime per genre (top 30)

    11040.0h 6.85% Nachrichten
    7972.0h  4.95% Verkaufsshow
    6633.7h  4.12% Krimiserie
    5400.6h  3.35% Werbesendung
    5202.8h  3.23% Dokureihe
    4832.3h  3.00% Dokusoap
    4670.9h  2.90% Regionalmagazin
    4066.5h  2.52% Dokumentation
    3789.6h  2.35% *unknown*
    2991.1h  1.86% Animationsserie
    2955.3h  1.83% Zeichentrickserie
    2934.9h  1.82% Infomercial
    2636.9h  1.64% Comedyserie
    2238.8h  1.39% Morgenmagazin
    2233.5h  1.39% Programmende
    2092.4h  1.30% Religionsmagazin
    2065.1h  1.28% Talkshow
    1733.8h  1.08% Magazin
    1648.2h  1.02% E-Sport
    1525.3h  0.95% Sitcom
    1485.8h  0.92% Börsenmagazin
    1452.7h  0.90% Wetterbericht
    1293.8h  0.80% Wirtschaftsmagazin
    1256.6h  0.78% Wissensmagazin
    1226.0h  0.76% Musikmagazin
    1214.4h  0.75% Quiz
    1114.2h  0.69% Telenovela
    1114.1h  0.69% Gesundheitsmagazin
    1107.1h  0.69% Dramaserie
    1101.8h  0.68% Sportmagazin
