from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        # TODO создайте атрибут capacity_volume и occupied_volume Обязательно проверяйте типы (TypeError) и значения передаваемых аргументов (ValueError)
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

        if not isinstance (capacity_volume, (int, float)):
            raise TypeError("Аргументы должны быть числами.")
        if capacity_volume <= 0:
            raise ValueError("Объем должен быть больше 0")

        if not isinstance (occupied_volume, (int, float)):
            raise TypeError("Аргументы должны быть числами.")
        if occupied_volume < 0:
            raise ValueError("Заполненный объем не может быть меньше 0")
        if capacity_volume < occupied_volume:
            raise ValueError("Заполненный объем больше чем объем стакана")

if __name__ == "__main__":
    # TODO инициализировать два объекта от класса Стакан (Glass)
    glass1 = Glass (500,300)
    glass2 = Glass (400,200)
    try:
        Glass (300,500)  # TODO инициализировать не корректные объекты
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")