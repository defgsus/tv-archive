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

**97** channels, **529,111.2** hours playtime between **2023-01-17** and **2023-11-07**


### playtime per genre (top 30)

    34815.4h 6.58% Nachrichten
    25272.2h 4.78% Verkaufsshow
    21255.0h 4.02% Krimiserie
    17935.4h 3.39% Werbesendung
    17351.6h 3.28% Dokureihe
    16082.5h 3.04% Dokusoap
    15258.8h 2.88% Regionalmagazin
    13506.2h 2.55% Dokumentation
    12794.3h 2.42% *unknown*
    9847.6h  1.86% Zeichentrickserie
    9631.1h  1.82% Infomercial
    9457.0h  1.79% Animationsserie
    8341.7h  1.58% Comedyserie
    7509.5h  1.42% Morgenmagazin
    7139.7h  1.35% Religionsmagazin
    7057.6h  1.33% Talkshow
    6691.7h  1.26% Magazin
    5389.1h  1.02% Programmende
    5193.1h  0.98% E-Sport
    5057.4h  0.96% Sitcom
    4892.6h  0.92% Wetterbericht
    4781.0h  0.90% Börsenmagazin
    4421.0h  0.84% Quiz
    4143.8h  0.78% Komödie
    3998.4h  0.76% Wissensmagazin
    3979.4h  0.75% Wirtschaftsmagazin
    3937.9h  0.74% Musikmagazin
    3798.1h  0.72% Telenovela
    3647.9h  0.69% Politikmagazin
    3576.0h  0.68% Realityshow
