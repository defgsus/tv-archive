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

**99** channels, **711,046.2** hours playtime between **2023-01-17** and **2024-02-18**


### playtime per genre (top 30)

    46310.1h 6.51% Nachrichten
    34140.8h 4.80% Verkaufsshow
    28801.3h 4.05% Krimiserie
    24457.8h 3.44% Werbesendung
    22827.8h 3.21% Dokureihe
    21424.3h 3.01% Dokusoap
    20575.6h 2.89% Regionalmagazin
    18324.2h 2.58% Dokumentation
    18006.8h 2.53% *unknown*
    13185.8h 1.85% Zeichentrickserie
    12926.0h 1.82% Infomercial
    12503.9h 1.76% Animationsserie
    10769.9h 1.51% Comedyserie
    10073.3h 1.42% Morgenmagazin
    9607.9h  1.35% Religionsmagazin
    9503.8h  1.34% Magazin
    9419.4h  1.32% Talkshow
    7008.3h  0.99% E-Sport
    6785.3h  0.95% Programmende
    6752.2h  0.95% Sitcom
    6337.8h  0.89% Börsenmagazin
    6327.0h  0.89% Wetterbericht
    6048.0h  0.85% Komödie
    5934.6h  0.83% Quiz
    5332.4h  0.75% Wissensmagazin
    5208.6h  0.73% Realityshow
    5168.3h  0.73% Wirtschaftsmagazin
    5093.4h  0.72% Politikmagazin
    5067.6h  0.71% Telenovela
    4928.3h  0.69% Musikmagazin
