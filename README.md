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

**96** channels, **137,321.9** hours playtime between **2023-01-17** and **2023-04-03**


### playtime per genre (top 30)

    9570.6h 6.97% Nachrichten
    6840.4h 4.98% Verkaufsshow
    5721.7h 4.17% Krimiserie
    4639.7h 3.38% Werbesendung
    4335.8h 3.16% Dokureihe
    4217.7h 3.07% Dokusoap
    4017.8h 2.93% Regionalmagazin
    3411.3h 2.48% Dokumentation
    3135.1h 2.28% *unknown*
    2592.8h 1.89% Animationsserie
    2531.6h 1.84% Infomercial
    2515.2h 1.83% Zeichentrickserie
    2250.7h 1.64% Comedyserie
    1942.6h 1.41% Morgenmagazin
    1917.2h 1.40% Programmende
    1831.9h 1.33% Talkshow
    1796.0h 1.31% Religionsmagazin
    1458.2h 1.06% Magazin
    1419.8h 1.03% E-Sport
    1309.2h 0.95% Sitcom
    1288.7h 0.94% Börsenmagazin
    1226.1h 0.89% Wetterbericht
    1113.3h 0.81% Wirtschaftsmagazin
    1078.8h 0.79% Wissensmagazin
    1042.8h 0.76% Musikmagazin
    1034.3h 0.75% Quiz
    973.6h  0.71% Dramaserie
    954.1h  0.69% Telenovela
    951.0h  0.69% Sportmagazin
    942.7h  0.69% Gesundheitsmagazin
