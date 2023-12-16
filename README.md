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

**97** channels, **599,143.7** hours playtime between **2023-01-17** and **2023-12-17**


### playtime per genre (top 30)

    39346.9h 6.57% Nachrichten
    28762.8h 4.80% Verkaufsshow
    24217.5h 4.04% Krimiserie
    20368.7h 3.40% Werbesendung
    19464.5h 3.25% Dokureihe
    17991.8h 3.00% Dokusoap
    17335.8h 2.89% Regionalmagazin
    15352.4h 2.56% Dokumentation
    14679.3h 2.45% *unknown*
    11073.5h 1.85% Zeichentrickserie
    10919.0h 1.82% Infomercial
    10622.5h 1.77% Animationsserie
    9196.8h  1.53% Comedyserie
    8545.4h  1.43% Morgenmagazin
    8111.4h  1.35% Religionsmagazin
    8026.9h  1.34% Talkshow
    7729.6h  1.29% Magazin
    5922.6h  0.99% Programmende
    5891.2h  0.98% E-Sport
    5802.2h  0.97% Sitcom
    5482.1h  0.91% Wetterbericht
    5417.4h  0.90% Börsenmagazin
    4968.6h  0.83% Quiz
    4668.1h  0.78% Komödie
    4570.7h  0.76% Wissensmagazin
    4471.1h  0.75% Wirtschaftsmagazin
    4352.2h  0.73% Telenovela
    4336.3h  0.72% Musikmagazin
    4322.1h  0.72% Realityshow
    4254.4h  0.71% Politikmagazin
