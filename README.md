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

**97** channels, **638,279.2** hours playtime between **2023-01-17** and **2024-01-08**


### playtime per genre (top 30)

    41616.8h 6.52% Nachrichten
    30499.2h 4.78% Verkaufsshow
    25531.7h 4.00% Krimiserie
    21706.1h 3.40% Werbesendung
    20736.6h 3.25% Dokureihe
    19067.9h 2.99% Dokusoap
    18298.5h 2.87% Regionalmagazin
    16619.8h 2.60% Dokumentation
    15876.6h 2.49% *unknown*
    11777.8h 1.85% Zeichentrickserie
    11571.4h 1.81% Infomercial
    11224.1h 1.76% Animationsserie
    9677.0h  1.52% Comedyserie
    9004.6h  1.41% Morgenmagazin
    8644.7h  1.35% Religionsmagazin
    8421.5h  1.32% Talkshow
    8370.0h  1.31% Magazin
    6296.2h  0.99% E-Sport
    6226.1h  0.98% Programmende
    6178.0h  0.97% Sitcom
    5802.5h  0.91% Wetterbericht
    5693.8h  0.89% Börsenmagazin
    5431.8h  0.85% Komödie
    5241.3h  0.82% Quiz
    4803.6h  0.75% Wissensmagazin
    4680.4h  0.73% Wirtschaftsmagazin
    4628.4h  0.73% Realityshow
    4567.7h  0.72% Musikmagazin
    4530.2h  0.71% Telenovela
    4477.1h  0.70% Politikmagazin
