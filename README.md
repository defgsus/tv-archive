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

**109** channels, **1,150,125.8** hours playtime between **2023-01-17** and **2024-11-22**


### playtime per genre (top 30)

    75040.5h 6.52% Nachrichten
    52551.8h 4.57% Verkaufsshow
    47999.0h 4.17% Krimiserie
    42341.3h 3.68% Werbesendung
    35866.8h 3.12% Dokureihe
    34272.0h 2.98% Dokusoap
    33677.2h 2.93% Regionalmagazin
    30222.0h 2.63% Dokumentation
    27141.6h 2.36% *unknown*
    21528.9h 1.87% Zeichentrickserie
    21223.9h 1.85% Infomercial
    20548.0h 1.79% Animationsserie
    16474.1h 1.43% Comedyserie
    16102.9h 1.40% Morgenmagazin
    15322.6h 1.33% Religionsmagazin
    15243.9h 1.33% Talkshow
    14358.0h 1.25% Magazin
    11364.1h 0.99% E-Sport
    11134.0h 0.97% Sitcom
    10405.1h 0.90% Wetterbericht
    10177.6h 0.88% Quiz
    10162.0h 0.88% Programmende
    10092.1h 0.88% Komödie
    8838.0h  0.77% Realityshow
    8740.5h  0.76% Politikmagazin
    8649.2h  0.75% Wissensmagazin
    8578.9h  0.75% Börsenmagazin
    7706.0h  0.67% Wirtschaftsmagazin
    7614.7h  0.66% Telenovela
    7584.7h  0.66% Dramaserie
