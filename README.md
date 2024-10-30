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

**109** channels, **1,116,104.2** hours playtime between **2023-01-17** and **2024-10-31**


### playtime per genre (top 30)

    72698.6h 6.51% Nachrichten
    51353.6h 4.60% Verkaufsshow
    46412.9h 4.16% Krimiserie
    40917.9h 3.67% Werbesendung
    34883.2h 3.13% Dokureihe
    33378.3h 2.99% Dokusoap
    32658.9h 2.93% Regionalmagazin
    29277.5h 2.62% Dokumentation
    26433.1h 2.37% *unknown*
    20848.3h 1.87% Zeichentrickserie
    20547.5h 1.84% Infomercial
    19952.1h 1.79% Animationsserie
    16088.4h 1.44% Comedyserie
    15628.0h 1.40% Morgenmagazin
    14998.3h 1.34% Religionsmagazin
    14765.2h 1.32% Talkshow
    14098.5h 1.26% Magazin
    11035.1h 0.99% E-Sport
    10760.8h 0.96% Sitcom
    10103.7h 0.91% Wetterbericht
    9900.2h  0.89% Programmende
    9810.3h  0.88% Quiz
    9776.2h  0.88% Komödie
    8505.9h  0.76% Realityshow
    8472.0h  0.76% Börsenmagazin
    8449.8h  0.76% Politikmagazin
    8390.0h  0.75% Wissensmagazin
    7505.2h  0.67% Wirtschaftsmagazin
    7366.8h  0.66% Telenovela
    7300.1h  0.65% Dramaserie
