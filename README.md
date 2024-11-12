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

**109** channels, **1,135,945.1** hours playtime between **2023-01-17** and **2024-11-13**


### playtime per genre (top 30)

    74016.7h 6.52% Nachrichten
    52029.8h 4.58% Verkaufsshow
    47325.8h 4.17% Krimiserie
    41745.7h 3.67% Werbesendung
    35476.1h 3.12% Dokureihe
    33900.1h 2.98% Dokusoap
    33219.2h 2.92% Regionalmagazin
    29854.8h 2.63% Dokumentation
    26890.1h 2.37% *unknown*
    21242.8h 1.87% Zeichentrickserie
    20935.5h 1.84% Infomercial
    20309.9h 1.79% Animationsserie
    16301.6h 1.44% Comedyserie
    15885.7h 1.40% Morgenmagazin
    15194.7h 1.34% Religionsmagazin
    15033.9h 1.32% Talkshow
    14250.1h 1.25% Magazin
    11216.0h 0.99% E-Sport
    10977.0h 0.97% Sitcom
    10271.4h 0.90% Wetterbericht
    10052.5h 0.88% Programmende
    10019.5h 0.88% Quiz
    9997.4h  0.88% Komödie
    8685.3h  0.76% Realityshow
    8602.9h  0.76% Politikmagazin
    8532.1h  0.75% Wissensmagazin
    8528.7h  0.75% Börsenmagazin
    7611.7h  0.67% Wirtschaftsmagazin
    7500.4h  0.66% Telenovela
    7437.2h  0.65% Arztserie
