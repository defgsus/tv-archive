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

**109** channels, **1,187,516.8** hours playtime between **2023-01-17** and **2024-12-18**


### playtime per genre (top 30)

    77685.3h 6.54% Nachrichten
    53984.0h 4.55% Verkaufsshow
    49520.9h 4.17% Krimiserie
    43842.2h 3.69% Werbesendung
    36946.5h 3.11% Dokureihe
    35131.6h 2.96% Dokusoap
    34769.5h 2.93% Regionalmagazin
    31353.3h 2.64% Dokumentation
    28069.5h 2.36% *unknown*
    22266.0h 1.88% Zeichentrickserie
    21993.2h 1.85% Infomercial
    21239.0h 1.79% Animationsserie
    16838.3h 1.42% Comedyserie
    16648.2h 1.40% Morgenmagazin
    15765.1h 1.33% Talkshow
    15679.7h 1.32% Religionsmagazin
    14642.3h 1.23% Magazin
    11753.3h 0.99% E-Sport
    11426.0h 0.96% Sitcom
    10739.8h 0.90% Wetterbericht
    10516.9h 0.89% Quiz
    10490.2h 0.88% Komödie
    10468.1h 0.88% Programmende
    9166.7h  0.77% Realityshow
    9065.0h  0.76% Politikmagazin
    8887.8h  0.75% Wissensmagazin
    8695.0h  0.73% Börsenmagazin
    7924.8h  0.67% Wirtschaftsmagazin
    7875.7h  0.66% Telenovela
    7871.5h  0.66% Dramaserie
