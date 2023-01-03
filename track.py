#! /usr/bin/python3

import re
import argparse

# TODO list toplevel item
# TODO use json

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--month", type=str, help = "select the month markdown file to track")
args = parser.parse_args()

month = args.month

with open(month+'.md', 'r', encoding = 'utf-8') as f:
    content = f.read()

# top_items_pattern=re.compile(r'^-\.*')
total_pattern = re.compile(r'total=\d*')

food_pattern = re.compile(r'food\(.*\)=[^:\n]*|food=[^:\n]*')
tech_pattern = re.compile(r'tech\(.*\)=[^:\n]*|tech=[^:\n]*')
clothing_pattern = re.compile(r'clothing\(.*\)=[^:\n]*|clothing=[^:\n]*')
pharma_pattern = re.compile(r'pharma\(.*\)=[^:\n]*|pharma=[^:\n]*')
travel_pattern = re.compile(r'travel\(.*\)=[^:\n]*|travel=[^:\n]*')
transport_pattern = re.compile(r'transport\(.*\)=[^:\n]*|transport=[^:\n]*')
cleaning_pattern = re.compile(r'cleaning\(.*\)=[^:\n]*|cleaning=[^:\n]*')
fourniture_pattern = re.compile(r'fourniture\(.*\)=[^:\n]*|fourniture=[^:\n]*')
moto_pattern = re.compile(r'moto\(.*\)=[^:\n]*|moto=[^:\n]*')
naps_pattern = re.compile(r'naps\(.*\)=[^:\n]*|naps=[^:\n]*')
dons_pattern = re.compile(r'dons\(.*\)=[^:\n]*|dons=[^:\n]*')
gaz_pattern = re.compile(r'gaz\(.*\)=[^:\n]*|gaz=[^:\n]*')
services_pattern = re.compile(r'services\(.*\)=[^:\n]*|services=[^:\n]*')

# top_level_items=top_items_pattern.findall(content)
total = total_pattern.findall(content)

# print("top_level_items = ", top_level_items)

food = food_pattern.findall(content)
tech = tech_pattern.findall(content)
clothing = clothing_pattern.findall(content)
pharma = pharma_pattern.findall(content)
travel = travel_pattern.findall(content)
cleaning = cleaning_pattern.findall(content)
transport = transport_pattern.findall(content)
fourniture = fourniture_pattern.findall(content)
moto = moto_pattern.findall(content)
naps = naps_pattern.findall(content)
dons = dons_pattern.findall(content)
gaz = gaz_pattern.findall(content)
services = services_pattern.findall(content)

print(f'month: {month}\n')

#print(top_level_items)

def print_item(category, category_str):
    amounts_list=[]
    for item in category:
        amounts_list.append(float(item.split('=')[1]))
    sum_amounts=sum(amounts_list)
    print(f'{category_str} list = {amounts_list}')
    print(f'{category_str} count = {len(amounts_list)}')
    print(f'sum_{category_str} = {sum_amounts}')
    print(f'percent_{category_str} = {100*sum_amounts/sum_total} %\n')


total_c=[]
for item in total:
    total_c.append(float(item.split('=')[1]))
sum_total=sum(total_c)
print(f'total list = {total_c}')
print(f'total count = {len(total_c)}')
print(f'sum_total = {sum_total}\n')

print_item(food, 'food')
print_item(pharma, 'pharma')
print_item(clothing, 'clothing')
print_item(tech, 'tech')
print_item(travel, 'travel')
print_item(transport, 'transport')
print_item(cleaning, 'cleaning')
print_item(fourniture, 'fourniture')
print_item(moto, 'moto')
print_item(naps, 'naps')
print_item(dons, 'dons')
print_item(gaz, 'gaz')
print_item(services, 'services')
