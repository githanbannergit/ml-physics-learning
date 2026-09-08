import numpy as np
import matplotlib.pyplot as plt


def generate_data(
    A=1.0,
    omega=2.0,
    phi=0.0,
    noise_std=0.1,
    n_points=200
):
    t = np.linspace(0, 10, n_points)

    x_clean = A * np.cos(omega * t + phi)

    noise = np.random.normal(0, noise_std, size=n_points)

    x_noisy = x_clean + noise

    return t, x_clean, x_noisy


t, x_clean, x_noisy = generate_data()

plt.plot(t, x_clean, label="Clean")
plt.scatter(t, x_noisy, s=10, label="Noisy")

plt.xlabel("Time")
plt.ylabel("Position")
plt.legend()
plt.show()