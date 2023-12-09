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

**97** channels, **586,580.6** hours playtime between **2023-01-17** and **2023-12-10**


### playtime per genre (top 30)

    38545.3h 6.57% Nachrichten
    28136.7h 4.80% Verkaufsshow
    23704.6h 4.04% Krimiserie
    19937.7h 3.40% Werbesendung
    19074.3h 3.25% Dokureihe
    17659.7h 3.01% Dokusoap
    16960.2h 2.89% Regionalmagazin
    15012.7h 2.56% Dokumentation
    14353.0h 2.45% *unknown*
    10843.6h 1.85% Zeichentrickserie
    10690.8h 1.82% Infomercial
    10416.0h 1.78% Animationsserie
    9054.8h  1.54% Comedyserie
    8361.7h  1.43% Morgenmagazin
    7934.8h  1.35% Religionsmagazin
    7865.4h  1.34% Talkshow
    7546.0h  1.29% Magazin
    5817.9h  0.99% Programmende
    5751.2h  0.98% E-Sport
    5667.9h  0.97% Sitcom
    5374.6h  0.92% Wetterbericht
    5320.1h  0.91% Börsenmagazin
    4873.3h  0.83% Quiz
    4568.1h  0.78% Komödie
    4468.4h  0.76% Wissensmagazin
    4387.3h  0.75% Wirtschaftsmagazin
    4262.0h  0.73% Musikmagazin
    4258.1h  0.73% Telenovela
    4194.0h  0.71% Realityshow
    4155.1h  0.71% Politikmagazin
