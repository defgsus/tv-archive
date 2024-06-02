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

**108** channels, **883,593.7** hours playtime between **2023-01-17** and **2024-06-03**


### playtime per genre (top 30)

    57702.2h 6.53% Nachrichten
    41862.7h 4.74% Verkaufsshow
    35937.9h 4.07% Krimiserie
    31043.5h 3.51% Werbesendung
    27850.7h 3.15% Dokureihe
    26704.7h 3.02% Dokusoap
    25649.2h 2.90% Regionalmagazin
    22936.9h 2.60% Dokumentation
    22373.2h 2.53% *unknown*
    16243.2h 1.84% Zeichentrickserie
    16077.9h 1.82% Infomercial
    15743.0h 1.78% Animationsserie
    13251.1h 1.50% Comedyserie
    12577.5h 1.42% Magazin
    12416.5h 1.41% Morgenmagazin
    11966.1h 1.35% Religionsmagazin
    11776.7h 1.33% Talkshow
    8761.3h  0.99% E-Sport
    8182.2h  0.93% Sitcom
    8131.0h  0.92% Programmende
    7864.5h  0.89% Wetterbericht
    7724.5h  0.87% Börsenmagazin
    7641.0h  0.86% Quiz
    7639.9h  0.86% Komödie
    6550.5h  0.74% Wissensmagazin
    6524.0h  0.74% Realityshow
    6502.4h  0.74% Politikmagazin
    6252.2h  0.71% Wirtschaftsmagazin
    6192.8h  0.70% Telenovela
    5841.5h  0.66% Musikmagazin
