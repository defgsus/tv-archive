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

**96** channels, **357,166.7** hours playtime between **2023-01-17** and **2023-08-03**


### playtime per genre (top 30)

    23697.0h 6.63% Nachrichten
    17037.5h 4.77% Verkaufsshow
    14401.9h 4.03% Krimiserie
    12008.8h 3.36% Werbesendung
    11698.1h 3.28% Dokureihe
    10777.7h 3.02% Dokusoap
    10255.0h 2.87% Regionalmagazin
    8993.8h  2.52% Dokumentation
    8674.1h  2.43% *unknown*
    6761.1h  1.89% Zeichentrickserie
    6531.9h  1.83% Infomercial
    6313.1h  1.77% Animationsserie
    5879.9h  1.65% Comedyserie
    5008.9h  1.40% Morgenmagazin
    4739.8h  1.33% Religionsmagazin
    4718.0h  1.32% Talkshow
    4249.7h  1.19% Magazin
    4058.0h  1.14% Programmende
    3526.0h  0.99% E-Sport
    3370.1h  0.94% Sitcom
    3353.4h  0.94% Wetterbericht
    3244.1h  0.91% Börsenmagazin
    2852.4h  0.80% Quiz
    2794.4h  0.78% Musikmagazin
    2749.9h  0.77% Wirtschaftsmagazin
    2747.4h  0.77% Komödie
    2695.8h  0.75% Wissensmagazin
    2471.4h  0.69% Telenovela
    2336.7h  0.65% Sportmagazin
    2296.8h  0.64% Reportagereihe
