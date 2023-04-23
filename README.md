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

**96** channels, **175,770.0** hours playtime between **2023-01-17** and **2023-04-24**


### playtime per genre (top 30)

    11949.1h 6.80% Nachrichten
    8668.3h  4.93% Verkaufsshow
    7212.0h  4.10% Krimiserie
    5876.8h  3.34% Werbesendung
    5684.4h  3.23% Dokureihe
    5228.3h  2.97% Dokusoap
    5068.7h  2.88% Regionalmagazin
    4428.2h  2.52% Dokumentation
    4207.7h  2.39% *unknown*
    3237.9h  1.84% Zeichentrickserie
    3232.0h  1.84% Animationsserie
    3212.6h  1.83% Infomercial
    2897.7h  1.65% Comedyserie
    2438.8h  1.39% Programmende
    2421.1h  1.38% Morgenmagazin
    2302.1h  1.31% Talkshow
    2297.8h  1.31% Religionsmagazin
    1924.2h  1.09% Magazin
    1794.6h  1.02% E-Sport
    1653.6h  0.94% Sitcom
    1592.9h  0.91% Börsenmagazin
    1585.4h  0.90% Wetterbericht
    1398.0h  0.80% Wirtschaftsmagazin
    1376.6h  0.78% Wissensmagazin
    1348.2h  0.77% Musikmagazin
    1326.0h  0.75% Quiz
    1218.5h  0.69% Sportmagazin
    1217.5h  0.69% Telenovela
    1212.3h  0.69% Gesundheitsmagazin
    1194.6h  0.68% Komödie
