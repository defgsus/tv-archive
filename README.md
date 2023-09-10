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

**97** channels, **427,082.3** hours playtime between **2023-01-17** and **2023-09-11**


### playtime per genre (top 30)

    28159.1h 6.59% Nachrichten
    20244.6h 4.74% Verkaufsshow
    17319.5h 4.06% Krimiserie
    14419.4h 3.38% Werbesendung
    14075.5h 3.30% Dokureihe
    12975.5h 3.04% Dokusoap
    12266.9h 2.87% Regionalmagazin
    10775.8h 2.52% Dokumentation
    10176.4h 2.38% *unknown*
    8066.5h  1.89% Zeichentrickserie
    7795.3h  1.83% Infomercial
    7561.8h  1.77% Animationsserie
    6913.4h  1.62% Comedyserie
    6014.8h  1.41% Morgenmagazin
    5722.4h  1.34% Religionsmagazin
    5652.5h  1.32% Talkshow
    5338.7h  1.25% Magazin
    4605.7h  1.08% Programmende
    4227.2h  0.99% E-Sport
    4031.9h  0.94% Wetterbericht
    3999.6h  0.94% Sitcom
    3860.5h  0.90% Börsenmagazin
    3505.1h  0.82% Quiz
    3373.6h  0.79% Musikmagazin
    3336.3h  0.78% Komödie
    3231.6h  0.76% Wirtschaftsmagazin
    3189.5h  0.75% Wissensmagazin
    2996.0h  0.70% Telenovela
    2810.4h  0.66% Reportagereihe
    2766.2h  0.65% Politikmagazin
