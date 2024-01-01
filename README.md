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

**97** channels, **627,732.6** hours playtime between **2023-01-17** and **2024-01-02**


### playtime per genre (top 30)

    40946.6h 6.52% Nachrichten
    30041.0h 4.79% Verkaufsshow
    25069.0h 3.99% Krimiserie
    21326.1h 3.40% Werbesendung
    20372.8h 3.25% Dokureihe
    18778.0h 2.99% Dokusoap
    18012.4h 2.87% Regionalmagazin
    16319.3h 2.60% Dokumentation
    15576.3h 2.48% *unknown*
    11565.8h 1.84% Zeichentrickserie
    11376.9h 1.81% Infomercial
    11047.9h 1.76% Animationsserie
    9536.3h  1.52% Comedyserie
    8855.7h  1.41% Morgenmagazin
    8509.1h  1.36% Religionsmagazin
    8304.3h  1.32% Talkshow
    8213.4h  1.31% Magazin
    6169.4h  0.98% E-Sport
    6143.6h  0.98% Programmende
    6097.8h  0.97% Sitcom
    5716.8h  0.91% Wetterbericht
    5610.5h  0.89% Börsenmagazin
    5333.8h  0.85% Komödie
    5127.1h  0.82% Quiz
    4730.1h  0.75% Wissensmagazin
    4619.6h  0.74% Wirtschaftsmagazin
    4548.8h  0.72% Realityshow
    4519.7h  0.72% Musikmagazin
    4476.2h  0.71% Telenovela
    4416.9h  0.70% Politikmagazin
