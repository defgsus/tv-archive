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

**96** channels, **303,399.9** hours playtime between **2023-01-17** and **2023-07-04**


### playtime per genre (top 30)

    20225.8h 6.67% Nachrichten
    14561.3h 4.80% Verkaufsshow
    12132.8h 4.00% Krimiserie
    10142.9h 3.34% Werbesendung
    9841.4h  3.24% Dokureihe
    9202.0h  3.03% Dokusoap
    8670.8h  2.86% Regionalmagazin
    7678.6h  2.53% Dokumentation
    7509.0h  2.47% *unknown*
    5786.7h  1.91% Zeichentrickserie
    5552.4h  1.83% Infomercial
    5346.4h  1.76% Animationsserie
    5044.3h  1.66% Comedyserie
    4233.8h  1.40% Morgenmagazin
    4032.3h  1.33% Talkshow
    4005.7h  1.32% Religionsmagazin
    3651.8h  1.20% Programmende
    3571.5h  1.18% Magazin
    2995.0h  0.99% E-Sport
    2869.6h  0.95% Sitcom
    2804.8h  0.92% Wetterbericht
    2686.6h  0.89% Börsenmagazin
    2401.1h  0.79% Quiz
    2378.2h  0.78% Musikmagazin
    2363.3h  0.78% Wirtschaftsmagazin
    2329.4h  0.77% Wissensmagazin
    2292.6h  0.76% Komödie
    2143.1h  0.71% Telenovela
    2029.5h  0.67% Sportmagazin
    1969.2h  0.65% Wirtschaftstalk
