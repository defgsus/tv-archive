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

**97** channels, **416,299.9** hours playtime between **2023-01-17** and **2023-09-05**


### playtime per genre (top 30)

    27463.3h 6.60% Nachrichten
    19712.9h 4.74% Verkaufsshow
    16897.2h 4.06% Krimiserie
    14047.4h 3.37% Werbesendung
    13734.2h 3.30% Dokureihe
    12652.4h 3.04% Dokusoap
    11953.6h 2.87% Regionalmagazin
    10541.3h 2.53% Dokumentation
    9988.1h  2.40% *unknown*
    7865.8h  1.89% Zeichentrickserie
    7601.1h  1.83% Infomercial
    7365.4h  1.77% Animationsserie
    6763.6h  1.62% Comedyserie
    5863.3h  1.41% Morgenmagazin
    5568.3h  1.34% Religionsmagazin
    5489.8h  1.32% Talkshow
    5183.7h  1.25% Magazin
    4522.2h  1.09% Programmende
    4113.1h  0.99% E-Sport
    3938.9h  0.95% Wetterbericht
    3902.0h  0.94% Sitcom
    3760.6h  0.90% Börsenmagazin
    3403.0h  0.82% Quiz
    3301.1h  0.79% Musikmagazin
    3263.9h  0.78% Komödie
    3156.1h  0.76% Wirtschaftsmagazin
    3112.6h  0.75% Wissensmagazin
    2915.2h  0.70% Telenovela
    2749.8h  0.66% Reportagereihe
    2692.1h  0.65% Politikmagazin
