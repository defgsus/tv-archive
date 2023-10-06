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

**97** channels, **473,517.9** hours playtime between **2023-01-17** and **2023-10-07**


### playtime per genre (top 30)

    31235.7h 6.60% Nachrichten
    22567.7h 4.77% Verkaufsshow
    19084.0h 4.03% Krimiserie
    15974.1h 3.37% Werbesendung
    15614.2h 3.30% Dokureihe
    14477.8h 3.06% Dokusoap
    13655.0h 2.88% Regionalmagazin
    11946.5h 2.52% Dokumentation
    11302.1h 2.39% *unknown*
    8889.5h  1.88% Zeichentrickserie
    8623.6h  1.82% Infomercial
    8419.6h  1.78% Animationsserie
    7605.7h  1.61% Comedyserie
    6704.9h  1.42% Morgenmagazin
    6345.2h  1.34% Religionsmagazin
    6283.7h  1.33% Talkshow
    5901.4h  1.25% Magazin
    4959.4h  1.05% Programmende
    4676.8h  0.99% E-Sport
    4493.6h  0.95% Sitcom
    4427.6h  0.94% Wetterbericht
    4279.0h  0.90% Börsenmagazin
    3974.1h  0.84% Quiz
    3674.0h  0.78% Komödie
    3627.3h  0.77% Musikmagazin
    3578.6h  0.76% Wirtschaftsmagazin
    3562.4h  0.75% Wissensmagazin
    3376.8h  0.71% Telenovela
    3197.2h  0.68% Politikmagazin
    3079.5h  0.65% Reportagereihe
