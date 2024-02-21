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

**99** channels, **718,158.7** hours playtime between **2023-01-17** and **2024-02-22**


### playtime per genre (top 30)

    46781.0h 6.51% Nachrichten
    34480.9h 4.80% Verkaufsshow
    29121.7h 4.06% Krimiserie
    24757.6h 3.45% Werbesendung
    23035.7h 3.21% Dokureihe
    21651.6h 3.01% Dokusoap
    20811.5h 2.90% Regionalmagazin
    18530.0h 2.58% Dokumentation
    18218.8h 2.54% *unknown*
    13320.9h 1.85% Zeichentrickserie
    13054.7h 1.82% Infomercial
    12630.5h 1.76% Animationsserie
    10878.2h 1.51% Comedyserie
    10183.9h 1.42% Morgenmagazin
    9712.5h  1.35% Religionsmagazin
    9618.8h  1.34% Magazin
    9527.9h  1.33% Talkshow
    7082.0h  0.99% E-Sport
    6848.1h  0.95% Programmende
    6817.2h  0.95% Sitcom
    6406.3h  0.89% Börsenmagazin
    6390.1h  0.89% Wetterbericht
    6100.9h  0.85% Komödie
    6012.5h  0.84% Quiz
    5386.8h  0.75% Wissensmagazin
    5257.7h  0.73% Realityshow
    5213.5h  0.73% Wirtschaftsmagazin
    5163.2h  0.72% Politikmagazin
    5125.4h  0.71% Telenovela
    4963.8h  0.69% Musikmagazin
