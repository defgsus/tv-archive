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

**97** channels, **407,371.0** hours playtime between **2023-01-17** and **2023-08-31**


### playtime per genre (top 30)

    26901.5h 6.60% Nachrichten
    19264.5h 4.73% Verkaufsshow
    16543.9h 4.06% Krimiserie
    13737.0h 3.37% Werbesendung
    13482.9h 3.31% Dokureihe
    12349.1h 3.03% Dokusoap
    11715.0h 2.88% Regionalmagazin
    10316.5h 2.53% Dokumentation
    9819.5h  2.41% *unknown*
    7684.2h  1.89% Zeichentrickserie
    7440.0h  1.83% Infomercial
    7202.1h  1.77% Animationsserie
    6638.1h  1.63% Comedyserie
    5744.7h  1.41% Morgenmagazin
    5439.2h  1.34% Religionsmagazin
    5359.5h  1.32% Talkshow
    5065.4h  1.24% Magazin
    4454.5h  1.09% Programmende
    4047.0h  0.99% E-Sport
    3854.7h  0.95% Wetterbericht
    3816.5h  0.94% Sitcom
    3692.3h  0.91% Börsenmagazin
    3322.2h  0.82% Quiz
    3231.6h  0.79% Musikmagazin
    3172.2h  0.78% Komödie
    3097.0h  0.76% Wirtschaftsmagazin
    3048.1h  0.75% Wissensmagazin
    2856.4h  0.70% Telenovela
    2674.0h  0.66% Reportagereihe
    2631.9h  0.65% Politikmagazin
