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

**109** channels, **1,065,391.4** hours playtime between **2023-01-17** and **2024-09-27**


### playtime per genre (top 30)

    69335.1h 6.51% Nachrichten
    49338.9h 4.63% Verkaufsshow
    44040.7h 4.13% Krimiserie
    38741.6h 3.64% Werbesendung
    33381.5h 3.13% Dokureihe
    32006.7h 3.00% Dokusoap
    31148.7h 2.92% Regionalmagazin
    27872.4h 2.62% Dokumentation
    25537.8h 2.40% *unknown*
    19779.2h 1.86% Zeichentrickserie
    19565.8h 1.84% Infomercial
    19087.3h 1.79% Animationsserie
    15543.8h 1.46% Comedyserie
    14933.3h 1.40% Morgenmagazin
    14494.6h 1.36% Religionsmagazin
    14044.7h 1.32% Talkshow
    13786.4h 1.29% Magazin
    10540.3h 0.99% E-Sport
    10232.9h 0.96% Sitcom
    9652.4h  0.91% Wetterbericht
    9513.0h  0.89% Programmende
    9318.1h  0.87% Komödie
    9289.8h  0.87% Quiz
    8317.9h  0.78% Börsenmagazin
    8017.1h  0.75% Politikmagazin
    8007.3h  0.75% Realityshow
    8002.1h  0.75% Wissensmagazin
    7221.1h  0.68% Wirtschaftsmagazin
    7029.6h  0.66% Telenovela
    6957.2h  0.65% Dramaserie
