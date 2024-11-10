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

**109** channels, **1,132,329.0** hours playtime between **2023-01-17** and **2024-11-11**


### playtime per genre (top 30)

    73744.1h 6.51% Nachrichten
    51914.4h 4.58% Verkaufsshow
    47118.1h 4.16% Krimiserie
    41591.6h 3.67% Werbesendung
    35405.3h 3.13% Dokureihe
    33810.7h 2.99% Dokusoap
    33085.3h 2.92% Regionalmagazin
    29773.5h 2.63% Dokumentation
    26829.3h 2.37% *unknown*
    21173.0h 1.87% Zeichentrickserie
    20863.9h 1.84% Infomercial
    20249.5h 1.79% Animationsserie
    16261.6h 1.44% Comedyserie
    15817.9h 1.40% Morgenmagazin
    15163.8h 1.34% Religionsmagazin
    14993.0h 1.32% Talkshow
    14224.9h 1.26% Magazin
    11179.9h 0.99% E-Sport
    10928.8h 0.97% Sitcom
    10235.2h 0.90% Wetterbericht
    10026.2h 0.89% Programmende
    9984.6h  0.88% Komödie
    9965.1h  0.88% Quiz
    8649.3h  0.76% Realityshow
    8560.2h  0.76% Politikmagazin
    8512.8h  0.75% Börsenmagazin
    8512.4h  0.75% Wissensmagazin
    7584.8h  0.67% Wirtschaftsmagazin
    7463.3h  0.66% Telenovela
    7403.1h  0.65% Arztserie
