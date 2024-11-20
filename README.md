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

**109** channels, **1,148,578.0** hours playtime between **2023-01-17** and **2024-11-21**


### playtime per genre (top 30)

    74902.5h 6.52% Nachrichten
    52506.8h 4.57% Verkaufsshow
    47928.0h 4.17% Krimiserie
    42280.0h 3.68% Werbesendung
    35826.2h 3.12% Dokureihe
    34240.7h 2.98% Dokusoap
    33619.2h 2.93% Regionalmagazin
    30185.9h 2.63% Dokumentation
    27110.7h 2.36% *unknown*
    21490.8h 1.87% Zeichentrickserie
    21187.5h 1.84% Infomercial
    20518.6h 1.79% Animationsserie
    16462.0h 1.43% Comedyserie
    16063.7h 1.40% Morgenmagazin
    15311.1h 1.33% Religionsmagazin
    15217.1h 1.32% Talkshow
    14346.3h 1.25% Magazin
    11346.1h 0.99% E-Sport
    11123.0h 0.97% Sitcom
    10393.7h 0.90% Wetterbericht
    10152.8h 0.88% Quiz
    10148.9h 0.88% Programmende
    10091.0h 0.88% Komödie
    8806.9h  0.77% Realityshow
    8720.5h  0.76% Politikmagazin
    8635.6h  0.75% Wissensmagazin
    8570.5h  0.75% Börsenmagazin
    7689.8h  0.67% Wirtschaftsmagazin
    7597.2h  0.66% Telenovela
    7559.6h  0.66% Dramaserie
