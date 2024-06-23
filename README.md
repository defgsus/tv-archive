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

**109** channels, **916,194.3** hours playtime between **2023-01-17** and **2024-06-24**


### playtime per genre (top 30)

    59824.0h 6.53% Nachrichten
    43107.8h 4.71% Verkaufsshow
    37348.4h 4.08% Krimiserie
    32412.4h 3.54% Werbesendung
    28821.4h 3.15% Dokureihe
    27709.0h 3.02% Dokusoap
    26616.2h 2.91% Regionalmagazin
    23810.7h 2.60% Dokumentation
    23012.3h 2.51% *unknown*
    16857.8h 1.84% Zeichentrickserie
    16704.5h 1.82% Infomercial
    16359.3h 1.79% Animationsserie
    13691.6h 1.49% Comedyserie
    13072.8h 1.43% Magazin
    12884.0h 1.41% Morgenmagazin
    12420.2h 1.36% Religionsmagazin
    12204.2h 1.33% Talkshow
    9059.3h  0.99% E-Sport
    8564.9h  0.93% Sitcom
    8379.5h  0.91% Programmende
    8179.0h  0.89% Wetterbericht
    7942.3h  0.87% Komödie
    7904.2h  0.86% Quiz
    7826.9h  0.85% Börsenmagazin
    6871.5h  0.75% Politikmagazin
    6807.2h  0.74% Wissensmagazin
    6782.6h  0.74% Realityshow
    6421.0h  0.70% Wirtschaftsmagazin
    6303.8h  0.69% Telenovela
    6012.8h  0.66% Musikmagazin
