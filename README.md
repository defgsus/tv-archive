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

**99** channels, **673,694.4** hours playtime between **2023-01-17** and **2024-01-28**


### playtime per genre (top 30)

    43930.0h 6.52% Nachrichten
    32268.9h 4.79% Verkaufsshow
    27117.2h 4.03% Krimiserie
    23019.7h 3.42% Werbesendung
    21858.8h 3.24% Dokureihe
    20173.6h 2.99% Dokusoap
    19445.4h 2.89% Regionalmagazin
    17418.6h 2.59% Dokumentation
    16879.9h 2.51% *unknown*
    12473.0h 1.85% Zeichentrickserie
    12240.9h 1.82% Infomercial
    11839.5h 1.76% Animationsserie
    10195.2h 1.51% Comedyserie
    9529.6h  1.41% Morgenmagazin
    9089.1h  1.35% Religionsmagazin
    8957.4h  1.33% Magazin
    8909.8h  1.32% Talkshow
    6622.2h  0.98% E-Sport
    6495.4h  0.96% Programmende
    6461.5h  0.96% Sitcom
    6050.9h  0.90% Wetterbericht
    5993.3h  0.89% Börsenmagazin
    5717.6h  0.85% Komödie
    5591.3h  0.83% Quiz
    5065.4h  0.75% Wissensmagazin
    4925.8h  0.73% Realityshow
    4916.6h  0.73% Wirtschaftsmagazin
    4794.4h  0.71% Telenovela
    4770.4h  0.71% Politikmagazin
    4737.6h  0.70% Musikmagazin
