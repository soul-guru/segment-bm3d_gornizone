import json
import logging

import aiohttp
import json_numpy
from pprint import pprint

import numpy as np
from loguru import logger

from aiohttp import web

import sdk
from sdk import fs
from sdk.modules.context_to_3d import context_to_3d
from sdk.modules.scan_closest_points_and_links import scan_closest_points_and_links


async def find_links_and_cords(request):
    json_body = await request.json()
    namespace = json_body.get("namespace")
    
    _3d_request = context_to_3d(json_body.get('body'))
    _data = []
    
    for query in _3d_request[1]:
        pprint(query)
        fs.read_db_file(
            namespace,
            lambda lines: _data.append(
                scan_closest_points_and_links(
                    lines,
                    [
                        np.float32(query[0][0]),
                        np.float32(query[0][1]),
                        np.float32(query[0][2]),
                        query[1],
                    ],
                    0.000001
                )
            )
        )

    # for points in cords:
    #     print(cords)
    #     x, y, z = points
    # 
    #     namespace = json_body.get("namespace")
    # 
    #     npc = np.array([
    #         np.float32(x),
    #         np.float32(y),
    #         np.float32(z),
    #     ])
    # 
    #     results = await search(npc, namespace)
    # 
    #     _data.append(results)

    return web.Response(text=json_numpy.dumps({
        "scan": _data
    }), content_type="application/json")


async def prompt_for_brain(request):
    json_data = await request.json()
    raw = json_data.get('body')
    namespace = json_data.get('namespace')

    points = context_to_3d(raw)

    with open(f"l2db/{namespace}", 'a+') as infile:
        infile.write(json_numpy.dumps({"p": points}) + "\n")

    return web.Response(text=json_numpy.dumps({
        "isOk": True,
        "data": 1
    }))


async def get_brain_nn(request):
    return web.Response(text=json_numpy.dumps({
        "isOk": True,
    }))


async def index(request):
    return web.Response(text=json_numpy.dumps({
        "manifest": {
            "name": sdk.__PRODUCT_NAME__,
            "version": sdk.__VERSION__
        },
        "routes": {
            "/opt/brain/listen": {
                "method": "POST",
                "exampleData": {
                    "body": "string",
                    "namespace": "string"
                }
            },
            "/opt/brain/find": {
                "method": "POST",
                "exampleData": {
                    "body": "string",
                    "namespace": "string"
                }
            }
        }
    }))


async def search(query_point, namespace):
    _result = []

    fs.read_db_file(
        namespace,
        lambda lines: _result.append(
            scan_closest_points_and_links(
                lines,
                query_point,
                0.000001
            )
        )
    )

    return _result


app = web.Application()

app.add_routes([
    web.get('/', index),
    web.post('/opt/brain/listen', prompt_for_brain),
    web.post('/opt/brain/find', find_links_and_cords),
])


async def on_request_start(session, context, params):
    logger.debug(f'Starting request <{params}>')


if __name__ == "__main__":
    logger.info("Hello world")
    logger.debug("Software is a 'segment-bm3d_gornizone'")

    logging.basicConfig(level=logging.DEBUG)
    
    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_start.append(on_request_start)
    
    web.access_logger = logger
        
    web.run_app(app, host='127.0.0.1', port=8080, print=logger.debug)

    # search()
