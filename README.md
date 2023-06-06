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

**96** channels, **255,088.9** hours playtime between **2023-01-17** and **2023-06-07**


### playtime per genre (top 30)

    17022.5h 6.67% Nachrichten
    12300.3h 4.82% Verkaufsshow
    10241.1h 4.01% Krimiserie
    8484.5h  3.33% Werbesendung
    8310.2h  3.26% Dokureihe
    7613.8h  2.98% Dokusoap
    7287.1h  2.86% Regionalmagazin
    6531.7h  2.56% Dokumentation
    6342.4h  2.49% *unknown*
    4809.8h  1.89% Zeichentrickserie
    4673.4h  1.83% Infomercial
    4546.2h  1.78% Animationsserie
    4241.7h  1.66% Comedyserie
    3527.4h  1.38% Morgenmagazin
    3364.9h  1.32% Talkshow
    3344.0h  1.31% Religionsmagazin
    3279.5h  1.29% Programmende
    2961.9h  1.16% Magazin
    2556.1h  1.00% E-Sport
    2391.7h  0.94% Sitcom
    2332.1h  0.91% Wetterbericht
    2303.2h  0.90% Börsenmagazin
    2000.3h  0.78% Wirtschaftsmagazin
    1989.0h  0.78% Musikmagazin
    1982.2h  0.78% Quiz
    1972.8h  0.77% Wissensmagazin
    1889.8h  0.74% Komödie
    1804.9h  0.71% Telenovela
    1749.8h  0.69% Sportmagazin
    1671.8h  0.66% Gesundheitsmagazin
