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

**96** channels, **274,832.1** hours playtime between **2023-01-17** and **2023-06-18**


### playtime per genre (top 30)

    18308.0h 6.66% Nachrichten
    13250.4h 4.82% Verkaufsshow
    10993.9h 4.00% Krimiserie
    9147.6h  3.33% Werbesendung
    8951.1h  3.26% Dokureihe
    8257.2h  3.00% Dokusoap
    7847.5h  2.86% Regionalmagazin
    7041.6h  2.56% Dokumentation
    6862.1h  2.50% *unknown*
    5223.5h  1.90% Zeichentrickserie
    5034.8h  1.83% Infomercial
    4865.9h  1.77% Animationsserie
    4561.6h  1.66% Comedyserie
    3817.0h  1.39% Morgenmagazin
    3622.0h  1.32% Talkshow
    3601.1h  1.31% Religionsmagazin
    3430.6h  1.25% Programmende
    3197.2h  1.16% Magazin
    2756.1h  1.00% E-Sport
    2600.2h  0.95% Sitcom
    2522.3h  0.92% Wetterbericht
    2458.8h  0.89% Börsenmagazin
    2157.1h  0.78% Wirtschaftsmagazin
    2143.8h  0.78% Quiz
    2135.4h  0.78% Musikmagazin
    2117.3h  0.77% Wissensmagazin
    2060.4h  0.75% Komödie
    1947.6h  0.71% Telenovela
    1857.0h  0.68% Sportmagazin
    1784.2h  0.65% Wirtschaftstalk
