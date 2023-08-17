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

**97** channels, **384,154.2** hours playtime between **2023-01-17** and **2023-08-18**


### playtime per genre (top 30)

    25444.6h 6.62% Nachrichten
    18141.3h 4.72% Verkaufsshow
    15543.1h 4.05% Krimiserie
    12933.1h 3.37% Werbesendung
    12701.8h 3.31% Dokureihe
    11626.8h 3.03% Dokusoap
    11036.8h 2.87% Regionalmagazin
    9697.9h  2.52% Dokumentation
    9335.0h  2.43% *unknown*
    7261.4h  1.89% Zeichentrickserie
    7016.4h  1.83% Infomercial
    6788.7h  1.77% Animationsserie
    6289.5h  1.64% Comedyserie
    5416.1h  1.41% Morgenmagazin
    5111.6h  1.33% Religionsmagazin
    5045.0h  1.31% Talkshow
    4752.2h  1.24% Magazin
    4267.9h  1.11% Programmende
    3804.3h  0.99% E-Sport
    3626.8h  0.94% Wetterbericht
    3605.3h  0.94% Sitcom
    3486.6h  0.91% Börsenmagazin
    3102.5h  0.81% Quiz
    3027.6h  0.79% Musikmagazin
    2961.0h  0.77% Komödie
    2942.9h  0.77% Wirtschaftsmagazin
    2883.4h  0.75% Wissensmagazin
    2683.6h  0.70% Telenovela
    2517.0h  0.66% Reportagereihe
    2475.5h  0.64% Sportmagazin
