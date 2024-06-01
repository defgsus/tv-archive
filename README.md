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

**108** channels, **881,777.2** hours playtime between **2023-01-17** and **2024-06-02**


### playtime per genre (top 30)

    57613.6h 6.53% Nachrichten
    41800.0h 4.74% Verkaufsshow
    35885.2h 4.07% Krimiserie
    30966.3h 3.51% Werbesendung
    27771.2h 3.15% Dokureihe
    26666.3h 3.02% Dokusoap
    25615.6h 2.90% Regionalmagazin
    22895.1h 2.60% Dokumentation
    22327.2h 2.53% *unknown*
    16210.4h 1.84% Zeichentrickserie
    16042.6h 1.82% Infomercial
    15712.0h 1.78% Animationsserie
    13237.5h 1.50% Comedyserie
    12545.8h 1.42% Magazin
    12409.3h 1.41% Morgenmagazin
    11922.2h 1.35% Religionsmagazin
    11740.6h 1.33% Talkshow
    8738.9h  0.99% E-Sport
    8171.3h  0.93% Sitcom
    8117.2h  0.92% Programmende
    7850.0h  0.89% Wetterbericht
    7724.5h  0.88% Börsenmagazin
    7634.0h  0.87% Quiz
    7620.6h  0.86% Komödie
    6515.3h  0.74% Wissensmagazin
    6506.4h  0.74% Realityshow
    6496.5h  0.74% Politikmagazin
    6245.0h  0.71% Wirtschaftsmagazin
    6192.4h  0.70% Telenovela
    5828.7h  0.66% Musikmagazin
