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

**96** channels, **278,394.7** hours playtime between **2023-01-17** and **2023-06-20**


### playtime per genre (top 30)

    18530.2h 6.66% Nachrichten
    13424.8h 4.82% Verkaufsshow
    11114.3h 3.99% Krimiserie
    9265.7h  3.33% Werbesendung
    9069.8h  3.26% Dokureihe
    8369.4h  3.01% Dokusoap
    7942.5h  2.85% Regionalmagazin
    7130.7h  2.56% Dokumentation
    6950.1h  2.50% *unknown*
    5296.2h  1.90% Zeichentrickserie
    5098.0h  1.83% Infomercial
    4924.5h  1.77% Animationsserie
    4613.9h  1.66% Comedyserie
    3859.8h  1.39% Morgenmagazin
    3682.4h  1.32% Talkshow
    3662.6h  1.32% Religionsmagazin
    3458.5h  1.24% Programmende
    3241.0h  1.16% Magazin
    2782.3h  1.00% E-Sport
    2630.2h  0.94% Sitcom
    2557.3h  0.92% Wetterbericht
    2481.7h  0.89% Börsenmagazin
    2180.3h  0.78% Quiz
    2179.7h  0.78% Wirtschaftsmagazin
    2168.4h  0.78% Musikmagazin
    2144.0h  0.77% Wissensmagazin
    2089.4h  0.75% Komödie
    1964.2h  0.71% Telenovela
    1881.9h  0.68% Sportmagazin
    1811.4h  0.65% Wirtschaftstalk
