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

**109** channels, **1,171,874.9** hours playtime between **2023-01-17** and **2024-12-08**


### playtime per genre (top 30)

    76580.3h 6.53% Nachrichten
    53342.0h 4.55% Verkaufsshow
    48890.4h 4.17% Krimiserie
    43207.0h 3.69% Werbesendung
    36518.4h 3.12% Dokureihe
    34772.9h 2.97% Dokusoap
    34303.5h 2.93% Regionalmagazin
    30867.0h 2.63% Dokumentation
    27639.6h 2.36% *unknown*
    21970.7h 1.87% Zeichentrickserie
    21679.0h 1.85% Infomercial
    20953.8h 1.79% Animationsserie
    16688.3h 1.42% Comedyserie
    16416.5h 1.40% Morgenmagazin
    15547.8h 1.33% Talkshow
    15535.0h 1.33% Religionsmagazin
    14522.5h 1.24% Magazin
    11572.6h 0.99% E-Sport
    11303.6h 0.96% Sitcom
    10590.3h 0.90% Wetterbericht
    10361.8h 0.88% Quiz
    10342.1h 0.88% Programmende
    10305.9h 0.88% Komödie
    9023.7h  0.77% Realityshow
    8925.8h  0.76% Politikmagazin
    8784.5h  0.75% Wissensmagazin
    8647.0h  0.74% Börsenmagazin
    7830.4h  0.67% Wirtschaftsmagazin
    7767.9h  0.66% Telenovela
    7756.7h  0.66% Dramaserie
