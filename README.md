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

**96** channels, **315,955.3** hours playtime between **2023-01-17** and **2023-07-11**


### playtime per genre (top 30)

    21031.7h 6.66% Nachrichten
    15126.9h 4.79% Verkaufsshow
    12656.3h 4.01% Krimiserie
    10599.3h 3.35% Werbesendung
    10283.9h 3.25% Dokureihe
    9572.8h  3.03% Dokusoap
    9034.9h  2.86% Regionalmagazin
    7940.9h  2.51% Dokumentation
    7775.4h  2.46% *unknown*
    6011.8h  1.90% Zeichentrickserie
    5783.3h  1.83% Infomercial
    5565.8h  1.76% Animationsserie
    5235.3h  1.66% Comedyserie
    4412.6h  1.40% Morgenmagazin
    4189.2h  1.33% Talkshow
    4177.5h  1.32% Religionsmagazin
    3748.3h  1.19% Programmende
    3747.5h  1.19% Magazin
    3129.6h  0.99% E-Sport
    2992.2h  0.95% Sitcom
    2931.0h  0.93% Wetterbericht
    2820.9h  0.89% Börsenmagazin
    2507.0h  0.79% Quiz
    2482.4h  0.79% Musikmagazin
    2453.8h  0.78% Wirtschaftsmagazin
    2421.7h  0.77% Wissensmagazin
    2409.7h  0.76% Komödie
    2211.9h  0.70% Telenovela
    2111.9h  0.67% Sportmagazin
    2008.4h  0.64% Wirtschaftstalk
