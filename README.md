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

**97** channels, **414,539.3** hours playtime between **2023-01-17** and **2023-09-04**


### playtime per genre (top 30)

    27327.6h 6.59% Nachrichten
    19620.1h 4.73% Verkaufsshow
    16827.7h 4.06% Krimiserie
    13987.4h 3.37% Werbesendung
    13685.0h 3.30% Dokureihe
    12584.4h 3.04% Dokusoap
    11895.4h 2.87% Regionalmagazin
    10497.9h 2.53% Dokumentation
    9964.3h  2.40% *unknown*
    7830.4h  1.89% Zeichentrickserie
    7570.4h  1.83% Infomercial
    7334.2h  1.77% Animationsserie
    6733.6h  1.62% Comedyserie
    5828.5h  1.41% Morgenmagazin
    5550.3h  1.34% Religionsmagazin
    5466.4h  1.32% Talkshow
    5163.8h  1.25% Magazin
    4509.2h  1.09% Programmende
    4098.0h  0.99% E-Sport
    3921.2h  0.95% Wetterbericht
    3874.2h  0.93% Sitcom
    3737.6h  0.90% Börsenmagazin
    3371.6h  0.81% Quiz
    3293.6h  0.79% Musikmagazin
    3262.1h  0.79% Komödie
    3143.5h  0.76% Wirtschaftsmagazin
    3099.6h  0.75% Wissensmagazin
    2896.7h  0.70% Telenovela
    2735.6h  0.66% Reportagereihe
    2666.1h  0.64% Politikmagazin
