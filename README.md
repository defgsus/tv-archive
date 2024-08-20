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

**109** channels, **1,006,980.6** hours playtime between **2023-01-17** and **2024-08-21**


### playtime per genre (top 30)

    65494.7h 6.50% Nachrichten
    46915.2h 4.66% Verkaufsshow
    41363.7h 4.11% Krimiserie
    36258.5h 3.60% Werbesendung
    31661.8h 3.14% Dokureihe
    30448.7h 3.02% Dokusoap
    29354.5h 2.92% Regionalmagazin
    26272.2h 2.61% Dokumentation
    24600.5h 2.44% *unknown*
    18675.6h 1.85% Zeichentrickserie
    18438.6h 1.83% Infomercial
    18029.9h 1.79% Animationsserie
    14801.0h 1.47% Comedyserie
    14112.6h 1.40% Morgenmagazin
    13693.0h 1.36% Religionsmagazin
    13526.2h 1.34% Magazin
    13199.3h 1.31% Talkshow
    9959.7h  0.99% E-Sport
    9580.6h  0.95% Sitcom
    9084.2h  0.90% Wetterbericht
    9069.5h  0.90% Programmende
    8846.8h  0.88% Komödie
    8673.1h  0.86% Quiz
    8128.1h  0.81% Börsenmagazin
    7530.2h  0.75% Politikmagazin
    7497.9h  0.74% Wissensmagazin
    7455.2h  0.74% Realityshow
    6874.8h  0.68% Wirtschaftsmagazin
    6615.3h  0.66% Telenovela
    6551.9h  0.65% Dramaserie
