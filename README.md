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

**96** channels, **283,738.4** hours playtime between **2023-01-17** and **2023-06-23**


### playtime per genre (top 30)

    18943.8h 6.68% Nachrichten
    13661.2h 4.81% Verkaufsshow
    11344.6h 4.00% Krimiserie
    9459.1h  3.33% Werbesendung
    9220.2h  3.25% Dokureihe
    8576.4h  3.02% Dokusoap
    8131.5h  2.87% Regionalmagazin
    7246.7h  2.55% Dokumentation
    7057.2h  2.49% *unknown*
    5404.6h  1.90% Zeichentrickserie
    5196.9h  1.83% Infomercial
    5012.6h  1.77% Animationsserie
    4716.9h  1.66% Comedyserie
    3963.5h  1.40% Morgenmagazin
    3750.6h  1.32% Talkshow
    3727.3h  1.31% Religionsmagazin
    3499.6h  1.23% Programmende
    3316.6h  1.17% Magazin
    2825.5h  1.00% E-Sport
    2692.2h  0.95% Sitcom
    2611.2h  0.92% Wetterbericht
    2535.4h  0.89% Börsenmagazin
    2227.9h  0.79% Wirtschaftsmagazin
    2224.3h  0.78% Quiz
    2215.4h  0.78% Musikmagazin
    2184.6h  0.77% Wissensmagazin
    2125.6h  0.75% Komödie
    2016.1h  0.71% Telenovela
    1911.5h  0.67% Sportmagazin
    1847.9h  0.65% Wirtschaftstalk
