import time
import matplotlib.pyplot as plt

# ==================================================
# inputs
# ==================================================

population = int(input("Population: "))
infected = int(input("Infected Start: "))
infection_rate = float(input("Infection Rate %: "))
recovery_rate = float(input("Recovery Rate %: "))
generations = int(input("Generations to run: "))

# ==================================================
# variable definitions
# ==================================================

generations_plot = generations
susceptible = population - infected
printed_generations = 1
recovered_remainder = 0
infection_remainder = 0
recovered = 0

susceptible_list = [population]
infected_list = [infected]
recovered_list = [0]

print("---------------")
print(f"Generation: 0")
print("Susceptible: ", population)
print("Infected: ", infected)
print("Recovered: 0")
print("Infected Remainder: 0")
print("Recovered Remainder: 0")
print("---------------")

# ==================================================
# simulation function
# ==================================================


def simulation(susceptible_list, recovered_list, recovery_rate, recovered, generations, printed_generations, infected, infection_rate, susceptible, recovered_remainder, infection_remainder, infected_list):
    while generations > 0:

        # ==================================================
        # population calculations
        # ==================================================

        new_recovered = infected * (recovery_rate / 100)
        new_infections = susceptible * (infection_rate / 100)

        whole_infections = int(new_infections)
        infection_decimal = new_infections - whole_infections
        # ==================================================
        # population updates
        # ==================================================

        whole_recovered = int(new_recovered)
        recovered_decimal = new_recovered - whole_recovered

        infected += whole_infections
        infected -= new_recovered
        recovered += new_recovered
        susceptible = population - infected - recovered

        # ==================================================
        # remainder check
        # ==================================================

        infection_remainder += infection_decimal
        if infection_remainder >= 1:
            infected += 1
            infection_remainder -= 1

        recovered_remainder += recovered_decimal
        if recovered_remainder >= 1:
            recovered += 1
            recovered_remainder -= 1
        # ==================================================
        # prints
        # ==================================================

        print(f"Generation: {printed_generations}")
        printed_generations += 1
        generations -= 1

        print(f"Susceptible: {round(susceptible)}")
        print(f"Infected: {round(infected)}")
        print(f"Recovered: {round(recovered)}")
        print(f"Infected Remainder: {infection_remainder}")
        print(f"Recovered Remainder: {recovered_remainder}")

        print("---------------")

        susceptible_list.append(susceptible)
        infected_list.append(infected)
        recovered_list.append(recovered)

        time.sleep(0.01)
        if susceptible <= 0:
            break


simulation(susceptible_list, recovered_list, recovery_rate, recovered, generations, printed_generations,
           infected, infection_rate, susceptible, recovered_remainder, infection_remainder, infected_list)

# ==================================================
# matplotlib
# ==================================================
x = list(range(0, generations_plot + 1))

plt.figure("Susceptible-Infected-Recovered Simulation")

plt.title("Susceptible-Infected-Recovered")

plt.plot(x, susceptible_list, label="Susceptible")
plt.plot(x, infected_list, label="Infected")
plt.plot(x, recovered_list, label="Recovered")

plt.ylabel("Population")
plt.xlabel("Generations")
plt.legend(loc="upper left")
plt.show()
