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

**96** channels, **253,288.9** hours playtime between **2023-01-17** and **2023-06-06**


### playtime per genre (top 30)

    16889.4h 6.67% Nachrichten
    12221.0h 4.82% Verkaufsshow
    10150.1h 4.01% Krimiserie
    8426.8h  3.33% Werbesendung
    8243.9h  3.25% Dokureihe
    7556.3h  2.98% Dokusoap
    7224.4h  2.85% Regionalmagazin
    6487.1h  2.56% Dokumentation
    6292.1h  2.48% *unknown*
    4772.4h  1.88% Zeichentrickserie
    4640.0h  1.83% Infomercial
    4517.6h  1.78% Animationsserie
    4208.0h  1.66% Comedyserie
    3492.7h  1.38% Morgenmagazin
    3345.9h  1.32% Talkshow
    3320.0h  1.31% Religionsmagazin
    3265.5h  1.29% Programmende
    2939.1h  1.16% Magazin
    2534.4h  1.00% E-Sport
    2373.2h  0.94% Sitcom
    2313.7h  0.91% Wetterbericht
    2291.2h  0.90% Börsenmagazin
    1986.9h  0.78% Wirtschaftsmagazin
    1971.4h  0.78% Quiz
    1969.6h  0.78% Musikmagazin
    1960.6h  0.77% Wissensmagazin
    1889.5h  0.75% Komödie
    1784.7h  0.70% Telenovela
    1735.2h  0.69% Sportmagazin
    1658.5h  0.65% Gesundheitsmagazin
