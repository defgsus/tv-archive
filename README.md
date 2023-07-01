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

**96** channels, **299,857.8** hours playtime between **2023-01-17** and **2023-07-02**


### playtime per genre (top 30)

    20007.2h 6.67% Nachrichten
    14411.7h 4.81% Verkaufsshow
    12008.7h 4.00% Krimiserie
    10017.8h 3.34% Werbesendung
    9737.6h  3.25% Dokureihe
    9096.3h  3.03% Dokusoap
    8583.2h  2.86% Regionalmagazin
    7589.3h  2.53% Dokumentation
    7425.2h  2.48% *unknown*
    5717.6h  1.91% Zeichentrickserie
    5490.2h  1.83% Infomercial
    5283.7h  1.76% Animationsserie
    4994.1h  1.67% Comedyserie
    4191.4h  1.40% Morgenmagazin
    3979.0h  1.33% Talkshow
    3947.8h  1.32% Religionsmagazin
    3624.0h  1.21% Programmende
    3521.0h  1.17% Magazin
    2969.9h  0.99% E-Sport
    2840.5h  0.95% Sitcom
    2767.9h  0.92% Wetterbericht
    2660.4h  0.89% Börsenmagazin
    2363.5h  0.79% Quiz
    2348.2h  0.78% Musikmagazin
    2339.2h  0.78% Wirtschaftsmagazin
    2302.2h  0.77% Wissensmagazin
    2258.6h  0.75% Komödie
    2126.5h  0.71% Telenovela
    2004.8h  0.67% Sportmagazin
    1957.0h  0.65% Wirtschaftstalk
