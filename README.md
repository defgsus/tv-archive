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

**99** channels, **707,483.7** hours playtime between **2023-01-17** and **2024-02-16**


### playtime per genre (top 30)

    46109.6h 6.52% Nachrichten
    33965.3h 4.80% Verkaufsshow
    28653.0h 4.05% Krimiserie
    24309.7h 3.44% Werbesendung
    22735.6h 3.21% Dokureihe
    21310.6h 3.01% Dokusoap
    20491.5h 2.90% Regionalmagazin
    18233.5h 2.58% Dokumentation
    17895.6h 2.53% *unknown*
    13121.2h 1.85% Zeichentrickserie
    12859.2h 1.82% Infomercial
    12438.3h 1.76% Animationsserie
    10719.8h 1.52% Comedyserie
    10034.4h 1.42% Morgenmagazin
    9564.5h  1.35% Religionsmagazin
    9457.0h  1.34% Magazin
    9362.6h  1.32% Talkshow
    6967.4h  0.98% E-Sport
    6765.1h  0.96% Programmende
    6730.2h  0.95% Sitcom
    6302.3h  0.89% Börsenmagazin
    6301.2h  0.89% Wetterbericht
    5996.5h  0.85% Komödie
    5903.9h  0.83% Quiz
    5309.7h  0.75% Wissensmagazin
    5189.9h  0.73% Realityshow
    5154.2h  0.73% Wirtschaftsmagazin
    5073.0h  0.72% Politikmagazin
    5046.9h  0.71% Telenovela
    4909.4h  0.69% Musikmagazin
