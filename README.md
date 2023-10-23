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

**97** channels, **503,976.8** hours playtime between **2023-01-17** and **2023-10-24**


### playtime per genre (top 30)

    33191.2h 6.59% Nachrichten
    24065.7h 4.78% Verkaufsshow
    20261.5h 4.02% Krimiserie
    17034.1h 3.38% Werbesendung
    16574.1h 3.29% Dokureihe
    15376.7h 3.05% Dokusoap
    14531.5h 2.88% Regionalmagazin
    12779.0h 2.54% Dokumentation
    12123.4h 2.41% *unknown*
    9425.4h  1.87% Zeichentrickserie
    9176.7h  1.82% Infomercial
    8998.3h  1.79% Animationsserie
    8000.8h  1.59% Comedyserie
    7126.0h  1.41% Morgenmagazin
    6781.9h  1.35% Religionsmagazin
    6712.2h  1.33% Talkshow
    6331.1h  1.26% Magazin
    5194.9h  1.03% Programmende
    4959.2h  0.98% E-Sport
    4803.7h  0.95% Sitcom
    4682.6h  0.93% Wetterbericht
    4541.0h  0.90% Börsenmagazin
    4231.0h  0.84% Quiz
    3917.3h  0.78% Komödie
    3808.2h  0.76% Wissensmagazin
    3797.2h  0.75% Musikmagazin
    3796.4h  0.75% Wirtschaftsmagazin
    3603.2h  0.71% Telenovela
    3459.2h  0.69% Politikmagazin
    3313.8h  0.66% Realityshow
