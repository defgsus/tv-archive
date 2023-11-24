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

**97** channels, **561,439.4** hours playtime between **2023-01-17** and **2023-11-25**


### playtime per genre (top 30)

    36978.6h 6.59% Nachrichten
    26879.1h 4.79% Verkaufsshow
    22676.5h 4.04% Krimiserie
    19039.1h 3.39% Werbesendung
    18299.1h 3.26% Dokureihe
    16981.0h 3.02% Dokusoap
    16260.3h 2.90% Regionalmagazin
    14311.0h 2.55% Dokumentation
    13658.7h 2.43% *unknown*
    10392.8h 1.85% Zeichentrickserie
    10230.6h 1.82% Infomercial
    10003.9h 1.78% Animationsserie
    8772.8h  1.56% Comedyserie
    8016.7h  1.43% Morgenmagazin
    7572.8h  1.35% Religionsmagazin
    7515.0h  1.34% Talkshow
    7177.5h  1.28% Magazin
    5637.6h  1.00% Programmende
    5503.0h  0.98% E-Sport
    5400.7h  0.96% Sitcom
    5151.6h  0.92% Wetterbericht
    5100.0h  0.91% Börsenmagazin
    4693.6h  0.84% Quiz
    4364.3h  0.78% Komödie
    4265.9h  0.76% Wissensmagazin
    4221.0h  0.75% Wirtschaftsmagazin
    4122.1h  0.73% Musikmagazin
    4077.6h  0.73% Telenovela
    3950.3h  0.70% Politikmagazin
    3930.5h  0.70% Realityshow
