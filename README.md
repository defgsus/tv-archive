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

**97** channels, **396,736.9** hours playtime between **2023-01-17** and **2023-08-25**


### playtime per genre (top 30)

    26251.5h 6.62% Nachrichten
    18708.1h 4.72% Verkaufsshow
    16083.1h 4.05% Krimiserie
    13359.8h 3.37% Werbesendung
    13146.9h 3.31% Dokureihe
    12029.8h 3.03% Dokusoap
    11409.3h 2.88% Regionalmagazin
    10055.2h 2.53% Dokumentation
    9598.8h  2.42% *unknown*
    7485.2h  1.89% Zeichentrickserie
    7246.1h  1.83% Infomercial
    7016.9h  1.77% Animationsserie
    6480.3h  1.63% Comedyserie
    5601.3h  1.41% Morgenmagazin
    5278.1h  1.33% Religionsmagazin
    5206.6h  1.31% Talkshow
    4957.5h  1.25% Magazin
    4371.1h  1.10% Programmende
    3936.0h  0.99% E-Sport
    3750.6h  0.95% Wetterbericht
    3716.9h  0.94% Sitcom
    3578.4h  0.90% Börsenmagazin
    3227.7h  0.81% Quiz
    3132.6h  0.79% Musikmagazin
    3069.6h  0.77% Komödie
    3028.0h  0.76% Wirtschaftsmagazin
    2969.1h  0.75% Wissensmagazin
    2784.8h  0.70% Telenovela
    2612.2h  0.66% Reportagereihe
    2561.0h  0.65% Politikmagazin
