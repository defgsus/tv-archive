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

**102** channels, **834,737.1** hours playtime between **2023-01-17** and **2024-05-01**


### playtime per genre (top 30)

    54420.6h 6.52% Nachrichten
    39969.2h 4.79% Verkaufsshow
    34002.0h 4.07% Krimiserie
    29185.2h 3.50% Werbesendung
    26355.9h 3.16% Dokureihe
    25180.0h 3.02% Dokusoap
    24284.8h 2.91% Regionalmagazin
    21622.4h 2.59% Dokumentation
    21329.5h 2.56% *unknown*
    15334.6h 1.84% Zeichentrickserie
    15168.9h 1.82% Infomercial
    14864.0h 1.78% Animationsserie
    12623.7h 1.51% Comedyserie
    11770.9h 1.41% Morgenmagazin
    11733.6h 1.41% Magazin
    11278.9h 1.35% Religionsmagazin
    11114.6h 1.33% Talkshow
    8267.9h  0.99% E-Sport
    7757.6h  0.93% Programmende
    7674.1h  0.92% Sitcom
    7410.8h  0.89% Wetterbericht
    7347.1h  0.88% Börsenmagazin
    7217.5h  0.86% Quiz
    7109.8h  0.85% Komödie
    6174.4h  0.74% Wissensmagazin
    6119.8h  0.73% Politikmagazin
    6063.9h  0.73% Realityshow
    5964.6h  0.71% Wirtschaftsmagazin
    5963.9h  0.71% Telenovela
    5559.9h  0.67% Musikmagazin
