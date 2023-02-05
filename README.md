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

**96** channels, **37,419.0** hours playtime between **2023-01-17** and **2023-02-06**


### playtime per genre (top 30)

    2570.0h 6.87% Nachrichten
    1964.2h 5.25% Verkaufsshow
    1570.2h 4.20% Krimiserie
    1306.0h 3.49% Dokusoap
    1268.3h 3.39% Werbesendung
    1159.6h 3.10% Dokureihe
    1065.1h 2.85% Regionalmagazin
    954.5h  2.55% Dokumentation
    926.8h  2.48% *unknown*
    726.8h  1.94% Zeichentrickserie
    704.1h  1.88% Infomercial
    660.9h  1.77% Animationsserie
    622.5h  1.66% Comedyserie
    502.4h  1.34% Religionsmagazin
    501.9h  1.34% Morgenmagazin
    489.1h  1.31% Programmende
    479.3h  1.28% Talkshow
    422.0h  1.13% Magazin
    410.3h  1.10% E-Sport
    336.5h  0.90% Sitcom
    322.1h  0.86% Börsenmagazin
    316.6h  0.85% Wetterbericht
    309.6h  0.83% Wirtschaftsmagazin
    301.1h  0.80% Wissensmagazin
    284.2h  0.76% Musikmagazin
    282.4h  0.75% Quiz
    281.4h  0.75% Dramaserie
    263.6h  0.70% Gesundheitsmagazin
    252.2h  0.67% Telenovela
    249.6h  0.67% Sportmagazin
