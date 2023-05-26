in_worldpop = open('worldpop.txt', 'r', encoding='utf-8')
in_worldarea = open('worldarea.txt', 'r', encoding='utf-8')

out_file = open('densities.txt', 'w', encoding='utf-8')

in_worldpop.readline()
in_worldarea.readline()

pop_line = in_worldpop.readline()
area_line = in_worldarea.readline()
out_file.write("Population per square km for top 10 countries by population\n")
while pop_line != "" and area_line !="":
    country, pop = pop_line.split(':')
    country, area = area_line.split(':')
    pop_line = in_worldpop.readline()
    area_line = in_worldarea.readline()
    out_file.write(f'{country}:{int(pop)/int(area):.2f}\n')

in_worldpop.close()
in_worldarea.close()
out_file.close()
