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

**99** channels, **737,727.8** hours playtime between **2023-01-17** and **2024-03-04**


### playtime per genre (top 30)

    47978.5h 6.50% Nachrichten
    35412.1h 4.80% Verkaufsshow
    29974.9h 4.06% Krimiserie
    25523.4h 3.46% Werbesendung
    23618.8h 3.20% Dokureihe
    22287.9h 3.02% Dokusoap
    21372.5h 2.90% Regionalmagazin
    19012.2h 2.58% Dokumentation
    18939.5h 2.57% *unknown*
    13658.7h 1.85% Zeichentrickserie
    13414.4h 1.82% Infomercial
    12995.5h 1.76% Animationsserie
    11169.3h 1.51% Comedyserie
    10444.3h 1.42% Morgenmagazin
    9978.3h  1.35% Religionsmagazin
    9937.7h  1.35% Magazin
    9809.5h  1.33% Talkshow
    7291.4h  0.99% E-Sport
    7000.1h  0.95% Programmende
    6954.2h  0.94% Sitcom
    6583.3h  0.89% Börsenmagazin
    6557.9h  0.89% Wetterbericht
    6275.6h  0.85% Komödie
    6208.9h  0.84% Quiz
    5521.6h  0.75% Wissensmagazin
    5365.9h  0.73% Realityshow
    5340.9h  0.72% Wirtschaftsmagazin
    5306.8h  0.72% Politikmagazin
    5248.4h  0.71% Telenovela
    5062.7h  0.69% Musikmagazin
