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

**97** channels, **568,632.9** hours playtime between **2023-01-17** and **2023-11-29**


### playtime per genre (top 30)

    37403.9h 6.58% Nachrichten
    27226.8h 4.79% Verkaufsshow
    22969.5h 4.04% Krimiserie
    19306.5h 3.40% Werbesendung
    18504.7h 3.25% Dokureihe
    17184.4h 3.02% Dokusoap
    16450.1h 2.89% Regionalmagazin
    14506.9h 2.55% Dokumentation
    13862.4h 2.44% *unknown*
    10522.5h 1.85% Zeichentrickserie
    10360.9h 1.82% Infomercial
    10118.5h 1.78% Animationsserie
    8853.6h  1.56% Comedyserie
    8097.9h  1.42% Morgenmagazin
    7681.3h  1.35% Religionsmagazin
    7602.9h  1.34% Talkshow
    7264.3h  1.28% Magazin
    5692.1h  1.00% Programmende
    5565.9h  0.98% E-Sport
    5471.9h  0.96% Sitcom
    5211.7h  0.92% Wetterbericht
    5166.7h  0.91% Börsenmagazin
    4737.1h  0.83% Quiz
    4402.5h  0.77% Komödie
    4322.8h  0.76% Wissensmagazin
    4263.4h  0.75% Wirtschaftsmagazin
    4163.7h  0.73% Musikmagazin
    4121.6h  0.72% Telenovela
    4010.8h  0.71% Politikmagazin
    4005.1h  0.70% Realityshow
