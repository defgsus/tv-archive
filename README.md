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

**109** channels, **1,063,554.0** hours playtime between **2023-01-17** and **2024-09-26**


### playtime per genre (top 30)

    69206.1h 6.51% Nachrichten
    49266.1h 4.63% Verkaufsshow
    43944.3h 4.13% Krimiserie
    38666.9h 3.64% Werbesendung
    33336.2h 3.13% Dokureihe
    31956.7h 3.00% Dokusoap
    31081.8h 2.92% Regionalmagazin
    27823.8h 2.62% Dokumentation
    25504.2h 2.40% *unknown*
    19744.8h 1.86% Zeichentrickserie
    19526.9h 1.84% Infomercial
    19054.6h 1.79% Animationsserie
    15518.8h 1.46% Comedyserie
    14899.9h 1.40% Morgenmagazin
    14477.6h 1.36% Religionsmagazin
    14019.6h 1.32% Talkshow
    13767.6h 1.29% Magazin
    10522.3h 0.99% E-Sport
    10211.6h 0.96% Sitcom
    9634.1h  0.91% Wetterbericht
    9498.5h  0.89% Programmende
    9305.6h  0.87% Komödie
    9262.7h  0.87% Quiz
    8308.9h  0.78% Börsenmagazin
    7999.7h  0.75% Politikmagazin
    7989.6h  0.75% Wissensmagazin
    7981.8h  0.75% Realityshow
    7206.7h  0.68% Wirtschaftsmagazin
    7010.3h  0.66% Telenovela
    6934.9h  0.65% Dramaserie
