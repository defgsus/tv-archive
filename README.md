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

**96** channels, **321,344.7** hours playtime between **2023-01-17** and **2023-07-14**


### playtime per genre (top 30)

    21417.9h 6.67% Nachrichten
    15382.5h 4.79% Verkaufsshow
    12901.8h 4.01% Krimiserie
    10776.0h 3.35% Werbesendung
    10466.5h 3.26% Dokureihe
    9747.1h  3.03% Dokusoap
    9219.6h  2.87% Regionalmagazin
    8079.1h  2.51% Dokumentation
    7893.2h  2.46% *unknown*
    6114.7h  1.90% Zeichentrickserie
    5875.4h  1.83% Infomercial
    5659.6h  1.76% Animationsserie
    5333.4h  1.66% Comedyserie
    4515.3h  1.41% Morgenmagazin
    4262.0h  1.33% Talkshow
    4244.5h  1.32% Religionsmagazin
    3823.8h  1.19% Magazin
    3789.9h  1.18% Programmende
    3181.2h  0.99% E-Sport
    3052.9h  0.95% Sitcom
    2989.4h  0.93% Wetterbericht
    2874.8h  0.89% Börsenmagazin
    2554.7h  0.80% Quiz
    2525.5h  0.79% Musikmagazin
    2500.1h  0.78% Wirtschaftsmagazin
    2468.3h  0.77% Wissensmagazin
    2429.1h  0.76% Komödie
    2254.9h  0.70% Telenovela
    2139.6h  0.67% Sportmagazin
    2045.7h  0.64% Dramaserie
