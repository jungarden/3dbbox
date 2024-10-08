import numpy as np
import matplotlib.pyplot as plt
import os 

backupdir = '../baseline/backup/glove00'
data = np.load(os.path.join(backupdir, "costs.npz"))

#load data
training_iters = data['training_iters']
training_losses = data['training_losses']
testing_iters = data['testing_iters']
testing_losses = data['testing_losses']


for key in data.files:
    print(f"{key}: {data[key]}")
data.close()

plt.figure(figsize=(10, 6))
plt.plot(training_iters, training_losses, label='Training Loss')
plt.plot(testing_iters, testing_losses, label='Testing Loss')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.title('Training and Testing Loss per Iteration')
plt.legend()
plt.grid(True)

save_path = os.path.join(backupdir, 'loss_graph.png')
plt.savefig(save_path)