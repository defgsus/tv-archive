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

**108** channels, **890,811.1** hours playtime between **2023-01-17** and **2024-06-07**


### playtime per genre (top 30)

    58245.3h 6.54% Nachrichten
    42116.7h 4.73% Verkaufsshow
    36256.3h 4.07% Krimiserie
    31358.8h 3.52% Werbesendung
    28044.1h 3.15% Dokureihe
    26943.3h 3.02% Dokusoap
    25922.8h 2.91% Regionalmagazin
    23125.2h 2.60% Dokumentation
    22513.7h 2.53% *unknown*
    16380.6h 1.84% Zeichentrickserie
    16215.8h 1.82% Infomercial
    15881.0h 1.78% Animationsserie
    13360.5h 1.50% Comedyserie
    12707.1h 1.43% Magazin
    12554.2h 1.41% Morgenmagazin
    12050.6h 1.35% Religionsmagazin
    11865.0h 1.33% Talkshow
    8824.1h  0.99% E-Sport
    8283.8h  0.93% Sitcom
    8186.1h  0.92% Programmende
    7939.8h  0.89% Wetterbericht
    7756.9h  0.87% Börsenmagazin
    7726.3h  0.87% Quiz
    7665.6h  0.86% Komödie
    6638.8h  0.75% Politikmagazin
    6603.8h  0.74% Wissensmagazin
    6600.4h  0.74% Realityshow
    6303.3h  0.71% Wirtschaftsmagazin
    6230.3h  0.70% Telenovela
    5879.7h  0.66% Musikmagazin
