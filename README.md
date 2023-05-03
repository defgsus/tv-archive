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

**96** channels, **193,962.8** hours playtime between **2023-01-17** and **2023-05-04**


### playtime per genre (top 30)

    13149.2h 6.78% Nachrichten
    9493.8h  4.89% Verkaufsshow
    7907.5h  4.08% Krimiserie
    6445.8h  3.32% Werbesendung
    6268.0h  3.23% Dokureihe
    5761.2h  2.97% Dokusoap
    5598.2h  2.89% Regionalmagazin
    4920.3h  2.54% Dokumentation
    4714.4h  2.43% *unknown*
    3591.6h  1.85% Zeichentrickserie
    3545.9h  1.83% Infomercial
    3531.8h  1.82% Animationsserie
    3233.2h  1.67% Comedyserie
    2687.8h  1.39% Morgenmagazin
    2672.9h  1.38% Programmende
    2542.9h  1.31% Talkshow
    2526.6h  1.30% Religionsmagazin
    2156.3h  1.11% Magazin
    1949.2h  1.00% E-Sport
    1839.4h  0.95% Sitcom
    1760.3h  0.91% Börsenmagazin
    1752.5h  0.90% Wetterbericht
    1540.1h  0.79% Wirtschaftsmagazin
    1518.7h  0.78% Wissensmagazin
    1490.8h  0.77% Musikmagazin
    1488.2h  0.77% Quiz
    1362.8h  0.70% Telenovela
    1349.8h  0.70% Sportmagazin
    1345.5h  0.69% Gesundheitsmagazin
    1333.3h  0.69% Komödie
