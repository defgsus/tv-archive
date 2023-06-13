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

**96** channels, **267,604.3** hours playtime between **2023-01-17** and **2023-06-14**


### playtime per genre (top 30)

    17822.5h 6.66% Nachrichten
    12889.9h 4.82% Verkaufsshow
    10709.8h 4.00% Krimiserie
    8894.2h  3.32% Werbesendung
    8731.0h  3.26% Dokureihe
    8030.9h  3.00% Dokusoap
    7631.8h  2.85% Regionalmagazin
    6863.2h  2.56% Dokumentation
    6696.9h  2.50% *unknown*
    5072.8h  1.90% Zeichentrickserie
    4902.9h  1.83% Infomercial
    4749.4h  1.77% Animationsserie
    4442.2h  1.66% Comedyserie
    3708.2h  1.39% Morgenmagazin
    3525.4h  1.32% Talkshow
    3513.8h  1.31% Religionsmagazin
    3375.8h  1.26% Programmende
    3113.7h  1.16% Magazin
    2675.0h  1.00% E-Sport
    2520.2h  0.94% Sitcom
    2452.3h  0.92% Wetterbericht
    2423.0h  0.91% Börsenmagazin
    2102.8h  0.79% Wirtschaftsmagazin
    2083.6h  0.78% Quiz
    2081.4h  0.78% Musikmagazin
    2062.5h  0.77% Wissensmagazin
    1995.4h  0.75% Komödie
    1894.2h  0.71% Telenovela
    1827.5h  0.68% Sportmagazin
    1739.8h  0.65% Gesundheitsmagazin
