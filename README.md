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

**97** channels, **584,790.2** hours playtime between **2023-01-17** and **2023-12-09**


### playtime per genre (top 30)

    38467.8h 6.58% Nachrichten
    28045.2h 4.80% Verkaufsshow
    23643.8h 4.04% Krimiserie
    19867.7h 3.40% Werbesendung
    19027.3h 3.25% Dokureihe
    17630.5h 3.01% Dokusoap
    16939.2h 2.90% Regionalmagazin
    14941.5h 2.56% Dokumentation
    14289.8h 2.44% *unknown*
    10801.6h 1.85% Zeichentrickserie
    10656.1h 1.82% Infomercial
    10382.2h 1.78% Animationsserie
    9037.6h  1.55% Comedyserie
    8356.7h  1.43% Morgenmagazin
    7906.0h  1.35% Religionsmagazin
    7836.4h  1.34% Talkshow
    7529.4h  1.29% Magazin
    5811.2h  0.99% Programmende
    5735.2h  0.98% E-Sport
    5653.8h  0.97% Sitcom
    5359.1h  0.92% Wetterbericht
    5312.1h  0.91% Börsenmagazin
    4867.9h  0.83% Quiz
    4539.4h  0.78% Komödie
    4456.9h  0.76% Wissensmagazin
    4381.9h  0.75% Wirtschaftsmagazin
    4255.7h  0.73% Telenovela
    4252.1h  0.73% Musikmagazin
    4189.0h  0.72% Realityshow
    4152.8h  0.71% Politikmagazin
