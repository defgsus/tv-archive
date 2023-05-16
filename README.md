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

**96** channels, **217,395.5** hours playtime between **2023-01-17** and **2023-05-17**


### playtime per genre (top 30)

    14658.8h 6.74% Nachrichten
    10549.6h 4.85% Verkaufsshow
    8848.8h  4.07% Krimiserie
    7226.2h  3.32% Werbesendung
    7066.3h  3.25% Dokureihe
    6422.9h  2.95% Dokusoap
    6243.1h  2.87% Regionalmagazin
    5516.8h  2.54% Dokumentation
    5365.7h  2.47% *unknown*
    4046.2h  1.86% Zeichentrickserie
    3988.3h  1.83% Infomercial
    3925.1h  1.81% Animationsserie
    3623.2h  1.67% Comedyserie
    3017.2h  1.39% Morgenmagazin
    2989.2h  1.37% Programmende
    2873.5h  1.32% Talkshow
    2845.7h  1.31% Religionsmagazin
    2477.8h  1.14% Magazin
    2178.8h  1.00% E-Sport
    2054.3h  0.94% Sitcom
    1992.0h  0.92% Börsenmagazin
    1968.1h  0.91% Wetterbericht
    1720.0h  0.79% Wirtschaftsmagazin
    1700.0h  0.78% Wissensmagazin
    1679.1h  0.77% Musikmagazin
    1670.2h  0.77% Quiz
    1538.2h  0.71% Telenovela
    1514.2h  0.70% Sportmagazin
    1490.0h  0.69% Komödie
    1474.6h  0.68% Gesundheitsmagazin
