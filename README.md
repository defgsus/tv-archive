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

**96** channels, **326,737.3** hours playtime between **2023-01-17** and **2023-07-17**


### playtime per genre (top 30)

    21713.6h 6.65% Nachrichten
    15624.3h 4.78% Verkaufsshow
    13099.2h 4.01% Krimiserie
    10967.2h 3.36% Werbesendung
    10690.1h 3.27% Dokureihe
    9892.1h  3.03% Dokusoap
    9333.3h  2.86% Regionalmagazin
    8217.5h  2.52% Dokumentation
    8016.8h  2.45% *unknown*
    6217.9h  1.90% Zeichentrickserie
    5973.5h  1.83% Infomercial
    5751.4h  1.76% Animationsserie
    5389.4h  1.65% Comedyserie
    4556.2h  1.39% Morgenmagazin
    4348.2h  1.33% Talkshow
    4333.2h  1.33% Religionsmagazin
    3894.2h  1.19% Magazin
    3831.2h  1.17% Programmende
    3233.1h  0.99% E-Sport
    3095.4h  0.95% Sitcom
    3044.4h  0.93% Wetterbericht
    2908.9h  0.89% Börsenmagazin
    2587.1h  0.79% Quiz
    2566.2h  0.79% Musikmagazin
    2524.6h  0.77% Wirtschaftsmagazin
    2503.5h  0.77% Wissensmagazin
    2489.2h  0.76% Komödie
    2268.7h  0.69% Telenovela
    2166.9h  0.66% Sportmagazin
    2089.1h  0.64% Wirtschaftstalk
