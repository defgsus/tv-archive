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

**109** channels, **1,065,346.2** hours playtime between **2023-01-17** and **2024-09-27**


### playtime per genre (top 30)

    69336.1h 6.51% Nachrichten
    49338.9h 4.63% Verkaufsshow
    44038.6h 4.13% Krimiserie
    38741.6h 3.64% Werbesendung
    33381.4h 3.13% Dokureihe
    31999.9h 3.00% Dokusoap
    31147.1h 2.92% Regionalmagazin
    27869.7h 2.62% Dokumentation
    25534.5h 2.40% *unknown*
    19778.6h 1.86% Zeichentrickserie
    19565.8h 1.84% Infomercial
    19087.5h 1.79% Animationsserie
    15545.2h 1.46% Comedyserie
    14927.8h 1.40% Morgenmagazin
    14494.2h 1.36% Religionsmagazin
    14040.8h 1.32% Talkshow
    13786.8h 1.29% Magazin
    10540.3h 0.99% E-Sport
    10232.0h 0.96% Sitcom
    9652.3h  0.91% Wetterbericht
    9513.2h  0.89% Programmende
    9318.1h  0.87% Komödie
    9288.8h  0.87% Quiz
    8317.8h  0.78% Börsenmagazin
    8017.1h  0.75% Politikmagazin
    8006.8h  0.75% Realityshow
    8001.6h  0.75% Wissensmagazin
    7221.1h  0.68% Wirtschaftsmagazin
    7029.6h  0.66% Telenovela
    6954.2h  0.65% Dramaserie
