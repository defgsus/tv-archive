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

**97** channels, **582,990.6** hours playtime between **2023-01-17** and **2023-12-08**


### playtime per genre (top 30)

    38347.9h 6.58% Nachrichten
    27947.8h 4.79% Verkaufsshow
    23562.9h 4.04% Krimiserie
    19812.0h 3.40% Werbesendung
    18981.3h 3.26% Dokureihe
    17583.0h 3.02% Dokusoap
    16886.6h 2.90% Regionalmagazin
    14912.3h 2.56% Dokumentation
    14246.9h 2.44% *unknown*
    10771.2h 1.85% Zeichentrickserie
    10625.8h 1.82% Infomercial
    10357.2h 1.78% Animationsserie
    9010.4h  1.55% Comedyserie
    8321.9h  1.43% Morgenmagazin
    7883.2h  1.35% Religionsmagazin
    7810.6h  1.34% Talkshow
    7506.0h  1.29% Magazin
    5797.9h  0.99% Programmende
    5712.8h  0.98% E-Sport
    5636.7h  0.97% Sitcom
    5342.0h  0.92% Wetterbericht
    5283.6h  0.91% Börsenmagazin
    4854.7h  0.83% Quiz
    4507.8h  0.77% Komödie
    4440.9h  0.76% Wissensmagazin
    4367.9h  0.75% Wirtschaftsmagazin
    4243.3h  0.73% Musikmagazin
    4242.6h  0.73% Telenovela
    4164.9h  0.71% Realityshow
    4136.8h  0.71% Politikmagazin
