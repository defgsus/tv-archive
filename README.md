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

**101** channels, **762,391.4** hours playtime between **2023-01-17** and **2024-03-18**


### playtime per genre (top 30)

    49596.9h 6.51% Nachrichten
    36620.4h 4.80% Verkaufsshow
    31057.8h 4.07% Krimiserie
    26451.7h 3.47% Werbesendung
    24299.5h 3.19% Dokureihe
    23023.7h 3.02% Dokusoap
    22126.3h 2.90% Regionalmagazin
    19678.3h 2.58% Dokumentation
    19559.7h 2.57% *unknown*
    14074.0h 1.85% Zeichentrickserie
    13868.6h 1.82% Infomercial
    13491.1h 1.77% Animationsserie
    11565.1h 1.52% Comedyserie
    10799.9h 1.42% Morgenmagazin
    10404.0h 1.36% Magazin
    10306.6h 1.35% Religionsmagazin
    10165.1h 1.33% Talkshow
    7514.9h  0.99% E-Sport
    7191.6h  0.94% Programmende
    7143.0h  0.94% Sitcom
    6770.5h  0.89% Wetterbericht
    6766.7h  0.89% Börsenmagazin
    6476.4h  0.85% Quiz
    6428.9h  0.84% Komödie
    5699.9h  0.75% Wissensmagazin
    5514.2h  0.72% Politikmagazin
    5514.1h  0.72% Realityshow
    5500.4h  0.72% Wirtschaftsmagazin
    5440.7h  0.71% Telenovela
    5189.7h  0.68% Musikmagazin
