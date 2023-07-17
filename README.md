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

**96** channels, **328,517.5** hours playtime between **2023-01-17** and **2023-07-18**


### playtime per genre (top 30)

    21845.8h 6.65% Nachrichten
    15707.8h 4.78% Verkaufsshow
    13170.8h 4.01% Krimiserie
    11022.8h 3.36% Werbesendung
    10725.6h 3.26% Dokureihe
    9946.8h  3.03% Dokusoap
    9396.4h  2.86% Regionalmagazin
    8267.1h  2.52% Dokumentation
    8049.7h  2.45% *unknown*
    6252.5h  1.90% Zeichentrickserie
    6004.1h  1.83% Infomercial
    5786.5h  1.76% Animationsserie
    5423.1h  1.65% Comedyserie
    4591.0h  1.40% Morgenmagazin
    4355.1h  1.33% Talkshow
    4354.0h  1.33% Religionsmagazin
    3909.7h  1.19% Magazin
    3845.3h  1.17% Programmende
    3253.6h  0.99% E-Sport
    3112.4h  0.95% Sitcom
    3064.3h  0.93% Wetterbericht
    2934.2h  0.89% Börsenmagazin
    2618.1h  0.80% Quiz
    2574.6h  0.78% Musikmagazin
    2539.6h  0.77% Wirtschaftsmagazin
    2516.6h  0.77% Wissensmagazin
    2498.6h  0.76% Komödie
    2281.3h  0.69% Telenovela
    2176.7h  0.66% Sportmagazin
    2095.7h  0.64% Reportagereihe
