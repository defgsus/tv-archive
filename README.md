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

**96** channels, **97,478.2** hours playtime between **2023-01-17** and **2023-03-11**


### playtime per genre (top 30)

    6905.8h 7.08% Nachrichten
    4905.2h 5.03% Verkaufsshow
    4113.4h 4.22% Krimiserie
    3302.7h 3.39% Werbesendung
    3176.0h 3.26% Dokusoap
    2915.9h 2.99% Dokureihe
    2901.5h 2.98% Regionalmagazin
    2381.4h 2.44% Dokumentation
    2350.0h 2.41% *unknown*
    1868.5h 1.92% Animationsserie
    1785.4h 1.83% Infomercial
    1754.0h 1.80% Zeichentrickserie
    1592.8h 1.63% Comedyserie
    1405.0h 1.44% Morgenmagazin
    1320.9h 1.36% Programmende
    1295.5h 1.33% Talkshow
    1272.1h 1.31% Religionsmagazin
    1015.2h 1.04% Magazin
    1010.1h 1.04% E-Sport
    932.7h  0.96% Sitcom
    903.3h  0.93% Börsenmagazin
    862.9h  0.89% Wetterbericht
    799.4h  0.82% Wirtschaftsmagazin
    763.4h  0.78% Wissensmagazin
    735.6h  0.75% Quiz
    715.9h  0.73% Musikmagazin
    704.6h  0.72% Dramaserie
    692.3h  0.71% Telenovela
    683.4h  0.70% Gesundheitsmagazin
    631.2h  0.65% Gerichtsshow
