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

**109** channels, **1,039,615.6** hours playtime between **2023-01-17** and **2024-09-11**


### playtime per genre (top 30)

    67628.7h 6.51% Nachrichten
    48296.1h 4.65% Verkaufsshow
    42861.1h 4.12% Krimiserie
    37651.0h 3.62% Werbesendung
    32664.7h 3.14% Dokureihe
    31324.0h 3.01% Dokusoap
    30343.1h 2.92% Regionalmagazin
    27190.4h 2.62% Dokumentation
    25066.0h 2.41% *unknown*
    19295.4h 1.86% Zeichentrickserie
    19062.6h 1.83% Infomercial
    18627.1h 1.79% Animationsserie
    15212.1h 1.46% Comedyserie
    14550.9h 1.40% Morgenmagazin
    14138.6h 1.36% Religionsmagazin
    13651.6h 1.31% Talkshow
    13620.3h 1.31% Magazin
    10269.6h 0.99% E-Sport
    9946.2h  0.96% Sitcom
    9405.8h  0.90% Wetterbericht
    9318.7h  0.90% Programmende
    9136.3h  0.88% Komödie
    8995.2h  0.87% Quiz
    8230.7h  0.79% Börsenmagazin
    7786.0h  0.75% Politikmagazin
    7785.3h  0.75% Wissensmagazin
    7743.1h  0.74% Realityshow
    7069.1h  0.68% Wirtschaftsmagazin
    6841.2h  0.66% Telenovela
    6755.6h  0.65% Dramaserie
