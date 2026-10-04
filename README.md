# Fourier Analysis of AI-Generated Images

A small project exploring differences between real and AI-generated images using the Fourier transform.

## Idea

Instead of analysing the images directly in the spatial domain, I compare their frequency spectra using a 2D Fourier transform.

The process is simple:

1. Convert the image to grayscale.
2. Store it as a NumPy matrix.
3. Compute its 2D Fourier transform.
4. Shift the zero frequency to the centre.
5. Visualize the magnitude spectrum using a logarithmic scale.

## Results

In the images tested so far, I found a noticeable difference between real and AI-generated images.

Real photographs tend to produce a more homogeneous frequency spectrum, while some AI-generated images show visible bands and structured patterns in their Fourier transform.

These results are experimental and do not represent a general-purpose AI image detector.

## Example

### Real image

![Real image](images/real.png)

### AI-generated image

![AI-generated image](images/ai.png)

### Fourier spectra

![Fourier comparison](results/fourier_comparison.png)

## Technologies

- Python
- NumPy
- Pillow
- Matplotlib

## Current status

This is a small experimental project. The next step is to test the behaviour on a larger set of images and try to quantify the patterns found in the frequency domain.
