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

**96** channels, **360,772.0** hours playtime between **2023-01-17** and **2023-08-05**


### playtime per genre (top 30)

    23943.3h 6.64% Nachrichten
    17181.9h 4.76% Verkaufsshow
    14554.6h 4.03% Krimiserie
    12137.2h 3.36% Werbesendung
    11829.4h 3.28% Dokureihe
    10918.0h 3.03% Dokusoap
    10374.4h 2.88% Regionalmagazin
    9097.8h  2.52% Dokumentation
    8791.1h  2.44% *unknown*
    6824.9h  1.89% Zeichentrickserie
    6597.1h  1.83% Infomercial
    6384.0h  1.77% Animationsserie
    5939.1h  1.65% Comedyserie
    5078.4h  1.41% Morgenmagazin
    4778.2h  1.32% Religionsmagazin
    4760.8h  1.32% Talkshow
    4314.5h  1.20% Magazin
    4094.4h  1.13% Programmende
    3567.0h  0.99% E-Sport
    3399.6h  0.94% Sitcom
    3389.2h  0.94% Wetterbericht
    3280.8h  0.91% Börsenmagazin
    2886.0h  0.80% Quiz
    2830.4h  0.78% Musikmagazin
    2780.2h  0.77% Wirtschaftsmagazin
    2755.0h  0.76% Komödie
    2719.9h  0.75% Wissensmagazin
    2510.8h  0.70% Telenovela
    2347.2h  0.65% Sportmagazin
    2317.5h  0.64% Reportagereihe
