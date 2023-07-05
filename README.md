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

**96** channels, **306,996.7** hours playtime between **2023-01-17** and **2023-07-06**


### playtime per genre (top 30)

    20478.9h 6.67% Nachrichten
    14726.2h 4.80% Verkaufsshow
    12296.6h 4.01% Krimiserie
    10272.3h 3.35% Werbesendung
    9964.6h  3.25% Dokureihe
    9302.1h  3.03% Dokusoap
    8798.4h  2.87% Regionalmagazin
    7755.9h  2.53% Dokumentation
    7580.2h  2.47% *unknown*
    5855.2h  1.91% Zeichentrickserie
    5617.0h  1.83% Infomercial
    5409.9h  1.76% Animationsserie
    5106.4h  1.66% Comedyserie
    4303.2h  1.40% Morgenmagazin
    4076.8h  1.33% Talkshow
    4050.9h  1.32% Religionsmagazin
    3679.3h  1.20% Programmende
    3617.2h  1.18% Magazin
    3030.3h  0.99% E-Sport
    2910.7h  0.95% Sitcom
    2841.6h  0.93% Wetterbericht
    2735.9h  0.89% Börsenmagazin
    2431.6h  0.79% Quiz
    2408.4h  0.78% Musikmagazin
    2390.5h  0.78% Wirtschaftsmagazin
    2357.5h  0.77% Wissensmagazin
    2319.2h  0.76% Komödie
    2170.4h  0.71% Telenovela
    2050.7h  0.67% Sportmagazin
    1974.7h  0.64% Wirtschaftstalk
