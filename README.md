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

**110** channels, **1,270,683.9** hours playtime between **2023-01-17** and **2025-02-12**


### playtime per genre (top 30)

    83365.8h 6.56% Nachrichten
    57000.9h 4.49% Verkaufsshow
    52787.6h 4.15% Krimiserie
    47455.0h 3.73% Werbesendung
    39424.9h 3.10% Dokureihe
    37271.6h 2.93% Dokusoap
    36961.9h 2.91% Regionalmagazin
    34070.3h 2.68% Dokumentation
    30217.8h 2.38% *unknown*
    23984.6h 1.89% Zeichentrickserie
    23688.4h 1.86% Infomercial
    22739.7h 1.79% Animationsserie
    17761.2h 1.40% Morgenmagazin
    17704.1h 1.39% Comedyserie
    16768.9h 1.32% Talkshow
    16441.4h 1.29% Religionsmagazin
    15149.1h 1.19% Magazin
    12607.0h 0.99% E-Sport
    12166.8h 0.96% Sitcom
    11597.4h 0.91% Komödie
    11529.7h 0.91% Wetterbericht
    11335.3h 0.89% Quiz
    11121.7h 0.88% Programmende
    9904.3h  0.78% Realityshow
    9724.1h  0.77% Politikmagazin
    9322.3h  0.73% Wissensmagazin
    8930.5h  0.70% Börsenmagazin
    8457.2h  0.67% Dramaserie
    8451.9h  0.67% Arztserie
    8397.1h  0.66% Wirtschaftsmagazin
