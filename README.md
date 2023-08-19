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

**97** channels, **387,758.4** hours playtime between **2023-01-17** and **2023-08-20**


### playtime per genre (top 30)

    25648.5h 6.61% Nachrichten
    18295.2h 4.72% Verkaufsshow
    15713.4h 4.05% Krimiserie
    13067.0h 3.37% Werbesendung
    12819.7h 3.31% Dokureihe
    11732.7h 3.03% Dokusoap
    11117.9h 2.87% Regionalmagazin
    9793.5h  2.53% Dokumentation
    9421.5h  2.43% *unknown*
    7321.2h  1.89% Zeichentrickserie
    7082.9h  1.83% Infomercial
    6850.2h  1.77% Animationsserie
    6337.6h  1.63% Comedyserie
    5456.9h  1.41% Morgenmagazin
    5156.8h  1.33% Religionsmagazin
    5093.8h  1.31% Talkshow
    4817.5h  1.24% Magazin
    4300.9h  1.11% Programmende
    3844.8h  0.99% E-Sport
    3662.0h  0.94% Wetterbericht
    3633.5h  0.94% Sitcom
    3498.1h  0.90% Börsenmagazin
    3129.3h  0.81% Quiz
    3055.4h  0.79% Musikmagazin
    3002.8h  0.77% Komödie
    2960.0h  0.76% Wirtschaftsmagazin
    2901.8h  0.75% Wissensmagazin
    2704.8h  0.70% Telenovela
    2546.2h  0.66% Reportagereihe
    2497.4h  0.64% Sportmagazin
