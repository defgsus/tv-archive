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

**99** channels, **670,139.7** hours playtime between **2023-01-17** and **2024-01-26**


### playtime per genre (top 30)

    43733.2h 6.53% Nachrichten
    32079.8h 4.79% Verkaufsshow
    26967.6h 4.02% Krimiserie
    22873.1h 3.41% Werbesendung
    21753.7h 3.25% Dokureihe
    20057.6h 2.99% Dokusoap
    19352.0h 2.89% Regionalmagazin
    17332.3h 2.59% Dokumentation
    16774.1h 2.50% *unknown*
    12404.9h 1.85% Zeichentrickserie
    12174.4h 1.82% Infomercial
    11775.9h 1.76% Animationsserie
    10147.4h 1.51% Comedyserie
    9494.7h  1.42% Morgenmagazin
    9048.4h  1.35% Religionsmagazin
    8920.0h  1.33% Magazin
    8860.2h  1.32% Talkshow
    6584.4h  0.98% E-Sport
    6468.9h  0.97% Programmende
    6442.8h  0.96% Sitcom
    6027.7h  0.90% Wetterbericht
    5957.7h  0.89% Börsenmagazin
    5675.4h  0.85% Komödie
    5562.8h  0.83% Quiz
    5043.4h  0.75% Wissensmagazin
    4904.6h  0.73% Realityshow
    4898.8h  0.73% Wirtschaftsmagazin
    4775.2h  0.71% Telenovela
    4756.4h  0.71% Politikmagazin
    4721.8h  0.70% Musikmagazin
