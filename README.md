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

**97** channels, **575,843.3** hours playtime between **2023-01-17** and **2023-12-04**


### playtime per genre (top 30)

    37831.6h 6.57% Nachrichten
    27567.6h 4.79% Verkaufsshow
    23235.4h 4.04% Krimiserie
    19573.3h 3.40% Werbesendung
    18743.7h 3.26% Dokureihe
    17359.0h 3.01% Dokusoap
    16632.3h 2.89% Regionalmagazin
    14700.2h 2.55% Dokumentation
    14077.7h 2.44% *unknown*
    10651.5h 1.85% Zeichentrickserie
    10494.0h 1.82% Infomercial
    10241.5h 1.78% Animationsserie
    8917.4h  1.55% Comedyserie
    8182.9h  1.42% Morgenmagazin
    7794.8h  1.35% Religionsmagazin
    7708.6h  1.34% Talkshow
    7395.0h  1.28% Magazin
    5742.5h  1.00% Programmende
    5637.2h  0.98% E-Sport
    5544.3h  0.96% Sitcom
    5274.0h  0.92% Wetterbericht
    5216.4h  0.91% Börsenmagazin
    4780.4h  0.83% Quiz
    4469.0h  0.78% Komödie
    4381.6h  0.76% Wissensmagazin
    4307.1h  0.75% Wirtschaftsmagazin
    4209.4h  0.73% Musikmagazin
    4164.0h  0.72% Telenovela
    4076.2h  0.71% Realityshow
    4060.6h  0.71% Politikmagazin
