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

**96** channels, **351,837.9** hours playtime between **2023-01-17** and **2023-07-31**


### playtime per genre (top 30)

    23312.4h 6.63% Nachrichten
    16802.1h 4.78% Verkaufsshow
    14169.1h 4.03% Krimiserie
    11826.2h 3.36% Werbesendung
    11539.8h 3.28% Dokureihe
    10622.9h 3.02% Dokusoap
    10069.0h 2.86% Regionalmagazin
    8856.0h  2.52% Dokumentation
    8552.5h  2.43% *unknown*
    6660.4h  1.89% Zeichentrickserie
    6437.4h  1.83% Infomercial
    6206.7h  1.76% Animationsserie
    5780.1h  1.64% Comedyserie
    4906.9h  1.39% Morgenmagazin
    4675.4h  1.33% Religionsmagazin
    4662.2h  1.33% Talkshow
    4199.2h  1.19% Magazin
    4023.7h  1.14% Programmende
    3476.4h  0.99% E-Sport
    3314.0h  0.94% Sitcom
    3300.8h  0.94% Wetterbericht
    3175.7h  0.90% Börsenmagazin
    2798.9h  0.80% Quiz
    2760.6h  0.78% Musikmagazin
    2724.4h  0.77% Komödie
    2703.2h  0.77% Wirtschaftsmagazin
    2663.6h  0.76% Wissensmagazin
    2421.7h  0.69% Telenovela
    2302.2h  0.65% Sportmagazin
    2253.1h  0.64% Reportagereihe
