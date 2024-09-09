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

**109** channels, **1,037,841.9** hours playtime between **2023-01-17** and **2024-09-10**


### playtime per genre (top 30)

    67502.4h 6.50% Nachrichten
    48223.4h 4.65% Verkaufsshow
    42752.2h 4.12% Krimiserie
    37581.4h 3.62% Werbesendung
    32613.0h 3.14% Dokureihe
    31271.1h 3.01% Dokusoap
    30274.6h 2.92% Regionalmagazin
    27145.6h 2.62% Dokumentation
    25052.1h 2.41% *unknown*
    19258.8h 1.86% Zeichentrickserie
    19030.2h 1.83% Infomercial
    18593.5h 1.79% Animationsserie
    15179.8h 1.46% Comedyserie
    14522.0h 1.40% Morgenmagazin
    14114.8h 1.36% Religionsmagazin
    13630.5h 1.31% Talkshow
    13613.8h 1.31% Magazin
    10248.2h 0.99% E-Sport
    9927.7h  0.96% Sitcom
    9389.1h  0.90% Wetterbericht
    9304.7h  0.90% Programmende
    9123.4h  0.88% Komödie
    8975.4h  0.86% Quiz
    8222.1h  0.79% Börsenmagazin
    7769.1h  0.75% Wissensmagazin
    7755.9h  0.75% Politikmagazin
    7725.6h  0.74% Realityshow
    7058.1h  0.68% Wirtschaftsmagazin
    6822.7h  0.66% Telenovela
    6750.4h  0.65% Dramaserie
