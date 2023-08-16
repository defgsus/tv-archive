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

**97** channels, **382,350.3** hours playtime between **2023-01-17** and **2023-08-17**


### playtime per genre (top 30)

    25310.5h 6.62% Nachrichten
    18059.6h 4.72% Verkaufsshow
    15466.3h 4.05% Krimiserie
    12875.2h 3.37% Werbesendung
    12630.3h 3.30% Dokureihe
    11551.0h 3.02% Dokusoap
    10972.9h 2.87% Regionalmagazin
    9649.8h  2.52% Dokumentation
    9284.5h  2.43% *unknown*
    7230.3h  1.89% Zeichentrickserie
    6982.9h  1.83% Infomercial
    6754.5h  1.77% Animationsserie
    6259.5h  1.64% Comedyserie
    5381.4h  1.41% Morgenmagazin
    5086.5h  1.33% Religionsmagazin
    5033.1h  1.32% Talkshow
    4715.4h  1.23% Magazin
    4254.2h  1.11% Programmende
    3787.5h  0.99% E-Sport
    3608.9h  0.94% Wetterbericht
    3588.4h  0.94% Sitcom
    3475.2h  0.91% Börsenmagazin
    3075.4h  0.80% Quiz
    3009.7h  0.79% Musikmagazin
    2959.7h  0.77% Komödie
    2927.3h  0.77% Wirtschaftsmagazin
    2870.7h  0.75% Wissensmagazin
    2662.2h  0.70% Telenovela
    2494.3h  0.65% Reportagereihe
    2466.8h  0.65% Sportmagazin
