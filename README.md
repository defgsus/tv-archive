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

**96** channels, **71,998.5** hours playtime between **2023-01-17** and **2023-02-25**


### playtime per genre (top 30)

    5122.8h 7.12% Nachrichten
    3666.5h 5.09% Verkaufsshow
    3064.2h 4.26% Krimiserie
    2440.8h 3.39% Werbesendung
    2418.9h 3.36% Dokusoap
    2138.1h 2.97% Regionalmagazin
    2117.0h 2.94% Dokureihe
    1758.2h 2.44% *unknown*
    1739.5h 2.42% Dokumentation
    1349.6h 1.87% Animationsserie
    1337.2h 1.86% Zeichentrickserie
    1319.1h 1.83% Infomercial
    1190.0h 1.65% Comedyserie
    1046.1h 1.45% Morgenmagazin
    954.9h  1.33% Programmende
    951.5h  1.32% Talkshow
    936.9h  1.30% Religionsmagazin
    777.2h  1.08% Magazin
    744.2h  1.03% E-Sport
    683.6h  0.95% Sitcom
    642.4h  0.89% Börsenmagazin
    636.9h  0.88% Wetterbericht
    593.2h  0.82% Wirtschaftsmagazin
    563.6h  0.78% Wissensmagazin
    543.8h  0.76% Quiz
    531.8h  0.74% Dramaserie
    528.5h  0.73% Musikmagazin
    510.0h  0.71% Gesundheitsmagazin
    505.8h  0.70% Telenovela
    470.2h  0.65% Gerichtsshow
