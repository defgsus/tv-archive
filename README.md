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

**97** channels, **400,340.0** hours playtime between **2023-01-17** and **2023-08-27**


### playtime per genre (top 30)

    26456.2h 6.61% Nachrichten
    18899.2h 4.72% Verkaufsshow
    16247.5h 4.06% Krimiserie
    13490.2h 3.37% Werbesendung
    13252.4h 3.31% Dokureihe
    12133.5h 3.03% Dokusoap
    11485.5h 2.87% Regionalmagazin
    10148.5h 2.53% Dokumentation
    9673.0h  2.42% *unknown*
    7551.1h  1.89% Zeichentrickserie
    7312.4h  1.83% Infomercial
    7074.6h  1.77% Animationsserie
    6523.2h  1.63% Comedyserie
    5639.6h  1.41% Morgenmagazin
    5334.5h  1.33% Religionsmagazin
    5264.1h  1.31% Talkshow
    4998.6h  1.25% Magazin
    4397.6h  1.10% Programmende
    3968.8h  0.99% E-Sport
    3788.4h  0.95% Wetterbericht
    3750.6h  0.94% Sitcom
    3607.6h  0.90% Börsenmagazin
    3253.1h  0.81% Quiz
    3170.4h  0.79% Musikmagazin
    3120.6h  0.78% Komödie
    3044.2h  0.76% Wirtschaftsmagazin
    2993.9h  0.75% Wissensmagazin
    2803.8h  0.70% Telenovela
    2635.3h  0.66% Reportagereihe
    2571.0h  0.64% Politikmagazin
