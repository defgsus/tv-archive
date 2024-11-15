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

**109** channels, **1,139,578.0** hours playtime between **2023-01-17** and **2024-11-16**


### playtime per genre (top 30)

    74286.9h 6.52% Nachrichten
    52166.5h 4.58% Verkaufsshow
    47507.7h 4.17% Krimiserie
    41903.1h 3.68% Werbesendung
    35563.7h 3.12% Dokureihe
    34008.7h 2.98% Dokusoap
    33353.7h 2.93% Regionalmagazin
    29943.9h 2.63% Dokumentation
    26940.3h 2.36% *unknown*
    21310.5h 1.87% Zeichentrickserie
    21005.3h 1.84% Infomercial
    20368.2h 1.79% Animationsserie
    16365.9h 1.44% Comedyserie
    15953.1h 1.40% Morgenmagazin
    15220.3h 1.34% Religionsmagazin
    15085.5h 1.32% Talkshow
    14274.2h 1.25% Magazin
    11255.8h 0.99% E-Sport
    11024.9h 0.97% Sitcom
    10309.4h 0.90% Wetterbericht
    10079.9h 0.88% Programmende
    10066.9h 0.88% Quiz
    10006.6h 0.88% Komödie
    8715.9h  0.76% Realityshow
    8649.8h  0.76% Politikmagazin
    8559.1h  0.75% Wissensmagazin
    8545.2h  0.75% Börsenmagazin
    7641.9h  0.67% Wirtschaftsmagazin
    7538.3h  0.66% Telenovela
    7478.3h  0.66% Dramaserie
