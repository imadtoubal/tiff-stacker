"""Command line interface for stiff."""
import os

import click
import numpy as np
import skimage.io as sio


@click.command()
@click.argument('input_dir', required=True)
@click.argument('output', required=True)
@click.option('--input-extension', default='tif', help='Input file extension')
@click.option('--axis', default=0, help='Axis to stack along')
def main(input_dir, output, input_extension='tif', axis=0):
  """Stack images into a tiff stack"""
  ext = output.split('.')[-1].lower()
  assert ext in ['tif', 'tiff'], 'Output must be a tiff file'

  if input_extension.startswith('.'):
    input_extension = input_extension[1:]

  pattern = os.path.join(input_dir, '*.' + input_extension)
  print(pattern)
  images = sio.imread_collection(pattern)
  stack = np.stack(images, axis=axis)
  sio.imsave(output, stack)
