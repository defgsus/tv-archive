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

**96** channels, **285,534.8** hours playtime between **2023-01-17** and **2023-06-24**


### playtime per genre (top 30)

    19077.5h 6.68% Nachrichten
    13738.2h 4.81% Verkaufsshow
    11421.0h 4.00% Krimiserie
    9514.6h  3.33% Werbesendung
    9267.4h  3.25% Dokureihe
    8636.9h  3.02% Dokusoap
    8193.7h  2.87% Regionalmagazin
    7264.1h  2.54% Dokumentation
    7104.1h  2.49% *unknown*
    5440.1h  1.91% Zeichentrickserie
    5228.9h  1.83% Infomercial
    5042.1h  1.77% Animationsserie
    4741.4h  1.66% Comedyserie
    3997.8h  1.40% Morgenmagazin
    3771.9h  1.32% Talkshow
    3749.1h  1.31% Religionsmagazin
    3513.9h  1.23% Programmende
    3349.9h  1.17% Magazin
    2842.7h  1.00% E-Sport
    2707.7h  0.95% Sitcom
    2629.0h  0.92% Wetterbericht
    2546.7h  0.89% Börsenmagazin
    2243.9h  0.79% Wirtschaftsmagazin
    2242.3h  0.79% Quiz
    2232.0h  0.78% Musikmagazin
    2196.4h  0.77% Wissensmagazin
    2139.5h  0.75% Komödie
    2033.9h  0.71% Telenovela
    1918.6h  0.67% Sportmagazin
    1865.1h  0.65% Wirtschaftstalk
