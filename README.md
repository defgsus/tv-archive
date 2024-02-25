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

**99** channels, **725,280.5** hours playtime between **2023-01-17** and **2024-02-26**


### playtime per genre (top 30)

    47197.9h 6.51% Nachrichten
    34808.5h 4.80% Verkaufsshow
    29427.3h 4.06% Krimiserie
    25044.0h 3.45% Werbesendung
    23251.2h 3.21% Dokureihe
    21888.1h 3.02% Dokusoap
    20995.2h 2.89% Regionalmagazin
    18705.8h 2.58% Dokumentation
    18482.9h 2.55% *unknown*
    13437.7h 1.85% Zeichentrickserie
    13187.6h 1.82% Infomercial
    12764.2h 1.76% Animationsserie
    10976.1h 1.51% Comedyserie
    10262.7h 1.41% Morgenmagazin
    9808.3h  1.35% Religionsmagazin
    9735.3h  1.34% Magazin
    9631.8h  1.33% Talkshow
    7163.5h  0.99% E-Sport
    6903.2h  0.95% Programmende
    6860.6h  0.95% Sitcom
    6469.0h  0.89% Börsenmagazin
    6447.5h  0.89% Wetterbericht
    6167.1h  0.85% Komödie
    6076.0h  0.84% Quiz
    5437.1h  0.75% Wissensmagazin
    5292.7h  0.73% Realityshow
    5255.3h  0.72% Wirtschaftsmagazin
    5202.1h  0.72% Politikmagazin
    5163.0h  0.71% Telenovela
    5000.9h  0.69% Musikmagazin
