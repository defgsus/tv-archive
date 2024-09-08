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

**109** channels, **1,036,055.1** hours playtime between **2023-01-17** and **2024-09-09**


### playtime per genre (top 30)

    67366.4h 6.50% Nachrichten
    48146.4h 4.65% Verkaufsshow
    42673.7h 4.12% Krimiserie
    37507.7h 3.62% Werbesendung
    32585.9h 3.15% Dokureihe
    31225.2h 3.01% Dokusoap
    30203.8h 2.92% Regionalmagazin
    27086.7h 2.61% Dokumentation
    25046.8h 2.42% *unknown*
    19223.7h 1.86% Zeichentrickserie
    18998.2h 1.83% Infomercial
    18561.0h 1.79% Animationsserie
    15151.2h 1.46% Comedyserie
    14492.1h 1.40% Morgenmagazin
    14091.4h 1.36% Religionsmagazin
    13616.6h 1.31% Talkshow
    13606.8h 1.31% Magazin
    10229.5h 0.99% E-Sport
    9901.1h  0.96% Sitcom
    9370.3h  0.90% Wetterbericht
    9291.2h  0.90% Programmende
    9116.6h  0.88% Komödie
    8942.5h  0.86% Quiz
    8213.5h  0.79% Börsenmagazin
    7761.4h  0.75% Wissensmagazin
    7735.1h  0.75% Politikmagazin
    7710.6h  0.74% Realityshow
    7045.0h  0.68% Wirtschaftsmagazin
    6805.7h  0.66% Telenovela
    6735.9h  0.65% Dramaserie
