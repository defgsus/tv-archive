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

**96** channels, **271,223.3** hours playtime between **2023-01-17** and **2023-06-16**


### playtime per genre (top 30)

    18099.7h 6.67% Nachrichten
    13071.2h 4.82% Verkaufsshow
    10858.5h 4.00% Krimiserie
    9022.2h  3.33% Werbesendung
    8826.6h  3.25% Dokureihe
    8165.3h  3.01% Dokusoap
    7762.8h  2.86% Regionalmagazin
    6945.2h  2.56% Dokumentation
    6783.0h  2.50% *unknown*
    5145.9h  1.90% Zeichentrickserie
    4970.1h  1.83% Infomercial
    4806.8h  1.77% Animationsserie
    4511.9h  1.66% Comedyserie
    3776.8h  1.39% Morgenmagazin
    3574.1h  1.32% Talkshow
    3551.9h  1.31% Religionsmagazin
    3403.4h  1.25% Programmende
    3157.1h  1.16% Magazin
    2716.6h  1.00% E-Sport
    2563.7h  0.95% Sitcom
    2488.1h  0.92% Wetterbericht
    2446.0h  0.90% Börsenmagazin
    2136.2h  0.79% Wirtschaftsmagazin
    2116.2h  0.78% Quiz
    2109.6h  0.78% Musikmagazin
    2095.6h  0.77% Wissensmagazin
    2009.5h  0.74% Komödie
    1929.1h  0.71% Telenovela
    1842.2h  0.68% Sportmagazin
    1764.5h  0.65% Gesundheitsmagazin
