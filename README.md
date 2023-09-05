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

**97** channels, **418,095.4** hours playtime between **2023-01-17** and **2023-09-06**


### playtime per genre (top 30)

    27592.8h 6.60% Nachrichten
    19797.6h 4.74% Verkaufsshow
    16982.0h 4.06% Krimiserie
    14110.7h 3.37% Werbesendung
    13796.4h 3.30% Dokureihe
    12698.4h 3.04% Dokusoap
    12022.6h 2.88% Regionalmagazin
    10578.4h 2.53% Dokumentation
    10012.1h 2.39% *unknown*
    7899.6h  1.89% Zeichentrickserie
    7633.5h  1.83% Infomercial
    7400.3h  1.77% Animationsserie
    6794.1h  1.63% Comedyserie
    5898.0h  1.41% Morgenmagazin
    5593.7h  1.34% Religionsmagazin
    5506.8h  1.32% Talkshow
    5210.1h  1.25% Magazin
    4536.0h  1.08% Programmende
    4128.6h  0.99% E-Sport
    3954.8h  0.95% Wetterbericht
    3917.8h  0.94% Sitcom
    3772.1h  0.90% Börsenmagazin
    3423.1h  0.82% Quiz
    3315.2h  0.79% Musikmagazin
    3274.8h  0.78% Komödie
    3169.8h  0.76% Wirtschaftsmagazin
    3122.8h  0.75% Wissensmagazin
    2936.6h  0.70% Telenovela
    2752.2h  0.66% Reportagereihe
    2711.9h  0.65% Politikmagazin
