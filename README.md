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

**97** channels, **538,091.2** hours playtime between **2023-01-17** and **2023-11-12**


### playtime per genre (top 30)

    35420.6h 6.58% Nachrichten
    25723.3h 4.78% Verkaufsshow
    21667.7h 4.03% Krimiserie
    18240.0h 3.39% Werbesendung
    17604.8h 3.27% Dokureihe
    16325.4h 3.03% Dokusoap
    15533.6h 2.89% Regionalmagazin
    13706.2h 2.55% Dokumentation
    13056.0h 2.43% *unknown*
    9990.4h  1.86% Zeichentrickserie
    9800.7h  1.82% Infomercial
    9617.2h  1.79% Animationsserie
    8471.7h  1.57% Comedyserie
    7652.0h  1.42% Morgenmagazin
    7247.2h  1.35% Religionsmagazin
    7182.7h  1.33% Talkshow
    6818.9h  1.27% Magazin
    5456.4h  1.01% Programmende
    5286.6h  0.98% E-Sport
    5150.3h  0.96% Sitcom
    4964.1h  0.92% Wetterbericht
    4871.0h  0.91% Börsenmagazin
    4490.6h  0.83% Quiz
    4211.9h  0.78% Komödie
    4069.6h  0.76% Wissensmagazin
    4048.2h  0.75% Wirtschaftsmagazin
    3990.9h  0.74% Musikmagazin
    3878.5h  0.72% Telenovela
    3726.0h  0.69% Politikmagazin
    3673.1h  0.68% Realityshow
