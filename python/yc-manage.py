import argparse
import os
import json
import requests

YC_TOKEN = os.getenv("YC_TOKEN")
FOLDER_ID = "b1gdegge71708tm0i2in"

BASE_URL = "https://compute.api.cloud.yandex.net/compute/v1/instances"
headers = {
    'Authorization': f"Bearer {YC_TOKEN}"
}

def get_instance_id(host):
    url = f"{BASE_URL}?folderId={FOLDER_ID}"
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        instances = response.json().get("instances", [])
        target = None
        for instance in instances:
            if instance.get("name") == args.host:
                target = instance
                break
        if not target:
            print(f"Not found host {host}")
        target_id = target.get("id")
        return target_id


parser = argparse.ArgumentParser(description="YC stop/start VM")
parser.add_argument("--action")
parser.add_argument("--list", action="store_true")
parser.add_argument("--host")

args = parser.parse_args()

if args.list:
    url = f"{BASE_URL}?folderId={FOLDER_ID}"
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        instances = response.json().get("instances", [])
        for instance in instances:
            print(f"HOST: {instance.get('name')}\tSTATE: {instance.get('status')}")

if args.action == "start":
    target = get_instance_id(args.host)
    start_url = f"{BASE_URL}/{target}:start"
    response = requests.post(start_url, headers=headers, timeout=10)
    if response.status_code == 200:
        print(f"Instance {target} starting")
    else:
        print(f"Failed to start {target}")
elif args.action == "stop":
    target = get_instance_id(args.host)
    stop_url = f"{BASE_URL}/{target}:stop"
    response = requests.post(stop_url, headers=headers, timeout=10)
    if response.status_code == 200:
        print(f"Instance {target} stopping")
    else:
        print(f"Failed to stop instance {target}")
