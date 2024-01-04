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

**97** channels, **632,993.3** hours playtime between **2023-01-17** and **2024-01-05**


### playtime per genre (top 30)

    41322.6h 6.53% Nachrichten
    30282.1h 4.78% Verkaufsshow
    25342.1h 4.00% Krimiserie
    21505.2h 3.40% Werbesendung
    20559.5h 3.25% Dokureihe
    18924.9h 2.99% Dokusoap
    18183.9h 2.87% Regionalmagazin
    16433.0h 2.60% Dokumentation
    15710.1h 2.48% *unknown*
    11676.4h 1.84% Zeichentrickserie
    11476.8h 1.81% Infomercial
    11128.7h 1.76% Animationsserie
    9620.6h  1.52% Comedyserie
    8957.5h  1.42% Morgenmagazin
    8564.9h  1.35% Religionsmagazin
    8351.7h  1.32% Talkshow
    8294.0h  1.31% Magazin
    6229.3h  0.98% E-Sport
    6184.7h  0.98% Programmende
    6151.4h  0.97% Sitcom
    5763.1h  0.91% Wetterbericht
    5660.9h  0.89% Börsenmagazin
    5363.0h  0.85% Komödie
    5197.2h  0.82% Quiz
    4760.9h  0.75% Wissensmagazin
    4661.1h  0.74% Wirtschaftsmagazin
    4599.7h  0.73% Realityshow
    4542.7h  0.72% Musikmagazin
    4518.4h  0.71% Telenovela
    4457.3h  0.70% Politikmagazin
