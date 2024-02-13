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

**99** channels, **703,924.9** hours playtime between **2023-01-17** and **2024-02-14**


### playtime per genre (top 30)

    45852.2h 6.51% Nachrichten
    33779.8h 4.80% Verkaufsshow
    28472.0h 4.04% Krimiserie
    24177.7h 3.43% Werbesendung
    22666.6h 3.22% Dokureihe
    21188.2h 3.01% Dokusoap
    20361.1h 2.89% Regionalmagazin
    18130.3h 2.58% Dokumentation
    17792.4h 2.53% *unknown*
    13053.5h 1.85% Zeichentrickserie
    12794.1h 1.82% Infomercial
    12376.6h 1.76% Animationsserie
    10657.7h 1.51% Comedyserie
    9966.5h  1.42% Morgenmagazin
    9514.1h  1.35% Religionsmagazin
    9382.5h  1.33% Magazin
    9320.2h  1.32% Talkshow
    6938.1h  0.99% E-Sport
    6737.6h  0.96% Programmende
    6697.9h  0.95% Sitcom
    6280.9h  0.89% Börsenmagazin
    6272.8h  0.89% Wetterbericht
    5986.8h  0.85% Komödie
    5863.2h  0.83% Quiz
    5282.8h  0.75% Wissensmagazin
    5178.3h  0.74% Realityshow
    5122.3h  0.73% Wirtschaftsmagazin
    5029.9h  0.71% Politikmagazin
    5008.4h  0.71% Telenovela
    4893.6h  0.70% Musikmagazin
