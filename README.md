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

**96** channels, **262,287.4** hours playtime between **2023-01-17** and **2023-06-11**


### playtime per genre (top 30)

    17483.0h 6.67% Nachrichten
    12653.0h 4.82% Verkaufsshow
    10493.6h 4.00% Krimiserie
    8711.0h  3.32% Werbesendung
    8571.8h  3.27% Dokureihe
    7859.7h  3.00% Dokusoap
    7472.9h  2.85% Regionalmagazin
    6720.3h  2.56% Dokumentation
    6551.4h  2.50% *unknown*
    4962.8h  1.89% Zeichentrickserie
    4805.9h  1.83% Infomercial
    4659.2h  1.78% Animationsserie
    4355.0h  1.66% Comedyserie
    3635.3h  1.39% Morgenmagazin
    3444.9h  1.31% Talkshow
    3438.1h  1.31% Religionsmagazin
    3327.4h  1.27% Programmende
    3054.9h  1.16% Magazin
    2631.8h  1.00% E-Sport
    2468.6h  0.94% Sitcom
    2403.3h  0.92% Wetterbericht
    2354.3h  0.90% Börsenmagazin
    2064.6h  0.79% Wirtschaftsmagazin
    2041.1h  0.78% Quiz
    2040.6h  0.78% Musikmagazin
    2022.8h  0.77% Wissensmagazin
    1959.0h  0.75% Komödie
    1859.6h  0.71% Telenovela
    1783.8h  0.68% Sportmagazin
    1710.0h  0.65% Gesundheitsmagazin
