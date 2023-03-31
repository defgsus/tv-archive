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

**96** channels, **133,645.1** hours playtime between **2023-01-17** and **2023-04-01**


### playtime per genre (top 30)

    9410.9h 7.04% Nachrichten
    6682.5h 5.00% Verkaufsshow
    5579.4h 4.17% Krimiserie
    4512.7h 3.38% Werbesendung
    4169.8h 3.12% Dokureihe
    4142.3h 3.10% Dokusoap
    3962.3h 2.96% Regionalmagazin
    3289.4h 2.46% Dokumentation
    3055.5h 2.29% *unknown*
    2536.1h 1.90% Animationsserie
    2462.8h 1.84% Infomercial
    2449.8h 1.83% Zeichentrickserie
    2206.0h 1.65% Comedyserie
    1928.5h 1.44% Morgenmagazin
    1850.2h 1.38% Programmende
    1778.4h 1.33% Talkshow
    1727.9h 1.29% Religionsmagazin
    1405.0h 1.05% Magazin
    1391.7h 1.04% E-Sport
    1281.0h 0.96% Sitcom
    1267.8h 0.95% Börsenmagazin
    1200.2h 0.90% Wetterbericht
    1096.9h 0.82% Wirtschaftsmagazin
    1049.7h 0.79% Wissensmagazin
    1027.0h 0.77% Quiz
    1009.1h 0.76% Musikmagazin
    954.9h  0.71% Dramaserie
    951.8h  0.71% Telenovela
    917.6h  0.69% Gesundheitsmagazin
    904.9h  0.68% Sportmagazin
