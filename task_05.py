from datetime import datetime, timedelta

# Разработать метод date_in_future(integer), который вернет дату через integer дней.
# Если integer не является целым числом, то метод должен вывести текущую дату.
# Формат возвращаемой методом даты должен иметь следующий вид '24-03-2001
# 22:33:44'.


def formatDateTime(date: datetime) -> str:
    return date.strftime("%d-%m-%Y %H:%M:%S")


def date_in_future(offest: int | None):
    now = datetime.now()
    if not isinstance(offest, int):
        return formatDateTime(now)
    future_date = now + timedelta(days=offest)
    return formatDateTime(future_date)


if __name__ == "__main__":
    print(date_in_future(-1))
    print(date_in_future(None))
    print(date_in_future(1))
