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

**96** channels, **193,913.7** hours playtime between **2023-01-17** and **2023-05-04**


### playtime per genre (top 30)

    13143.9h 6.78% Nachrichten
    9466.3h  4.88% Verkaufsshow
    7907.6h  4.08% Krimiserie
    6445.8h  3.32% Werbesendung
    6266.5h  3.23% Dokureihe
    5761.2h  2.97% Dokusoap
    5598.4h  2.89% Regionalmagazin
    4920.9h  2.54% Dokumentation
    4710.4h  2.43% *unknown*
    3591.3h  1.85% Zeichentrickserie
    3545.4h  1.83% Infomercial
    3532.2h  1.82% Animationsserie
    3233.2h  1.67% Comedyserie
    2687.8h  1.39% Morgenmagazin
    2672.9h  1.38% Programmende
    2543.1h  1.31% Talkshow
    2526.6h  1.30% Religionsmagazin
    2156.2h  1.11% Magazin
    1949.5h  1.01% E-Sport
    1839.3h  0.95% Sitcom
    1760.4h  0.91% Börsenmagazin
    1753.7h  0.90% Wetterbericht
    1540.1h  0.79% Wirtschaftsmagazin
    1518.7h  0.78% Wissensmagazin
    1490.8h  0.77% Musikmagazin
    1488.2h  0.77% Quiz
    1362.7h  0.70% Telenovela
    1350.3h  0.70% Sportmagazin
    1340.7h  0.69% Gesundheitsmagazin
    1333.3h  0.69% Komödie
