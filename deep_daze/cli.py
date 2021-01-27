import sys

import fire

from deep_daze import Imagine


def train(
        text,
        learning_rate=1e-5,
        num_layers=16,
        batch_size=4,
        gradient_accumulate_every=4,
        epochs=20,
        iterations=1050,
        save_every=100,
        image_width=512,
        deeper=False,
        overwrite=False,
        save_progress=False,
        seed=None,
        open_folder=True
):
    """
    :param text: (required) A phrase less than 77 characters which you would like to visualize.
    :param learning_rate: The learning rate of the neural net.
    :param num_layers: The number of hidden layers to use in the Siren neural net.
    :param batch_size: The number of generated images to pass into Siren before calculating loss. Decreasing this can lower memory and accuracy.
    :param gradient_accumulate_every: Calculate a weighted loss of n samples for each iteration. Increasing this can help increase accuracy with lower batch sizes.
    :param epochs: The number of epochs to run.
    :param iterations: The number of times to calculate and backpropagate loss in a given epoch.
    :param save_progress: Whether or not to save images generated before training Siren is complete.
    :param save_every: Generate an image every time iterations is a multiple of this number.
    :param open_folder:  Whether or not to open a folder showing your generated images.
    :param overwrite: Whether or not to overwrite existing generated images of the same name.
    :param deeper: Uses a Siren neural net with 32 hidden layers.
    :param image_width: The desired resolution of the image.
    :param seed: A seed to be used for deterministic runs.

    """
    print('Starting up...')

    if deeper:
        num_layers = 32

    imagine = Imagine(
        text,
        lr=learning_rate,
        num_layers=num_layers,
        batch_size=batch_size,
        gradient_accumulate_every=gradient_accumulate_every,
        epochs=epochs,
        iterations=iterations,
        image_width=image_width,
        save_every=save_every,
        save_progress=save_progress,
        seed=seed,
        open_folder=open_folder
    )

    if not overwrite and imagine.filename.exists():
        answer = input('Imagined image already exists, do you want to overwrite? (y/n) ').lower()
        if answer not in ('yes', 'y'):
            sys.exit()

    imagine()


def main():
    fire.Fire(train)
