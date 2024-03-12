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

**101** channels, **753,605.8** hours playtime between **2023-01-17** and **2024-03-13**


### playtime per genre (top 30)

    49034.5h 6.51% Nachrichten
    36200.0h 4.80% Verkaufsshow
    30702.1h 4.07% Krimiserie
    26124.3h 3.47% Werbesendung
    24049.1h 3.19% Dokureihe
    22776.7h 3.02% Dokusoap
    21880.1h 2.90% Regionalmagazin
    19446.3h 2.58% Dokumentation
    19314.8h 2.56% *unknown*
    13930.5h 1.85% Zeichentrickserie
    13705.3h 1.82% Infomercial
    13305.5h 1.77% Animationsserie
    11445.5h 1.52% Comedyserie
    10691.7h 1.42% Morgenmagazin
    10215.5h 1.36% Magazin
    10180.7h 1.35% Religionsmagazin
    10034.9h 1.33% Talkshow
    7425.8h  0.99% E-Sport
    7123.8h  0.95% Programmende
    7079.2h  0.94% Sitcom
    6709.7h  0.89% Börsenmagazin
    6693.1h  0.89% Wetterbericht
    6393.4h  0.85% Quiz
    6369.5h  0.85% Komödie
    5628.4h  0.75% Wissensmagazin
    5471.8h  0.73% Realityshow
    5447.5h  0.72% Wirtschaftsmagazin
    5440.7h  0.72% Politikmagazin
    5381.8h  0.71% Telenovela
    5143.6h  0.68% Musikmagazin
