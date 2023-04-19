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

**96** channels, **168,447.9** hours playtime between **2023-01-17** and **2023-04-20**


### playtime per genre (top 30)

    11521.4h 6.84% Nachrichten
    8332.9h  4.95% Verkaufsshow
    6923.6h  4.11% Krimiserie
    5626.7h  3.34% Werbesendung
    5433.6h  3.23% Dokureihe
    5028.0h  2.98% Dokusoap
    4891.9h  2.90% Regionalmagazin
    4255.6h  2.53% Dokumentation
    4018.1h  2.39% *unknown*
    3113.7h  1.85% Animationsserie
    3093.4h  1.84% Zeichentrickserie
    3072.8h  1.82% Infomercial
    2777.9h  1.65% Comedyserie
    2344.2h  1.39% Morgenmagazin
    2324.1h  1.38% Programmende
    2191.6h  1.30% Religionsmagazin
    2183.7h  1.30% Talkshow
    1826.2h  1.08% Magazin
    1727.4h  1.03% E-Sport
    1592.6h  0.95% Sitcom
    1567.6h  0.93% Börsenmagazin
    1520.4h  0.90% Wetterbericht
    1352.8h  0.80% Wirtschaftsmagazin
    1322.7h  0.79% Wissensmagazin
    1284.0h  0.76% Quiz
    1283.0h  0.76% Musikmagazin
    1174.1h  0.70% Telenovela
    1168.7h  0.69% Gesundheitsmagazin
    1158.0h  0.69% Sportmagazin
    1150.2h  0.68% Dramaserie
