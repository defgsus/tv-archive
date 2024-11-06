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

**109** channels, **1,126,850.9** hours playtime between **2023-01-17** and **2024-11-07**


### playtime per genre (top 30)

    73389.6h 6.51% Nachrichten
    51684.1h 4.59% Verkaufsshow
    46881.9h 4.16% Krimiserie
    41375.2h 3.67% Werbesendung
    35212.4h 3.12% Dokureihe
    33668.1h 2.99% Dokusoap
    32959.7h 2.92% Regionalmagazin
    29589.5h 2.63% Dokumentation
    26728.5h 2.37% *unknown*
    21068.6h 1.87% Zeichentrickserie
    20750.0h 1.84% Infomercial
    20148.6h 1.79% Animationsserie
    16202.0h 1.44% Comedyserie
    15775.3h 1.40% Morgenmagazin
    15100.8h 1.34% Religionsmagazin
    14913.5h 1.32% Talkshow
    14173.2h 1.26% Magazin
    11126.1h 0.99% E-Sport
    10884.4h 0.97% Sitcom
    10189.5h 0.90% Wetterbericht
    9982.4h  0.89% Programmende
    9918.4h  0.88% Quiz
    9918.2h  0.88% Komödie
    8603.2h  0.76% Realityshow
    8533.3h  0.76% Politikmagazin
    8504.0h  0.75% Börsenmagazin
    8463.1h  0.75% Wissensmagazin
    7562.2h  0.67% Wirtschaftsmagazin
    7442.0h  0.66% Telenovela
    7383.2h  0.66% Dramaserie
