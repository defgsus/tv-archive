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

**96** channels, **350,042.0** hours playtime between **2023-01-17** and **2023-07-30**


### playtime per genre (top 30)

    23235.3h 6.64% Nachrichten
    16717.2h 4.78% Verkaufsshow
    14099.2h 4.03% Krimiserie
    11763.0h 3.36% Werbesendung
    11444.8h 3.27% Dokureihe
    10589.9h 3.03% Dokusoap
    10036.9h 2.87% Regionalmagazin
    8813.5h  2.52% Dokumentation
    8513.7h  2.43% *unknown*
    6629.8h  1.89% Zeichentrickserie
    6405.9h  1.83% Infomercial
    6174.5h  1.76% Animationsserie
    5769.7h  1.65% Comedyserie
    4902.8h  1.40% Morgenmagazin
    4636.8h  1.32% Religionsmagazin
    4621.2h  1.32% Talkshow
    4178.9h  1.19% Magazin
    4011.1h  1.15% Programmende
    3452.8h  0.99% E-Sport
    3305.1h  0.94% Sitcom
    3283.8h  0.94% Wetterbericht
    3159.7h  0.90% Börsenmagazin
    2790.5h  0.80% Quiz
    2742.3h  0.78% Musikmagazin
    2695.7h  0.77% Wirtschaftsmagazin
    2682.5h  0.77% Komödie
    2646.6h  0.76% Wissensmagazin
    2421.7h  0.69% Telenovela
    2296.1h  0.66% Sportmagazin
    2243.6h  0.64% Reportagereihe
