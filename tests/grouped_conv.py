import torch
import torch.optim as optim

from models.ACNN_Grouped_CNN.grouped_conv import ACNN
from utilities.data import load_data
from utilities.train_helpers import train, test

if __name__ == '__main__':

    # HyperParams and Others
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    epochs = 30
    batch_size = 64
    learning_rate = 0.01

    # Loading Data
    data_loc = r'E:\Datasets'
    train_loader, test_loader = load_data(data_loc, batch_size, download=False)

    # noinspection PyUnresolvedReferences
    model = ACNN(device=device).to(device=device)
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)

    for epoch in range(1, epochs + 1):
        train(model, device, train_loader, optimizer, epoch, 100)
        test(model, device, test_loader)

    # visualize(model, device, test_dataset, save_dir='data/visuals', num_visualize=10)
