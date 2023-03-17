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

**96** channels, **110,098.2** hours playtime between **2023-01-17** and **2023-03-18**


### playtime per genre (top 30)

    7788.1h 7.07% Nachrichten
    5532.2h 5.02% Verkaufsshow
    4627.4h 4.20% Krimiserie
    3721.9h 3.38% Werbesendung
    3533.3h 3.21% Dokusoap
    3319.0h 3.01% Dokureihe
    3269.3h 2.97% Regionalmagazin
    2682.8h 2.44% Dokumentation
    2603.1h 2.36% *unknown*
    2104.7h 1.91% Animationsserie
    2021.2h 1.84% Infomercial
    1983.7h 1.80% Zeichentrickserie
    1808.9h 1.64% Comedyserie
    1589.8h 1.44% Morgenmagazin
    1501.6h 1.36% Programmende
    1467.8h 1.33% Talkshow
    1432.3h 1.30% Religionsmagazin
    1148.4h 1.04% Magazin
    1135.7h 1.03% E-Sport
    1053.0h 0.96% Sitcom
    1024.7h 0.93% Börsenmagazin
    979.1h  0.89% Wetterbericht
    907.1h  0.82% Wirtschaftsmagazin
    866.5h  0.79% Wissensmagazin
    832.7h  0.76% Quiz
    815.8h  0.74% Musikmagazin
    799.9h  0.73% Dramaserie
    779.8h  0.71% Telenovela
    761.7h  0.69% Gesundheitsmagazin
    712.2h  0.65% Gerichtsshow
