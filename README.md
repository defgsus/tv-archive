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

**96** channels, **308,794.8** hours playtime between **2023-01-17** and **2023-07-07**


### playtime per genre (top 30)

    20619.5h 6.68% Nachrichten
    14796.7h 4.79% Verkaufsshow
    12381.8h 4.01% Krimiserie
    10337.7h 3.35% Werbesendung
    10017.9h 3.24% Dokureihe
    9375.2h  3.04% Dokusoap
    8858.2h  2.87% Regionalmagazin
    7790.1h  2.52% Dokumentation
    7617.3h  2.47% *unknown*
    5886.2h  1.91% Zeichentrickserie
    5653.9h  1.83% Infomercial
    5443.8h  1.76% Animationsserie
    5138.0h  1.66% Comedyserie
    4337.5h  1.40% Morgenmagazin
    4094.9h  1.33% Talkshow
    4069.2h  1.32% Religionsmagazin
    3692.4h  1.20% Programmende
    3657.7h  1.18% Magazin
    3051.8h  0.99% E-Sport
    2928.8h  0.95% Sitcom
    2863.1h  0.93% Wetterbericht
    2748.1h  0.89% Börsenmagazin
    2448.0h  0.79% Quiz
    2424.4h  0.79% Musikmagazin
    2408.1h  0.78% Wirtschaftsmagazin
    2377.0h  0.77% Wissensmagazin
    2317.8h  0.75% Komödie
    2183.4h  0.71% Telenovela
    2057.7h  0.67% Sportmagazin
    1975.2h  0.64% Wirtschaftstalk
