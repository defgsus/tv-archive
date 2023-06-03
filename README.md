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

**96** channels, **249,732.0** hours playtime between **2023-01-17** and **2023-06-04**


### playtime per genre (top 30)

    16671.2h 6.68% Nachrichten
    12067.1h 4.83% Verkaufsshow
    10030.0h 4.02% Krimiserie
    8304.9h  3.33% Werbesendung
    8112.8h  3.25% Dokureihe
    7458.6h  2.99% Dokusoap
    7134.1h  2.86% Regionalmagazin
    6398.7h  2.56% Dokumentation
    6202.9h  2.48% *unknown*
    4699.6h  1.88% Zeichentrickserie
    4575.6h  1.83% Infomercial
    4457.9h  1.79% Animationsserie
    4156.8h  1.66% Comedyserie
    3449.8h  1.38% Morgenmagazin
    3289.2h  1.32% Talkshow
    3261.6h  1.31% Religionsmagazin
    3237.8h  1.30% Programmende
    2879.0h  1.15% Magazin
    2498.6h  1.00% E-Sport
    2342.8h  0.94% Sitcom
    2278.0h  0.91% Wetterbericht
    2260.9h  0.91% Börsenmagazin
    1958.8h  0.78% Wirtschaftsmagazin
    1937.5h  0.78% Musikmagazin
    1931.7h  0.77% Quiz
    1931.7h  0.77% Wissensmagazin
    1835.2h  0.73% Komödie
    1765.1h  0.71% Telenovela
    1714.9h  0.69% Sportmagazin
    1644.2h  0.66% Gesundheitsmagazin
