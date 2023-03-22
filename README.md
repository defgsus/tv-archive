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

**96** channels, **119,160.1** hours playtime between **2023-01-17** and **2023-03-23**


### playtime per genre (top 30)

    8383.9h 7.04% Nachrichten
    5979.7h 5.02% Verkaufsshow
    4987.3h 4.19% Krimiserie
    4024.3h 3.38% Werbesendung
    3762.2h 3.16% Dokusoap
    3687.9h 3.09% Dokureihe
    3524.6h 2.96% Regionalmagazin
    2905.1h 2.44% Dokumentation
    2765.0h 2.32% *unknown*
    2269.6h 1.90% Animationsserie
    2189.2h 1.84% Infomercial
    2163.2h 1.82% Zeichentrickserie
    1962.6h 1.65% Comedyserie
    1707.0h 1.43% Morgenmagazin
    1632.8h 1.37% Programmende
    1592.0h 1.34% Talkshow
    1545.2h 1.30% Religionsmagazin
    1235.5h 1.04% E-Sport
    1234.9h 1.04% Magazin
    1143.8h 0.96% Sitcom
    1118.5h 0.94% Börsenmagazin
    1063.7h 0.89% Wetterbericht
    978.1h  0.82% Wirtschaftsmagazin
    936.5h  0.79% Wissensmagazin
    904.9h  0.76% Quiz
    891.5h  0.75% Musikmagazin
    863.2h  0.72% Dramaserie
    837.4h  0.70% Telenovela
    828.2h  0.70% Gesundheitsmagazin
    810.4h  0.68% Sportmagazin
