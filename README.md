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

**96** channels, **66,514.5** hours playtime between **2023-01-17** and **2023-02-22**


### playtime per genre (top 30)

    4692.4h 7.05% Nachrichten
    3395.2h 5.10% Verkaufsshow
    2812.4h 4.23% Krimiserie
    2266.5h 3.41% Werbesendung
    2241.2h 3.37% Dokusoap
    1953.1h 2.94% Dokureihe
    1927.8h 2.90% Regionalmagazin
    1637.2h 2.46% *unknown*
    1617.4h 2.43% Dokumentation
    1249.8h 1.88% Zeichentrickserie
    1232.5h 1.85% Animationsserie
    1221.0h 1.84% Infomercial
    1095.4h 1.65% Comedyserie
    941.8h  1.42% Morgenmagazin
    878.8h  1.32% Programmende
    874.7h  1.32% Religionsmagazin
    865.2h  1.30% Talkshow
    716.1h  1.08% Magazin
    690.2h  1.04% E-Sport
    621.8h  0.93% Sitcom
    586.5h  0.88% Börsenmagazin
    584.8h  0.88% Wetterbericht
    543.6h  0.82% Wirtschaftsmagazin
    513.4h  0.77% Wissensmagazin
    496.2h  0.75% Quiz
    491.3h  0.74% Musikmagazin
    481.1h  0.72% Dramaserie
    465.5h  0.70% Gesundheitsmagazin
    450.3h  0.68% Telenovela
    437.8h  0.66% Sportmagazin
