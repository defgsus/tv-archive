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

**97** channels, **581,201.7** hours playtime between **2023-01-17** and **2023-12-07**


### playtime per genre (top 30)

    38219.5h 6.58% Nachrichten
    27858.3h 4.79% Verkaufsshow
    23463.8h 4.04% Krimiserie
    19752.6h 3.40% Werbesendung
    18910.7h 3.25% Dokureihe
    17522.2h 3.01% Dokusoap
    16821.2h 2.89% Regionalmagazin
    14870.8h 2.56% Dokumentation
    14206.3h 2.44% *unknown*
    10740.6h 1.85% Zeichentrickserie
    10591.7h 1.82% Infomercial
    10328.7h 1.78% Animationsserie
    8992.0h  1.55% Comedyserie
    8287.2h  1.43% Morgenmagazin
    7866.4h  1.35% Religionsmagazin
    7780.8h  1.34% Talkshow
    7473.6h  1.29% Magazin
    5785.1h  1.00% Programmende
    5698.4h  0.98% E-Sport
    5619.3h  0.97% Sitcom
    5325.4h  0.92% Wetterbericht
    5272.2h  0.91% Börsenmagazin
    4834.7h  0.83% Quiz
    4490.1h  0.77% Komödie
    4426.1h  0.76% Wissensmagazin
    4350.0h  0.75% Wirtschaftsmagazin
    4232.1h  0.73% Musikmagazin
    4222.5h  0.73% Telenovela
    4128.1h  0.71% Realityshow
    4118.5h  0.71% Politikmagazin
