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

**99** channels, **723,497.4** hours playtime between **2023-01-17** and **2024-02-25**


### playtime per genre (top 30)

    47114.3h 6.51% Nachrichten
    34734.2h 4.80% Verkaufsshow
    29369.3h 4.06% Krimiserie
    24969.2h 3.45% Werbesendung
    23167.2h 3.20% Dokureihe
    21827.7h 3.02% Dokusoap
    20960.7h 2.90% Regionalmagazin
    18655.8h 2.58% Dokumentation
    18391.5h 2.54% *unknown*
    13409.9h 1.85% Zeichentrickserie
    13154.7h 1.82% Infomercial
    12731.3h 1.76% Animationsserie
    10961.2h 1.52% Comedyserie
    10254.8h 1.42% Morgenmagazin
    9769.6h  1.35% Religionsmagazin
    9700.2h  1.34% Magazin
    9598.1h  1.33% Talkshow
    7141.9h  0.99% E-Sport
    6883.1h  0.95% Programmende
    6847.7h  0.95% Sitcom
    6452.0h  0.89% Börsenmagazin
    6436.2h  0.89% Wetterbericht
    6145.0h  0.85% Komödie
    6071.6h  0.84% Quiz
    5419.0h  0.75% Wissensmagazin
    5282.7h  0.73% Realityshow
    5247.2h  0.73% Wirtschaftsmagazin
    5198.0h  0.72% Politikmagazin
    5162.1h  0.71% Telenovela
    4990.1h  0.69% Musikmagazin
