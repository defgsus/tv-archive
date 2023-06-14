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

**96** channels, **269,429.9** hours playtime between **2023-01-17** and **2023-06-15**


### playtime per genre (top 30)

    17964.8h 6.67% Nachrichten
    12968.8h 4.81% Verkaufsshow
    10776.1h 4.00% Krimiserie
    8961.0h  3.33% Werbesendung
    8786.8h  3.26% Dokureihe
    8085.1h  3.00% Dokusoap
    7702.3h  2.86% Regionalmagazin
    6905.7h  2.56% Dokumentation
    6733.5h  2.50% *unknown*
    5109.8h  1.90% Zeichentrickserie
    4936.4h  1.83% Infomercial
    4777.7h  1.77% Animationsserie
    4478.2h  1.66% Comedyserie
    3743.0h  1.39% Morgenmagazin
    3554.1h  1.32% Talkshow
    3533.2h  1.31% Religionsmagazin
    3389.9h  1.26% Programmende
    3131.7h  1.16% Magazin
    2698.6h  1.00% E-Sport
    2544.2h  0.94% Sitcom
    2469.9h  0.92% Wetterbericht
    2433.4h  0.90% Börsenmagazin
    2120.5h  0.79% Wirtschaftsmagazin
    2100.9h  0.78% Quiz
    2089.5h  0.78% Musikmagazin
    2076.2h  0.77% Wissensmagazin
    2008.4h  0.75% Komödie
    1911.4h  0.71% Telenovela
    1836.7h  0.68% Sportmagazin
    1759.1h  0.65% Gesundheitsmagazin
