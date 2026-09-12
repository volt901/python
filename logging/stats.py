import logging

logging.basicConfig (
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename= "app.log",
    filemode= "a"
                    )

def stats(*args):
    logging.info("вызов функции stats")
    try:
        if not args:
            logging.warning("передано ноль аргументов")
            return "нет данных для анализа"
        sort_args = sorted(args)
        if len(sort_args) % 2 != 1:
            median = sort_args[len(sort_args) // 2]
        else:
            median = (sort_args[len(sort_args) // 2] + sort_args[len(sort_args) // 2 - 1]) / 2

        numbers = {
            "min": sort_args[0] ,
            "max": sort_args[-1],
            "avg": round(sum(args) / len(args),2),
            "median": median,
            "count": len(args),
        }
        return numbers
    except Exception as E:
        logging.error(f"ошибка - {E}")

stats()