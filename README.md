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

**99** channels, **680,795.5** hours playtime between **2023-01-17** and **2024-02-01**


### playtime per genre (top 30)

    44390.8h 6.52% Nachrichten
    32616.2h 4.79% Verkaufsshow
    27428.3h 4.03% Krimiserie
    23317.4h 3.43% Werbesendung
    22033.0h 3.24% Dokureihe
    20411.0h 3.00% Dokusoap
    19681.8h 2.89% Regionalmagazin
    17576.2h 2.58% Dokumentation
    17108.9h 2.51% *unknown*
    12620.4h 1.85% Zeichentrickserie
    12369.9h 1.82% Infomercial
    11963.4h 1.76% Animationsserie
    10305.2h 1.51% Comedyserie
    9631.5h  1.41% Morgenmagazin
    9195.9h  1.35% Religionsmagazin
    9045.9h  1.33% Magazin
    9004.9h  1.32% Talkshow
    6693.9h  0.98% E-Sport
    6558.4h  0.96% Programmende
    6523.9h  0.96% Sitcom
    6103.4h  0.90% Wetterbericht
    6062.4h  0.89% Börsenmagazin
    5781.6h  0.85% Komödie
    5660.5h  0.83% Quiz
    5124.7h  0.75% Wissensmagazin
    4991.1h  0.73% Realityshow
    4969.1h  0.73% Wirtschaftsmagazin
    4851.7h  0.71% Telenovela
    4848.2h  0.71% Politikmagazin
    4774.6h  0.70% Musikmagazin
