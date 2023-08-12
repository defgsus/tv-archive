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

**96** channels, **375,192.8** hours playtime between **2023-01-17** and **2023-08-13**


### playtime per genre (top 30)

    24835.0h 6.62% Nachrichten
    17774.8h 4.74% Verkaufsshow
    15188.7h 4.05% Krimiserie
    12639.8h 3.37% Werbesendung
    12348.7h 3.29% Dokureihe
    11354.6h 3.03% Dokusoap
    10759.6h 2.87% Regionalmagazin
    9454.4h  2.52% Dokumentation
    9116.6h  2.43% *unknown*
    7094.5h  1.89% Zeichentrickserie
    6858.0h  1.83% Infomercial
    6633.1h  1.77% Animationsserie
    6150.0h  1.64% Comedyserie
    5269.7h  1.40% Morgenmagazin
    4981.5h  1.33% Religionsmagazin
    4941.5h  1.32% Talkshow
    4567.4h  1.22% Magazin
    4200.8h  1.12% Programmende
    3718.7h  0.99% E-Sport
    3535.8h  0.94% Wetterbericht
    3524.1h  0.94% Sitcom
    3392.6h  0.90% Börsenmagazin
    3007.4h  0.80% Quiz
    2951.3h  0.79% Musikmagazin
    2887.4h  0.77% Komödie
    2874.1h  0.77% Wirtschaftsmagazin
    2819.0h  0.75% Wissensmagazin
    2605.6h  0.69% Telenovela
    2436.7h  0.65% Reportagereihe
    2427.8h  0.65% Sportmagazin
