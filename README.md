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

**99** channels, **721,706.4** hours playtime between **2023-01-17** and **2024-02-24**


### playtime per genre (top 30)

    47038.2h 6.52% Nachrichten
    34655.8h 4.80% Verkaufsshow
    29306.2h 4.06% Krimiserie
    24891.5h 3.45% Werbesendung
    23094.3h 3.20% Dokureihe
    21782.2h 3.02% Dokusoap
    20934.7h 2.90% Regionalmagazin
    18624.9h 2.58% Dokumentation
    18330.6h 2.54% *unknown*
    13384.8h 1.85% Zeichentrickserie
    13119.5h 1.82% Infomercial
    12693.9h 1.76% Animationsserie
    10946.3h 1.52% Comedyserie
    10249.8h 1.42% Morgenmagazin
    9746.9h  1.35% Religionsmagazin
    9671.7h  1.34% Magazin
    9574.1h  1.33% Talkshow
    7120.9h  0.99% E-Sport
    6868.1h  0.95% Programmende
    6841.8h  0.95% Sitcom
    6444.0h  0.89% Börsenmagazin
    6422.3h  0.89% Wetterbericht
    6110.1h  0.85% Komödie
    6058.4h  0.84% Quiz
    5407.6h  0.75% Wissensmagazin
    5278.9h  0.73% Realityshow
    5244.0h  0.73% Wirtschaftsmagazin
    5196.5h  0.72% Politikmagazin
    5161.1h  0.72% Telenovela
    4981.1h  0.69% Musikmagazin
