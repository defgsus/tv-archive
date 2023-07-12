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

**96** channels, **319,553.8** hours playtime between **2023-01-17** and **2023-07-13**


### playtime per genre (top 30)

    21286.9h 6.66% Nachrichten
    15288.5h 4.78% Verkaufsshow
    12824.1h 4.01% Krimiserie
    10721.6h 3.36% Werbesendung
    10405.8h 3.26% Dokureihe
    9670.2h  3.03% Dokusoap
    9160.0h  2.87% Regionalmagazin
    8035.5h  2.51% Dokumentation
    7854.7h  2.46% *unknown*
    6082.5h  1.90% Zeichentrickserie
    5847.9h  1.83% Infomercial
    5627.6h  1.76% Animationsserie
    5300.9h  1.66% Comedyserie
    4480.6h  1.40% Morgenmagazin
    4242.2h  1.33% Talkshow
    4222.0h  1.32% Religionsmagazin
    3797.6h  1.19% Magazin
    3775.9h  1.18% Programmende
    3164.4h  0.99% E-Sport
    3033.7h  0.95% Sitcom
    2970.2h  0.93% Wetterbericht
    2864.2h  0.90% Börsenmagazin
    2538.0h  0.79% Quiz
    2511.2h  0.79% Musikmagazin
    2483.7h  0.78% Wirtschaftsmagazin
    2449.5h  0.77% Wissensmagazin
    2421.7h  0.76% Komödie
    2239.8h  0.70% Telenovela
    2133.1h  0.67% Sportmagazin
    2027.4h  0.63% Dramaserie
