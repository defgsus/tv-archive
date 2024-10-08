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

**109** channels, **1,085,276.1** hours playtime between **2023-01-17** and **2024-10-11**


### playtime per genre (top 30)

    70664.6h 6.51% Nachrichten
    50134.6h 4.62% Verkaufsshow
    44966.0h 4.14% Krimiserie
    39589.8h 3.65% Werbesendung
    33962.5h 3.13% Dokureihe
    32514.0h 3.00% Dokusoap
    31734.7h 2.92% Regionalmagazin
    28401.6h 2.62% Dokumentation
    25897.8h 2.39% *unknown*
    20192.7h 1.86% Zeichentrickserie
    19947.7h 1.84% Infomercial
    19433.4h 1.79% Animationsserie
    15762.5h 1.45% Comedyserie
    15198.5h 1.40% Morgenmagazin
    14700.4h 1.35% Religionsmagazin
    14320.3h 1.32% Talkshow
    13903.2h 1.28% Magazin
    10726.6h 0.99% E-Sport
    10450.2h 0.96% Sitcom
    9827.3h  0.91% Wetterbericht
    9663.8h  0.89% Programmende
    9508.0h  0.88% Quiz
    9503.1h  0.88% Komödie
    8377.9h  0.77% Börsenmagazin
    8219.8h  0.76% Realityshow
    8189.4h  0.75% Politikmagazin
    8153.6h  0.75% Wissensmagazin
    7330.8h  0.68% Wirtschaftsmagazin
    7155.1h  0.66% Telenovela
    7100.4h  0.65% Dramaserie
