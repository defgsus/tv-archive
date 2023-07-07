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

**96** channels, **310,595.2** hours playtime between **2023-01-17** and **2023-07-08**


### playtime per genre (top 30)

    20742.3h 6.68% Nachrichten
    14877.1h 4.79% Verkaufsshow
    12442.9h 4.01% Krimiserie
    10398.6h 3.35% Werbesendung
    10072.1h 3.24% Dokureihe
    9430.2h  3.04% Dokusoap
    8919.5h  2.87% Regionalmagazin
    7822.4h  2.52% Dokumentation
    7663.4h  2.47% *unknown*
    5919.7h  1.91% Zeichentrickserie
    5685.9h  1.83% Infomercial
    5473.1h  1.76% Animationsserie
    5167.3h  1.66% Comedyserie
    4371.8h  1.41% Morgenmagazin
    4119.4h  1.33% Talkshow
    4091.4h  1.32% Religionsmagazin
    3706.4h  1.19% Programmende
    3683.1h  1.19% Magazin
    3070.8h  0.99% E-Sport
    2944.6h  0.95% Sitcom
    2880.2h  0.93% Wetterbericht
    2775.7h  0.89% Börsenmagazin
    2464.5h  0.79% Quiz
    2438.2h  0.79% Musikmagazin
    2424.3h  0.78% Wirtschaftsmagazin
    2386.2h  0.77% Wissensmagazin
    2325.9h  0.75% Komödie
    2196.5h  0.71% Telenovela
    2071.2h  0.67% Sportmagazin
    1975.9h  0.64% Wirtschaftstalk
