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

**97** channels, **450,227.6** hours playtime between **2023-01-17** and **2023-09-24**


### playtime per genre (top 30)

    29719.3h 6.60% Nachrichten
    21430.2h 4.76% Verkaufsshow
    18208.6h 4.04% Krimiserie
    15191.8h 3.37% Werbesendung
    14833.0h 3.29% Dokureihe
    13699.8h 3.04% Dokusoap
    12961.3h 2.88% Regionalmagazin
    11314.4h 2.51% Dokumentation
    10714.1h 2.38% *unknown*
    8482.7h  1.88% Zeichentrickserie
    8214.9h  1.82% Infomercial
    7991.6h  1.78% Animationsserie
    7280.9h  1.62% Comedyserie
    6365.4h  1.41% Morgenmagazin
    6026.1h  1.34% Religionsmagazin
    5953.4h  1.32% Talkshow
    5607.2h  1.25% Magazin
    4783.6h  1.06% Programmende
    4440.1h  0.99% E-Sport
    4243.5h  0.94% Sitcom
    4231.8h  0.94% Wetterbericht
    4055.3h  0.90% Börsenmagazin
    3759.1h  0.83% Quiz
    3490.1h  0.78% Musikmagazin
    3472.7h  0.77% Komödie
    3404.1h  0.76% Wirtschaftsmagazin
    3371.8h  0.75% Wissensmagazin
    3191.9h  0.71% Telenovela
    2978.9h  0.66% Politikmagazin
    2957.1h  0.66% Reportagereihe
