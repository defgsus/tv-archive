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

**96** channels, **305,149.8** hours playtime between **2023-01-17** and **2023-07-05**


### playtime per genre (top 30)

    20346.8h 6.67% Nachrichten
    14642.2h 4.80% Verkaufsshow
    12234.9h 4.01% Krimiserie
    10208.5h 3.35% Werbesendung
    9901.8h  3.24% Dokureihe
    9253.1h  3.03% Dokusoap
    8723.3h  2.86% Regionalmagazin
    7715.3h  2.53% Dokumentation
    7546.4h  2.47% *unknown*
    5820.3h  1.91% Zeichentrickserie
    5584.4h  1.83% Infomercial
    5381.5h  1.76% Animationsserie
    5071.6h  1.66% Comedyserie
    4268.5h  1.40% Morgenmagazin
    4052.1h  1.33% Talkshow
    4022.1h  1.32% Religionsmagazin
    3665.3h  1.20% Programmende
    3586.6h  1.18% Magazin
    3012.4h  0.99% E-Sport
    2887.8h  0.95% Sitcom
    2823.3h  0.93% Wetterbericht
    2712.6h  0.89% Börsenmagazin
    2413.7h  0.79% Quiz
    2396.8h  0.79% Musikmagazin
    2373.5h  0.78% Wirtschaftsmagazin
    2342.3h  0.77% Wissensmagazin
    2304.8h  0.76% Komödie
    2153.9h  0.71% Telenovela
    2031.7h  0.67% Sportmagazin
    1972.0h  0.65% Wirtschaftstalk
