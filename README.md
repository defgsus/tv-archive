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

**96** channels, **323,125.5** hours playtime between **2023-01-17** and **2023-07-15**


### playtime per genre (top 30)

    21545.9h 6.67% Nachrichten
    15460.3h 4.78% Verkaufsshow
    12963.9h 4.01% Krimiserie
    10834.2h 3.35% Werbesendung
    10511.1h 3.25% Dokureihe
    9805.7h  3.03% Dokusoap
    9267.8h  2.87% Regionalmagazin
    8130.2h  2.52% Dokumentation
    7937.9h  2.46% *unknown*
    6148.7h  1.90% Zeichentrickserie
    5907.4h  1.83% Infomercial
    5689.9h  1.76% Animationsserie
    5362.8h  1.66% Comedyserie
    4550.1h  1.41% Morgenmagazin
    4291.2h  1.33% Talkshow
    4266.9h  1.32% Religionsmagazin
    3844.8h  1.19% Magazin
    3803.2h  1.18% Programmende
    3205.7h  0.99% E-Sport
    3067.9h  0.95% Sitcom
    3008.7h  0.93% Wetterbericht
    2886.0h  0.89% Börsenmagazin
    2573.3h  0.80% Quiz
    2537.5h  0.79% Musikmagazin
    2514.3h  0.78% Wirtschaftsmagazin
    2476.8h  0.77% Wissensmagazin
    2441.0h  0.76% Komödie
    2265.8h  0.70% Telenovela
    2146.9h  0.66% Sportmagazin
    2065.1h  0.64% Wirtschaftstalk
