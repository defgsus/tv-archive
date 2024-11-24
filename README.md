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

**109** channels, **1,153,286.2** hours playtime between **2023-01-17** and **2024-11-25**


### playtime per genre (top 30)

    75218.4h 6.52% Nachrichten
    52679.2h 4.57% Verkaufsshow
    48094.8h 4.17% Krimiserie
    42464.8h 3.68% Werbesendung
    35990.8h 3.12% Dokureihe
    34342.0h 2.98% Dokusoap
    33735.0h 2.93% Regionalmagazin
    30322.5h 2.63% Dokumentation
    27217.8h 2.36% *unknown*
    21598.8h 1.87% Zeichentrickserie
    21295.6h 1.85% Infomercial
    20608.1h 1.79% Animationsserie
    16491.9h 1.43% Comedyserie
    16120.4h 1.40% Morgenmagazin
    15372.8h 1.33% Religionsmagazin
    15292.7h 1.33% Talkshow
    14395.5h 1.25% Magazin
    11402.5h 0.99% E-Sport
    11137.9h 0.97% Sitcom
    10419.8h 0.90% Wetterbericht
    10190.5h 0.88% Programmende
    10179.1h 0.88% Quiz
    10129.8h 0.88% Komödie
    8850.6h  0.77% Realityshow
    8747.1h  0.76% Politikmagazin
    8671.5h  0.75% Wissensmagazin
    8578.7h  0.74% Börsenmagazin
    7711.2h  0.67% Wirtschaftsmagazin
    7614.5h  0.66% Telenovela
    7581.8h  0.66% Dramaserie
