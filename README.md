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

**96** channels, **353,611.7** hours playtime between **2023-01-17** and **2023-08-01**


### playtime per genre (top 30)

    23441.8h 6.63% Nachrichten
    16884.2h 4.77% Verkaufsshow
    14237.2h 4.03% Krimiserie
    11887.4h 3.36% Werbesendung
    11577.1h 3.27% Dokureihe
    10672.4h 3.02% Dokusoap
    10133.4h 2.87% Regionalmagazin
    8901.8h  2.52% Dokumentation
    8587.4h  2.43% *unknown*
    6695.3h  1.89% Zeichentrickserie
    6468.8h  1.83% Infomercial
    6241.1h  1.76% Animationsserie
    5814.9h  1.64% Comedyserie
    4941.2h  1.40% Morgenmagazin
    4694.6h  1.33% Religionsmagazin
    4683.2h  1.32% Talkshow
    4217.1h  1.19% Magazin
    4037.9h  1.14% Programmende
    3494.4h  0.99% E-Sport
    3331.1h  0.94% Sitcom
    3318.3h  0.94% Wetterbericht
    3201.0h  0.91% Börsenmagazin
    2826.3h  0.80% Quiz
    2770.7h  0.78% Musikmagazin
    2724.6h  0.77% Komödie
    2718.7h  0.77% Wirtschaftsmagazin
    2673.8h  0.76% Wissensmagazin
    2436.3h  0.69% Telenovela
    2313.8h  0.65% Sportmagazin
    2278.9h  0.64% Reportagereihe
