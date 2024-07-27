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

**109** channels, **968,675.5** hours playtime between **2023-01-17** and **2024-07-28**


### playtime per genre (top 30)

    63069.3h 6.51% Nachrichten
    45238.5h 4.67% Verkaufsshow
    39721.6h 4.10% Krimiserie
    34678.5h 3.58% Werbesendung
    30466.0h 3.15% Dokureihe
    29342.8h 3.03% Dokusoap
    28179.8h 2.91% Regionalmagazin
    25184.8h 2.60% Dokumentation
    24053.3h 2.48% *unknown*
    17933.5h 1.85% Zeichentrickserie
    17712.6h 1.83% Infomercial
    17332.4h 1.79% Animationsserie
    14372.8h 1.48% Comedyserie
    13627.9h 1.41% Morgenmagazin
    13423.9h 1.39% Magazin
    13149.3h 1.36% Religionsmagazin
    12799.3h 1.32% Talkshow
    9600.6h  0.99% E-Sport
    9157.0h  0.95% Sitcom
    8772.1h  0.91% Programmende
    8700.2h  0.90% Wetterbericht
    8468.2h  0.87% Komödie
    8356.6h  0.86% Quiz
    8002.1h  0.83% Börsenmagazin
    7283.9h  0.75% Politikmagazin
    7195.1h  0.74% Wissensmagazin
    7179.4h  0.74% Realityshow
    6689.1h  0.69% Wirtschaftsmagazin
    6464.7h  0.67% Telenovela
    6313.3h  0.65% Dramaserie
