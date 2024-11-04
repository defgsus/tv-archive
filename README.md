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

**109** channels, **1,123,295.8** hours playtime between **2023-01-17** and **2024-11-05**


### playtime per genre (top 30)

    73152.9h 6.51% Nachrichten
    51590.8h 4.59% Verkaufsshow
    46705.1h 4.16% Krimiserie
    41220.5h 3.67% Werbesendung
    35113.7h 3.13% Dokureihe
    33574.5h 2.99% Dokusoap
    32821.6h 2.92% Regionalmagazin
    29522.7h 2.63% Dokumentation
    26581.5h 2.37% *unknown*
    21000.7h 1.87% Zeichentrickserie
    20684.0h 1.84% Infomercial
    20086.9h 1.79% Animationsserie
    16160.1h 1.44% Comedyserie
    15713.0h 1.40% Morgenmagazin
    15073.7h 1.34% Religionsmagazin
    14862.6h 1.32% Talkshow
    14151.0h 1.26% Magazin
    11094.1h 0.99% E-Sport
    10836.7h 0.96% Sitcom
    10159.9h 0.90% Wetterbericht
    9954.5h  0.89% Programmende
    9896.1h  0.88% Komödie
    9874.5h  0.88% Quiz
    8558.7h  0.76% Realityshow
    8489.6h  0.76% Politikmagazin
    8489.1h  0.76% Börsenmagazin
    8434.8h  0.75% Wissensmagazin
    7541.6h  0.67% Wirtschaftsmagazin
    7404.1h  0.66% Telenovela
    7341.9h  0.65% Dramaserie
