#!/usr/bin/env python3

import argparse
import json
import os
import requests
import sys

CMDB_URL = os.getenv("CMDB_URL", "http://localhost:8080")

parser = argparse.ArgumentParser(prog="cmdb-client")
parser.add_argument("--json", action="store_true", help="Output in json")
parser.add_argument("--url", default=CMDB_URL, help="API url")

subparsers = parser.add_subparsers(dest="command", required=True)

# ARGS FOR list comand
p_list = subparsers.add_parser("list", help="List all")
# фильтр по типу сервера
p_list.add_argument("--type", dest="entity_type")
# фильтр по окружению (dev/prod/demo)
p_list.add_argument("--env")
# какое поле вывести
p_list.add_argument("--field", default="id")
p_list.set_defaults(action="list")

# ARGS FOR get command
p_get = subparsers.add_parser("get", help="Get info about one server")
p_get.add_argument("id")
p_get.add_argument("--type", dest="entity_type")
p_get.set_defaults(action="get")


args = parser.parse_args()
base_url = args.url

if args.action == "list":
  response = requests.get(f"{base_url}/all", timeout=10)
  if response.status_code != 200:
    print(f"Error: HTTP {response.status_code}")
    sys.exit(1)
  data = response.json()

  if "entities" in data:
    entities = data["entities"]
  else:
    entities = []
    for key, value in data.items():
      if isinstance(value, list):
        for item in value:
          if "type" not in item:
            item["type"] = key
          entities.append(item)

  if args.entity_type:
    entities = [e for e in entities if e.get("type") == args.entity_type]

  if args.env:
    entities = [e for e in entities if e.get("environment") == args.env]

  if args.json:
    print(json.dumps(entities, indent=2))
    #return

  field = args.field
  for e in entities:
    val = e.get(field) or e.get("id")
    print(val)
elif args.action == "get":
  response = requests.get(f"{base_url}/all", timeout=10)
  if response.status_code != 200:
    print(f"Error: HTTP {response.status_code}")
    sys.exit(1)
  data = response.json()

  if "entities" in data:
    entities = data["entities"]
  else:
    entities = []
    for key, value in data.items():
      if isinstance(value, list):
        for item in value:
          if "type" not in item:
            item["type"] = key
          entities.append(item)
  target = None
  for e in entities:
    if str(e.get("id")) == args.id:
      if args.entity_type and e.get("type") != args.entity_type:
        continue
      target = e
      break
  if not target:
    print(f"Entity not found")
    sys.exit(1)

  if args.json:
    print(json.dumps(target, indent=2))
  else:
    for k, v in target.items():
      print(f"{k}: {v}")
