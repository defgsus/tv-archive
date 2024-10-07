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

**109** channels, **1,079,877.6** hours playtime between **2023-01-17** and **2024-10-08**


### playtime per genre (top 30)

    70251.6h 6.51% Nachrichten
    49914.2h 4.62% Verkaufsshow
    44679.2h 4.14% Krimiserie
    39360.0h 3.64% Werbesendung
    33822.6h 3.13% Dokureihe
    32377.8h 3.00% Dokusoap
    31529.8h 2.92% Regionalmagazin
    28270.8h 2.62% Dokumentation
    25819.1h 2.39% *unknown*
    20081.3h 1.86% Zeichentrickserie
    19843.0h 1.84% Infomercial
    19343.0h 1.79% Animationsserie
    15692.7h 1.45% Comedyserie
    15103.8h 1.40% Morgenmagazin
    14662.1h 1.36% Religionsmagazin
    14250.4h 1.32% Talkshow
    13876.7h 1.29% Magazin
    10678.4h 0.99% E-Sport
    10383.6h 0.96% Sitcom
    9772.6h  0.90% Wetterbericht
    9623.1h  0.89% Programmende
    9472.5h  0.88% Komödie
    9436.0h  0.87% Quiz
    8351.4h  0.77% Börsenmagazin
    8129.7h  0.75% Realityshow
    8117.9h  0.75% Politikmagazin
    8112.4h  0.75% Wissensmagazin
    7290.0h  0.68% Wirtschaftsmagazin
    7104.1h  0.66% Telenovela
    7045.7h  0.65% Dramaserie
