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

**97** channels, **436,021.9** hours playtime between **2023-01-17** and **2023-09-16**


### playtime per genre (top 30)

    28817.0h 6.61% Nachrichten
    20723.7h 4.75% Verkaufsshow
    17656.9h 4.05% Krimiserie
    14695.8h 3.37% Werbesendung
    14362.4h 3.29% Dokureihe
    13270.2h 3.04% Dokusoap
    12592.9h 2.89% Regionalmagazin
    10969.3h 2.52% Dokumentation
    10343.6h 2.37% *unknown*
    8230.0h  1.89% Zeichentrickserie
    7954.7h  1.82% Infomercial
    7731.2h  1.77% Animationsserie
    7074.8h  1.62% Comedyserie
    6187.5h  1.42% Morgenmagazin
    5826.5h  1.34% Religionsmagazin
    5783.0h  1.33% Talkshow
    5449.8h  1.25% Magazin
    4674.3h  1.07% Programmende
    4313.2h  0.99% E-Sport
    4115.3h  0.94% Wetterbericht
    4106.5h  0.94% Sitcom
    3949.3h  0.91% Börsenmagazin
    3611.2h  0.83% Quiz
    3422.6h  0.78% Musikmagazin
    3370.2h  0.77% Komödie
    3312.7h  0.76% Wirtschaftsmagazin
    3265.2h  0.75% Wissensmagazin
    3092.8h  0.71% Telenovela
    2866.3h  0.66% Reportagereihe
    2857.2h  0.66% Politikmagazin
