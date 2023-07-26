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

**96** channels, **344,665.6** hours playtime between **2023-01-17** and **2023-07-27**


### playtime per genre (top 30)

    22905.5h 6.65% Nachrichten
    16448.6h 4.77% Verkaufsshow
    13871.8h 4.02% Krimiserie
    11580.8h 3.36% Werbesendung
    11247.0h 3.26% Dokureihe
    10408.4h 3.02% Dokusoap
    9893.5h  2.87% Regionalmagazin
    8676.0h  2.52% Dokumentation
    8389.7h  2.43% *unknown*
    6535.8h  1.90% Zeichentrickserie
    6299.9h  1.83% Infomercial
    6082.6h  1.76% Animationsserie
    5691.1h  1.65% Comedyserie
    4831.2h  1.40% Morgenmagazin
    4568.3h  1.33% Religionsmagazin
    4557.4h  1.32% Talkshow
    4115.1h  1.19% Magazin
    3968.8h  1.15% Programmende
    3410.4h  0.99% E-Sport
    3261.6h  0.95% Sitcom
    3229.9h  0.94% Wetterbericht
    3120.7h  0.91% Börsenmagazin
    2753.0h  0.80% Quiz
    2695.6h  0.78% Musikmagazin
    2661.6h  0.77% Wirtschaftsmagazin
    2631.7h  0.76% Komödie
    2615.8h  0.76% Wissensmagazin
    2378.2h  0.69% Telenovela
    2273.1h  0.66% Sportmagazin
    2208.6h  0.64% Reportagereihe
