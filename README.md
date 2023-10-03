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

**97** channels, **468,146.8** hours playtime between **2023-01-17** and **2023-10-04**


### playtime per genre (top 30)

    30846.7h 6.59% Nachrichten
    22282.6h 4.76% Verkaufsshow
    18868.9h 4.03% Krimiserie
    15805.3h 3.38% Werbesendung
    15454.8h 3.30% Dokureihe
    14284.3h 3.05% Dokusoap
    13458.8h 2.87% Regionalmagazin
    11824.1h 2.53% Dokumentation
    11159.9h 2.38% *unknown*
    8792.4h  1.88% Zeichentrickserie
    8526.9h  1.82% Infomercial
    8313.7h  1.78% Animationsserie
    7526.1h  1.61% Comedyserie
    6601.1h  1.41% Morgenmagazin
    6289.6h  1.34% Religionsmagazin
    6196.3h  1.32% Talkshow
    5821.5h  1.24% Magazin
    4923.3h  1.05% Programmende
    4621.8h  0.99% E-Sport
    4424.1h  0.95% Sitcom
    4377.4h  0.94% Wetterbericht
    4224.6h  0.90% Börsenmagazin
    3916.4h  0.84% Quiz
    3637.6h  0.78% Komödie
    3599.8h  0.77% Musikmagazin
    3527.9h  0.75% Wirtschaftsmagazin
    3516.0h  0.75% Wissensmagazin
    3318.9h  0.71% Telenovela
    3143.2h  0.67% Politikmagazin
    3046.2h  0.65% Reportagereihe
