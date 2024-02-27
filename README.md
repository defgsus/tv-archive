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

**99** channels, **728,799.4** hours playtime between **2023-01-17** and **2024-02-28**


### playtime per genre (top 30)

    47445.9h 6.51% Nachrichten
    34980.2h 4.80% Verkaufsshow
    29605.5h 4.06% Krimiserie
    25180.1h 3.46% Werbesendung
    23338.3h 3.20% Dokureihe
    21987.7h 3.02% Dokusoap
    21124.2h 2.90% Regionalmagazin
    18789.2h 2.58% Dokumentation
    18593.4h 2.55% *unknown*
    13504.7h 1.85% Zeichentrickserie
    13248.8h 1.82% Infomercial
    12827.7h 1.76% Animationsserie
    11042.4h 1.52% Comedyserie
    10330.2h 1.42% Morgenmagazin
    9852.9h  1.35% Religionsmagazin
    9773.7h  1.34% Magazin
    9675.0h  1.33% Talkshow
    7205.5h  0.99% E-Sport
    6931.6h  0.95% Programmende
    6890.6h  0.95% Sitcom
    6509.9h  0.89% Börsenmagazin
    6480.9h  0.89% Wetterbericht
    6168.8h  0.85% Komödie
    6126.9h  0.84% Quiz
    5456.4h  0.75% Wissensmagazin
    5329.3h  0.73% Realityshow
    5282.2h  0.72% Wirtschaftsmagazin
    5244.9h  0.72% Politikmagazin
    5195.3h  0.71% Telenovela
    5017.9h  0.69% Musikmagazin
