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

**96** channels, **362,589.5** hours playtime between **2023-01-17** and **2023-08-06**


### playtime per genre (top 30)

    24021.0h 6.62% Nachrichten
    17262.6h 4.76% Verkaufsshow
    14644.6h 4.04% Krimiserie
    12213.0h 3.37% Werbesendung
    11896.5h 3.28% Dokureihe
    10967.2h 3.02% Dokusoap
    10396.1h 2.87% Regionalmagazin
    9144.4h  2.52% Dokumentation
    8833.8h  2.44% *unknown*
    6858.6h  1.89% Zeichentrickserie
    6631.7h  1.83% Infomercial
    6404.6h  1.77% Animationsserie
    5954.0h  1.64% Comedyserie
    5084.4h  1.40% Morgenmagazin
    4810.4h  1.33% Religionsmagazin
    4776.3h  1.32% Talkshow
    4330.2h  1.19% Magazin
    4108.9h  1.13% Programmende
    3589.3h  0.99% E-Sport
    3416.2h  0.94% Sitcom
    3407.7h  0.94% Wetterbericht
    3282.7h  0.91% Börsenmagazin
    2892.3h  0.80% Quiz
    2847.4h  0.79% Musikmagazin
    2783.2h  0.77% Wirtschaftsmagazin
    2775.1h  0.77% Komödie
    2728.8h  0.75% Wissensmagazin
    2511.6h  0.69% Telenovela
    2365.1h  0.65% Sportmagazin
    2340.1h  0.65% Reportagereihe
