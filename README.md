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

**97** channels, **409,160.8** hours playtime between **2023-01-17** and **2023-09-01**


### playtime per genre (top 30)

    27034.5h 6.61% Nachrichten
    19358.5h 4.73% Verkaufsshow
    16616.3h 4.06% Krimiserie
    13792.7h 3.37% Werbesendung
    13520.6h 3.30% Dokureihe
    12425.3h 3.04% Dokusoap
    11780.1h 2.88% Regionalmagazin
    10366.2h 2.53% Dokumentation
    9852.7h  2.41% *unknown*
    7714.4h  1.89% Zeichentrickserie
    7473.5h  1.83% Infomercial
    7238.1h  1.77% Animationsserie
    6667.8h  1.63% Comedyserie
    5779.4h  1.41% Morgenmagazin
    5460.9h  1.33% Religionsmagazin
    5376.2h  1.31% Talkshow
    5095.6h  1.25% Magazin
    4467.9h  1.09% Programmende
    4061.4h  0.99% E-Sport
    3873.1h  0.95% Wetterbericht
    3832.8h  0.94% Sitcom
    3703.5h  0.91% Börsenmagazin
    3343.5h  0.82% Quiz
    3247.5h  0.79% Musikmagazin
    3174.0h  0.78% Komödie
    3113.9h  0.76% Wirtschaftsmagazin
    3063.5h  0.75% Wissensmagazin
    2875.6h  0.70% Telenovela
    2691.8h  0.66% Reportagereihe
    2647.1h  0.65% Politikmagazin
