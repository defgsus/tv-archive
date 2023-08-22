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

**97** channels, **393,106.3** hours playtime between **2023-01-17** and **2023-08-23**


### playtime per genre (top 30)

    25987.5h 6.61% Nachrichten
    18528.8h 4.71% Verkaufsshow
    15948.0h 4.06% Krimiserie
    13240.8h 3.37% Werbesendung
    13032.8h 3.32% Dokureihe
    11883.2h 3.02% Dokusoap
    11276.5h 2.87% Regionalmagazin
    9945.0h  2.53% Dokumentation
    9531.8h  2.42% *unknown*
    7428.4h  1.89% Zeichentrickserie
    7180.2h  1.83% Infomercial
    6943.1h  1.77% Animationsserie
    6418.2h  1.63% Comedyserie
    5534.6h  1.41% Morgenmagazin
    5240.9h  1.33% Religionsmagazin
    5164.6h  1.31% Talkshow
    4890.8h  1.24% Magazin
    4343.6h  1.10% Programmende
    3900.7h  0.99% E-Sport
    3714.1h  0.94% Wetterbericht
    3678.2h  0.94% Sitcom
    3553.5h  0.90% Börsenmagazin
    3181.1h  0.81% Quiz
    3103.4h  0.79% Musikmagazin
    3044.9h  0.77% Komödie
    2995.5h  0.76% Wirtschaftsmagazin
    2942.4h  0.75% Wissensmagazin
    2745.2h  0.70% Telenovela
    2587.1h  0.66% Reportagereihe
    2532.0h  0.64% Sportmagazin
