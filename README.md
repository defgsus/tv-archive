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

**99** channels, **719,934.8** hours playtime between **2023-01-17** and **2024-02-23**


### playtime per genre (top 30)

    46913.9h 6.52% Nachrichten
    34566.6h 4.80% Verkaufsshow
    29227.8h 4.06% Krimiserie
    24829.3h 3.45% Werbesendung
    23057.4h 3.20% Dokureihe
    21713.1h 3.02% Dokusoap
    20876.1h 2.90% Regionalmagazin
    18589.4h 2.58% Dokumentation
    18278.2h 2.54% *unknown*
    13353.9h 1.85% Zeichentrickserie
    13087.9h 1.82% Infomercial
    12662.2h 1.76% Animationsserie
    10912.6h 1.52% Comedyserie
    10216.9h 1.42% Morgenmagazin
    9727.9h  1.35% Religionsmagazin
    9646.6h  1.34% Magazin
    9541.9h  1.33% Talkshow
    7100.0h  0.99% E-Sport
    6862.4h  0.95% Programmende
    6828.3h  0.95% Sitcom
    6416.4h  0.89% Börsenmagazin
    6406.5h  0.89% Wetterbericht
    6096.5h  0.85% Komödie
    6036.2h  0.84% Quiz
    5397.2h  0.75% Wissensmagazin
    5266.3h  0.73% Realityshow
    5230.6h  0.73% Wirtschaftsmagazin
    5187.3h  0.72% Politikmagazin
    5144.6h  0.71% Telenovela
    4972.2h  0.69% Musikmagazin
