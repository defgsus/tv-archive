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

**109** channels, **1,206,622.5** hours playtime between **2023-01-17** and **2024-12-31**


### playtime per genre (top 30)

    78874.7h 6.54% Nachrichten
    54749.4h 4.54% Verkaufsshow
    50128.8h 4.15% Krimiserie
    44669.2h 3.70% Werbesendung
    37525.6h 3.11% Dokureihe
    35522.0h 2.94% Dokusoap
    35203.5h 2.92% Regionalmagazin
    32069.3h 2.66% Dokumentation
    28614.7h 2.37% *unknown*
    22649.7h 1.88% Zeichentrickserie
    22340.4h 1.85% Infomercial
    21556.3h 1.79% Animationsserie
    17017.2h 1.41% Comedyserie
    16864.3h 1.40% Morgenmagazin
    15945.9h 1.32% Talkshow
    15848.5h 1.31% Religionsmagazin
    14767.7h 1.22% Magazin
    11926.3h 0.99% E-Sport
    11560.9h 0.96% Sitcom
    10978.0h 0.91% Komödie
    10917.5h 0.90% Wetterbericht
    10681.0h 0.89% Quiz
    10611.0h 0.88% Programmende
    9305.4h  0.77% Realityshow
    9189.1h  0.76% Politikmagazin
    8985.7h  0.74% Wissensmagazin
    8734.4h  0.72% Börsenmagazin
    8003.1h  0.66% Wirtschaftsmagazin
    7998.9h  0.66% Arztserie
    7983.4h  0.66% Dramaserie
