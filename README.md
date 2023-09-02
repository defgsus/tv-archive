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

**97** channels, **412,748.0** hours playtime between **2023-01-17** and **2023-09-03**


### playtime per genre (top 30)

    27248.8h 6.60% Nachrichten
    19539.5h 4.73% Verkaufsshow
    16768.8h 4.06% Krimiserie
    13919.2h 3.37% Werbesendung
    13629.9h 3.30% Dokureihe
    12529.9h 3.04% Dokusoap
    11864.1h 2.87% Regionalmagazin
    10457.1h 2.53% Dokumentation
    9920.3h  2.40% *unknown*
    7793.3h  1.89% Zeichentrickserie
    7539.7h  1.83% Infomercial
    7301.6h  1.77% Animationsserie
    6715.1h  1.63% Comedyserie
    5820.2h  1.41% Morgenmagazin
    5507.5h  1.33% Religionsmagazin
    5427.8h  1.32% Talkshow
    5140.9h  1.25% Magazin
    4495.0h  1.09% Programmende
    4074.7h  0.99% E-Sport
    3905.8h  0.95% Wetterbericht
    3865.7h  0.94% Sitcom
    3719.6h  0.90% Börsenmagazin
    3365.8h  0.82% Quiz
    3272.2h  0.79% Musikmagazin
    3223.8h  0.78% Komödie
    3133.8h  0.76% Wirtschaftsmagazin
    3087.3h  0.75% Wissensmagazin
    2896.7h  0.70% Telenovela
    2717.0h  0.66% Reportagereihe
    2661.7h  0.64% Politikmagazin
