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

**108** channels, **867,050.5** hours playtime between **2023-01-17** and **2024-05-23**


### playtime per genre (top 30)

    56638.8h 6.53% Nachrichten
    41232.6h 4.76% Verkaufsshow
    35282.5h 4.07% Krimiserie
    30380.7h 3.50% Werbesendung
    27297.7h 3.15% Dokureihe
    26214.1h 3.02% Dokusoap
    25209.1h 2.91% Regionalmagazin
    22509.5h 2.60% Dokumentation
    22006.2h 2.54% *unknown*
    15937.3h 1.84% Zeichentrickserie
    15763.5h 1.82% Infomercial
    15439.9h 1.78% Animationsserie
    13039.0h 1.50% Comedyserie
    12318.8h 1.42% Magazin
    12207.6h 1.41% Morgenmagazin
    11726.4h 1.35% Religionsmagazin
    11542.6h 1.33% Talkshow
    8584.2h  0.99% E-Sport
    8011.6h  0.92% Sitcom
    8007.1h  0.92% Programmende
    7712.9h  0.89% Wetterbericht
    7612.1h  0.88% Börsenmagazin
    7500.9h  0.87% Quiz
    7482.7h  0.86% Komödie
    6412.2h  0.74% Realityshow
    6410.7h  0.74% Wissensmagazin
    6366.2h  0.73% Politikmagazin
    6166.3h  0.71% Wirtschaftsmagazin
    6133.1h  0.71% Telenovela
    5738.1h  0.66% Musikmagazin
