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

**109** channels, **1,074,472.8** hours playtime between **2023-01-17** and **2024-10-04**


### playtime per genre (top 30)

    69907.9h 6.51% Nachrichten
    49692.3h 4.62% Verkaufsshow
    44437.2h 4.14% Krimiserie
    39125.7h 3.64% Werbesendung
    33666.8h 3.13% Dokureihe
    32238.4h 3.00% Dokusoap
    31389.4h 2.92% Regionalmagazin
    28127.8h 2.62% Dokumentation
    25727.0h 2.39% *unknown*
    19970.2h 1.86% Zeichentrickserie
    19727.1h 1.84% Infomercial
    19239.6h 1.79% Animationsserie
    15626.3h 1.45% Comedyserie
    15027.6h 1.40% Morgenmagazin
    14597.4h 1.36% Religionsmagazin
    14168.5h 1.32% Talkshow
    13837.5h 1.29% Magazin
    10623.9h 0.99% E-Sport
    10321.7h 0.96% Sitcom
    9732.9h  0.91% Wetterbericht
    9582.1h  0.89% Programmende
    9426.1h  0.88% Komödie
    9380.5h  0.87% Quiz
    8339.6h  0.78% Börsenmagazin
    8090.5h  0.75% Politikmagazin
    8079.9h  0.75% Realityshow
    8073.6h  0.75% Wissensmagazin
    7270.3h  0.68% Wirtschaftsmagazin
    7074.7h  0.66% Telenovela
    7009.5h  0.65% Dramaserie
