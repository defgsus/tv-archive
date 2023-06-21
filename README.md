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

**96** channels, **281,952.9** hours playtime between **2023-01-17** and **2023-06-22**


### playtime per genre (top 30)

    18806.5h 6.67% Nachrichten
    13579.8h 4.82% Verkaufsshow
    11269.6h 4.00% Krimiserie
    9395.7h  3.33% Werbesendung
    9178.5h  3.26% Dokureihe
    8486.2h  3.01% Dokusoap
    8071.5h  2.86% Regionalmagazin
    7203.6h  2.55% Dokumentation
    7022.3h  2.49% *unknown*
    5369.0h  1.90% Zeichentrickserie
    5164.1h  1.83% Infomercial
    4982.6h  1.77% Animationsserie
    4680.1h  1.66% Comedyserie
    3929.2h  1.39% Morgenmagazin
    3726.6h  1.32% Talkshow
    3710.0h  1.32% Religionsmagazin
    3486.0h  1.24% Programmende
    3285.9h  1.17% Magazin
    2810.9h  1.00% E-Sport
    2673.2h  0.95% Sitcom
    2593.0h  0.92% Wetterbericht
    2524.8h  0.90% Börsenmagazin
    2210.7h  0.78% Wirtschaftsmagazin
    2208.4h  0.78% Quiz
    2198.9h  0.78% Musikmagazin
    2168.5h  0.77% Wissensmagazin
    2120.8h  0.75% Komödie
    1999.1h  0.71% Telenovela
    1905.2h  0.68% Sportmagazin
    1829.2h  0.65% Wirtschaftstalk
