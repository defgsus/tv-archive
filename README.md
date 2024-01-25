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

**99** channels, **670,162.4** hours playtime between **2023-01-17** and **2024-01-26**


### playtime per genre (top 30)

    43735.3h 6.53% Nachrichten
    32079.1h 4.79% Verkaufsshow
    26969.2h 4.02% Krimiserie
    22874.1h 3.41% Werbesendung
    21750.6h 3.25% Dokureihe
    20060.6h 2.99% Dokusoap
    19352.1h 2.89% Regionalmagazin
    17334.8h 2.59% Dokumentation
    16779.3h 2.50% *unknown*
    12404.0h 1.85% Zeichentrickserie
    12174.4h 1.82% Infomercial
    11776.0h 1.76% Animationsserie
    10148.0h 1.51% Comedyserie
    9494.7h  1.42% Morgenmagazin
    9048.4h  1.35% Religionsmagazin
    8920.1h  1.33% Magazin
    8862.5h  1.32% Talkshow
    6584.4h  0.98% E-Sport
    6469.0h  0.97% Programmende
    6442.8h  0.96% Sitcom
    6028.0h  0.90% Wetterbericht
    5957.7h  0.89% Börsenmagazin
    5675.7h  0.85% Komödie
    5562.7h  0.83% Quiz
    5043.5h  0.75% Wissensmagazin
    4905.2h  0.73% Realityshow
    4898.7h  0.73% Wirtschaftsmagazin
    4775.1h  0.71% Telenovela
    4757.6h  0.71% Politikmagazin
    4721.8h  0.70% Musikmagazin
