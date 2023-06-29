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

**96** channels, **296,260.0** hours playtime between **2023-01-17** and **2023-06-30**


### playtime per genre (top 30)

    19797.2h 6.68% Nachrichten
    14256.4h 4.81% Verkaufsshow
    11851.3h 4.00% Krimiserie
    9886.9h  3.34% Werbesendung
    9620.0h  3.25% Dokureihe
    8993.7h  3.04% Dokusoap
    8499.7h  2.87% Regionalmagazin
    7537.8h  2.54% Dokumentation
    7337.6h  2.48% *unknown*
    5651.9h  1.91% Zeichentrickserie
    5423.7h  1.83% Infomercial
    5222.4h  1.76% Animationsserie
    4936.4h  1.67% Comedyserie
    4150.7h  1.40% Morgenmagazin
    3926.2h  1.33% Talkshow
    3895.0h  1.31% Religionsmagazin
    3596.7h  1.21% Programmende
    3477.2h  1.17% Magazin
    2940.3h  0.99% E-Sport
    2809.9h  0.95% Sitcom
    2733.1h  0.92% Wetterbericht
    2629.7h  0.89% Börsenmagazin
    2337.7h  0.79% Quiz
    2319.9h  0.78% Wirtschaftsmagazin
    2316.9h  0.78% Musikmagazin
    2282.7h  0.77% Wissensmagazin
    2224.0h  0.75% Komödie
    2106.3h  0.71% Telenovela
    1989.3h  0.67% Sportmagazin
    1949.3h  0.66% Wirtschaftstalk
