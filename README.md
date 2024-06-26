# Котокафе

## Правила игры

1. Каждый игрок берет лист с 5 башнями.
2. Возьмите нужное кол-во кубиков - на один больше, чем игроков.
3. Каждый раунд первый игрок будет бросать кубики, а затем каждый по порядку выберет себе один. Последний кубик останется — его могут использовать все участники.
4. Так у каждого игрока в распоряжении два кубика. Один из них должен указать предмет, который вы будете рисовать на башне. Второй кубик покажет, на какой этаж башни поместить выбранный предмет.
5. Побеждает тот, кто быстрее заполнит 3 башни предметами.

## Текстовый интерфейс

Предметы:
1 - домик
2 - клубок
3 - бабочка
4 - миска
5 - подушка
6 - мышь

Пусть будет два игрока: Dendi, Pudge

```
numbers on cubes: 6 3 2
Dendi choose: 6
Pudge choose: 3
central cube: 2
Dendi play: башня-1, предмет-6, этаж-2
Pudge play: башня-5, предмет-2, этаж-3
-----
numbers on cubes: 5 1 6
Pudge choose: 5
Dendi choose: 1
central cube: 6
Dendi play: башня-1, предмет-1, этаж-6
Pudge play: башня-5, предмет-6, этаж-5
-----
numbers on cubes: 4 1 4
Dendi choose: 1
Pudge choose: 4
central cube: 4
Dendi play: башня-1, предмет-4, этаж-1
Pudge play: башня-5, предмет-4, этаж-4
-----
numbers on cubes: 1 3 2
Pudge choose: 2
Dendi choose: 3
central cube: 1
Dendi play: башня-2, предмет-3, этаж-1
Pudge play: башня-5, предмет-1, этаж-2
-----
numbers on cubes: 2 6 1
Dendi choose: 1
Pudge choose: 6
central cube: 2
Dendi play: башня-2, предмет-1, этаж-2
Pudge play: башня-5, предмет-2, этаж-6
-----
-----
-----
Pudge win!
```

## Пример save-файла

```
{
  "cube_numbers":"6 3 2",
  "current_player_index": 0,
  "players":[
    {
      "name":"Dendi",
      "choosen_cube": 6
    },
    {
      "name":"Pudge",
      "choosen_cube": 3
    }
  ]
} 
```
