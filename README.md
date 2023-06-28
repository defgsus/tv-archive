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

**96** channels, **294,488.0** hours playtime between **2023-01-17** and **2023-06-29**


### playtime per genre (top 30)

    19660.5h 6.68% Nachrichten
    14167.2h 4.81% Verkaufsshow
    11771.0h 4.00% Krimiserie
    9830.2h  3.34% Werbesendung
    9584.9h  3.25% Dokureihe
    8909.1h  3.03% Dokusoap
    8436.8h  2.86% Regionalmagazin
    7490.1h  2.54% Dokumentation
    7300.9h  2.48% *unknown*
    5619.1h  1.91% Zeichentrickserie
    5390.9h  1.83% Infomercial
    5191.4h  1.76% Animationsserie
    4898.2h  1.66% Comedyserie
    4115.9h  1.40% Morgenmagazin
    3906.1h  1.33% Talkshow
    3876.3h  1.32% Religionsmagazin
    3583.0h  1.22% Programmende
    3441.5h  1.17% Magazin
    2928.8h  0.99% E-Sport
    2792.1h  0.95% Sitcom
    2715.7h  0.92% Wetterbericht
    2618.6h  0.89% Börsenmagazin
    2320.7h  0.79% Quiz
    2304.3h  0.78% Wirtschaftsmagazin
    2299.6h  0.78% Musikmagazin
    2262.5h  0.77% Wissensmagazin
    2225.7h  0.76% Komödie
    2089.8h  0.71% Telenovela
    1984.5h  0.67% Sportmagazin
    1930.7h  0.66% Wirtschaftstalk
