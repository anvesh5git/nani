import streamlit as st

def calculate_superposition(currents, resistances):
    total_voltage = 0
    for current, resistance in zip(currents, resistances):
        total_voltage += current * resistance
    return total_voltage

def main():
    st.title("Superposition Theorem Calculator")
    
    num_sources = st.number_input("Number of independent sources", min_value=1, value=2, step=1)
    
    currents = []
    resistances = []
    
    for i in range(num_sources):
        st.header(f"Source {i+1}")
        current = st.number_input(f"Current (I{i+1}) in Amperes", value=1.0, step=0.1, format="%.1f")
        resistance = st.number_input(f"Resistance (R{i+1}) in Ohms", value=1.0, step=0.1, format="%.1f")
        currents.append(current)
        resistances.append(resistance)
    
    if st.button("Calculate Voltage using Superposition"):
        total_voltage = calculate_superposition(currents, resistances)
        st.write(f"The total voltage across the resistors is: {total_voltage} V")
    
    st.write("Note: This example assumes all sources and resistances are in series and superposition is applied to calculate the total voltage.")

if __name__ == "__main__":
    main()
