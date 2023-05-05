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

**96** channels, **197,579.5** hours playtime between **2023-01-17** and **2023-05-06**


### playtime per genre (top 30)

    13414.1h 6.79% Nachrichten
    9664.8h  4.89% Verkaufsshow
    8051.4h  4.08% Krimiserie
    6567.2h  3.32% Werbesendung
    6378.7h  3.23% Dokureihe
    5886.9h  2.98% Dokusoap
    5716.9h  2.89% Regionalmagazin
    4998.2h  2.53% Dokumentation
    4801.5h  2.43% *unknown*
    3660.4h  1.85% Zeichentrickserie
    3616.4h  1.83% Infomercial
    3590.7h  1.82% Animationsserie
    3308.9h  1.67% Comedyserie
    2753.5h  1.39% Morgenmagazin
    2721.6h  1.38% Programmende
    2605.5h  1.32% Talkshow
    2573.1h  1.30% Religionsmagazin
    2207.4h  1.12% Magazin
    1985.0h  1.00% E-Sport
    1873.7h  0.95% Sitcom
    1796.4h  0.91% Börsenmagazin
    1787.7h  0.90% Wetterbericht
    1573.0h  0.80% Wirtschaftsmagazin
    1548.2h  0.78% Wissensmagazin
    1522.1h  0.77% Quiz
    1519.5h  0.77% Musikmagazin
    1403.9h  0.71% Telenovela
    1366.3h  0.69% Sportmagazin
    1365.7h  0.69% Gesundheitsmagazin
    1344.7h  0.68% Komödie
