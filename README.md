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

**109** channels, **937,928.9** hours playtime between **2023-01-17** and **2024-07-08**


### playtime per genre (top 30)

    61144.8h 6.52% Nachrichten
    43920.1h 4.68% Verkaufsshow
    38322.3h 4.09% Krimiserie
    33349.8h 3.56% Werbesendung
    29517.4h 3.15% Dokureihe
    28369.3h 3.02% Dokusoap
    27245.2h 2.90% Regionalmagazin
    24333.3h 2.59% Dokumentation
    23444.1h 2.50% *unknown*
    17286.5h 1.84% Zeichentrickserie
    17122.2h 1.83% Infomercial
    16771.1h 1.79% Animationsserie
    13975.4h 1.49% Comedyserie
    13332.7h 1.42% Magazin
    13191.4h 1.41% Morgenmagazin
    12720.6h 1.36% Religionsmagazin
    12445.1h 1.33% Talkshow
    9287.8h  0.99% E-Sport
    8809.1h  0.94% Sitcom
    8537.9h  0.91% Programmende
    8388.3h  0.89% Wetterbericht
    8162.2h  0.87% Komödie
    8093.4h  0.86% Quiz
    7895.5h  0.84% Börsenmagazin
    7062.6h  0.75% Politikmagazin
    6977.3h  0.74% Realityshow
    6976.1h  0.74% Wissensmagazin
    6534.8h  0.70% Wirtschaftsmagazin
    6367.9h  0.68% Telenovela
    6122.1h  0.65% Musikmagazin
