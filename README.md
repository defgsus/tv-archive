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

**96** channels, **314,171.8** hours playtime between **2023-01-17** and **2023-07-10**


### playtime per genre (top 30)

    20903.8h 6.65% Nachrichten
    15045.4h 4.79% Verkaufsshow
    12581.6h 4.00% Krimiserie
    10538.2h 3.35% Werbesendung
    10226.2h 3.25% Dokureihe
    9521.2h  3.03% Dokusoap
    8971.9h  2.86% Regionalmagazin
    7917.9h  2.52% Dokumentation
    7744.0h  2.46% *unknown*
    5980.6h  1.90% Zeichentrickserie
    5752.4h  1.83% Infomercial
    5530.9h  1.76% Animationsserie
    5199.2h  1.65% Comedyserie
    4377.8h  1.39% Morgenmagazin
    4175.7h  1.33% Talkshow
    4159.6h  1.32% Religionsmagazin
    3734.9h  1.19% Programmende
    3723.2h  1.19% Magazin
    3104.8h  0.99% E-Sport
    2975.1h  0.95% Sitcom
    2912.3h  0.93% Wetterbericht
    2795.7h  0.89% Börsenmagazin
    2475.9h  0.79% Quiz
    2472.4h  0.79% Musikmagazin
    2436.8h  0.78% Wirtschaftsmagazin
    2407.8h  0.77% Wissensmagazin
    2407.2h  0.77% Komödie
    2198.6h  0.70% Telenovela
    2103.8h  0.67% Sportmagazin
    2004.2h  0.64% Wirtschaftstalk
