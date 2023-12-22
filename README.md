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

**97** channels, **609,918.3** hours playtime between **2023-01-17** and **2023-12-23**


### playtime per genre (top 30)

    40074.8h 6.57% Nachrichten
    29281.7h 4.80% Verkaufsshow
    24636.9h 4.04% Krimiserie
    20736.8h 3.40% Werbesendung
    19833.1h 3.25% Dokureihe
    18313.0h 3.00% Dokusoap
    17690.5h 2.90% Regionalmagazin
    15634.3h 2.56% Dokumentation
    14961.3h 2.45% *unknown*
    11264.8h 1.85% Zeichentrickserie
    11110.5h 1.82% Infomercial
    10781.4h 1.77% Animationsserie
    9331.7h  1.53% Comedyserie
    8726.1h  1.43% Morgenmagazin
    8263.2h  1.35% Religionsmagazin
    8151.4h  1.34% Talkshow
    7894.9h  1.29% Magazin
    6004.1h  0.98% Programmende
    6000.9h  0.98% E-Sport
    5920.6h  0.97% Sitcom
    5577.2h  0.91% Wetterbericht
    5498.8h  0.90% Börsenmagazin
    5055.5h  0.83% Quiz
    4798.0h  0.79% Komödie
    4645.0h  0.76% Wissensmagazin
    4551.4h  0.75% Wirtschaftsmagazin
    4448.5h  0.73% Telenovela
    4426.4h  0.73% Realityshow
    4397.4h  0.72% Musikmagazin
    4336.4h  0.71% Politikmagazin
