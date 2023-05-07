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

**96** channels, **201,222.9** hours playtime between **2023-01-17** and **2023-05-08**


### playtime per genre (top 30)

    13565.2h 6.74% Nachrichten
    9837.6h  4.89% Verkaufsshow
    8203.8h  4.08% Krimiserie
    6702.0h  3.33% Werbesendung
    6503.4h  3.23% Dokureihe
    5972.7h  2.97% Dokusoap
    5766.2h  2.87% Regionalmagazin
    5116.6h  2.54% Dokumentation
    4907.7h  2.44% *unknown*
    3733.6h  1.86% Zeichentrickserie
    3684.6h  1.83% Infomercial
    3656.9h  1.82% Animationsserie
    3337.7h  1.66% Comedyserie
    2787.7h  1.39% Programmende
    2763.6h  1.37% Morgenmagazin
    2654.4h  1.32% Talkshow
    2640.1h  1.31% Religionsmagazin
    2242.8h  1.11% Magazin
    2028.8h  1.01% E-Sport
    1897.8h  0.94% Sitcom
    1817.3h  0.90% Wetterbericht
    1816.4h  0.90% Börsenmagazin
    1588.3h  0.79% Wirtschaftsmagazin
    1573.8h  0.78% Wissensmagazin
    1554.8h  0.77% Musikmagazin
    1528.4h  0.76% Quiz
    1407.6h  0.70% Sportmagazin
    1406.8h  0.70% Telenovela
    1386.3h  0.69% Gesundheitsmagazin
    1376.8h  0.68% Komödie
