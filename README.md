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

**97** channels, **641,746.0** hours playtime between **2023-01-17** and **2024-01-10**


### playtime per genre (top 30)

    41868.7h 6.52% Nachrichten
    30665.4h 4.78% Verkaufsshow
    25719.8h 4.01% Krimiserie
    21834.6h 3.40% Werbesendung
    20860.2h 3.25% Dokureihe
    19183.3h 2.99% Dokusoap
    18429.5h 2.87% Regionalmagazin
    16686.5h 2.60% Dokumentation
    15965.1h 2.49% *unknown*
    11849.7h 1.85% Zeichentrickserie
    11635.8h 1.81% Infomercial
    11281.7h 1.76% Animationsserie
    9736.8h  1.52% Comedyserie
    9067.0h  1.41% Morgenmagazin
    8685.6h  1.35% Religionsmagazin
    8460.9h  1.32% Talkshow
    8415.0h  1.31% Magazin
    6322.7h  0.99% E-Sport
    6253.5h  0.97% Programmende
    6212.7h  0.97% Sitcom
    5829.0h  0.91% Wetterbericht
    5734.4h  0.89% Börsenmagazin
    5449.5h  0.85% Komödie
    5282.1h  0.82% Quiz
    4828.0h  0.75% Wissensmagazin
    4705.7h  0.73% Wirtschaftsmagazin
    4666.9h  0.73% Realityshow
    4584.3h  0.71% Musikmagazin
    4562.4h  0.71% Telenovela
    4513.5h  0.70% Politikmagazin
