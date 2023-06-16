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

**96** channels, **273,022.8** hours playtime between **2023-01-17** and **2023-06-17**


### playtime per genre (top 30)

    18224.9h 6.68% Nachrichten
    13161.9h 4.82% Verkaufsshow
    10930.4h 4.00% Krimiserie
    9080.0h  3.33% Werbesendung
    8871.0h  3.25% Dokureihe
    8215.9h  3.01% Dokusoap
    7825.2h  2.87% Regionalmagazin
    6976.0h  2.56% Dokumentation
    6827.5h  2.50% *unknown*
    5179.0h  1.90% Zeichentrickserie
    4999.8h  1.83% Infomercial
    4836.3h  1.77% Animationsserie
    4543.3h  1.66% Comedyserie
    3811.0h  1.40% Morgenmagazin
    3604.3h  1.32% Talkshow
    3577.2h  1.31% Religionsmagazin
    3417.0h  1.25% Programmende
    3179.6h  1.16% Magazin
    2731.9h  1.00% E-Sport
    2582.2h  0.95% Sitcom
    2505.1h  0.92% Wetterbericht
    2455.8h  0.90% Börsenmagazin
    2152.8h  0.79% Wirtschaftsmagazin
    2134.2h  0.78% Quiz
    2122.6h  0.78% Musikmagazin
    2108.6h  0.77% Wissensmagazin
    2015.7h  0.74% Komödie
    1944.5h  0.71% Telenovela
    1848.5h  0.68% Sportmagazin
    1771.0h  0.65% Gesundheitsmagazin
