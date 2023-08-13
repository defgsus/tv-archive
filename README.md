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

**96** channels, **376,988.3** hours playtime between **2023-01-17** and **2023-08-14**


### playtime per genre (top 30)

    24917.4h 6.61% Nachrichten
    17847.0h 4.73% Verkaufsshow
    15250.7h 4.05% Krimiserie
    12703.2h 3.37% Werbesendung
    12442.7h 3.30% Dokureihe
    11394.7h 3.02% Dokusoap
    10790.0h 2.86% Regionalmagazin
    9513.4h  2.52% Dokumentation
    9169.0h  2.43% *unknown*
    7129.0h  1.89% Zeichentrickserie
    6889.4h  1.83% Infomercial
    6664.1h  1.77% Animationsserie
    6160.4h  1.63% Comedyserie
    5277.1h  1.40% Morgenmagazin
    5022.7h  1.33% Religionsmagazin
    4983.3h  1.32% Talkshow
    4598.9h  1.22% Magazin
    4215.7h  1.12% Programmende
    3736.8h  0.99% E-Sport
    3553.1h  0.94% Wetterbericht
    3530.2h  0.94% Sitcom
    3408.6h  0.90% Börsenmagazin
    3014.6h  0.80% Quiz
    2971.8h  0.79% Musikmagazin
    2915.8h  0.77% Komödie
    2880.6h  0.76% Wirtschaftsmagazin
    2835.0h  0.75% Wissensmagazin
    2605.6h  0.69% Telenovela
    2457.6h  0.65% Reportagereihe
    2433.6h  0.65% Sportmagazin
