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

**97** channels, **559,637.0** hours playtime between **2023-01-17** and **2023-11-24**


### playtime per genre (top 30)

    36853.1h 6.59% Nachrichten
    26778.0h 4.78% Verkaufsshow
    22580.9h 4.03% Krimiserie
    18981.1h 3.39% Werbesendung
    18248.2h 3.26% Dokureihe
    16931.2h 3.03% Dokusoap
    16202.9h 2.90% Regionalmagazin
    14278.6h 2.55% Dokumentation
    13622.2h 2.43% *unknown*
    10362.4h 1.85% Zeichentrickserie
    10198.2h 1.82% Infomercial
    9974.0h  1.78% Animationsserie
    8742.2h  1.56% Comedyserie
    7982.7h  1.43% Morgenmagazin
    7550.1h  1.35% Religionsmagazin
    7482.0h  1.34% Talkshow
    7154.9h  1.28% Magazin
    5624.2h  1.00% Programmende
    5477.9h  0.98% E-Sport
    5384.5h  0.96% Sitcom
    5136.4h  0.92% Wetterbericht
    5071.8h  0.91% Börsenmagazin
    4676.0h  0.84% Quiz
    4368.7h  0.78% Komödie
    4248.8h  0.76% Wissensmagazin
    4207.3h  0.75% Wirtschaftsmagazin
    4113.8h  0.74% Musikmagazin
    4056.8h  0.72% Telenovela
    3935.4h  0.70% Politikmagazin
    3907.2h  0.70% Realityshow
