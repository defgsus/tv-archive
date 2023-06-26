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

**96** channels, **290,898.6** hours playtime between **2023-01-17** and **2023-06-27**


### playtime per genre (top 30)

    19390.4h 6.67% Nachrichten
    13991.8h 4.81% Verkaufsshow
    11614.1h 3.99% Krimiserie
    9711.2h  3.34% Werbesendung
    9462.5h  3.25% Dokureihe
    8791.1h  3.02% Dokusoap
    8310.0h  2.86% Regionalmagazin
    7407.9h  2.55% Dokumentation
    7234.1h  2.49% *unknown*
    5550.1h  1.91% Zeichentrickserie
    5325.7h  1.83% Infomercial
    5131.4h  1.76% Animationsserie
    4823.9h  1.66% Comedyserie
    4046.4h  1.39% Morgenmagazin
    3845.8h  1.32% Talkshow
    3832.4h  1.32% Religionsmagazin
    3554.6h  1.22% Programmende
    3411.3h  1.17% Magazin
    2884.8h  0.99% E-Sport
    2753.7h  0.95% Sitcom
    2678.6h  0.92% Wetterbericht
    2575.9h  0.89% Börsenmagazin
    2291.6h  0.79% Quiz
    2274.4h  0.78% Wirtschaftsmagazin
    2273.3h  0.78% Musikmagazin
    2233.5h  0.77% Wissensmagazin
    2194.3h  0.75% Komödie
    2052.9h  0.71% Telenovela
    1961.2h  0.67% Sportmagazin
    1913.3h  0.66% Wirtschaftstalk
