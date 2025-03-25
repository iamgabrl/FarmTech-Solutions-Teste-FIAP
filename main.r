dados <- read.csv("data.csv")

media_area <- mean(dados$area)
media_total_liters <- mean(dados$total_liters)
media_number_of_rows <- mean(dados$number_of_rows)

print("Média área:")
print(media_area)

print("Média total de litros:")
print(media_total_liters)

print("Média número de ruas:")
print(media_number_of_rows)

detour_area <- sd(dados$area)
detour_total_liters <- sd(dados$total_liters)
detour_number_of_rows <- sd(dados$number_of_rows)

print("Desvio área:")
print(detour_area)

print("Desvio total de litros:")
print(detour_total_liters)

print("Desvio número de ruas:")
print(detour_number_of_rows)