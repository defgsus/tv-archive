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

**97** channels, **398,536.8** hours playtime between **2023-01-17** and **2023-08-26**


### playtime per genre (top 30)

    26378.8h 6.62% Nachrichten
    18810.1h 4.72% Verkaufsshow
    16146.0h 4.05% Krimiserie
    13416.8h 3.37% Werbesendung
    13202.5h 3.31% Dokureihe
    12095.5h 3.03% Dokusoap
    11465.5h 2.88% Regionalmagazin
    10095.4h 2.53% Dokumentation
    9627.3h  2.42% *unknown*
    7519.8h  1.89% Zeichentrickserie
    7277.8h  1.83% Infomercial
    7046.7h  1.77% Animationsserie
    6507.5h  1.63% Comedyserie
    5633.6h  1.41% Morgenmagazin
    5305.3h  1.33% Religionsmagazin
    5238.7h  1.31% Talkshow
    4982.2h  1.25% Magazin
    4383.1h  1.10% Programmende
    3951.0h  0.99% E-Sport
    3769.4h  0.95% Wetterbericht
    3733.4h  0.94% Sitcom
    3605.6h  0.90% Börsenmagazin
    3245.9h  0.81% Quiz
    3145.3h  0.79% Musikmagazin
    3091.8h  0.78% Komödie
    3042.4h  0.76% Wirtschaftsmagazin
    2981.4h  0.75% Wissensmagazin
    2802.2h  0.70% Telenovela
    2621.7h  0.66% Reportagereihe
    2569.8h  0.64% Politikmagazin
