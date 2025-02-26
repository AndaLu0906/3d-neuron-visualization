import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# Constants
UM_PER_MM = 1000  # 1 mm = 1000 µm

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to create a dendritic tree
def create_dendrites(num_branches, length):
    dendrites = []
    for _ in range(num_branches):
        x = np.linspace(0, np.random.uniform(0.5, 1.5) * length, 100)
        y = np.random.normal(0, 0.1, 100).cumsum()
        z = np.random.normal(0, 0.1, 100).cumsum()
        dendrites.append(np.column_stack((x, y, z)))
    return dendrites

# Function to create a myelinated axon
def create_axon(length):
    x = np.linspace(0, length, 100)
    y = np.zeros(100)
    z = np.zeros(100)

    # Add myelin sheath segments
    for i in range(0, 100, 10):
        # Myelin sheath (thicker segments)
        ax.plot(x[i:i+5], y[i:i+5], z[i:i+5], color='lightgray', linewidth=4, alpha=0.8)
        # Axon (inner part)
        ax.plot(x[i:i+5], y[i:i+5], z[i:i+5], color='green', linewidth=2)
    return np.column_stack((x, y, z))

# Function to create synaptic connections
def create_synapses(neuron1, neuron2):
    synapses = []
    for dendrite in neuron1:
        for i in range(0, len(dendrite), 20):
            start_point = dendrite[i]
            target_dendrite = neuron2[np.random.randint(0, len(neuron2))]
            end_point = target_dendrite[np.random.randint(0, len(target_dendrite))]
            synapses.append((start_point, end_point))
    return synapses

# Create primary neuron components
dendrites = create_dendrites(num_branches=10, length=50)  # 50 µm
axon = create_axon(length=100)  # 100 µm
soma = np.array([[0, 0, 0]])  # Single soma for the primary neuron

# Plot dendrites (with a single label)
for i, dendrite in enumerate(dendrites):
    ax.plot(dendrite[:, 0], dendrite[:, 1], dendrite[:, 2], color='blue', alpha=0.6, label='Dendrites' if i == 0 else "")

# Plot axon (with a single label)
ax.plot(axon[:, 0], axon[:, 1], axon[:, 2], color='green', linewidth=2, label='Axon')

# Plot soma (with a single label)
ax.scatter(soma[:, 0], soma[:, 1], soma[:, 2], color='red', s=100, label='Soma')

# Create a second neuron (no soma for simplicity)
dendrites2 = create_dendrites(num_branches=8, length=40)  # 40 µm
axon2 = create_axon(length=80)  # 80 µm

# Plot second neuron (no labels)
for dendrite in dendrites2:
    ax.plot(dendrite[:, 0], dendrite[:, 1], dendrite[:, 2], color='blue', alpha=0.6)
ax.plot(axon2[:, 0], axon2[:, 1], axon2[:, 2], color='green', linewidth=2)

# Create synapses (with a single label)
synapses = create_synapses(dendrites, dendrites2)
for i, synapse in enumerate(synapses):
    start, end = synapse
    x_coords = [start[0], end[0]]
    y_coords = [start[1], end[1]]
    z_coords = [start[2], end[2]]
    ax.plot(x_coords, y_coords, z_coords, color='orange', alpha=0.4, label='Synapses' if i == 0 else "")

# Add labels and title
ax.set_xlabel('X-axis (µm)')
ax.set_ylabel('Y-axis (µm)')
ax.set_zlabel('Z-axis (µm)')
ax.set_title('3D Neuron Visualization with Realistic Units')

# Set consistent axis scaling
ax.set_box_aspect([1, 1, 1])  # Ensures equal scaling for all axes

# Add legend
ax.legend(loc='upper right')

# Show the plot
ax.view_init(elev=20, azim=30)
plt.show()
