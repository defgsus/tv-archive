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

**96** channels, **378,768.8** hours playtime between **2023-01-17** and **2023-08-15**


### playtime per genre (top 30)

    25051.3h 6.61% Nachrichten
    17914.6h 4.73% Verkaufsshow
    15326.3h 4.05% Krimiserie
    12766.2h 3.37% Werbesendung
    12503.0h 3.30% Dokureihe
    11450.9h 3.02% Dokusoap
    10854.3h 2.87% Regionalmagazin
    9561.0h  2.52% Dokumentation
    9201.0h  2.43% *unknown*
    7168.9h  1.89% Zeichentrickserie
    6920.5h  1.83% Infomercial
    6692.0h  1.77% Animationsserie
    6196.7h  1.64% Comedyserie
    5311.9h  1.40% Morgenmagazin
    5040.6h  1.33% Religionsmagazin
    4997.3h  1.32% Talkshow
    4638.6h  1.22% Magazin
    4229.8h  1.12% Programmende
    3751.2h  0.99% E-Sport
    3571.3h  0.94% Wetterbericht
    3549.4h  0.94% Sitcom
    3433.9h  0.91% Börsenmagazin
    3046.4h  0.80% Quiz
    2982.6h  0.79% Musikmagazin
    2912.7h  0.77% Komödie
    2896.3h  0.76% Wirtschaftsmagazin
    2845.8h  0.75% Wissensmagazin
    2623.9h  0.69% Telenovela
    2471.0h  0.65% Reportagereihe
    2445.3h  0.65% Sportmagazin
