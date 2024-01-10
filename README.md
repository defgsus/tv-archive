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

**98** channels, **643,554.1** hours playtime between **2023-01-17** and **2024-01-11**


### playtime per genre (top 30)

    42005.9h 6.53% Nachrichten
    30747.4h 4.78% Verkaufsshow
    25789.0h 4.01% Krimiserie
    21898.8h 3.40% Werbesendung
    20911.9h 3.25% Dokureihe
    19222.4h 2.99% Dokusoap
    18496.1h 2.87% Regionalmagazin
    16739.1h 2.60% Dokumentation
    16014.1h 2.49% *unknown*
    11882.4h 1.85% Zeichentrickserie
    11669.5h 1.81% Infomercial
    11311.7h 1.76% Animationsserie
    9760.4h  1.52% Comedyserie
    9100.9h  1.41% Morgenmagazin
    8704.1h  1.35% Religionsmagazin
    8492.9h  1.32% Talkshow
    8462.5h  1.31% Magazin
    6333.9h  0.98% E-Sport
    6268.1h  0.97% Programmende
    6232.4h  0.97% Sitcom
    5842.7h  0.91% Wetterbericht
    5746.9h  0.89% Börsenmagazin
    5460.8h  0.85% Komödie
    5303.7h  0.82% Quiz
    4845.3h  0.75% Wissensmagazin
    4722.9h  0.73% Wirtschaftsmagazin
    4679.9h  0.73% Realityshow
    4589.0h  0.71% Musikmagazin
    4581.0h  0.71% Telenovela
    4532.7h  0.70% Politikmagazin
