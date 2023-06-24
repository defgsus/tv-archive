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

**96** channels, **287,331.4** hours playtime between **2023-01-17** and **2023-06-25**


### playtime per genre (top 30)

    19162.7h 6.67% Nachrichten
    13818.2h 4.81% Verkaufsshow
    11489.2h 4.00% Krimiserie
    9586.5h  3.34% Werbesendung
    9337.2h  3.25% Dokureihe
    8676.0h  3.02% Dokusoap
    8215.0h  2.86% Regionalmagazin
    7314.6h  2.55% Dokumentation
    7133.6h  2.48% *unknown*
    5481.8h  1.91% Zeichentrickserie
    5263.8h  1.83% Infomercial
    5070.7h  1.76% Animationsserie
    4765.2h  1.66% Comedyserie
    4003.8h  1.39% Morgenmagazin
    3790.6h  1.32% Talkshow
    3774.4h  1.31% Religionsmagazin
    3527.8h  1.23% Programmende
    3366.9h  1.17% Magazin
    2847.3h  0.99% E-Sport
    2723.7h  0.95% Sitcom
    2646.8h  0.92% Wetterbericht
    2549.7h  0.89% Börsenmagazin
    2252.2h  0.78% Quiz
    2247.9h  0.78% Wirtschaftsmagazin
    2247.4h  0.78% Musikmagazin
    2204.5h  0.77% Wissensmagazin
    2170.5h  0.76% Komödie
    2036.0h  0.71% Telenovela
    1931.5h  0.67% Sportmagazin
    1886.1h  0.66% Wirtschaftstalk
