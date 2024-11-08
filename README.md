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

**109** channels, **1,128,665.3** hours playtime between **2023-01-17** and **2024-11-09**


### playtime per genre (top 30)

    73537.3h 6.52% Nachrichten
    51784.3h 4.59% Verkaufsshow
    46989.5h 4.16% Krimiserie
    41443.3h 3.67% Werbesendung
    35263.7h 3.12% Dokureihe
    33721.0h 2.99% Dokusoap
    33028.0h 2.93% Regionalmagazin
    29627.1h 2.62% Dokumentation
    26749.5h 2.37% *unknown*
    21102.2h 1.87% Zeichentrickserie
    20788.9h 1.84% Infomercial
    20180.7h 1.79% Animationsserie
    16222.0h 1.44% Comedyserie
    15801.0h 1.40% Morgenmagazin
    15116.7h 1.34% Religionsmagazin
    14943.1h 1.32% Talkshow
    14186.8h 1.26% Magazin
    11136.0h 0.99% E-Sport
    10906.2h 0.97% Sitcom
    10207.4h 0.90% Wetterbericht
    9994.9h  0.89% Programmende
    9941.5h  0.88% Quiz
    9920.7h  0.88% Komödie
    8619.0h  0.76% Realityshow
    8549.2h  0.76% Politikmagazin
    8512.9h  0.75% Börsenmagazin
    8474.2h  0.75% Wissensmagazin
    7578.2h  0.67% Wirtschaftsmagazin
    7461.8h  0.66% Telenovela
    7386.9h  0.65% Dramaserie
