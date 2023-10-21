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

**97** channels, **500,409.7** hours playtime between **2023-01-17** and **2023-10-22**


### playtime per genre (top 30)

    32969.6h 6.59% Nachrichten
    23895.8h 4.78% Verkaufsshow
    20137.2h 4.02% Krimiserie
    16914.8h 3.38% Werbesendung
    16452.8h 3.29% Dokureihe
    15270.6h 3.05% Dokusoap
    14431.9h 2.88% Regionalmagazin
    12660.2h 2.53% Dokumentation
    12037.6h 2.41% *unknown*
    9361.2h  1.87% Zeichentrickserie
    9114.7h  1.82% Infomercial
    8931.8h  1.78% Animationsserie
    7958.6h  1.59% Comedyserie
    7082.4h  1.42% Morgenmagazin
    6719.3h  1.34% Religionsmagazin
    6662.6h  1.33% Talkshow
    6284.6h  1.26% Magazin
    5167.2h  1.03% Programmende
    4921.8h  0.98% E-Sport
    4771.0h  0.95% Sitcom
    4651.4h  0.93% Wetterbericht
    4510.7h  0.90% Börsenmagazin
    4201.6h  0.84% Quiz
    3884.4h  0.78% Komödie
    3776.5h  0.75% Musikmagazin
    3776.3h  0.75% Wissensmagazin
    3772.6h  0.75% Wirtschaftsmagazin
    3583.1h  0.72% Telenovela
    3429.8h  0.69% Politikmagazin
    3272.8h  0.65% Realityshow
