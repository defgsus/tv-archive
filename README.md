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

**97** channels, **393,132.0** hours playtime between **2023-01-17** and **2023-08-23**


### playtime per genre (top 30)

    25988.2h 6.61% Nachrichten
    18530.3h 4.71% Verkaufsshow
    15947.8h 4.06% Krimiserie
    13241.8h 3.37% Werbesendung
    13031.2h 3.31% Dokureihe
    11883.1h 3.02% Dokusoap
    11278.2h 2.87% Regionalmagazin
    9945.4h  2.53% Dokumentation
    9537.3h  2.43% *unknown*
    7428.4h  1.89% Zeichentrickserie
    7180.4h  1.83% Infomercial
    6943.6h  1.77% Animationsserie
    6418.4h  1.63% Comedyserie
    5534.6h  1.41% Morgenmagazin
    5242.8h  1.33% Religionsmagazin
    5164.5h  1.31% Talkshow
    4892.9h  1.24% Magazin
    4343.6h  1.10% Programmende
    3901.7h  0.99% E-Sport
    3713.7h  0.94% Wetterbericht
    3679.7h  0.94% Sitcom
    3555.2h  0.90% Börsenmagazin
    3181.1h  0.81% Quiz
    3103.4h  0.79% Musikmagazin
    3044.9h  0.77% Komödie
    2995.5h  0.76% Wirtschaftsmagazin
    2942.7h  0.75% Wissensmagazin
    2745.2h  0.70% Telenovela
    2587.1h  0.66% Reportagereihe
    2532.2h  0.64% Sportmagazin
