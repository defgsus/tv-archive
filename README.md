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

**96** channels, **339,279.0** hours playtime between **2023-01-17** and **2023-07-24**


### playtime per genre (top 30)

    22517.7h 6.64% Nachrichten
    16196.9h 4.77% Verkaufsshow
    13637.1h 4.02% Krimiserie
    11399.1h 3.36% Werbesendung
    11108.2h 3.27% Dokureihe
    10253.8h 3.02% Dokusoap
    9693.5h  2.86% Regionalmagazin
    8534.9h  2.52% Dokumentation
    8287.5h  2.44% *unknown*
    6441.0h  1.90% Zeichentrickserie
    6202.0h  1.83% Infomercial
    5978.4h  1.76% Animationsserie
    5590.7h  1.65% Comedyserie
    4731.2h  1.39% Morgenmagazin
    4509.2h  1.33% Religionsmagazin
    4504.9h  1.33% Talkshow
    4051.4h  1.19% Magazin
    3927.3h  1.16% Programmende
    3348.2h  0.99% E-Sport
    3208.1h  0.95% Sitcom
    3175.2h  0.94% Wetterbericht
    3054.2h  0.90% Börsenmagazin
    2699.1h  0.80% Quiz
    2658.9h  0.78% Musikmagazin
    2617.2h  0.77% Komödie
    2614.9h  0.77% Wirtschaftsmagazin
    2584.5h  0.76% Wissensmagazin
    2332.3h  0.69% Telenovela
    2240.9h  0.66% Sportmagazin
    2170.5h  0.64% Reportagereihe
