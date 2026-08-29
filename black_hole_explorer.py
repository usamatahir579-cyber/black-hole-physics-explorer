"""
Black Hole Physics Explorer

A computational exploration of Schwarzschild black-hole
thermodynamics, Hawking evaporation, and the information paradox.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ---------------------------------------------------------
# Physical constants
# ---------------------------------------------------------

G = 6.6743e-11
C = 299_792_458
HBAR = 1.054571817e-34
K_B = 1.380649e-23
M_SUN = 1.988e30
SECONDS_PER_YEAR = 365.25 * 24 * 60 * 60

# ---------------------------------------------------------
# Output directory
# ---------------------------------------------------------

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------
# Black-hole physics functions
# ---------------------------------------------------------

def schwarzschild_radius(mass_kg):
    """Return Schwarzschild radius in metres."""
    return (2 * G * mass_kg) / C**2


def hawking_temperature(mass_kg):
    """Return Hawking temperature in kelvin."""
    return (
        HBAR * C**3
        / (8 * np.pi * G * mass_kg * K_B)
    )


def black_hole_entropy(mass_kg):
    """Return Bekenstein-Hawking entropy in J/K."""
    radius = schwarzschild_radius(mass_kg)
    area = 4 * np.pi * radius**2

    return (
        K_B * C**3 * area
        / (4 * G * HBAR)
    )


def evaporation_time(mass_kg):
    """Return idealized Hawking evaporation time in seconds."""
    return (
        5120
        * np.pi
        * G**2
        * mass_kg**3
        / (HBAR * C**4)
    )


def mass_during_evaporation(initial_mass_kg, time_seconds):
    """Return remaining mass during idealized evaporation."""
    lifetime = evaporation_time(initial_mass_kg)

    remaining_fraction = 1 - time_seconds / lifetime
    remaining_fraction = np.maximum(
        remaining_fraction,
        0
    )

    return (
        initial_mass_kg
        * remaining_fraction**(1 / 3)
    )


def conceptual_page_curve(time_fraction, page_time=0.5):
    """
    Return an illustrative normalized unitary Page curve.

    This is a conceptual visualization, not a first-principles
    quantum-gravity calculation.
    """
    return np.where(
        time_fraction <= page_time,
        time_fraction / page_time,
        (1 - time_fraction) / (1 - page_time)
    )


# ---------------------------------------------------------
# Numerical summary
# ---------------------------------------------------------

def print_black_hole_properties(mass_solar):
    """Print main properties for a black hole."""

    mass_kg = mass_solar * M_SUN

    radius_km = schwarzschild_radius(mass_kg) / 1000
    temperature = hawking_temperature(mass_kg)
    entropy_kb = black_hole_entropy(mass_kg) / K_B

    lifetime_years = (
        evaporation_time(mass_kg)
        / SECONDS_PER_YEAR
    )

    print("\nBLACK HOLE PROPERTIES")
    print("-" * 45)

    print(f"Mass: {mass_solar:.3g} solar masses")
    print(f"Schwarzschild radius: {radius_km:.3e} km")
    print(f"Hawking temperature: {temperature:.3e} K")
    print(f"Entropy (S/k_B): {entropy_kb:.3e}")
    print(
        f"Evaporation lifetime: "
        f"{lifetime_years:.3e} years"
    )


def print_comparison_table():
    """Print properties for several black-hole masses."""

    masses = [0.001, 1, 10, 100, 1000]

    print("\nBLACK HOLE COMPARISON TABLE")
    print("-" * 105)

    print(
        f"{'Mass (M_sun)':<15}"
        f"{'Radius (km)':<18}"
        f"{'Temperature (K)':<22}"
        f"{'Entropy (S/k_B)':<25}"
        f"{'Lifetime (yr)':<20}"
    )

    print("-" * 105)

    for mass_solar in masses:
        mass_kg = mass_solar * M_SUN

        radius = (
            schwarzschild_radius(mass_kg) / 1000
        )

        temperature = hawking_temperature(mass_kg)

        entropy = (
            black_hole_entropy(mass_kg) / K_B
        )

        lifetime = (
            evaporation_time(mass_kg)
            / SECONDS_PER_YEAR
        )

        print(
            f"{mass_solar:<15.3g}"
            f"{radius:<18.3e}"
            f"{temperature:<22.3e}"
            f"{entropy:<25.3e}"
            f"{lifetime:<20.3e}"
        )

def save_figure(filename):
    """Save the current figure as a high-resolution PNG."""
    plt.tight_layout()

    output_path = RESULTS_DIR / filename

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"Saved figure: {output_path}")        



# ---------------------------------------------------------
# Plotting functions
# ---------------------------------------------------------

def plot_radius_vs_mass():
    masses_solar = np.logspace(-3, 3, 300)
    masses_kg = masses_solar * M_SUN

    radii_km = (
        schwarzschild_radius(masses_kg)
        / 1000
    )

    plt.figure(figsize=(8, 5))

    plt.loglog(
        masses_solar,
        radii_km
    )

    plt.xlabel("Black Hole Mass (Solar Masses)")
    plt.ylabel("Schwarzschild Radius (km)")
    plt.title("Black Hole Mass vs Schwarzschild Radius")
    plt.grid(True, which="both")

    save_figure("01_schwarzschild_radius_vs_mass.png")
plt.close()

def plot_temperature_vs_mass():
    masses_solar = np.logspace(-3, 3, 300)
    masses_kg = masses_solar * M_SUN

    temperatures = hawking_temperature(masses_kg)

    plt.figure(figsize=(8, 5))

    plt.loglog(
        masses_solar,
        temperatures
    )

    plt.xlabel("Black Hole Mass (Solar Masses)")
    plt.ylabel("Hawking Temperature (K)")
    plt.title("Black Hole Mass vs Hawking Temperature")
    plt.grid(True, which="both")

    save_figure("02_hawking_temperature_vs_mass.png")
plt.close()


def plot_entropy_vs_mass():
    masses_solar = np.logspace(-3, 3, 300)
    masses_kg = masses_solar * M_SUN

    entropy_kb = (
        black_hole_entropy(masses_kg)
        / K_B
    )

    plt.figure(figsize=(8, 5))

    plt.loglog(
        masses_solar,
        entropy_kb
    )

    plt.xlabel("Black Hole Mass (Solar Masses)")
    plt.ylabel("Entropy (S/k_B)")
    plt.title(
        "Black Hole Mass vs Bekenstein-Hawking Entropy"
    )
    plt.grid(True, which="both")

    save_figure("03_entropy_vs_mass.png")
plt.close()


def plot_lifetime_vs_mass():
    masses_solar = np.logspace(-6, 3, 300)
    masses_kg = masses_solar * M_SUN

    lifetime_years = (
        evaporation_time(masses_kg)
        / SECONDS_PER_YEAR
    )

    plt.figure(figsize=(8, 5))

    plt.loglog(
        masses_solar,
        lifetime_years
    )

    plt.xlabel("Black Hole Mass (Solar Masses)")
    plt.ylabel("Evaporation Lifetime (Years)")
    plt.title(
        "Black Hole Mass vs Evaporation Lifetime"
    )
    plt.grid(True, which="both")

    save_figure("04_evaporation_lifetime_vs_mass.png")
plt.close()


def plot_page_curve():
    time_fraction = np.linspace(0, 1, 500)

    page_time = 0.5

    hawking_entropy = time_fraction

    page_entropy = conceptual_page_curve(
        time_fraction,
        page_time
    )

    plt.figure(figsize=(8, 5))

    plt.plot(
        time_fraction,
        hawking_entropy,
        label="Semiclassical Hawking Prediction"
    )

    plt.plot(
        time_fraction,
        page_entropy,
        label="Illustrative Unitary Page Curve"
    )

    plt.axvline(
        page_time,
        linestyle="--",
        label="Illustrative Page Time"
    )

    plt.xlabel("Normalized Evaporation Time")
    plt.ylabel("Normalized Radiation Entropy")
    plt.title(
        "Conceptual Page Curve for an Evaporating Black Hole"
    )

    plt.legend()
    plt.grid(True)

    save_figure("05_conceptual_page_curve.png")
plt.close()


def plot_evaporation_evolution():
    initial_mass = M_SUN

    lifetime = evaporation_time(initial_mass)

    time_fraction = np.linspace(
        0,
        0.999,
        500
    )

    times = time_fraction * lifetime

    mass_t = mass_during_evaporation(
        initial_mass,
        times
    )

    mass_fraction = mass_t / initial_mass

    entropy_t = black_hole_entropy(mass_t)

    entropy_fraction = (
        entropy_t
        / black_hole_entropy(initial_mass)
    )

    page_entropy = conceptual_page_curve(
        time_fraction
    )

    plt.figure(figsize=(9, 6))

    plt.plot(
        time_fraction,
        mass_fraction,
        label="Remaining Mass"
    )

    plt.plot(
        time_fraction,
        entropy_fraction,
        label="Black Hole Entropy"
    )

    plt.plot(
        time_fraction,
        page_entropy,
        label="Illustrative Radiation Page Curve"
    )

    plt.axvline(
        0.5,
        linestyle="--",
        label="Illustrative Page Time"
    )

    plt.xlabel("Fraction of Evaporation Lifetime")
    plt.ylabel("Normalized Quantity")

    plt.title(
        "Black Hole Evaporation and Information Evolution"
    )

    plt.legend()
    plt.grid(True)

    save_figure("06_evaporation_information_evolution.png")
plt.close()


def plot_temperature_evolution():
    initial_mass = M_SUN

    lifetime = evaporation_time(initial_mass)

    time_fraction = np.linspace(
        0,
        0.999,
        500
    )

    times = time_fraction * lifetime

    mass_t = mass_during_evaporation(
        initial_mass,
        times
    )

    temperature_t = hawking_temperature(mass_t)

    temperature_ratio = (
        temperature_t
        / hawking_temperature(initial_mass)
    )

    plt.figure(figsize=(9, 6))

    plt.semilogy(
        time_fraction,
        temperature_ratio
    )

    plt.xlabel("Fraction of Evaporation Lifetime")
    plt.ylabel("Temperature / Initial Temperature")

    plt.title(
        "Growth of Hawking Temperature During Evaporation"
    )

    plt.grid(True)

    save_figure("07_temperature_during_evaporation.png")
plt.close()


# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------

def main():
    print("BLACK HOLE PHYSICS EXPLORER")
    print("=" * 45)

    try:
        mass_solar = float(
            input(
                "Enter black hole mass "
                "in solar masses: "
            )
        )

        if mass_solar <= 0:
            print("Mass must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    print_black_hole_properties(mass_solar)

    print_comparison_table()

    plot_radius_vs_mass()
    plot_temperature_vs_mass()
    plot_entropy_vs_mass()
    plot_lifetime_vs_mass()
    plot_page_curve()
    plot_evaporation_evolution()
    plot_temperature_evolution()


if __name__ == "__main__":
    main()