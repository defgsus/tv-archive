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

**96** channels, **144,655.0** hours playtime between **2023-01-17** and **2023-04-07**


### playtime per genre (top 30)

    10082.5h 6.97% Nachrichten
    7194.0h  4.97% Verkaufsshow
    6036.3h  4.17% Krimiserie
    4861.6h  3.36% Werbesendung
    4604.2h  3.18% Dokureihe
    4427.4h  3.06% Dokusoap
    4276.4h  2.96% Regionalmagazin
    3589.7h  2.48% Dokumentation
    3351.2h  2.32% *unknown*
    2720.0h  1.88% Animationsserie
    2672.9h  1.85% Infomercial
    2653.7h  1.83% Zeichentrickserie
    2389.7h  1.65% Comedyserie
    2073.9h  1.43% Morgenmagazin
    2010.3h  1.39% Programmende
    1905.7h  1.32% Talkshow
    1879.3h  1.30% Religionsmagazin
    1551.7h  1.07% Magazin
    1488.8h  1.03% E-Sport
    1390.3h  0.96% Sitcom
    1358.6h  0.94% Börsenmagazin
    1299.2h  0.90% Wetterbericht
    1186.6h  0.82% Wirtschaftsmagazin
    1140.4h  0.79% Wissensmagazin
    1111.2h  0.77% Quiz
    1094.3h  0.76% Musikmagazin
    1031.5h  0.71% Telenovela
    1014.8h  0.70% Dramaserie
    999.9h   0.69% Gesundheitsmagazin
    991.7h   0.69% Sportmagazin
