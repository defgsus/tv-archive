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

**96** channels, **260,476.9** hours playtime between **2023-01-17** and **2023-06-10**


### playtime per genre (top 30)

    17400.5h 6.68% Nachrichten
    12564.8h 4.82% Verkaufsshow
    10433.1h 4.01% Krimiserie
    8647.6h  3.32% Werbesendung
    8500.1h  3.26% Dokureihe
    7817.2h  3.00% Dokusoap
    7452.2h  2.86% Regionalmagazin
    6662.6h  2.56% Dokumentation
    6508.5h  2.50% *unknown*
    4914.5h  1.89% Zeichentrickserie
    4770.4h  1.83% Infomercial
    4632.1h  1.78% Animationsserie
    4333.0h  1.66% Comedyserie
    3629.3h  1.39% Morgenmagazin
    3427.7h  1.32% Talkshow
    3410.4h  1.31% Religionsmagazin
    3320.8h  1.27% Programmende
    3040.4h  1.17% Magazin
    2604.8h  1.00% E-Sport
    2452.5h  0.94% Sitcom
    2385.7h  0.92% Wetterbericht
    2353.3h  0.90% Börsenmagazin
    2059.8h  0.79% Wirtschaftsmagazin
    2032.4h  0.78% Quiz
    2028.6h  0.78% Musikmagazin
    2012.0h  0.77% Wissensmagazin
    1923.0h  0.74% Komödie
    1856.6h  0.71% Telenovela
    1775.1h  0.68% Sportmagazin
    1699.1h  0.65% Gesundheitsmagazin
