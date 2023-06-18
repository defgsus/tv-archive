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

**96** channels, **276,610.2** hours playtime between **2023-01-17** and **2023-06-19**


### playtime per genre (top 30)

    18390.5h 6.65% Nachrichten
    13333.6h 4.82% Verkaufsshow
    11052.9h 4.00% Krimiserie
    9211.9h  3.33% Werbesendung
    9016.5h  3.26% Dokureihe
    8306.8h  3.00% Dokusoap
    7881.0h  2.85% Regionalmagazin
    7091.6h  2.56% Dokumentation
    6909.2h  2.50% *unknown*
    5257.0h  1.90% Zeichentrickserie
    5066.4h  1.83% Infomercial
    4896.5h  1.77% Animationsserie
    4574.0h  1.65% Comedyserie
    3825.0h  1.38% Morgenmagazin
    3661.3h  1.32% Talkshow
    3646.0h  1.32% Religionsmagazin
    3445.2h  1.25% Programmende
    3221.8h  1.16% Magazin
    2766.2h  1.00% E-Sport
    2610.7h  0.94% Sitcom
    2538.7h  0.92% Wetterbericht
    2459.8h  0.89% Börsenmagazin
    2166.5h  0.78% Wirtschaftsmagazin
    2156.1h  0.78% Musikmagazin
    2149.7h  0.78% Quiz
    2132.6h  0.77% Wissensmagazin
    2099.7h  0.76% Komödie
    1947.6h  0.70% Telenovela
    1872.4h  0.68% Sportmagazin
    1807.2h  0.65% Wirtschaftstalk
