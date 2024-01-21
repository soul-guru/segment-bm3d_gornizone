import json

import numpy as np
import pandas as pd


def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


def scan_closest_points_and_links(
        # [x, y, z, g]
        data: list[
            (
                str,
                list[
                    (
                        (
                            np.float32,
                            np.float32,
                            np.float32
                        ),
                        int,
                        str
                    )        
                ]
            )
        ],
        
        # [x, y, z]
        query: list[np.float32, np.float32, np.float32, np.float32],
        
        # float
        precision: float = 4
) -> object:
    query_x, query_y, query_z, query_g = query
    relevant_records = []
    records_by_g = {}  # Словарь для хранения записей по каждому G

    # # Перебор всех записей и классификация по G
    for record in data:
        print(record)
        link, points = record[0], record[1:]
        for point in points:
            for coords, g, text in point:
                if g not in records_by_g:
                    records_by_g[g] = []
                records_by_g[g].append(record)

    def add_relevant_record(record, coords: float):
        distance = euclidean_distance((query_x, query_y, query_z), coords)
        for i in relevant_records:
            if i[0][0] == record[0]:
                return
            
        relevant_records.append((record, distance))

    # Поиск в изначальном G
    if query_g in records_by_g:
        for record in records_by_g[query_g]:
            link, points = record[0], record[1:]
            for point in points:
                for coords, g, text in point:
                    if euclidean_distance((query_x, query_y, query_z), coords) <= precision:
                        add_relevant_record(record, coords)
                        break  # Найдена подходящая точка в этой G-группе

    # Если ничего не найдено в изначальном G, ищем в других G
    if not relevant_records:
        for g, records in records_by_g.items():
            if g != query_g:
                for record in records:
                    link, points = record[0], record[1:]
                    for point in points:
                        for coords, _, text in point:
                            if euclidean_distance((query_x, query_y, query_z), coords) <= precision:
                                add_relevant_record(record, coords)
                                break  # Найдена подходящая точка в другой G-группе

    # Извлечение уникальных идентификаторов из данных
    ids = np.array([item[0][0] for item in relevant_records])
    
    # Уникализация идентификаторов
    unique_ids = np.unique(ids)
    
    # Фильтрация исходных данных по уникальным идентификаторам
    unique_data = [item for item in relevant_records if item[0][0] in unique_ids]
    
    return unique_data

    
    # processed_points: list[([np.float32], str)] = [
    #     (
    #         np.array(
    #             [
    #                 np.float32(chunks[0][0]),
    #                 np.float32(chunks[0][1]),
    #                 np.float32(chunks[0][2])
    #             ]
    #         ), link
    #     ) for link, chunks in points
    # ]
    # 
    # links: dict[str, list[float]] = {}
    # 
    # for point, link in processed_points:
    #     if link in links:
    #         links[link].append(point.tolist())
    #     else:
    #         links[link] = [point.tolist()]
    # 
    # distances = [
    #     (
    #         square_distance(
    #             np.array(query_point, dtype=np.float32).tolist(),
    #             np.array(point, dtype=np.float32).tolist()
    #         ), link
    #     ) for point, link in processed_points
    # ]
    # 
    # distances.sort(key=lambda x: x[0])
    # 
    # result = []
    # 
    # for i in distances:
    #     if i[0] <= n:
    #         result.append(i)
    # 
    # return result
