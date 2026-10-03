import time
import matplotlib.pyplot as plt

plt.ylabel("Infected")
plt.xlabel("Generations")

population = int(input("Population: "))
infection_rate = float(input("Infection Rate: "))
infected = int(input("Infected Start: "))
generations = int(input("Generations to run: "))
generations_plot = generations
healthy = population - infected
printed_generations = 1
remainder = 0
infected_list = []
print("---------------")


def simulation(generations, printed_generations, infected, infection_rate, healthy, remainder, infected_list):
    while generations > 0:

        new_infections = healthy * (infection_rate / 100)
        whole_infections = int(new_infections)
        decimal_part = new_infections - whole_infections

        infected += whole_infections
        remainder += decimal_part

        if remainder >= 1:
            infected += 1
            remainder -= 1

        healthy = population - infected
        print(f"Generation: {printed_generations}")
        printed_generations += 1
        generations -= 1
        print(f"Infected: {infected}")
        print(f"Healthy: {healthy}")
        print(f"Remainder: {remainder}")
        print("---------------")

        infected_list.append(infected)
        time.sleep(0.2)
        if healthy <= 0:
            break


simulation(generations, printed_generations, infected,
           infection_rate, healthy, remainder, infected_list)
plt.plot((list(range(1, generations_plot + 1))), infected_list)
plt.show()
