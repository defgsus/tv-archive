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

**97** channels, **557,843.6** hours playtime between **2023-01-17** and **2023-11-23**


### playtime per genre (top 30)

    36723.4h 6.58% Nachrichten
    26679.8h 4.78% Verkaufsshow
    22484.2h 4.03% Krimiserie
    18923.8h 3.39% Werbesendung
    18199.2h 3.26% Dokureihe
    16879.9h 3.03% Dokusoap
    16136.6h 2.89% Regionalmagazin
    14233.9h 2.55% Dokumentation
    13580.1h 2.43% *unknown*
    10334.2h 1.85% Zeichentrickserie
    10166.3h 1.82% Infomercial
    9941.9h  1.78% Animationsserie
    8721.7h  1.56% Comedyserie
    7948.4h  1.42% Morgenmagazin
    7530.7h  1.35% Religionsmagazin
    7461.4h  1.34% Talkshow
    7132.8h  1.28% Magazin
    5609.8h  1.01% Programmende
    5462.0h  0.98% E-Sport
    5373.2h  0.96% Sitcom
    5120.7h  0.92% Wetterbericht
    5063.6h  0.91% Börsenmagazin
    4657.1h  0.83% Quiz
    4345.8h  0.78% Komödie
    4235.2h  0.76% Wissensmagazin
    4189.3h  0.75% Wirtschaftsmagazin
    4101.9h  0.74% Musikmagazin
    4038.2h  0.72% Telenovela
    3913.0h  0.70% Politikmagazin
    3872.8h  0.69% Realityshow
