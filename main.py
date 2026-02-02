import pandas as pd
import matplotlib.pyplot as plt


def main():
    print("Logistics Analysis Project Started")

    data = {
        "Delivery": [1, 2, 3, 4],
        "Delay_days": [0, 1, 3, 0],
        "Cost": [120, 200, 150, 180]
    }

    df = pd.DataFrame(data)

    print("\nDelivery data:")
    print(df)

    average_delay = df["Delay_days"].mean()
    average_cost = df["Cost"].mean()

    print("\nAverage delay:", average_delay)
    print("Average cost:", average_cost)

    # Delay chart
    plt.figure()
    plt.bar(df["Delivery"], df["Delay_days"])
    plt.title("Delay per Delivery")
    plt.xlabel("Delivery")
    plt.ylabel("Delay (Days)")
    plt.show()


if __name__ == "__main__":
    main()
